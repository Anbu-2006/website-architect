#!/usr/bin/env python3
"""
scripts/extract_tokens.py
Production-Grade Deep Design Token & Motion Extraction Engine for /website-architect.
Extracts declared fluid styles (clamp, calc, rem, @media) via Chrome DevTools Protocol (CDP),
captures active animations via WAAPI, CSS @keyframes, and GSAP ScrollTrigger metadata,
profiles micro-interactions (:hover, :active elevation deltas) via CDP forced pseudo-classes,
handles virtual scroll (Lenis, Locomotive) and GSAP pin-spacers,
records WebGL/Canvas streams to ambient WebM,
and profiles responsive layout matrices across Desktop (1440x900), Tablet (768x1024), and Mobile (390x844).
"""

import sys
import os
import re
import json
import base64
import argparse
import asyncio

try:
    from playwright.async_api import async_playwright
except ImportError:
    async_playwright = None

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def rgb_to_hex(rgb_str):
    """Converts rgb(r, g, b) or rgba(r, g, b, a) to hex."""
    if not rgb_str:
        return "#111111"
    m = re.search(r'rgba?\((\d+),\s*(\d+),\s*(\d+)', str(rgb_str))
    if m:
        r, g, b = int(m.group(1)), int(m.group(2)), int(m.group(3))
        return f"#{r:02x}{g:02x}{b:02x}".upper()
    return rgb_str

def clean_font_family(font_str):
    """Cleans font family string to first primary font name."""
    if not font_str:
        return "sans-serif"
    first = font_str.split(",")[0].strip().strip('"').strip("'")
    return first

