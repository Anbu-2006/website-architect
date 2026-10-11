#!/usr/bin/env python3
"""
scripts/crawl_sitemap.py
Production-Grade Multi-Viewport & Virtual-Scroll-Aware Sitemap Crawler for /website-architect.
Recursively traverses reference URLs up to depth 2, discovering primary navigation routes,
handling virtual scroll (Lenis/GSAP) via synthetic mouse wheel delta,
and profiling navigation structures across Desktop (1440px) and Mobile Drawer (390px).
"""

import asyncio
import json
import sys
import os
import socket
import ipaddress
from urllib.parse import urlparse, urljoin
from playwright.async_api import async_playwright

def validate_safe_url(url: str) -> bool:
    """Validates URL to protect against SSRF, DNS rebinding, and IPv6/IPv4-mapped attacks."""
    if not url:
        return False
    try:
        parsed = urlparse(url)
        if parsed.scheme not in ("http", "https"):
            return False
        hostname = (parsed.hostname or "").lower().strip("[]")
        if not hostname or hostname in ("localhost", "metadata.google.internal", "instance-data"):
            return False
        addr_info = socket.getaddrinfo(hostname, None)
        for item in addr_info:
            ip = ipaddress.ip_address(item[4][0])
            if ip.version == 6 and ip.ipv4_mapped:
                ip = ip.ipv4_mapped
            if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_multicast or ip.is_reserved:
                return False
            if str(ip) == "169.254.169.254":
                return False
        return True
    except Exception:
        return False

async def discover_sitemap(start_url: str, max_depth: int = 2, max_pages: int = 20, out_path: str = "sitemap_manifest.json"):
    if not validate_safe_url(start_url):
        print(f"[SECURITY] Refusing to crawl unsafe or private URL: {start_url}", file=sys.stderr)
        return []
    domain = urlparse(start_url).netloc
    visited = set()
    queue = [(start_url, 0)]
    sitemap = []

    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch(headless=True)
        except Exception:
            browser = await p.chromium.launch(channel="chrome", headless=True)

        context = await browser.new_context(
            viewport={"width": 1440, "height": 900},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        while queue and len(visited) < max_pages:
            url, depth = queue.pop(0)
            clean_url = url.split('#')[0].rstrip('/')
            if clean_url in visited or depth > max_depth:
                continue

            visited.add(clean_url)
            try:
                await page.set_viewport_size({"width": 1440, "height": 900})
                await page.goto(clean_url, wait_until="domcontentloaded", timeout=25000)
                await page.wait_for_timeout(1000)
                title = await page.title()

                # Step 2: Handle virtual scroll & lazy loaded navigation
                is_virt = await page.evaluate("() => Boolean(window.Lenis || window.LocomotiveScroll || window.ScrollTrigger || document.querySelector('[data-scroll-container]'))")
                if is_virt:
                    # Synthetic mouse wheel to trigger lazy loaders
                    await page.mouse.move(720, 450)
                    for _ in range(3):
                        await page.mouse.wheel(delta_x=0, delta_y=350)
                        await page.wait_for_timeout(150)
                    await page.mouse.wheel(delta_x=0, delta_y=-1050)
                    await page.wait_for_timeout(200)

                # Extract desktop links
                desktop_links = await page.eval_on_selector_all('nav a, header a, a[href^="/"]', """
                    elements => elements.map(e => ({
                        text: e.innerText.trim(),
                        href: e.href
                    })).filter(l => l.text && l.href)
                """)

                # Step 3: Check mobile viewport (390x844) for mobile drawer links
                await page.set_viewport_size({"width": 390, "height": 844})
                await page.wait_for_timeout(300)
                
                # Check for hamburger/drawer toggle button
                drawer_links = []
                mobile_menu_btn = await page.query_selector("button[aria-label*='menu'], button[class*='hamburger'], [class*='mobile-menu'], button[aria-expanded]")
                if mobile_menu_btn:
                    try:
                        expanded = await mobile_menu_btn.get_attribute("aria-expanded")
                        if expanded != "true":
                            await mobile_menu_btn.click(timeout=1500)
                            await page.wait_for_timeout(400)
                        drawer_links = await page.eval_on_selector_all('[role="dialog"] a, [class*="drawer"] a, [class*="mobile-nav"] a, nav a', """
                            elements => elements.map(e => ({
                                text: e.innerText.trim(),
                                href: e.href
                            })).filter(l => l.text && l.href)
                        """)
                    except Exception:
                        pass

                # Merge links deduplicated
                all_links = {l["href"]: l["text"] for l in desktop_links}
                for dl in drawer_links:
                    all_links[dl["href"]] = dl["text"]

                route_info = {
                    "url": clean_url,
                    "path": urlparse(clean_url).path or "/",
                    "title": title,
                    "depth": depth,
                    "nav_links": [{"href": h, "text": t} for h, t in all_links.items()],
                    "mobile_drawer_detected": bool(mobile_menu_btn and drawer_links)
                }

                for link_href in all_links.keys():
                    parsed = urlparse(link_href)
                    if parsed.netloc == domain and link_href not in visited:
                        if depth + 1 <= max_depth:
                            queue.append((link_href, depth + 1))

                sitemap.append(route_info)
                print(f"[+] Crawled: {clean_url} (Found {len(route_info['nav_links'])} links, depth {depth})")
            except Exception as e:
                print(f"[-] Error crawling {clean_url}: {e}")

        await browser.close()

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(sitemap, f, indent=2)
    print(f"[*] Saved {len(sitemap)} routes to {out_path}")
    return sitemap

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Multi-Viewport & Virtual-Scroll-Aware Sitemap Crawler")
    parser.add_argument("url", nargs="?", default=None, help="Reference website URL to crawl")
    parser.add_argument("--url", dest="opt_url", help="Reference website URL to crawl (flag option)")
    parser.add_argument("--out", "-o", default=None, help="Output JSON path (default: sitemap_manifest.json)")
    parser.add_argument("positional_out", nargs="?", default=None, help="Positional output JSON path")
    parser.add_argument("--depth", type=int, default=2, help="Max crawling depth (default: 2)")
    parser.add_argument("--max-pages", type=int, default=20, help="Max pages to crawl (default: 20)")

    args = parser.parse_args()
    target_url = args.opt_url or args.url
    if not target_url:
        parser.print_help()
        sys.exit(1)

    out_file = args.out or args.positional_out or "sitemap_manifest.json"
    asyncio.run(discover_sitemap(target_url, max_depth=args.depth, max_pages=args.max_pages, out_path=out_file))
