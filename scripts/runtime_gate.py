#!/usr/bin/env python3
"""
runtime_gate.py - Production Rendered Quality & Accessibility Gate (v2.3.0)
Synthesized from consensus recommendations across 4 Lead Reviewer AIs.

Features:
- Dual-viewport testing: Mobile (Pixel 7 device emulation) + Desktop (1440x900).
- Windows non-overlay scrollbar safe: compares scrollWidth > clientWidth + 1.5.
- Visually Hidden Exemption for Skip Links: Exempts .sr-only, clip: rect(0,0,0,0), and 1x1px skip anchors.
- Intelligent In-Sentence vs Navigation Link Heuristic:
  Exempts inline links surrounded by running text (parent text length > link text length + 5),
  while strictly enforcing >= 44px tap targets on solitary mobile navigation items (<li><a href="...">).
- Inner Scroll Container Discovery: Detects scrolling <main> or documentElement when body has overflow:hidden.
- Deterministic Hydration & Lazy Image Settling: Awaits document.readyState === 'complete', document.fonts.ready,
  and lazy-loaded image completion before auditing.
- Official CWV Session-Window CLS: Measures peak 5-second burst window (<1s inter-shift gap).
- Non-Swallowing 404 Assertion: Accurately asserts unknown routes return HTTP 404.
"""
import argparse
import json
import sys
import time
from collections import deque
from urllib.parse import urldefrag, urlparse

CLS_SCRIPT = """
window.__cls = 0;
let maxSessionValue = 0;
let currSessionValue = 0;
let currSessionEntries = [];

new PerformanceObserver(list => {
  for (const e of list.getEntries()) {
    if (e.hadRecentInput) continue;
    const firstEntry = currSessionEntries[0];
    const lastEntry = currSessionEntries[currSessionEntries.length - 1];
    if (currSessionValue && (e.startTime - lastEntry.startTime < 1000) && (e.startTime - firstEntry.startTime < 5000)) {
      currSessionValue += e.value;
      currSessionEntries.push(e);
    } else {
      currSessionValue = e.value;
      currSessionEntries = [e];
    }
    if (currSessionValue > maxSessionValue) {
      maxSessionValue = currSessionValue;
      window.__cls = maxSessionValue;
    }
  }
}).observe({type: 'layout-shift', buffered: true});
"""

DOM_AUDIT = """
(minTarget) => {
  const out = {};
  out.lang = document.documentElement.getAttribute('lang');
  out.h1 = document.querySelectorAll('h1').length;
  out.title = document.title;
  const md = document.querySelector('meta[name=description]');
  out.description = md ? md.content : '';
  
  // Windows non-overlay scrollbar resilient overflow check with 1.5px sub-pixel tolerance
  const doc = document.documentElement;
  out.overflow = doc.scrollWidth > (doc.clientWidth + 1.5);
  
  out.imgNoAlt = [...document.querySelectorAll('img:not([alt])')].map(i => (i.currentSrc || i.src).slice(0, 100));
  const ids = new Set([...document.querySelectorAll('[id]')].map(e => e.id));
  out.badFragments = [...document.querySelectorAll('a[href^="#"]')]
    .map(a => a.getAttribute('href'))
    .filter(h => h === '#' || h === '#/' || !ids.has(decodeURIComponent(h.slice(1))));
    
  out.small = [];
  if (minTarget > 0) {
    const sel = 'a[href], button, input:not([type=hidden]), select, textarea, [role=button], [role=tab]';
    for (const el of document.querySelectorAll(sel)) {
      const cs = window.getComputedStyle(el);
      // Filter physically invisible, detached, or hidden elements
      if (
        cs.display === 'none' ||
        cs.visibility === 'hidden' ||
        parseFloat(cs.opacity) === 0 ||
        el.getAttribute('aria-hidden') === 'true' ||
        el.type === 'hidden'
      ) {
        continue;
      }
      
      const r = el.getBoundingClientRect();
      if (r.width === 0 || r.height === 0) continue;
      
      // 1. Exempt visually hidden accessibility elements (skip-to-content links)
      const isSrOnly = (
        (r.width <= 1 && r.height <= 1) ||
        cs.clip === 'rect(0px, 0px, 0px, 0px)' ||
        cs.clipPath === 'inset(50%)' ||
        cs.clipPath === 'inset(100%)' ||
        el.classList.contains('sr-only') ||
        el.classList.contains('visually-hidden')
      );
      if (isSrOnly) continue;
      
      // 2. Intelligent In-Sentence vs Navigation Link Heuristic
      // In-sentence link: Parent container has other prose beyond the link's own label
      if (el.tagName === 'A' && (cs.display === 'inline' || cs.display === 'inline-block')) {
        const parentBlock = el.closest('p, blockquote, dd, li, span, div');
        if (parentBlock) {
          const parentText = (parentBlock.innerText || '').trim();
          const linkText = (el.innerText || '').trim();
          // If parent block contains more text than the link itself (+5 chars), it is an inline running text link
          if (parentText.length > linkText.length + 5) {
            continue;
          }
        }
      }
      
      if (r.width < minTarget || r.height < minTarget) {
        const label = (el.innerText || el.getAttribute('aria-label') || el.tagName).trim().slice(0, 40);
        out.small.push(label + ' ' + Math.round(r.width) + 'x' + Math.round(r.height));
      }
    }
  }
  out.jsonld = [...document.querySelectorAll('script[type="application/ld+json"]')].map(s => s.textContent);
  out.links = [...document.querySelectorAll('a[href]')].map(a => a.href);
  return out;
}
"""