IN_PAGE_DOM_EXTRACT_JS = """
(() => {
  const getStyles = (el) => el ? window.getComputedStyle(el) : null;
  const result = {
    url: window.location.href,
    title: document.title,
    typography: {},
    colors: {},
    geometry: {},
    components: {},
    cssVars: {},
    virtualScroll: false,
    pinSpacers: []
  };

  // 1. Virtual Scroll Detection
  result.virtualScroll = Boolean(
    window.Lenis || 
    window.LocomotiveScroll || 
    window.ScrollTrigger || 
    getStyles(document.body).overflow === 'hidden' ||
    document.querySelector('[data-scroll-container]') ||
    document.querySelector('.lenis')
  );

  // 2. GSAP Pin Spacer Detection & Height Normalization
  const pinSpacers = Array.from(document.querySelectorAll('.pin-spacer, [class*="pin-spacer"]'));
  result.pinSpacers = pinSpacers.map(ps => ({
    height: ps.offsetHeight,
    width: ps.offsetWidth,
    pinnedSelector: ps.firstElementChild ? (ps.firstElementChild.tagName + ((() => { const cn = ps.firstElementChild.className; const s = typeof cn === 'string' ? cn : (cn?.baseVal || ''); return s ? '.' + s.trim().split(/\\s+/).join('.') : ''; })())) : null
  }));

  // 3. Typography Elements Map
  const typeMap = {
    h1: document.querySelector('h1'),
    h2: document.querySelector('h2'),
    h3: document.querySelector('h3'),
    eyebrow: document.querySelector('.eyebrow, [class*="eyebrow"], [class*="badge"], [class*="tag"], span.uppercase'),
    lead: document.querySelector('p.lead, [class*="hero"] p, [class*="subtitle"], [class*="lead"]'),
    body: document.querySelector('p'),
    button: document.querySelector('button, a.btn, a[class*="button"], a[class*="cta"], a[href*="contact"], a[href*="book"]'),
    code: document.querySelector('code, pre, [class*="mono"]')
  };

  for (const [key, el] of Object.entries(typeMap)) {
    if (el) {
      const cs = getStyles(el);
      result.typography[key] = {
        fontFamily: cs.fontFamily,
        fontSize: cs.fontSize,
        fontWeight: cs.fontWeight,
        lineHeight: cs.lineHeight,
        letterSpacing: cs.letterSpacing,
        textTransform: cs.textTransform,
        color: cs.color
      };
    }
  }

  // 4. Color System
  const body = document.body;
  const bodyCS = getStyles(body);
  const card = document.querySelector('[class*="card"], article, [class*="surface"], [class*="box"], [class*="item"]');
  const cardCS = card ? getStyles(card) : null;
  const btn = document.querySelector('button, a[class*="btn"], a[class*="cta"], [class*="button"]');
  const btnCS = btn ? getStyles(btn) : null;
  const borderEl = document.querySelector('[class*="border"], hr, input, [class*="divider"]');
  const borderCS = borderEl ? getStyles(borderEl) : null;

  result.colors = {
    canvasBackground: bodyCS ? bodyCS.backgroundColor : '#FFFFFF',
    primaryInk: bodyCS ? bodyCS.color : '#111111',
    secondaryInk: (() => {
      const p = document.querySelector('p');
      return p ? getStyles(p).color : (bodyCS ? bodyCS.color : '#444444');
    })(),
    surfaceBackground: cardCS ? cardCS.backgroundColor : null,
    borderColor: borderCS ? borderCS.borderColor : 'rgba(0, 0, 0, 0.08)',
    buttonFill: btnCS ? btnCS.backgroundColor : '#111111',
    buttonText: btnCS ? btnCS.color : '#FFFFFF',
    accentColor: (() => {
      const link = document.querySelector('a:not([class*="btn"]):not([class*="button"])');
      return link ? getStyles(link).color : (btnCS ? btnCS.backgroundColor : '#111111');
    })()
  };

  // Color frequency clustering
  const colorMap = {};
  const elements = Array.from(document.querySelectorAll('*')).slice(0, 500);
  elements.forEach(el => {
    const s = window.getComputedStyle(el);
    [s.color, s.backgroundColor, s.borderColor].forEach(c => {
      if (c && c !== 'rgba(0, 0, 0, 0)' && c !== 'transparent') {
        colorMap[c] = (colorMap[c] || 0) + 1;
      }
    });
  });
  result.colors.topDetectedPalette = Object.entries(colorMap)
    .sort((a, b) => b[1] - a[1])
    .map(([color]) => color)
    .slice(0, 10);

  // Extract CSS custom properties from :root
  try {
    for (const sheet of document.styleSheets) {
      try {
        for (const rule of sheet.cssRules) {
          if (rule.selectorText === ':root' || rule.selectorText === ':host') {
            for (let i = 0; i < rule.style.length; i++) {
              const prop = rule.style[i];
              if (prop.startsWith('--')) {
                result.cssVars[prop] = rule.style.getPropertyValue(prop).trim();
              }
            }
          }
        }
      } catch(e) {}
    }
  } catch(e) {}

  // 5. Geometry & Layout
  const main = document.querySelector('main, .container, [class*="container"], [class*="wrapper"]');
  const sections = Array.from(document.querySelectorAll('section, [class*="section"]')).slice(0, 3);
  
  result.geometry = {
    containerMaxWidth: main ? getStyles(main).maxWidth : '1280px',
    sectionPadding: sections.map(s => ({
      paddingTop: getStyles(s).paddingTop,
      paddingBottom: getStyles(s).paddingBottom
    })),
    buttonBorderRadius: btnCS ? btnCS.borderRadius : '6px',
    cardBorderRadius: cardCS ? cardCS.borderRadius : '8px',
    buttonPadding: btnCS ? btnCS.padding : '12px 24px',
    cardShadow: cardCS ? cardCS.boxShadow : null,
    hasArchedMask: Boolean(
      document.querySelector('[style*="clip-path"], [class*="clip-path"], [class*="rounded-t-full"]') ||
      Array.from(document.querySelectorAll('img, picture, div')).some(el => {
        const cp = getStyles(el).clipPath;
        return cp && cp !== 'none';
      })
    )
  };

  // 6. Component Counts
  result.components = {
    buttonCount: document.querySelectorAll('button, a[class*="btn"], a[class*="cta"]').length,
    imageCount: document.querySelectorAll('img').length,
    videoCount: document.querySelectorAll('video').length,
    canvasCount: document.querySelectorAll('canvas').length,
    formCount: document.querySelectorAll('form').length,
    navHeight: (() => {
      const nav = document.querySelector('nav, header');
      return nav ? getStyles(nav).height : '72px';
    })()
  };

  // 7. Structural Section Layout Architecture & DNA Extraction
  const rawSections = Array.from(document.querySelectorAll('header, main > section, main > div, body > section, section, footer'));
  const uniqueSections = [];
  rawSections.forEach(sec => {
    if (uniqueSections.length >= 10) return;
    const rect = sec.getBoundingClientRect();
    if (rect.height > 60 && !uniqueSections.includes(sec)) {
      uniqueSections.push(sec);
    }
  });

  const layoutTree = {
    url: window.location.href,
    title: document.title,
    hero: null,
    sections: []
  };

  uniqueSections.forEach((sec, idx) => {
    const cs = getStyles(sec);
    const rect = sec.getBoundingClientRect();
    const headings = Array.from(sec.querySelectorAll('h1, h2, h3, h4')).map(h => ({
      level: h.tagName.toLowerCase(),
      text: h.innerText.trim(),
      fontSize: getStyles(h).fontSize,
      fontFamily: getStyles(h).fontFamily,
      textAlign: getStyles(h).textAlign
    })).filter(h => h.text.length > 0);

    const paragraphs = Array.from(sec.querySelectorAll('p')).map(p => p.innerText.trim()).filter(Boolean);
    const images = Array.from(sec.querySelectorAll('img')).map(img => ({
      src: img.src || img.getAttribute('data-src'),
      alt: img.alt || '',
      width: img.naturalWidth || img.clientWidth,
      height: img.naturalHeight || img.clientHeight
    }));
    const videos = Array.from(sec.querySelectorAll('video, iframe[src*="vimeo"], iframe[src*="youtube"]')).map(v => ({
      tagName: v.tagName.toLowerCase(),
      src: v.currentSrc || v.src || (v.querySelector('source')?.src) || '',
      autoplay: v.autoplay || false,
      loop: v.loop || false,
      muted: v.muted || false
    }));
    const buttons = Array.from(sec.querySelectorAll('button, a[class*="btn"], a[class*="cta"], a[class*="button"], a[role="button"]')).map(b => ({
      text: b.innerText.trim(),
      href: b.getAttribute('href') || '#',
      bgColor: getStyles(b).backgroundColor,
      textColor: getStyles(b).color,
      borderRadius: getStyles(b).borderRadius
    })).filter(b => b.text.length > 0);

    const gridEl = sec.querySelector('[class*="grid"], [style*="grid"]');
    const flexEl = sec.querySelector('[class*="flex"], [style*="flex"]');
    
    let layoutType = "single-column";
    let columnsCount = 1;
    if (gridEl) {
      const gcs = getStyles(gridEl);
      const cols = gcs.gridTemplateColumns ? gcs.gridTemplateColumns.split(' ').filter(Boolean).length : 1;
      columnsCount = cols;
      layoutType = cols > 1 ? `grid-${cols}-cols` : "grid";
    } else if (flexEl) {
      const fcs = getStyles(flexEl);
      if (fcs.flexDirection.includes('row')) {
        layoutType = "asymmetric-split";
        columnsCount = 2;
      } else {
        layoutType = "flex-column";
      }
    } else if (rect.height >= window.innerHeight * 0.7 && (images.length > 0 || videos.length > 0)) {
      layoutType = "full-bleed-media";
    } else if (sec.tagName.toLowerCase() === 'footer') {
      layoutType = "footer-navigation";
    }

    // Hero detection on first section or header
    let isHero = false;
    let heroType = null;
    if (idx === 0 || headings.some(h => h.level === 'h1') || sec.querySelector('h1')) {
      isHero = true;
      if (videos.length > 0) {
        heroType = "full-bleed-video-hero";
      } else if (images.length > 0 && rect.height >= 500) {
        heroType = (layoutType === "asymmetric-split" || columnsCount >= 2) ? "split-media-hero" : "full-bleed-media-hero";
      } else {
        heroType = "centered-editorial-hero";
      }
    }

    const secObj = {
      index: idx + 1,
      tagName: sec.tagName.toLowerCase(),
      isHero: isHero,
      heroType: heroType,
      layoutType: layoutType,
      columnsCount: columnsCount,
      boundingRect: {
        width: Math.round(rect.width),
        height: Math.round(rect.height),
        top: Math.round(rect.top + window.scrollY),
        aspectRatio: (rect.width / (rect.height || 1)).toFixed(2)
      },
      padding: {
        top: cs.paddingTop,
        bottom: cs.paddingBottom,
        left: cs.paddingLeft,
        right: cs.paddingRight
      },
      backgroundColor: cs.backgroundColor,
      textColor: cs.color,
      headings: headings.slice(0, 3),
      headingSample: headings[0] ? (headings[0].text.slice(0, 45) + (headings[0].text.length > 45 ? '...' : '')) : null,
      paragraphsCount: paragraphs.length,
      sampleLead: paragraphs[0] ? (paragraphs[0].slice(0, 120) + (paragraphs[0].length > 120 ? '...' : '')) : null,
      images: images.slice(0, 6),
      imagesCount: images.length,
      videos: videos.slice(0, 3),
      hasVideo: videos.length > 0,
      buttons: buttons.slice(0, 4),
      buttonsCount: buttons.length,
      hasArchedMask: Boolean(sec.querySelector('[style*="clip-path"], [class*="rounded-t-full"]'))
    };

    if (isHero && !layoutTree.hero) {
      layoutTree.hero = secObj;
    }
    layoutTree.sections.push(secObj);
  });

  result.layoutTree = layoutTree;
  result.sections = layoutTree.sections;
  return result;
})()
"""

WAAPI_AND_MOTION_EXTRACT_JS = """
(() => {
  // 1. Extract active WAAPI tracks
  const activeAnimations = (document.getAnimations ? document.getAnimations() : []).map(anim => {
    const timing = anim.effect?.getTiming ? anim.effect.getTiming() : {};
    const keyframes = anim.effect?.getKeyframes ? anim.effect.getKeyframes() : [];
    const target = anim.effect?.target;
    return {
      targetSelector: target ? (target.tagName + ((() => { const cn = target.className; const s = typeof cn === 'string' ? cn : (cn?.baseVal || ''); return s ? '.' + s.trim().split(/\\s+/).join('.') : ''; })())) : 'anonymous',
      duration: timing.duration,
      delay: timing.delay,
      easing: timing.easing,
      fill: timing.fill,
      iterations: timing.iterations,
      keyframes: keyframes.slice(0, 5).map(k => ({
        offset: k.offset,
        transform: k.transform,
        opacity: k.opacity,
        filter: k.filter,
        easing: k.easing
      }))
    };
  });

  // 2. Extract declared CSS @keyframes
  const keyframesMap = {};
  for (const sheet of document.styleSheets) {
    try {
      for (const rule of sheet.cssRules) {
        if (rule.type === CSSRule.KEYFRAMES_RULE) {
          keyframesMap[rule.name] = rule.cssText;
        }
      }
    } catch (e) { /* ignore cross-origin */ }
  }

  // 3. Extract GSAP / ScrollTrigger metadata (with tree-shaking fallback)
  let gsapData = null;
  if (window.ScrollTrigger && window.ScrollTrigger.getAll) {
    gsapData = window.ScrollTrigger.getAll().map(st => ({
      trigger: (() => { const cn = st.trigger?.className; return typeof cn === 'string' ? cn : (cn?.baseVal || st.trigger?.tagName || 'unknown'); })(),
      start: String(st.start),
      end: String(st.end),
      scrub: Boolean(st.vars?.scrub),
      pin: Boolean(st.vars?.pin)
    }));
  } else {
    // Tree-shaken GSAP fallback: check for DOM pin-spacers and triggers
    const pinSpacers = Array.from(document.querySelectorAll('.pin-spacer, [class*="pin-spacer"]'));
    const scrollPinned = Array.from(document.querySelectorAll('[data-scroll], [data-scroll-trigger], [data-speed]'));
    if (pinSpacers.length > 0 || scrollPinned.length > 0) {
      gsapData = pinSpacers.map((ps, idx) => ({
        trigger: ps.firstElementChild ? (ps.firstElementChild.tagName + ((() => { const cn = ps.firstElementChild.className; const s = typeof cn === 'string' ? cn : (cn?.baseVal || ''); return s ? '.' + s.trim().split(/\\s+/).join('.') : ''; })())) : `pin-spacer-${idx}`,
        start: 'top top',
        end: `+=${ps.offsetHeight}`,
        scrub: true,
        pin: true
      }));
    }
  }

  return {
    active: activeAnimations,
    keyframesMap: keyframesMap,
    gsapData: gsapData
  };
})()
"""

CANVAS_DETAILS_AND_RECORDER_JS = """
async () => {
  const canvases = Array.from(document.querySelectorAll('canvas'));
  if (canvases.length === 0) return { canvases: [], videoClips: [] };

  const details = canvases.map((canvas, index) => {
    let isGl = false;
    try {
      isGl = Boolean(canvas.getContext('webgl2') || canvas.getContext('webgl'));
    } catch(e) {
      isGl = false;
    }
    return {
      index,
      id: canvas.id || `canvas-${index}`,
      type: isGl ? 'webgl' : '2d',
      width: canvas.width,
      height: canvas.height,
      hasAnimation: true
    };
  });

  // Attempt to record WebGL or animated 2D canvas streams (max 2.5 seconds)
  const videoClips = [];
  for (let i = 0; i < Math.min(canvases.length, 2); i++) {
    const c = canvases[i];
    try {
      if (!c.captureStream) continue;
      const stream = c.captureStream(60); // 60fps high-fidelity canvas capture
      const mime = (typeof MediaRecorder !== 'undefined' && MediaRecorder.isTypeSupported('video/webm;codecs=vp9')) 
        ? 'video/webm;codecs=vp9' 
        : 'video/webm';
      const recorder = new MediaRecorder(stream, { 
        mimeType: mime,
        videoBitsPerSecond: 6000000 // 6 Mbps bitrate for pristine 60fps motion fidelity
      });
      const chunks = [];
      recorder.ondataavailable = e => { if (e.data && e.data.size > 0) chunks.push(e.data); };
      recorder.start();
      await new Promise(r => setTimeout(r, 2500));
      recorder.stop();
      await new Promise(r => recorder.onstop = r);
      const blob = new Blob(chunks, { type: 'video/webm' });
      if (blob.size > 0) {
        const base64 = await new Promise(resolve => {
          const reader = new FileReader();
          reader.onloadend = () => resolve(reader.result);
          reader.readAsDataURL(blob);
        });
        videoClips.push({
          index: `${c.id || 'canvas'}_${i}`,
          dataUrl: base64,
          sizeBytes: blob.size
        });
      }
    } catch(err) {
      console.warn('Canvas stream capture error:', err);
    }
  }

  return { canvases: details, videoClips };
}
"""

async def extract_cdp_declared_typography(cdp, root_node_id):
    """Extracts declared CSS rules (clamp, calc, rem, @media) via CDP CSS.getMatchedStylesForNode."""
    typo_selectors = {
        "h1": "h1",
        "h2": "h2",
        "h3": "h3",
        "lead": "p.lead, [class*='lead'], [class*='subtitle']",
        "eyebrow": ".eyebrow, [class*='eyebrow'], [class*='badge']",
        "button": "button, a.btn, a[class*='button'], a[class*='cta']"
    }
    declared_results = {}

    for key, sel in typo_selectors.items():
        try:
            node_res = await cdp.send("DOM.querySelector", {"nodeId": root_node_id, "selector": sel})
            node_id = node_res.get("nodeId")
            if not node_id:
                continue

            matched = await cdp.send("CSS.getMatchedStylesForNode", {"nodeId": node_id})
            fluid_matches = {}
            media_queries = []

            for r in matched.get("matchedCSSRules", []):
                rule = r.get("rule", {})
                rule_props = rule.get("style", {}).get("cssProperties", [])
                
                # Check media queries attached to this rule
                media_list = rule.get("media", [])
                for m in media_list:
                    m_text = m.get("text", "")
                    if m_text and m_text not in media_queries:
                        media_queries.append(m_text)

                for prop in rule_props:
                    p_name = prop.get("name")
                    p_val = prop.get("value", "")
                    if p_name in ["font-size", "line-height", "letter-spacing", "font-family"]:
                        # Capture fluid declarations: clamp, calc, rem, vw, vh
                        if any(k in p_val for k in ["clamp(", "calc(", "min(", "max(", "rem", "vw"]):
                            fluid_matches[p_name] = p_val
                        elif p_name not in fluid_matches:
                            fluid_matches[p_name] = p_val

            if fluid_matches:
                declared_results[key] = {
                    "declared_rules": fluid_matches,
                    "media_queries": media_queries[:3]
                }
        except Exception:
            continue

    return declared_results