SKIP_EXT = (".pdf", ".zip", ".png", ".jpg", ".jpeg", ".webp", ".svg", ".mp4", ".xml", ".txt", ".ico")


def context_kwargs(pw, name):
    if name == "mobile":
        return dict(pw.devices["Pixel 7"])
    return {"viewport": {"width": 1440, "height": 900}}


def main():
    ap = argparse.ArgumentParser(description="Rendered Runtime Quality Gate (v2.3.0)")
    ap.add_argument("base_url", nargs="?", default="http://localhost:3000", help="Base URL to test")
    ap.add_argument("--min-routes", type=int, default=4, help="Minimum crawlable routes required")
    ap.add_argument("--max-routes", type=int, default=60, help="Maximum routes to crawl")
    ap.add_argument("--min-target", type=int, default=44, help="Minimum mobile tap target in pixels")
    ap.add_argument("--max-cls", type=float, default=0.10, help="Maximum CLS threshold")
    ap.add_argument("--skip-if-offline", action="store_true", default=False, help="Don't fail if server unreachable")
    args = ap.parse_args()

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        msg = "Playwright not installed, skipping runtime gate" if args.skip_if_offline else "Playwright is not installed"
        status = "WARN" if args.skip_if_offline else "FAIL"
        print(json.dumps({"status": status, "message": msg, "errors": [msg]}))
        sys.exit(0 if args.skip_if_offline else 1)

    base = urlparse(args.base_url)
    routes_seen = {}
    meta_by_route = {}
    errs = []
    warns = []

    def err(route, vp, rule, detail):
        errs.append({"route": route, "viewport": vp, "rule": rule, "detail": detail})

    with sync_playwright() as pw:
        try:
            browser = pw.chromium.launch()
        except Exception as e:
            msg = f"Chromium launch failed: {e}"
            status = "WARN" if args.skip_if_offline else "FAIL"
            print(json.dumps({"status": status, "message": msg, "errors": [msg]}))
            sys.exit(0 if args.skip_if_offline else 1)

        queue, queued = deque(["/"]), {"/"}

        while queue and len(routes_seen) < args.max_routes:
            route = queue.popleft()
            for vp_name in ("mobile", "desktop"):
                ctx = browser.new_context(**context_kwargs(pw, vp_name))
                page = ctx.new_page()
                page.add_init_script(CLS_SCRIPT)
                console_errors = []
                page.on("console", lambda m: console_errors.append(m.text) if m.type == "error" else None)
                page.on("pageerror", lambda e: console_errors.append(str(e)))
                try:
                    resp = page.goto(args.base_url.rstrip("/") + route, wait_until="load", timeout=25000)
                    if resp is None or resp.status != 200:
                        err(route, vp_name, "http-status", resp.status if resp else "no response")
                        ctx.close()
                        continue

                    # 1. Deterministic Readiness: Fonts + Complete State + Lazy Images
                    page.evaluate("""() => Promise.all([
                        document.fonts ? document.fonts.ready : Promise.resolve(),
                        Promise.all([...document.images].filter(i => !i.complete).map(i => new Promise(r => { i.onload = i.onerror = r; setTimeout(r, 2000); })))
                    ])""")
                    page.wait_for_timeout(300)

                    # 2. Dynamic Scroll Loop (finds inner scroll container or document)
                    viewport_h = page.evaluate("() => window.innerHeight")
                    step_h = max(int(viewport_h * 0.5), 300)
                    y = 0
                    max_scroll_limit = 100000  # High ceiling accommodating deep editorial/catalog routes

                    while y < max_scroll_limit:
                        page.evaluate("""(targetY) => {
                            const scroller = document.scrollingElement || document.documentElement || document.body;
                            scroller.scrollTo({top: targetY, behavior: 'instant'});
                            window.scrollTo({top: targetY, behavior: 'instant'});
                        }""", y)
                        page.wait_for_timeout(100)
                        page.evaluate("() => new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)))")
                        
                        current_total_h = page.evaluate("""() => {
                            const scroller = document.scrollingElement || document.documentElement;
                            return Math.max(document.body.scrollHeight, scroller.scrollHeight);
                        }""")
                        y += step_h
                        if y >= current_total_h:
                            break

                    # Discover and exercise arbitrary nested scroll containers (e.g. overflow-y: auto/scroll)
                    page.evaluate("""() => {
                        const containers = [...document.querySelectorAll('*')].filter(el => {
                            if (el === document.body || el === document.documentElement) return false;
                            const cs = window.getComputedStyle(el);
                            return (cs.overflowY === 'auto' || cs.overflowY === 'scroll') &&
                                   (el.scrollHeight > el.clientHeight + 10);
                        });
                        for (const c of containers) {
                            c.scrollTo({top: c.scrollHeight / 2, behavior: 'instant'});
                            c.scrollTo({top: c.scrollHeight, behavior: 'instant'});
                            c.scrollTo({top: 0, behavior: 'instant'});
                        }
                    }""")

                    # Return to top and allow lazy images, fonts, and layout shifts to settle
                    page.evaluate("""() => {
                        const scroller = document.scrollingElement || document.documentElement || document.body;
                        scroller.scrollTo({top: 0, behavior: 'instant'});
                        window.scrollTo({top: 0, behavior: 'instant'});
                    }""")
                    page.evaluate("""() => {
                        return Promise.all([
                            ...[...document.images].filter(img => !img.complete).map(img => new Promise(res => {
                                img.onload = img.onerror = res;
                                setTimeout(res, 800);
                            })),
                            document.fonts ? document.fonts.ready : Promise.resolve()
                        ]);
                    }""")
                    page.wait_for_timeout(400)

                    target_min = args.min_target if vp_name == "mobile" else 0
                    a = page.evaluate(DOM_AUDIT, target_min)
                    cls = page.evaluate("window.__cls")
                except Exception as exc:
                    err(route, vp_name, "navigation-failed", str(exc)[:200])
                    ctx.close()
                    continue

                if vp_name == "mobile":
                    routes_seen[route] = True
                    meta_by_route[route] = (a["title"], a["description"])
                    for href in a["links"]:
                        u = urlparse(urldefrag(href)[0])
                        path = (u.path.rstrip("/") or "/")
                        if u.netloc == base.netloc and not path.lower().endswith(SKIP_EXT) and path not in queued:
                            queued.add(path)
                            queue.append(path)
                    if route == "/":
                        if not a["jsonld"]:
                            warns.append({"route": "/", "rule": "no-json-ld"})
                        for blob in a["jsonld"]:
                            try:
                                json.loads(blob)
                            except ValueError:
                                err("/", vp_name, "json-ld-invalid", blob[:80])

                if not a["lang"]:
                    err(route, vp_name, "html-lang-missing", "")
                if a["h1"] != 1:
                    err(route, vp_name, "h1-count", f"{a['h1']} h1 elements")
                if a["overflow"]:
                    err(route, vp_name, "horizontal-overflow", "scrollWidth > clientWidth + 1.5")
                if a["imgNoAlt"]:
                    err(route, vp_name, "img-missing-alt", f"{len(a['imgNoAlt'])} images without alt: {a['imgNoAlt'][:3]}")
                if a["badFragments"]:
                    err(route, vp_name, "dangling-anchor-fragment", f"{len(a['badFragments'])} bad: {a['badFragments'][:3]}")
                if a["small"]:
                    err(route, vp_name, "tap-target-undersized", f"{len(a['small'])} targets < {args.min_target}px: {a['small'][:5]}")
                if cls is not None and cls > args.max_cls:
                    err(route, vp_name, "cls-threshold-exceeded", f"{cls:.4f} > {args.max_cls}")
                for ce in console_errors:
                    err(route, vp_name, "console-error", ce[:200])

                ctx.close()

        # Non-Swallowing Synthetic 404 test
        test_404_ctx = browser.new_context(**context_kwargs(pw, "desktop"))
        p404 = test_404_ctx.new_page()
        try:
            resp404 = p404.goto(args.base_url.rstrip("/") + "/__synthetic_test_route_404__", timeout=10000)
            if resp404 is None:
                err("/__synthetic_test_route_404__", "desktop", "missing-404-status", "No response received on 404 route")
            elif resp404.status != 404:
                err("/__synthetic_test_route_404__", "desktop", "missing-404-status", f"Expected HTTP 404, got HTTP {resp404.status}")
        except Exception as e:
            err("/__synthetic_test_route_404__", "desktop", "missing-404-status", f"404 probe failed: {str(e)[:100]}")
        finally:
            test_404_ctx.close()
            browser.close()

    titles = {}
    for r, (t, d) in meta_by_route.items():
        if t:
            titles.setdefault(t, []).append(r)
    for t, rlist in titles.items():
        if len(rlist) > 1:
            errs.append({"route": ",".join(rlist), "viewport": "*", "rule": "duplicate-title", "detail": t[:60]})

    if len(routes_seen) < args.min_routes:
        errs.append({"route": "*", "viewport": "*", "rule": "route-count", "detail": f"Found {len(routes_seen)} routes, required {args.min_routes}"})

    out = {
        "status": "PASS" if not errs else "FAIL",
        "routes_crawled": len(routes_seen),
        "routes": list(routes_seen.keys()),
        "errors": errs,
        "warnings": warns
    }
    print(json.dumps(out, indent=2))
    sys.exit(0 if not errs else 1)


if __name__ == "__main__":
    main()