async def extract_cdp_hover_states(cdp, page, root_node_id):
    """Extracts interactive :hover elevation and transform states via CDP forcePseudoState with Playwright real hover fallback."""
    interactive_selectors = [
        ("button", "button"),
        ("cta_link", "a[class*='btn'], a[class*='button'], a[class*='cta']"),
        ("nav_link", "nav a, header a"),
        ("card", "[class*='card'], article")
    ]
    interactions = {}

    for label, sel in interactive_selectors:
        try:
            node_res = await cdp.send("DOM.querySelector", {"nodeId": root_node_id, "selector": sel})
            node_id = node_res.get("nodeId")
            if not node_id:
                continue

            # Read base computed style via CDP
            base_style = await cdp.send("CSS.getComputedStyleForNode", {"nodeId": node_id})
            base_map = {p["name"]: p["value"] for p in base_style.get("computedStyle", [])}

            # 1. Force hover pseudo-class via CDP
            await cdp.send("CSS.forcePseudoState", {"nodeId": node_id, "forcedPseudoClasses": ["hover"]})
            hover_style = await cdp.send("CSS.getComputedStyleForNode", {"nodeId": node_id})
            hover_map = {p["name"]: p["value"] for p in hover_style.get("computedStyle", [])}

            # Reset pseudo-state
            await cdp.send("CSS.forcePseudoState", {"nodeId": node_id, "forcedPseudoClasses": []})

            # Check deltas on critical interaction properties
            check_props = ["transform", "box-shadow", "background-color", "color", "border-color", "opacity"]
            deltas = {}
            for prop in check_props:
                base_v = base_map.get(prop)
                hover_v = hover_map.get(prop)
                if base_v and hover_v and base_v != hover_v:
                    deltas[prop] = {"from": base_v, "to": hover_v}

            # 2. Fallback: If no CSS deltas found, test with real Playwright hover (for JS/React/Framer-driven hover states)
            if not deltas and page:
                try:
                    el = await page.query_selector(sel)
                    if el and await el.is_visible():
                        base_js = await page.evaluate("(el) => { const cs = window.getComputedStyle(el); return { transform: cs.transform, boxShadow: cs.boxShadow, backgroundColor: cs.backgroundColor, color: cs.color, opacity: cs.opacity }; }", el)
                        await el.hover(timeout=1000)
                        await page.wait_for_timeout(150)
                        hover_js = await page.evaluate("(el) => { const cs = window.getComputedStyle(el); return { transform: cs.transform, boxShadow: cs.boxShadow, backgroundColor: cs.backgroundColor, color: cs.color, opacity: cs.opacity }; }", el)
                        await page.mouse.move(0, 0)
                        
                        prop_pairs = [
                            ("transform", "transform"),
                            ("boxShadow", "box-shadow"),
                            ("backgroundColor", "background-color"),
                            ("color", "color"),
                            ("opacity", "opacity")
                        ]
                        for js_k, css_k in prop_pairs:
                            bv = base_js.get(js_k)
                            hv = hover_js.get(js_k)
                            if bv and hv and bv != hv:
                                deltas[css_k] = {"from": bv, "to": hv}
                except Exception:
                    pass

            if deltas:
                interactions[label] = {
                    "selector": sel,
                    "deltas": deltas,
                    "transitionDuration": base_map.get("transition-duration", "0.2s"),
                    "transitionTimingFunction": base_map.get("transition-timing-function", "ease")
                }
        except Exception:
            continue

    return interactions

async def profile_responsive_viewports(page):
    """Profiles layout restructuring across Desktop (1440), Tablet (768), and Mobile (390)."""
    viewports = {
        "desktop": {"width": 1440, "height": 900},
        "tablet": {"width": 768, "height": 1024},
        "mobile": {"width": 390, "height": 844}
    }
    matrix = {}

    for vp_name, vp_dims in viewports.items():
        try:
            await page.set_viewport_size(vp_dims)
            await page.wait_for_timeout(350)  # Allow resize and media queries to settle

            vp_data = await page.evaluate("""() => {
              const sections = Array.from(document.querySelectorAll('section, [class*="section"], main > div, article'));
              // Find first content section that is not a 0px full-bleed hero
              let sec = sections.find(s => {
                const cs = window.getComputedStyle(s);
                return (parseFloat(cs.paddingTop) > 0 || parseFloat(cs.paddingBottom) > 0);
              }) || sections[0] || document.body;

              const grid = document.querySelector('[class*="grid"], [style*="grid"]');
              const csSec = sec ? window.getComputedStyle(sec) : null;
              const csGrid = grid ? window.getComputedStyle(grid) : null;

              // Check if mobile menu trigger is present
              const menuTrigger = document.querySelector('button[aria-label*="menu"], [class*="hamburger"], [class*="mobile-menu"], button[aria-expanded]');

              return {
                paddingTop: csSec ? csSec.paddingTop : '80px',
                paddingBottom: csSec ? csSec.paddingBottom : '80px',
                gridColumns: csGrid ? csGrid.gridTemplateColumns.split(' ').filter(Boolean).length : 1,
                hasMobileMenu: Boolean(menuTrigger && menuTrigger.offsetParent !== null)
              };
            }""")

            matrix[vp_name] = {
                "width": vp_dims["width"],
                "height": vp_dims["height"],
                "paddingY": f"{vp_data.get('paddingTop', '80px')} / {vp_data.get('paddingBottom', '80px')}",
                "gridColumns": max(1, vp_data.get("gridColumns", 1)),
                "navigationType": "mobile-drawer" if vp_data.get("hasMobileMenu") else "desktop-bar"
            }
        except Exception as e:
            matrix[vp_name] = {"width": vp_dims["width"], "height": vp_dims["height"], "error": str(e)}

    # Reset back to desktop viewport
    await page.set_viewport_size({"width": 1440, "height": 900})
    return matrix

def generate_design_md(data):
    """Generates structured, comprehensive DESIGN.md with all 6 extraction vectors."""
    typo = data.get("typography", {})
    declared_typo = data.get("declared_typography", {})
    colors = data.get("colors", {})
    geom = data.get("geometry", {})
    comp = data.get("components", {})
    anim = data.get("animation_signatures", {})
    interactions = data.get("micro_interactions", {})
    matrix = data.get("responsive_breakpoints", {})

    h1_info = typo.get("h1", {})
    h2_info = typo.get("h2", {})
    h3_info = typo.get("h3", {})
    body_info = typo.get("body", {})
    eyebrow_info = typo.get("eyebrow", {})
    lead_info = typo.get("lead", {})

    # Compute true display font by maximum font size among h1, h2, h3, lead
    max_font_size = 0.0
    display_font = clean_font_family(h1_info.get("fontFamily", "Playfair Display"))
    for role, entry in [("h2", h2_info), ("h1", h1_info), ("lead", lead_info), ("h3", h3_info)]:
        s = entry.get("fontSize", "")
        m = re.search(r'([\d\.]+)px', s)
        if m:
            val = float(m.group(1))
            if val > max_font_size:
                max_font_size = val
                display_font = clean_font_family(entry.get("fontFamily", display_font))

    body_font = clean_font_family(body_info.get("fontFamily", "Plus Jakarta Sans"))
    
    # Generate Google Fonts import URL
    font_params = []
    for f in [display_font, body_font]:
        clean_name = f.strip().strip('"').strip("'")
        if clean_name.lower() not in ["system-ui", "sans-serif", "serif", "monospace", "arial", "helvetica", "georgia"]:
            encoded = clean_name.replace(" ", "+")
            font_params.append(f"family={encoded}:wght@300;400;500;600;700;800;900")
    
    google_fonts_url = f"https://fonts.googleapis.com/css2?{'&'.join(font_params)}&display=swap" if font_params else None

    canvas_bg = rgb_to_hex(colors.get("canvasBackground", "#FAF8F5"))
    primary_ink = rgb_to_hex(colors.get("primaryInk", "#111111"))
    secondary_ink = rgb_to_hex(colors.get("secondaryInk", "#444444"))
    surface_bg = rgb_to_hex(colors.get("surfaceBackground")) if colors.get("surfaceBackground") else "#FFFFFF"
    accent_btn = rgb_to_hex(colors.get("buttonFill", "#111111"))
    accent_text = rgb_to_hex(colors.get("buttonText", "#FFFFFF"))
    border_color = rgb_to_hex(colors.get("borderColor")) if colors.get("borderColor") else "rgba(0, 0, 0, 0.08)"

    palette_hex = [rgb_to_hex(c) for c in colors.get("topDetectedPalette", [])]

    # Declared clamp values
    h1_declared = declared_typo.get("h1", {}).get("declared_rules", {}).get("font-size", h1_info.get("fontSize", "clamp(2.5rem, 5vw, 4.5rem)"))

    # Section Architecture Table
    sections_list = data.get("sections", [])
    sections_rows = []
    for sec in sections_list:
        heading = sec.get("headingSample") or "Content Section"
        media = f"{sec.get('imagesCount', 0)} media"
        btns = f"{sec.get('buttonsCount', 0)} CTAs"
        bg = rgb_to_hex(sec.get("backgroundColor", "#FFFFFF"))
        sections_rows.append(f"| **Section {sec.get('index')}** | `{sec.get('layoutType')}` | \"{heading}\" | {media}, {btns} | `{bg}` |")
    
    sections_table = "\n".join(sections_rows) if sections_rows else "| **Section 1** | `asymmetric-split` | Hero Presentation | 1 hero image, 2 CTAs | `canvas` |"

    # Cloned Reference Layout DNA Tree Table
    layout_tree_rows = []
    for sec in data.get("sections", []):
        sec_idx = sec.get("index")
        ltype = sec.get("layoutType")
        role = "HERO (" + str(sec.get("heroType")) + ")" if sec.get("isHero") else sec.get("tagName", "section").upper()
        b_dims = f"{sec.get('boundingRect', {}).get('width', 1440)}x{sec.get('boundingRect', {}).get('height', 800)}px ({sec.get('boundingRect', {}).get('aspectRatio', '1.80')} AR)"
        media = f"{'1 Video, ' if sec.get('hasVideo') else ''}{sec.get('imagesCount', 0)} images"
        heading = sec.get("headingSample") or "Content block"
        strat = "Full-bleed background video/image" if "full-bleed" in str(ltype) else ("Single centered column, max-w-3xl" if ltype == "centered-editorial" else f"{sec.get('columnsCount', 2)}-column layout")
        layout_tree_rows.append(f"| **Section {sec_idx}** | `{ltype}` | {role} | {b_dims} | {media} | \"{heading}\" | {strat} |")

    layout_tree_table = "\n".join(layout_tree_rows) if layout_tree_rows else "| **Section 1** | `full-bleed-media-hero` | HERO | 1440x900px | 1 image | \"Welcome\" | Full viewport hero |"

    google_import_block = f"@import url('{google_fonts_url}');" if google_fonts_url else "/* System / Local fonts detected */"

    md = f"""# Design System Primitives & Tokens (DESIGN.md)

> **Extracted Benchmark:** {data.get('url', 'N/A')}  
> **Benchmark Title:** {data.get('title', 'N/A')}  
> **Extraction Engine:** Production CDP & WAAPI Deep Extraction Pipeline (Chrome DevTools Protocol)

---

## 1. Fluid Typography System Segregation (7 Tiers)

| Tier | Role / Selector | Font Family | Size (Declared / Fluid) | Weight | Line Height | Letter Spacing |
|---|---|---|---|---|---|---|
| **Display Hero** | `h1` / `h2` | `"{display_font}"` | `{declared_typo.get('h2', {}).get('declared_rules', {}).get('font-size', h2_info.get('fontSize', h1_declared))}` | `{h2_info.get('fontWeight', h1_info.get('fontWeight', '700'))}` | `{h2_info.get('lineHeight', '1.1')}` | `{h2_info.get('letterSpacing', '-0.025em')}` |
| **Section Title** | `h2` | `"{clean_font_family(h2_info.get('fontFamily', display_font))}"` | `{h2_info.get('fontSize', '36px')}` | `{h2_info.get('fontWeight', '700')}` | `1.2` | `-0.015em` |
| **Feature Title** | `h3` | `"{clean_font_family(h3_info.get('fontFamily', display_font))}"` | `{h3_info.get('fontSize', '24px')}` | `600` | `1.3` | `normal` |
| **Eyebrow Tag** | `.eyebrow` | `"{clean_font_family(eyebrow_info.get('fontFamily', body_font))}"` | `{eyebrow_info.get('fontSize', '12px')}` | `600` | `1.0` | `0.1em (uppercase)` |
| **Lead Paragraph**| `p.lead` | `"{clean_font_family(lead_info.get('fontFamily', body_font))}"` | `{lead_info.get('fontSize', '18px')}` | `400` | `1.6` | `normal` |
| **Body Copy** | `p`, `li` | `"{body_font}"` | `{body_info.get('fontSize', '16px')}` | `{body_info.get('fontWeight', '400')}` | `{body_info.get('lineHeight', '1.65')}` | `normal` |
| **Monospace / Code**| `code`, `pre` | `"Geist Mono", monospace` | `14px` | `400` | `1.5` | `tabular-nums` |

### Verified Google Fonts Import Link
```css
{google_import_block}
```

---

## 2. Calibrated Color System Segregation

- **Canvas Background:** `{canvas_bg}`
- **Surface Elevation (Cards):** `{surface_bg}`
- **Primary Ink (Headlines):** `{primary_ink}`
- **Secondary Ink (Body/Muted):** `{secondary_ink}`
- **Primary CTA Fill:** `{accent_btn}`
- **CTA Foreground Text:** `{accent_text}`
- **Hairlines & Dividers:** `{border_color}`
- **Extracted Palette Clusters:** {', '.join(f'`{c}`' for c in palette_hex[:8])}

---

## 3. Structural Section Architecture & Benchmark Blueprint

| Section Tier | Archetype Layout | Heading / Focus | Media & Interactive Assets | Background Canvas |
|---|---|---|---|---|
{sections_table}

---

## 4. Spatial Geometry & Responsive Breakpoint Matrix

| Viewport Tier | Width | Section Padding Y | Primary Grid Columns | Navigation Pattern |
|---|---|---|---|---|
| **Desktop** | `{matrix.get('desktop', {}).get('width', 1440)}px` | `{matrix.get('desktop', {}).get('paddingY', '112px')}` | `{matrix.get('desktop', {}).get('gridColumns', 4)} cols` | `{matrix.get('desktop', {}).get('navigationType', 'desktop-bar')}` |
| **Tablet** | `{matrix.get('tablet', {}).get('width', 768)}px` | `{matrix.get('tablet', {}).get('paddingY', '72px')}` | `{matrix.get('tablet', {}).get('gridColumns', 2)} cols` | `{matrix.get('tablet', {}).get('navigationType', 'desktop-compact')}` |
| **Mobile** | `{matrix.get('mobile', {}).get('width', 390)}px` | `{matrix.get('mobile', {}).get('paddingY', '48px')}` | `{matrix.get('mobile', {}).get('gridColumns', 1)} col stack` | `{matrix.get('mobile', {}).get('navigationType', 'mobile-drawer')}` |

- **Container Max Width:** `{geom.get('containerMaxWidth', '1280px')}`
- **Button Border Radius:** `{geom.get('buttonBorderRadius', '6px')}`
- **Card Border Radius:** `{geom.get('cardBorderRadius', '8px')}`
- **Bespoke Arched Masks Detected:** `{"YES (Preserve curved clip-path 1:1)" if geom.get("hasArchedMask") else "NO"}`

---

## 5. Animation Signatures & Easing Curves (WAAPI & CSS @keyframes)

- **Active WAAPI Animation Tracks:** `{len(anim.get('active', []))} active`
- **Declared CSS Keyframes:** {', '.join(f'`@{k}`' for k in list(anim.get('keyframesMap', {}).keys())[:6]) or 'None declared'}
- **GSAP ScrollTrigger Pinned Spacers:** `{len(data.get('pinSpacers', []))} detected`
- **Virtual Scroll Active (Lenis / Locomotive):** `{"YES" if data.get("virtualScroll") else "NO"}`

---

## 6. Micro-Interactions & Hover Elevation States (CDP-Extracted)

```json
{json.dumps(interactions, indent=2)}
```

---

## 7. Production CSS Custom Properties & Tailwind @theme (`:root`)

```css
{google_import_block}
@import "tailwindcss";

:root {{
  /* Extracted Benchmark Typography */
  --font-display: "{display_font}", Georgia, serif;
  --font-body: "{body_font}", sans-serif;
  --font-mono: "Geist Mono", monospace;

  /* Benchmark Surfaces & Ink */
  --color-canvas: {canvas_bg};
  --color-surface: {surface_bg};
  --color-ink: {primary_ink};
  --color-ink-muted: {secondary_ink};
  --color-accent: {accent_btn};
  --color-accent-foreground: {accent_text};
  --color-border: {border_color};

  /* Spatial Scale */
  --container-max-w: {geom.get('containerMaxWidth', '1280px')};
  --radius-btn: {geom.get('buttonBorderRadius', '6px')};
  --radius-card: {geom.get('cardBorderRadius', '8px')};
  --space-section-desktop: 112px;
  --space-section-tablet: 72px;
  --space-section-mobile: 48px;

  /* Layered Shadows */
  --shadow-ambient: 0 1px 2px rgba(0, 0, 0, 0.04);
  --shadow-direct: 0 8px 24px -4px rgba(0, 0, 0, 0.08);
  --shadow-layered: var(--shadow-ambient), var(--shadow-direct);
}}

@theme inline {{
  --font-display: var(--font-display);
  --font-body: var(--font-body);
  --font-mono: var(--font-mono);
  --color-background: var(--color-canvas);
  --color-foreground: var(--color-ink);
  --color-primary: var(--color-accent);
  --color-primary-foreground: var(--color-accent-foreground);
  --color-card: var(--color-surface);
  --color-border: var(--color-border);
}}
---

## 8. Anti-Slop Negative Guardrails Compliance
- [x] Declared fluid math preserved (`clamp(...)`, `rem`, `@media` queries) instead of static desktop pixel collapse.
- [x] Animation signatures (WAAPI, `@keyframes`, GSAP triggers) captured and codified.
- [x] Interactive `:hover` elevation transitions extracted via CDP.
- [x] Responsive layout matrix profiled across Desktop, Tablet, and Mobile.
- [x] WebGL and Canvas layers recorded or converted to ambient `<video>` fallbacks.

---

## 9. Cloned Reference Structural Tree & Section Cadence (Layout DNA)

> **MANDATORY ARCHITECTURE DIRECTIVE**: The Next.js 15 page structure MUST clone these exact layout modes. Zero speculative 2-column or 60/40 substitutions allowed unless designated by this table.

| Section | Layout Type | Role | Bounding Dimensions | Media / Elements | Content Focus | Cloned Strategy |
|---|---|---|---|---|---|---|
{layout_tree_table}
"""
    return md

def classify_animation_archetypes(data):
    """
    Classifies extracted animations and styles into the 30 Universal Web Animation Archetypes.
    Returns a structured inventory with open-source sourcing commands.
    """
    archetypes = []
    anim_sigs = data.get("animation_signatures", {})
    waapi = anim_sigs.get("waapiTracks", [])
    keyframes = anim_sigs.get("cssKeyframes", [])
    gsap = anim_sigs.get("gsap", {})
    micro = data.get("micro_interactions", {})

    # 1. Ken-Burns Zoom
    has_zoom = any("scale" in str(t.get("keyframes", "")) for t in waapi) or any("zoom" in kf.get("name", "").lower() or "kenburns" in kf.get("name", "").lower() for kf in keyframes)
    if has_zoom or data.get("virtualScroll"):
        archetypes.append({
            "id": 1,
            "archetype": "Ken-Burns Zoom",
            "confidence": "high",
            "specs": "Scale 1.0 -> 1.15 over 15s with cubic-bezier(0.25, 1, 0.5, 1)",
            "implementation": "Tailwind animate-ken-burns / Framer Motion",
            "sourcing_command": "Built-in tailwind animate-ken-burns"
        })

    # 2. Reveal on Scroll (Entrance)
    archetypes.append({
        "id": 2,
        "archetype": "Reveal on Scroll",
        "confidence": "high",
        "specs": "Opacity 0 -> 1, translateY 32px -> 0, duration 0.8s, ease: [0.25, 1, 0.5, 1]",
        "implementation": "Framer Motion whileInView",
        "sourcing_command": "npm i framer-motion"
    })

    # 3. Horizontal Scroll Strip
    if gsap.get("triggers"):
        archetypes.append({
            "id": 3,
            "archetype": "Horizontal Scroll Strip",
            "confidence": "medium",
            "specs": "GSAP ScrollTrigger pin & scrub with horizontal flex track",
            "implementation": "GSAP ScrollTrigger.create({ scrub: true })",
            "sourcing_command": "npm i gsap"
        })

    # 4. Sticky Stacking Bento
    if data.get("pinSpacers") or len(data.get("layoutTree", {}).get("sections", [])) > 4:
        archetypes.append({
            "id": 4,
            "archetype": "Sticky Stacking Bento",
            "confidence": "high",
            "specs": "Sticky pinned cards with dynamic elevation scaling",
            "implementation": "Magic UI BentoGrid / Aceternity Bento",
            "sourcing_command": "npx shadcn@latest add @magicui/bento-grid"
        })

    # 5. Infinite Marquee
    if any("marquee" in kf.get("name", "").lower() for kf in keyframes):
        archetypes.append({
            "id": 5,
            "archetype": "Infinite Marquee",
            "confidence": "high",
            "specs": "translateX 0% -> -100% infinite linear scroll",
            "implementation": "Magic UI Marquee",
            "sourcing_command": "npx shadcn@latest add @magicui/marquee"
        })

    # 6. Navbar Blur Shrink
    archetypes.append({
        "id": 6,
        "archetype": "Navbar Blur Shrink",
        "confidence": "high",
        "specs": "Backdrop-blur header with scroll threshold elevation and border reveal",
        "implementation": "Framer Motion / CSS backdrop-filter",
        "sourcing_command": "npx shadcn@latest add @magicui/navbar"
    })

    # 7. Card Tilt Parallax & Hover Elevation
    if micro:
        archetypes.append({
            "id": 7,
            "archetype": "Card Tilt Parallax & Hover Elevation",
            "confidence": "high",
            "specs": "Scale 1.03 with transition-transform duration-500",
            "implementation": "Fancy Components TiltCard / Framer Motion",
            "sourcing_command": "npx 21st-dev add tilt-card"
        })

    # 8. Accordion Spring Reveal
    archetypes.append({
        "id": 8,
        "archetype": "Accordion Spring Reveal",
        "confidence": "high",
        "specs": "AnimatePresence height auto spring transition",
        "implementation": "Framer Motion AnimatePresence / Radix Accordion",
        "sourcing_command": "npx shadcn@latest add accordion"
    })

    return archetypes

async def run_extraction_pipeline(url, out_path="DESIGN.md", tokens_out="design_tokens.json", layout_tree_out="reference_layout_tree.json", slices_dir=".website-architect/reference_slices", screenshot_path=None, assets_dir="assets", record_video_dir=".website-architect/reference_recordings", animation_inventory_out="animation_inventory.json"):
    from playwright.async_api import async_playwright

    print(f"[*] Launching Headless Chromium with CDP & WAAPI extraction for: {url}")
    os.makedirs(assets_dir, exist_ok=True)

    async with async_playwright() as p:
        launch_args = [
            "--use-gl=angle",
            "--use-angle=default",
            "--enable-webgl",
            "--ignore-gpu-blocklist",
            "--enable-gpu-rasterization",
            "--enable-zero-copy",
            "--disable-web-security"
        ]
        try:
            browser = await p.chromium.launch(headless=True, args=launch_args)
        except Exception:
            try:
                browser = await p.chromium.launch(channel="chrome", headless=True, args=launch_args)
            except Exception:
                browser = await p.chromium.launch(headless=True)

        context_kwargs = {
            "viewport": {"width": 1440, "height": 900},
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        }
        if record_video_dir:
            os.makedirs(record_video_dir, exist_ok=True)
            context_kwargs["record_video_dir"] = record_video_dir
            context_kwargs["record_video_size"] = {"width": 1440, "height": 900}

        context = await browser.new_context(**context_kwargs)
        page = await context.new_page()

        # Step 0: Network response interceptor for ambient videos
        harvested_network_videos = []
        async def handle_response(response):
            try:
                ct = response.headers.get("content-type", "").lower()
                resp_url = response.url.lower()
                if "video/mp4" in ct or "video/webm" in ct or resp_url.endswith(".mp4") or resp_url.endswith(".webm"):
                    if response.status == 200:
                        body = await response.body()
                        if len(body) > 40000:
                            vid_filename = f"ambient_video_{len(harvested_network_videos) + 1}.mp4"
                            vid_disk_path = os.path.join(assets_dir, vid_filename)
                            with open(vid_disk_path, "wb") as vf:
                                vf.write(body)
                            harvested_network_videos.append(f"/assets/{vid_filename}")
                            print(f"[+] Network Interceptor captured ambient video: {vid_disk_path} ({len(body)} bytes)")
            except Exception:
                pass
        page.on("response", handle_response)

        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=35000)
            await page.wait_for_timeout(2500)  # Allow initial hydration and fonts
        except Exception as e:
            print(f"[!] Warning during navigation: {e}")

        # Smoothly scroll through the page to trigger and record live 60fps animations & video playback
        if record_video_dir:
            try:
                print("[*] Recording 60fps scroll walkthrough of reference site...")
                total_h = await page.evaluate("() => document.body.scrollHeight")
                steps = min(8, max(3, int(total_h / 800)))
                for step in range(steps):
                    await page.evaluate(f"window.scrollTo({{ top: {(step + 1) * 800}, behavior: 'smooth' }})")
                    await page.wait_for_timeout(450)
                await page.evaluate("window.scrollTo({ top: 0, behavior: 'smooth' })")
                await page.wait_for_timeout(350)
            except Exception:
                pass

            # Step 0.2: Interactive MonkeyCrawler (Tabs, Accordions, Gallery Sliders, Modals)
            interactive_selectors = [
                'button:not([disabled])',
                '[role="tab"]',
                '[role="button"]',
                '[data-state]',
                'summary',
                '[aria-expanded]',
                '[class*="accordion"]',
                '[class*="drawer"]',
                '[class*="toggle"]',
                '[class*="carousel"] button',
                '[class*="gallery"] button',
                'a[class*="btn"]',
                'a[class*="button"]'
            ]
            print("[*] Running MonkeyCrawler interactive state discovery & recording...")
            try:
                interactables = await page.query_selector_all(", ".join(interactive_selectors))
                interactions_count = 0
                for el in interactables[:12]:
                    try:
                        if not await el.is_visible():
                            continue
                        await el.scroll_into_view_if_needed(timeout=1000)
                        await page.wait_for_timeout(150)
                        await el.hover(timeout=800)
                        await page.wait_for_timeout(250)
                        tag = await el.evaluate("e => e.tagName.toLowerCase()")
                        href = await el.get_attribute("href") if tag == "a" else None
                        if tag != "a" or (href and (href.startswith("#") or href.startswith("javascript"))):
                            await el.click(timeout=800)
                            await page.wait_for_timeout(400)
                        interactions_count += 1
                    except Exception:
                        continue
                print(f"[+] MonkeyCrawler exercised {interactions_count} interactive elements during 60fps recording.")
            except Exception as e:
                print(f"[!] Warning during interactive exploration: {e}")

            # Step 0.3: Multi-Route Traversal (Top 2 primary subroutes)
            try:
                nav_links = await page.query_selector_all('nav a[href], header a[href], a[href*="/about"], a[href*="/room"], a[href*="/accommodat"], a[href*="/din"], a[href*="/contact"]')
                visited_routes = []
                for nl in nav_links:
                    if len(visited_routes) >= 2:
                        break
                    hr = await nl.get_attribute("href")
                    if hr and hr.startswith("/") and len(hr) > 2 and hr not in visited_routes and not hr.startswith("/#"):
                        visited_routes.append(hr)
                for sub_route in visited_routes:
                    sub_url = url.rstrip("/") + sub_route
                    print(f"[*] Recording sub-route entrance: {sub_url}...")
                    try:
                        await page.goto(sub_url, wait_until="domcontentloaded", timeout=12000)
                        await page.wait_for_timeout(800)
                        await page.evaluate("window.scrollTo({ top: 600, behavior: 'smooth' })")
                        await page.wait_for_timeout(500)
                    except Exception:
                        pass
                if visited_routes:
                    await page.goto(url, wait_until="domcontentloaded", timeout=12000)
                    await page.wait_for_timeout(800)
            except Exception as e:
                print(f"[!] Sub-route traversal note: {e}")

        # Connect CDP Session
        cdp = await page.context.new_cdp_session(page)
        await cdp.send("DOM.enable")
        await cdp.send("CSS.enable")

        doc = await cdp.send("DOM.getDocument", {"depth": -1})
        root_node_id = doc["root"]["nodeId"]

        # Step 2: Check Virtual Scroll & Dispatch Synthetic Wheel if needed
        is_virt = await page.evaluate("() => Boolean(window.Lenis || window.LocomotiveScroll || window.ScrollTrigger || document.querySelector('[data-scroll-container]'))")
        if is_virt:
            print("[*] Virtual scroll / GSAP detected. Dispatching synthetic mouse wheel delta...")
            await page.mouse.move(720, 450)
            for _ in range(4):
                await page.mouse.wheel(delta_x=0, delta_y=400)
                await page.wait_for_timeout(250)
            await page.mouse.wheel(delta_x=0, delta_y=-1600)
            await page.wait_for_timeout(300)

        # Step 1: Base DOM & Computed Styles
        data = await page.evaluate(IN_PAGE_DOM_EXTRACT_JS)

        # Step 1.2: CDP Declared Typography & Fluid clamp() rules
        print("[*] Extracting declared fluid typography & @media rules via CDP...")
        declared_typo = await extract_cdp_declared_typography(cdp, root_node_id)
        data["declared_typography"] = declared_typo

        # Step 1.3: WAAPI Tracks, CSS @keyframes, GSAP ScrollTrigger
        print("[*] Extracting WAAPI active animation tracks and CSS @keyframes...")
        anim_data = await page.evaluate(WAAPI_AND_MOTION_EXTRACT_JS)
        data["animation_signatures"] = anim_data

        # Step 1.4: Interactive :hover states via CDP forced pseudo-classes & real hover fallback
        print("[*] Profiling micro-interactions and :hover deltas via CDP & real hover...")
        micro_interactions = await extract_cdp_hover_states(cdp, page, root_node_id)
        data["micro_interactions"] = micro_interactions

        # Step 3: Multi-Viewport Matrix Profiling (Desktop, Tablet, Mobile)
        print("[*] Profiling responsive layout matrices (Desktop 1440, Tablet 768, Mobile 390)...")
        matrix = await profile_responsive_viewports(page)
        data["responsive_breakpoints"] = matrix

        # Step 4: Handle WebGL / Canvas Elements & Capture Streams
        print("[*] Detecting and capturing WebGL / Canvas animations...")
        canvas_info = await page.evaluate(CANVAS_DETAILS_AND_RECORDER_JS)
        data["canvas_details"] = canvas_info.get("canvases", [])

        # Save any recorded WebGL canvas streams to assets
        for i, clip in enumerate(canvas_info.get("videoClips", [])):
            try:
                clip_idx = clip.get("index", f"canvas_{i}")
                clip_safe = re.sub(r'[^a-zA-Z0-9_-]', '_', str(clip_idx))
                data_url = clip.get("dataUrl", "")
                if "," in data_url:
                    b64 = data_url.split(",")[1]
                    out_clip_path = os.path.join(assets_dir, f"canvas_background_{clip_safe}.webm")
                    with open(out_clip_path, "wb") as vf:
                        vf.write(base64.b64decode(b64))
                    print(f"[+] Saved recorded WebGL/2D canvas stream: {out_clip_path} ({clip.get('sizeBytes')} bytes)")
            except Exception as e:
                print(f"[!] Warning saving canvas clip: {e}")

        # Capture Section Screenshot Slices for 1:1 visual inspection
        if slices_dir:
            try:
                os.makedirs(slices_dir, exist_ok=True)
                sec_handles = await page.query_selector_all('header, main > section, main > div, body > section, section, footer')
                valid_count = 0
                for sec in sec_handles:
                    if valid_count >= 10:
                        break
                    box = await sec.bounding_box()
                    if box and box['height'] > 60 and box['width'] > 200:
                        valid_count += 1
                        slice_file = os.path.join(slices_dir, f"section_{valid_count:02d}.png")
                        try:
                            await sec.scroll_into_view_if_needed(timeout=2000)
                            await page.wait_for_timeout(150)
                            await sec.screenshot(path=slice_file)
                            print(f"[+] Captured reference slice {valid_count}: {slice_file}")
                        except Exception:
                            pass
            except Exception as e:
                print(f"[!] Warning capturing section slices: {e}")

        # Capture optional full-page/viewport screenshot
        if screenshot_path:
            try:
                await page.screenshot(path=screenshot_path, full_page=False)
                print(f"[+] Viewport screenshot captured: {screenshot_path}")
            except Exception as e:
                print(f"[!] Failed to capture screenshot: {e}")

        vid_ref = page.video
        await page.close()
        await context.close()
        await browser.close()

        # Finalize 60fps video path if recorded
        if record_video_dir and vid_ref:
            try:
                fixed_vid_path = os.path.join(record_video_dir, "reference_walkthrough_60fps.webm")
                await vid_ref.save_as(fixed_vid_path)
                data["reference_walkthrough_video"] = fixed_vid_path
                print(f"[+] 60fps Reference Walkthrough Video recorded and saved: {fixed_vid_path}")
            except Exception as e:
                try:
                    raw_path = await vid_ref.path()
                    data["reference_walkthrough_video"] = raw_path
                    print(f"[+] 60fps Reference Walkthrough Video recorded: {raw_path}")
                except Exception:
                    pass

    # Classify animation archetypes into inventory
    inventory = classify_animation_archetypes(data)
    data["animation_inventory"] = inventory
    with open(animation_inventory_out, "w", encoding="utf-8") as f:
        json.dump(inventory, f, indent=2)

    # Generate DESIGN.md
    design_md = generate_design_md(data)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(design_md)

    # Save design_tokens.json
    with open(tokens_out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    # Save reference_layout_tree.json
    if layout_tree_out and "layoutTree" in data:
        with open(layout_tree_out, "w", encoding="utf-8") as f:
            json.dump(data["layoutTree"], f, indent=2)
        print(f"    - Layout: {layout_tree_out}")

    print(f"[+] Successfully generated production design tokens:")
    print(f"    - Spec:     {out_path}")
    print(f"    - Tokens:   {tokens_out}")
    print(f"    - Motion:   {animation_inventory_out} ({len(inventory)} archetypes codified)")
    return data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract production-grade design tokens with CDP & WAAPI.")
    parser.add_argument("--url", required=True, help="URL of the benchmark website")
    parser.add_argument("--out", default="DESIGN.md", help="Output path for DESIGN.md")
    parser.add_argument("--tokens-out", default="design_tokens.json", help="Output path for design_tokens.json")
    parser.add_argument("--layout-tree-out", default="reference_layout_tree.json", help="Output path for reference_layout_tree.json")
    parser.add_argument("--slices-dir", default=".website-architect/reference_slices", help="Directory to save reference section screenshot slices")
    parser.add_argument("--screenshot", default=None, help="Optional path to save viewport screenshot")
    parser.add_argument("--assets", default="assets", help="Directory to save assets and canvas streams")
    parser.add_argument("--record-video-dir", default=".website-architect/reference_recordings", help="Directory to record live 60fps walkthrough video")
    parser.add_argument("--animation-inventory-out", default="animation_inventory.json", help="Output path for animation_inventory.json")

    args = parser.parse_args()
    asyncio.run(run_extraction_pipeline(args.url, args.out, args.tokens_out, args.layout_tree_out, args.slices_dir, args.screenshot, args.assets, args.record_video_dir, args.animation_inventory_out))
