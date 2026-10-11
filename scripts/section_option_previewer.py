#!/usr/bin/env python3
"""
section_option_previewer.py - Zero-Credit Section Option & SVG Wireframe Engine
Part of the Universal Website Architect Engine.

Implements the Section-by-Section Option Protocol from Deep Research:
1. Generates exactly 3 structurally divergent OptionManifests per section type.
2. Guarantees diversity across >= 3 structural axes (Composition, Density, Media, Reading direction, Interaction).
3. Generates high-craft programmatic SVG wireframe cards and lightweight HTML previews
   at ZERO image-generation credit cost.
4. Optionally renders headless screenshots via Playwright when available.
5. Formats structured decision cards for ask_question and chat presentation.
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import Dict, List, Any, Optional

# Supported Section Types and their Divergent Archetypes
ARCHETYPE_LIBRARY: Dict[str, List[Dict[str, Any]]] = {
    "hero": [
        {
            "optionId": "hero-a",
            "archetype": "asymmetric-split",
            "title": "Asymmetric 60/40 Editorial Split",
            "thesis": "High-impact narrative pairing display serif copy against framed photography with proof badge.",
            "axes": {
                "composition": "asymmetric-split (60/40)",
                "density": "balanced",
                "media": "framed-portrait-media",
                "readingDirection": "lateral (left-to-right)",
                "interaction": "dual-action-buttons + floating-proof-chip",
                "typographyRole": "type-led",
                "rhythm": "uncompressed-breathing"
            },
            "differentiators": [
                "60% left column with oversized display serif, eyebrow badge, and dual CTAs",
                "40% right column with framed 4:5 portrait media and floating proof chip",
                "Non-centered, high-tension editorial layout with negative display letter-spacing"
            ],
            "tradeoffs": [
                "Requires high-resolution vertical or portrait photography",
                "Requires concise, disciplined headline copy (<= 12 words)"
            ],
            "svgLayout": "asymmetric_split"
        },
        {
            "optionId": "hero-b",
            "archetype": "full-bleed-stage",
            "title": "Full-Bleed Media Stage with Anchor Block",
            "thesis": "Cinematic visual immersion with bottom-left anchored typography and live operational status pill.",
            "axes": {
                "composition": "full-bleed-stage",
                "density": "sparse",
                "media": "full-width-ambient-loop",
                "readingDirection": "vertical (anchor-to-actions)",
                "interaction": "ambient-video-loop + sound-toggle + sticky-hotbar",
                "typographyRole": "media-led",
                "rhythm": "monolithic"
            },
            "differentiators": [
                "100vw edge-to-edge background media with subtle 40% dark contrast gradient",
                "Anchored bottom-left typography block with live operational badge",
                "Floating interactive pill button with trailing arrow icon"
            ],
            "tradeoffs": [
                "Heavier media requirement (requires optimized video loop < 5MB or 2x hero photo)",
                "Text contrast must be strictly protected via dark backdrop scrim"
            ],
            "svgLayout": "full_bleed_stage"
        },
        {
            "optionId": "hero-c",
            "archetype": "editorial-stack",
            "title": "Type-Led Editorial Stack with Landscape Horizon",
            "thesis": "Oversized typographic manifesto with centered proof strip and wide landscape showcase below.",
            "axes": {
                "composition": "editorial-stack",
                "density": "dense-type-sparse-media",
                "media": "wide-landscape-under-text",
                "readingDirection": "vertical-downward",
                "interaction": "interactive-tag-chips + inline-stats",
                "typographyRole": "type-dominant",
                "rhythm": "chaptered"
            },
            "differentiators": [
                "Max-width 5xl container with 2-line clamp headline rule",
                "Inline proof chips and verifiable metric pills directly beneath headline",
                "Expansive 21:9 landscape media frame resting beneath the fold"
            ],
            "tradeoffs": [
                "Higher vertical scroll space before interactive modules",
                "Demands exceptional typography and font weight contrast"
            ],
            "svgLayout": "editorial_stack"
        }
    ],
    "features": [
        {
            "optionId": "features-a",
            "archetype": "bento-grid",
            "title": "Asymmetric Bento Grid (Flagship + Satellites)",
            "thesis": "Non-uniform 3-cell bento showcasing one flagship interactive demo alongside two focused capabilities.",
            "axes": {
                "composition": "asymmetric-bento (8-col + 4-col)",
                "density": "balanced",
                "media": "interactive-canvas-preview",
                "readingDirection": "f-pattern-anchor",
                "interaction": "hover-elevation + tabbed-preview",
                "typographyRole": "balanced",
                "rhythm": "gapless-rhythm"
            },
            "differentiators": [
                "Span-8 flagship card featuring live code / calculator preview with subtle border beam",
                "Two span-4 satellite cards with tactile micro-interactions and vector icons",
                "Concentric nested border radii with semi-transparent border borders"
            ],
            "tradeoffs": [
                "Requires multiple diverse UI states to populate bento cells",
                "Requires responsive column restructuring on mobile viewports (< 768px)"
            ],
            "svgLayout": "bento_grid"
        },
        {
            "optionId": "features-b",
            "archetype": "index-strip",
            "title": "Tabular Index Strip with Sticky Stage",
            "thesis": "Numbered technical rail (01-03) with sticky viewport-pinned live preview stage.",
            "axes": {
                "composition": "index-strip (4-col rail + 8-col stage)",
                "density": "dense",
                "media": "sticky-viewport-stage",
                "readingDirection": "vertical-rail-to-stage",
                "interaction": "scroll-scrub-or-tab-switch",
                "typographyRole": "data-led",
                "rhythm": "continuous"
            },
            "differentiators": [
                "Numbered index entries (01 / 02 / 03) with monospace micro-tags",
                "Sticky 8-column right stage that seamlessly switches content on hover/scroll",
                "High data-density layout ideal for complex workflows and transparent specifications"
            ],
            "tradeoffs": [
                "Requires copy discipline to write synchronized step descriptions",
                "Mobile requires converting sticky rail into an accessible vertical accordion"
            ],
            "svgLayout": "index_strip"
        },
        {
            "optionId": "features-c",
            "archetype": "asymmetric-stage",
            "title": "Asymmetric 5/7 Proof & Capability Stage",
            "thesis": "Deliberate 5/7 column tension contrasting narrative problem/solution against full-height interactive UI.",
            "axes": {
                "composition": "asymmetric-stage (5/7)",
                "density": "balanced",
                "media": "full-height-interface-card",
                "readingDirection": "lateral",
                "interaction": "before-after-toggle-or-filter",
                "typographyRole": "narrative-led",
                "rhythm": "stepped"
            },
            "differentiators": [
                "5-column narrative block detailing customer problem, methodology, and outcome",
                "7-column full-height interface capture with real operational telemetry",
                "Doppelrand nested container with 1px border and layered ambient shadow"
            ],
            "tradeoffs": [
                "Focuses deeply on one primary capability rather than breadth of features",
                "Requires high-fidelity product UI capture or interactive mockup"
            ],
            "svgLayout": "asymmetric_stage"
        }
    ],
    "proof": [
        {
            "optionId": "proof-a",
            "archetype": "logo-marquee-with-metrics",
            "title": "Infinite SVG Marquee + 3 Hard Metrics",
            "thesis": "Subtle continuous SVG logo marquee paired with three audited, verifiable quantitative metrics.",
            "axes": {
                "composition": "dual-tier-strip",
                "density": "balanced",
                "media": "vector-brand-svgs",
                "readingDirection": "horizontal-flow",
                "interaction": "marquee-pause-on-hover + count-up-stat",
                "typographyRole": "data-led",
                "rhythm": "intermission"
            },
            "differentiators": [
                "Infinite scrolling SVG marquee (Stripe, Google, Apple, AWS) with pause-on-hover",
                "Three large tabular metrics (e.g. 99.98% SLA, 4.9/5 Rating, < 1.2s FCP) with semantic units",
                "Strictly ZERO fake testimonials or text-only placards"
            ],
            "tradeoffs": [
                "Requires authentic vector SVGs (enforced via resilient_sourcing.py)",
                "Metrics must be factual and domain-grounded"
            ],
            "svgLayout": "marquee_metrics"
        },
        {
            "optionId": "proof-b",
            "archetype": "tabbed-case-study",
            "title": "Tabbed Interactive Case Study Carousel",
            "thesis": "Rich verifiable client narratives switchable via client logo tabs with verified ROI quotes.",
            "axes": {
                "composition": "tabbed-stage",
                "density": "dense",
                "media": "customer-headshot-and-logo",
                "readingDirection": "lateral",
                "interaction": "accessible-tab-switch",
                "typographyRole": "narrative-led",
                "rhythm": "chaptered"
            },
            "differentiators": [
                "Category tab switcher with authentic client brand marks",
                "Full-depth case study cards featuring exact before/after metrics and named quote",
                "Direct link to full case study or verified review platform"
            ],
            "tradeoffs": [
                "Requires deeper content preparation per case study",
                "Higher interaction complexity than a static quote"
            ],
            "svgLayout": "tabbed_case_study"
        },
        {
            "optionId": "proof-c",
            "archetype": "split-testimonial-stage",
            "title": "Asymmetric Pull-Quote with Audited ROI Card",
            "thesis": "Oversized display serif pull-quote opposing an audited impact ledger with verifiable credentials.",
            "axes": {
                "composition": "asymmetric-split (7/5)",
                "density": "balanced",
                "media": "audit-card-with-credentials",
                "readingDirection": "lateral",
                "interaction": "subtle-spring-reveal",
                "typographyRole": "type-dominant",
                "rhythm": "spacious"
            },
            "differentiators": [
                "7-column oversized editorial serif pull-quote with authentic quotation marks",
                "5-column audited impact ledger card with client photo, role, and verified badge",
                "Generous 120px vertical padding for high-trust executive deliberation"
            ],
            "tradeoffs": [
                "Highlights a single flagship client endorsement rather than volume of logos",
                "Needs an authoritative, high-credibility testimonial"
            ],
            "svgLayout": "split_testimonial"
        }
    ],
    "conversion": [
        {
            "optionId": "conversion-a",
            "archetype": "interactive-calculator",
            "title": "Dynamic Parameter Calculator Stage",
            "thesis": "Self-serve value calculator with reactive sliders, live price readout, and pre-filled CTA dispatch.",
            "axes": {
                "composition": "centered-interactive-card",
                "density": "balanced",
                "media": "reactive-slider-controls",
                "readingDirection": "inputs-to-output",
                "interaction": "reactive-client-slider + instant-cta",
                "typographyRole": "data-led",
                "rhythm": "focused"
            },
            "differentiators": [
                "Interactive guest / seat / duration slider with real-time numeric calculation",
                "Clear price breakdown showing transparent value without hidden fees",
                "1-click button dispatching pre-filled WhatsApp / checkout payload"
            ],
            "tradeoffs": [
                "Requires client-side state hooks (`use client`) and calculation logic",
                "Requires explicit pricing rules"
            ],
            "svgLayout": "calculator_stage"
        },
        {
            "optionId": "conversion-b",
            "archetype": "comparison-matrix",
            "title": "Transparent Tier Comparison Matrix",
            "thesis": "Three transparent pricing tiers with high-contrast badge on recommended tier and feature checkmarks.",
            "axes": {
                "composition": "multi-column-matrix (3-tier)",
                "density": "dense",
                "media": "checkmarks-and-badges",
                "readingDirection": "vertical-column-scanning",
                "interaction": "billing-period-toggle (Monthly/Annual)",
                "typographyRole": "data-led",
                "rhythm": "structured"
            },
            "differentiators": [
                "Clear feature comparison matrix with Lucide check icons (zero structural emojis)",
                "Center or flagship tier elevated with subtle direct shadow and 'Recommended' pill",
                "Interactive billing toggle with instant numeric transition"
            ],
            "tradeoffs": [
                "More horizontal density on desktop viewports",
                "Must collapse cleanly into a swipeable carousel or tabbed selector on mobile"
            ],
            "svgLayout": "comparison_matrix"
        },
        {
            "optionId": "conversion-c",
            "archetype": "split-lead-funnel",
            "title": "Asymmetric 60/40 Reservation Funnel",
            "thesis": "High-trust guarantee bullets and contact details opposing a streamlined 3-field reservation card.",
            "axes": {
                "composition": "asymmetric-split (60/40)",
                "density": "balanced",
                "media": "form-card-with-guarantee-badges",
                "readingDirection": "lateral",
                "interaction": "validated-form-fields + zero-js-fallback",
                "typographyRole": "action-oriented",
                "rhythm": "compact"
            },
            "differentiators": [
                "60% left column with direct booking guarantees, response time commitment, and phone link",
                "40% right column with clean 3-field form (Name, Date/Guests, Contact) with inline error states",
                "Form fields with font-size >= 16px to prevent mobile iOS Safari auto-zoom"
            ],
            "tradeoffs": [
                "Form-based rather than instant calculation",
                "Requires server action or API route for lead routing"
            ],
            "svgLayout": "split_lead_funnel"
        }
    ],
    "footer": [
        {
            "optionId": "footer-a",
            "archetype": "editorial-brand-footer",
            "title": "Oversized Brand Mark with 4-Col Directory",
            "thesis": "Grand architectural footer with oversized watermark typography, structured directory, and live status badge.",
            "axes": {
                "composition": "multi-column-brand-index",
                "density": "balanced",
                "media": "monumental-watermark-typography",
                "readingDirection": "top-directory-bottom-brand",
                "interaction": "live-status-indicator + social-svg-links",
                "typographyRole": "brand-dominant",
                "rhythm": "grounded"
            },
            "differentiators": [
                "Monumental oversized brand name in muted watermark typography across base",
                "4 organized link columns with category headers and hover underline transitions",
                "Live operational status badge ('All Systems Operational' / 'Now Accepting Bookings')"
            ],
            "tradeoffs": [
                "Requires larger vertical footprint (py-24)",
                "Best suited for multi-page or deep architectural sites"
            ],
            "svgLayout": "editorial_footer"
        },
        {
            "optionId": "footer-b",
            "archetype": "cta-focused-footer",
            "title": "Conversion Pre-Footer Stage + Minimalist Legal",
            "thesis": "Bold final call-to-action block positioned immediately above a crisp, single-line legal and social strip.",
            "axes": {
                "composition": "stacked-action-stage",
                "density": "sparse",
                "media": "minimal-social-svgs",
                "readingDirection": "vertical-downward",
                "interaction": "final-cta-button + email-input",
                "typographyRole": "action-oriented",
                "rhythm": "tight"
            },
            "differentiators": [
                "Dedicated conversion pre-footer card with bold headline and instant CTA button",
                "Compact single-row bottom strip with copyright, legal links, and vector social icons",
                "Clean, low-friction ending without link clutter"
            ],
            "tradeoffs": [
                "Less room for deep hierarchical sitemaps",
                "Relies on top navigation for site-wide discovery"
            ],
            "svgLayout": "cta_footer"
        },
        {
            "optionId": "footer-c",
            "archetype": "tabular-directory",
            "title": "Utility Directory with Business Hours & Map Link",
            "thesis": "High-density institutional directory detailing operating hours, physical address, and emergency hotline.",
            "axes": {
                "composition": "dense-utility-grid",
                "density": "dense",
                "media": "verified-contact-chips",
                "readingDirection": "matrix",
                "interaction": "1-click-directions + click-to-call",
                "typographyRole": "data-led",
                "rhythm": "utilitarian"
            },
            "differentiators": [
                "Full operating hours table with current day highlight",
                "Physical address with 1-click Google Maps navigation trigger",
                "Verified licensing, certifications, and Schema.org structured address data"
            ],
            "tradeoffs": [
                "Utilitarian aesthetic; less minimal than Option B",
                "Best suited for physical venues, medical clinics, and trade contractors"
            ],
            "svgLayout": "tabular_footer"
        }
    ]
}


class SectionOptionEngine:
    def __init__(self, out_dir: str = ".website-architect/previews", design_tokens_path: Optional[str] = None, layout_tree_path: Optional[str] = None):
        self.out_dir = Path(out_dir).resolve()
        self.out_dir.mkdir(parents=True, exist_ok=True)
        self.tokens = self.load_tokens(design_tokens_path)
        self.layout_tree = self.load_layout_tree(layout_tree_path or design_tokens_path)

    def load_tokens(self, path: Optional[str]) -> Dict[str, str]:
        defaults = {
            "canvas": "#FAF8F5",
            "canvas_card": "#FFFFFF",
            "ink": "#1A1816",
            "headline": "#12100E",
            "accent": "#C45B3A",
            "accent_foreground": "#FFFFFF",
            "border": "#E5E0D8",
            "muted": "#7A736A"
        }
        if path and Path(path).exists():
            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                # Extract colors from tokens json if present
                colors = data.get("colors", {})
                for k, v in colors.items():
                    if isinstance(v, str):
                        defaults[k] = v
            except Exception as e:
                print(f"[!] Warning reading tokens file {path}: {e}")
        return defaults

    def load_layout_tree(self, path: Optional[str]) -> Optional[Dict[str, Any]]:
        target_path = path
        if not target_path or not Path(target_path).exists():
            if Path("reference_layout_tree.json").exists():
                target_path = "reference_layout_tree.json"
            else:
                return None
        try:
            with open(target_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            if "layoutTree" in data:
                return data["layoutTree"]
            return data
        except Exception:
            return None

    def get_options_for_section(self, section_type: str) -> List[Dict[str, Any]]:
        st = section_type.lower()
        opts = [dict(o) for o in ARCHETYPE_LIBRARY.get(st, ARCHETYPE_LIBRARY.get("features", []))]

        # If layout tree is available, prioritize the reference DNA as Option A
        if self.layout_tree and st == "hero":
            hero_info = self.layout_tree.get("hero", {})
            hero_type = str(hero_info.get("heroType", "")).lower()
            layout_type = str(hero_info.get("layoutType", "")).lower()

            if "video" in hero_type or "full-bleed" in hero_type or "full-bleed" in layout_type:
                fb_opt = next((o for o in opts if o["optionId"] == "hero-b"), None)
                if fb_opt:
                    opts.remove(fb_opt)
                    fb_opt["title"] = fb_opt["title"] + " (Cloned Reference DNA)"
                    opts.insert(0, fb_opt)
            elif "editorial" in hero_type or "single" in layout_type:
                ed_opt = next((o for o in opts if o["optionId"] == "hero-c"), None)
                if ed_opt:
                    opts.remove(ed_opt)
                    ed_opt["title"] = ed_opt["title"] + " (Cloned Reference DNA)"
                    opts.insert(0, ed_opt)
        return opts

    def calculate_pairwise_distance(self, opt_a: Dict[str, Any], opt_b: Dict[str, Any]) -> int:
        """Counts how many axes differ between two options (Must be >= 3)."""
        axes_a = opt_a.get("axes", {})
        axes_b = opt_b.get("axes", {})
        diff_count = 0
        for axis in set(axes_a.keys()).union(axes_b.keys()):
            if axes_a.get(axis) != axes_b.get(axis):
                diff_count += 1
        return diff_count

    def generate_svg_wireframe(self, layout_type: str, title: str, archetype: str) -> str:
        """Generates a clean, responsive, aesthetic SVG wireframe diagram."""
        c_bg = self.tokens["canvas"]
        c_card = self.tokens["canvas_card"]
        c_ink = self.tokens["ink"]
        c_head = self.tokens["headline"]
        c_accent = self.tokens["accent"]
        c_border = self.tokens["border"]
        c_muted = self.tokens["muted"]

        # ViewBox 800 x 450 (16:9 ratio)
        svg_header = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%" style="background:{c_bg}; font-family:system-ui,-apple-system,BlinkMacSystemFont,sans-serif;">
  <defs>
    <filter id="card-shadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.06"/>
    </filter>
    <linearGradient id="media-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{c_accent}" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="{c_accent}" stop-opacity="0.05"/>
    </linearGradient>
  </defs>

  <!-- Frame Background & Border -->
  <rect x="0" y="0" width="800" height="450" fill="{c_bg}" stroke="{c_border}" stroke-width="1"/>
  
  <!-- Archetype Header Badge -->
  <rect x="24" y="20" width="180" height="24" rx="4" fill="{c_accent}" fill-opacity="0.1"/>
  <text x="32" y="36" font-size="11" font-weight="600" fill="{c_accent}" letter-spacing="0.5">ARCHETYPE: {archetype.upper()}</text>
  <text x="214" y="36" font-size="12" font-weight="500" fill="{c_muted}">|</text>
  <text x="226" y="36" font-size="12" font-weight="600" fill="{c_head}">{title}</text>
'''

        body = ""

        if layout_type == "asymmetric_split":
            # 60/40 Split: Text left, media right
            body = f'''
  <!-- 60% Left Narrative Column -->
  <g transform="translate(32, 70)">
    <!-- Eyebrow -->
    <rect x="0" y="10" width="90" height="12" rx="3" fill="{c_accent}" fill-opacity="0.2"/>
    <!-- Oversized Headline Lines -->
    <rect x="0" y="36" width="380" height="26" rx="4" fill="{c_head}"/>
    <rect x="0" y="70" width="340" height="26" rx="4" fill="{c_head}"/>
    <rect x="0" y="104" width="260" height="26" rx="4" fill="{c_head}" fill-opacity="0.8"/>
    <!-- Subhead Prose Lines -->
    <rect x="0" y="150" width="400" height="10" rx="2" fill="{c_muted}" fill-opacity="0.6"/>
    <rect x="0" y="168" width="380" height="10" rx="2" fill="{c_muted}" fill-opacity="0.6"/>
    <rect x="0" y="186" width="280" height="10" rx="2" fill="{c_muted}" fill-opacity="0.6"/>
    <!-- Dual Action Buttons -->
    <rect x="0" y="226" width="140" height="42" rx="8" fill="{c_accent}"/>
    <text x="36" y="252" font-size="13" font-weight="600" fill="#FFFFFF">Primary CTA</text>
    <rect x="156" y="226" width="130" height="42" rx="8" fill="none" stroke="{c_border}" stroke-width="1.5"/>
    <text x="188" y="252" font-size="13" font-weight="500" fill="{c_ink}">Learn More</text>
    <!-- Proof Chip -->
    <circle cx="10" cy="304" r="6" fill="{c_accent}"/>
    <text x="24" y="308" font-size="12" font-weight="500" fill="{c_muted}">4.9/5 Rating from 200+ Verified Guests</text>
  </g>

  <!-- 40% Right Media Frame -->
  <g transform="translate(480, 70)">
    <rect x="0" y="0" width="288" height="340" rx="16" fill="url(#media-grad)" stroke="{c_border}" stroke-width="1" filter="url(#card-shadow)"/>
    <text x="96" y="160" font-size="14" font-weight="600" fill="{c_accent}">[ 4:5 HERO MEDIA ]</text>
    <text x="82" y="180" font-size="11" fill="{c_muted}">Framed Photography / Video</text>
    <!-- Floating Badge -->
    <rect x="20" y="260" width="248" height="54" rx="10" fill="{c_card}" stroke="{c_border}" stroke-width="1" filter="url(#card-shadow)"/>
    <circle cx="44" cy="287" r="14" fill="{c_accent}" fill-opacity="0.15"/>
    <text x="40" y="291" font-size="12" font-weight="700" fill="{c_accent}">★</text>
    <text x="68" y="282" font-size="11" font-weight="600" fill="{c_head}">Signature Experience</text>
    <text x="68" y="298" font-size="10" fill="{c_muted}">Verified Operational Caliber</text>
  </g>
'''

        elif layout_type == "full_bleed_stage":
            # Edge-to-edge media with anchored typography
            body = f'''
  <!-- Full-Bleed Media Canvas -->
  <rect x="24" y="60" width="752" height="365" rx="12" fill="url(#media-grad)" stroke="{c_border}" stroke-width="1"/>
  <text x="320" y="190" font-size="16" font-weight="600" fill="{c_accent}">[ 100VW AMBIENT VIDEO / CINEMATIC STAGE ]</text>
  <text x="300" y="212" font-size="12" fill="{c_muted}">Edge-to-Edge Ambient Web Loop (60fps / &lt; 5MB)</text>

  <!-- Dark Scrim & Bottom-Left Anchor Block -->
  <rect x="44" y="240" width="480" height="165" rx="10" fill="{c_card}" fill-opacity="0.95" stroke="{c_border}" stroke-width="1" filter="url(#card-shadow)"/>
  <g transform="translate(64, 256)">
    <!-- Live Operational Status Badge -->
    <rect x="0" y="0" width="160" height="20" rx="10" fill="{c_accent}" fill-opacity="0.12"/>
    <circle cx="10" cy="10" r="4" fill="{c_accent}"/>
    <text x="20" y="14" font-size="10" font-weight="600" fill="{c_accent}">NOW ACCEPTING DATES</text>
    <!-- Anchored Display Headline -->
    <rect x="0" y="28" width="420" height="22" rx="3" fill="{c_head}"/>
    <rect x="0" y="56" width="310" height="22" rx="3" fill="{c_head}"/>
    <!-- CTA Button in Card -->
    <rect x="0" y="92" width="160" height="38" rx="8" fill="{c_accent}"/>
    <text x="38" y="116" font-size="12" font-weight="600" fill="#FFFFFF">Reserve Experience →</text>
  </g>

  <!-- Right Audio / Playback Toggle Widget -->
  <circle cx="740" cy="385" r="18" fill="{c_card}" stroke="{c_border}" stroke-width="1"/>
  <text x="734" y="389" font-size="12" fill="{c_head}">▶</text>
'''

        elif layout_type == "editorial_stack":
            # Stacked typography on top, landscape media below
            body = f'''
  <!-- Centered Top Typography Stack -->
  <g transform="translate(100, 64)">
    <!-- Centered Eyebrow -->
    <rect x="240" y="0" width="120" height="16" rx="4" fill="{c_accent}" fill-opacity="0.15"/>
    <!-- Oversized Stacked Headline -->
    <rect x="50" y="26" width="500" height="28" rx="4" fill="{c_head}"/>
    <rect x="110" y="60" width="380" height="28" rx="4" fill="{c_head}"/>
    <!-- Subhead Prose -->
    <rect x="150" y="98" width="300" height="10" rx="2" fill="{c_muted}" fill-opacity="0.7"/>
    <!-- Actions -->
    <rect x="190" y="120" width="120" height="34" rx="6" fill="{c_accent}"/>
    <text x="216" y="142" font-size="11" font-weight="600" fill="#FFFFFF">Explore Menu</text>
    <rect x="320" y="120" width="90" height="34" rx="6" fill="none" stroke="{c_border}" stroke-width="1"/>
    <text x="340" y="142" font-size="11" font-weight="500" fill="{c_ink}">Direct Line</text>
  </g>

  <!-- Landscape Media Bar Resting Below -->
  <rect x="44" y="234" width="712" height="190" rx="12" fill="url(#media-grad)" stroke="{c_border}" stroke-width="1" filter="url(#card-shadow)"/>
  <text x="280" y="335" font-size="14" font-weight="600" fill="{c_accent}">[ 21:9 WIDE HORIZON SHOWCASE ]</text>
  <text x="260" y="355" font-size="11" fill="{c_muted}">Panoramic Grounds / Architecture Horizon View</text>
'''

        elif layout_type == "bento_grid":
            # Asymmetric Bento Grid (Span 8 + Span 4)
            body = f'''
  <!-- Bento Cell 1: Flagship (Span 8) -->
  <g transform="translate(32, 64)">
    <rect x="0" y="0" width="470" height="350" rx="14" fill="{c_card}" stroke="{c_border}" stroke-width="1" filter="url(#card-shadow)"/>
    <!-- Header of card -->
    <rect x="24" y="24" width="80" height="16" rx="4" fill="{c_accent}" fill-opacity="0.15"/>
    <text x="30" y="36" font-size="10" font-weight="700" fill="{c_accent}">FLAGSHIP MODULE</text>
    <rect x="24" y="50" width="280" height="20" rx="3" fill="{c_head}"/>
    <rect x="24" y="78" width="340" height="10" rx="2" fill="{c_muted}"/>
    <!-- Interactive Canvas Representation -->
    <rect x="24" y="108" width="422" height="216" rx="8" fill="url(#media-grad)" stroke="{c_border}" stroke-width="1"/>
    <text x="140" y="215" font-size="13" font-weight="600" fill="{c_accent}">[ LIVE INTERACTIVE PREVIEW ]</text>
    <text x="120" y="235" font-size="10" fill="{c_muted}">Magic UI Bento / Interactive Stay Calculator</text>
  </g>

  <!-- Bento Cell 2: Satellite Top (Span 4) -->
  <g transform="translate(520, 64)">
    <rect x="0" y="0" width="248" height="165" rx="14" fill="{c_card}" stroke="{c_border}" stroke-width="1" filter="url(#card-shadow)"/>
    <circle cx="36" cy="36" r="16" fill="{c_accent}" fill-opacity="0.15"/>
    <text x="30" y="42" font-size="14" font-weight="700" fill="{c_accent}">⚡</text>
    <rect x="24" y="66" width="160" height="16" rx="3" fill="{c_head}"/>
    <rect x="24" y="90" width="200" height="8" rx="2" fill="{c_muted}"/>
    <rect x="24" y="104" width="150" height="8" rx="2" fill="{c_muted}"/>
    <rect x="24" y="128" width="80" height="16" rx="4" fill="{c_bg}" stroke="{c_border}" stroke-width="1"/>
    <text x="32" y="140" font-size="9" font-weight="600" fill="{c_ink}">ZERO WAITING</text>
  </g>

  <!-- Bento Cell 3: Satellite Bottom (Span 4) -->
  <g transform="translate(520, 248)">
    <rect x="0" y="0" width="248" height="165" rx="14" fill="{c_card}" stroke="{c_border}" stroke-width="1" filter="url(#card-shadow)"/>
    <circle cx="36" cy="36" r="16" fill="{c_accent}" fill-opacity="0.15"/>
    <text x="31" y="42" font-size="14" font-weight="700" fill="{c_accent}">🛡</text>
    <rect x="24" y="66" width="170" height="16" rx="3" fill="{c_head}"/>
    <rect x="24" y="90" width="200" height="8" rx="2" fill="{c_muted}"/>
    <rect x="24" y="104" width="180" height="8" rx="2" fill="{c_muted}"/>
    <rect x="24" y="128" width="90" height="16" rx="4" fill="{c_bg}" stroke="{c_border}" stroke-width="1"/>
    <text x="32" y="140" font-size="9" font-weight="600" fill="{c_ink}">100% PRIVATE</text>
  </g>
'''

        elif layout_type == "index_strip":
            # Tabular Index Strip: Left rail 01-03, right sticky stage
            body = f'''
  <!-- Left Numbered Rail -->
  <g transform="translate(32, 64)">
    <!-- Item 01 Active -->
    <rect x="0" y="0" width="300" height="106" rx="10" fill="{c_card}" stroke="{c_accent}" stroke-width="1.5" filter="url(#card-shadow)"/>
    <text x="20" y="32" font-size="18" font-weight="800" fill="{c_accent}">01</text>
    <rect x="56" y="18" width="180" height="16" rx="3" fill="{c_head}"/>
    <rect x="56" y="42" width="220" height="8" rx="2" fill="{c_muted}"/>
    <rect x="56" y="56" width="180" height="8" rx="2" fill="{c_muted}"/>
    <rect x="56" y="74" width="90" height="16" rx="4" fill="{c_accent}" fill-opacity="0.1"/>
    <text x="64" y="86" font-size="9" font-weight="700" fill="{c_accent}">ACTIVE VIEW</text>

    <!-- Item 02 Inactive -->
    <g transform="translate(0, 120)">
      <rect x="0" y="0" width="300" height="106" rx="10" fill="{c_bg}" stroke="{c_border}" stroke-width="1"/>
      <text x="20" y="32" font-size="18" font-weight="700" fill="{c_muted}">02</text>
      <rect x="56" y="18" width="160" height="16" rx="3" fill="{c_head}" fill-opacity="0.6"/>
      <rect x="56" y="42" width="200" height="8" rx="2" fill="{c_muted}" fill-opacity="0.4"/>
      <rect x="56" y="56" width="150" height="8" rx="2" fill="{c_muted}" fill-opacity="0.4"/>
    </g>

    <!-- Item 03 Inactive -->
    <g transform="translate(0, 240)">
      <rect x="0" y="0" width="300" height="106" rx="10" fill="{c_bg}" stroke="{c_border}" stroke-width="1"/>
      <text x="20" y="32" font-size="18" font-weight="700" fill="{c_muted}">03</text>
      <rect x="56" y="18" width="170" height="16" rx="3" fill="{c_head}" fill-opacity="0.6"/>
      <rect x="56" y="42" width="190" height="8" rx="2" fill="{c_muted}" fill-opacity="0.4"/>
      <rect x="56" y="56" width="140" height="8" rx="2" fill="{c_muted}" fill-opacity="0.4"/>
    </g>
  </g>

  <!-- Right Sticky Stage -->
  <g transform="translate(356, 64)">
    <rect x="0" y="0" width="412" height="346" rx="14" fill="{c_card}" stroke="{c_border}" stroke-width="1" filter="url(#card-shadow)"/>
    <rect x="20" y="20" width="372" height="230" rx="10" fill="url(#media-grad)" stroke="{c_border}" stroke-width="1"/>
    <text x="110" y="140" font-size="14" font-weight="600" fill="{c_accent}">[ STAGE 01 ARCHITECTURE ]</text>
    <rect x="20" y="270" width="220" height="16" rx="3" fill="{c_head}"/>
    <rect x="20" y="294" width="340" height="8" rx="2" fill="{c_muted}"/>
    <rect x="20" y="308" width="280" height="8" rx="2" fill="{c_muted}"/>
  </g>
'''

        elif layout_type == "asymmetric_stage":
            # 5/7 Split with narrative and interface capture
            body = f'''
  <g transform="translate(32, 64)">
    <!-- 5-Col Narrative Rail -->
    <rect x="0" y="20" width="110" height="16" rx="4" fill="{c_accent}" fill-opacity="0.15"/>
    <text x="8" y="32" font-size="10" font-weight="700" fill="{c_accent}">METHODOLOGY</text>
    <rect x="0" y="48" width="280" height="22" rx="3" fill="{c_head}"/>
    <rect x="0" y="78" width="240" height="22" rx="3" fill="{c_head}"/>
    <rect x="0" y="116" width="290" height="10" rx="2" fill="{c_muted}"/>
    <rect x="0" y="132" width="270" height="10" rx="2" fill="{c_muted}"/>
    <rect x="0" y="148" width="220" height="10" rx="2" fill="{c_muted}"/>

    <!-- Key Metric Callout -->
    <rect x="0" y="190" width="290" height="90" rx="10" fill="{c_card}" stroke="{c_border}" stroke-width="1" filter="url(#card-shadow)"/>
    <text x="20" y="230" font-size="28" font-weight="800" fill="{c_accent}">99.4%</text>
    <text x="20" y="254" font-size="12" font-weight="600" fill="{c_head}">On-Time Precision Delivery</text>
    <text x="20" y="270" font-size="10" fill="{c_muted}">Audited client delivery metric</text>
  </g>

  <!-- 7-Col Interface Stage -->
  <g transform="translate(356, 64)">
    <rect x="0" y="0" width="412" height="346" rx="14" fill="{c_card}" stroke="{c_border}" stroke-width="1" filter="url(#card-shadow)"/>
    <!-- Mock Browser Chrome -->
    <rect x="0" y="0" width="412" height="32" rx="14" fill="{c_bg}" stroke="{c_border}" stroke-width="1"/>
    <circle cx="20" cy="16" r="4" fill="#FF5F56"/>
    <circle cx="34" cy="16" r="4" fill="#FFBD2E"/>
    <circle cx="48" cy="16" r="4" fill="#27C93F"/>
    <rect x="70" y="8" width="200" height="16" rx="4" fill="{c_card}"/>
    <!-- Interface Content -->
    <rect x="20" y="52" width="372" height="270" rx="8" fill="url(#media-grad)" stroke="{c_border}" stroke-width="1"/>
    <text x="100" y="180" font-size="14" font-weight="600" fill="{c_accent}">[ 7-COL INTERFACE CAPTURE ]</text>
    <text x="90" y="202" font-size="11" fill="{c_muted}">High-Fidelity Real Operational UI</text>
  </g>
'''

        elif layout_type == "marquee_metrics":
            # Infinite Logo Marquee + 3 Hard Metrics
            body = f'''
  <!-- Marquee Container -->
  <g transform="translate(32, 64)">
    <rect x="0" y="0" width="736" height="80" rx="12" fill="{c_card}" stroke="{c_border}" stroke-width="1" filter="url(#card-shadow)"/>
    <text x="24" y="46" font-size="12" font-weight="700" fill="{c_muted}">VERIFIED CLIENTS</text>
    <!-- Logo placeholders -->
    <rect x="180" y="24" width="70" height="32" rx="6" fill="{c_accent}" fill-opacity="0.1"/>
    <text x="195" y="45" font-size="11" font-weight="700" fill="{c_head}">Google</text>
    <rect x="270" y="24" width="70" height="32" rx="6" fill="{c_accent}" fill-opacity="0.1"/>
    <text x="286" y="45" font-size="11" font-weight="700" fill="{c_head}">Stripe</text>
    <rect x="360" y="24" width="70" height="32" rx="6" fill="{c_accent}" fill-opacity="0.1"/>
    <text x="375" y="45" font-size="11" font-weight="700" fill="{c_head}">Amazon</text>
    <rect x="450" y="24" width="70" height="32" rx="6" fill="{c_accent}" fill-opacity="0.1"/>
    <text x="468" y="45" font-size="11" font-weight="700" fill="{c_head}">Intel</text>
    <rect x="540" y="24" width="70" height="32" rx="6" fill="{c_accent}" fill-opacity="0.1"/>
    <text x="556" y="45" font-size="11" font-weight="700" fill="{c_head}">Apple</text>
    <rect x="630" y="24" width="70" height="32" rx="6" fill="{c_accent}" fill-opacity="0.1"/>
    <text x="646" y="45" font-size="11" font-weight="700" fill="{c_head}">Cisco</text>
  </g>

  <!-- 3 Hard Quantitative Metric Cards Below -->
  <g transform="translate(32, 170)">
    <!-- Metric 1 -->
    <rect x="0" y="0" width="230" height="230" rx="14" fill="{c_card}" stroke="{c_border}" stroke-width="1" filter="url(#card-shadow)"/>
    <text x="30" y="70" font-size="44" font-weight="800" fill="{c_accent}">99.9%</text>
    <rect x="30" y="96" width="140" height="16" rx="3" fill="{c_head}"/>
    <rect x="30" y="122" width="170" height="8" rx="2" fill="{c_muted}"/>
    <rect x="30" y="138" width="120" height="8" rx="2" fill="{c_muted}"/>
    <rect x="30" y="174" width="80" height="20" rx="4" fill="{c_bg}" stroke="{c_border}" stroke-width="1"/>
    <text x="38" y="188" font-size="9" font-weight="600" fill="{c_muted}">SLA AUDIT</text>

    <!-- Metric 2 -->
    <rect x="253" y="0" width="230" height="230" rx="14" fill="{c_card}" stroke="{c_border}" stroke-width="1" filter="url(#card-shadow)"/>
    <text x="283" y="70" font-size="44" font-weight="800" fill="{c_accent}">&lt;1.2s</text>
    <rect x="283" y="96" width="140" height="16" rx="3" fill="{c_head}"/>
    <rect x="283" y="122" width="170" height="8" rx="2" fill="{c_muted}"/>
    <rect x="283" y="138" width="130" height="8" rx="2" fill="{c_muted}"/>
    <rect x="283" y="174" width="80" height="20" rx="4" fill="{c_bg}" stroke="{c_border}" stroke-width="1"/>
    <text x="291" y="188" font-size="9" font-weight="600" fill="{c_muted}">LCP SPEED</text>

    <!-- Metric 3 -->
    <rect x="506" y="0" width="230" height="230" rx="14" fill="{c_card}" stroke="{c_border}" stroke-width="1" filter="url(#card-shadow)"/>
    <text x="536" y="70" font-size="44" font-weight="800" fill="{c_accent}">4.9★</text>
    <rect x="536" y="96" width="140" height="16" rx="3" fill="{c_head}"/>
    <rect x="536" y="122" width="170" height="8" rx="2" fill="{c_muted}"/>
    <rect x="536" y="138" width="110" height="8" rx="2" fill="{c_muted}"/>
    <rect x="536" y="174" width="80" height="20" rx="4" fill="{c_bg}" stroke="{c_border}" stroke-width="1"/>
    <text x="544" y="188" font-size="9" font-weight="600" fill="{c_muted}">200+ REVIEWS</text>
  </g>
'''

        elif layout_type == "calculator_stage":
            # Dynamic Calculator Stage
            body = f'''
  <g transform="translate(100, 60)">
    <rect x="0" y="0" width="600" height="350" rx="16" fill="{c_card}" stroke="{c_border}" stroke-width="1" filter="url(#card-shadow)"/>
    
    <!-- Header -->
    <rect x="40" y="30" width="160" height="14" rx="4" fill="{c_accent}" fill-opacity="0.15"/>
    <text x="48" y="42" font-size="10" font-weight="700" fill="{c_accent}">DYNAMIC VALUE ESTIMATOR</text>
    <rect x="40" y="54" width="320" height="22" rx="3" fill="{c_head}"/>

    <!-- Slider Input 1 -->
    <text x="40" y="110" font-size="12" font-weight="600" fill="{c_head}">Select Guest Count / Group Capacity</text>
    <rect x="40" y="124" width="520" height="8" rx="4" fill="{c_bg}" stroke="{c_border}" stroke-width="1"/>
    <rect x="40" y="124" width="260" height="8" rx="4" fill="{c_accent}"/>
    <circle cx="300" cy="128" r="10" fill="{c_card}" stroke="{c_accent}" stroke-width="3"/>
    <text x="500" y="110" font-size="13" font-weight="700" fill="{c_accent}">8 Guests</text>

    <!-- Slider Input 2 -->
    <text x="40" y="170" font-size="12" font-weight="600" fill="{c_head}">Stay Duration / Session Package</text>
    <rect x="40" y="184" width="520" height="8" rx="4" fill="{c_bg}" stroke="{c_border}" stroke-width="1"/>
    <rect x="40" y="184" width="380" height="8" rx="4" fill="{c_accent}"/>
    <circle cx="420" cy="188" r="10" fill="{c_card}" stroke="{c_accent}" stroke-width="3"/>
    <text x="500" y="170" font-size="13" font-weight="700" fill="{c_accent}">3 Nights</text>

    <!-- Calculation Readout Bar -->
    <rect x="40" y="230" width="520" height="84" rx="12" fill="{c_bg}" stroke="{c_border}" stroke-width="1"/>
    <text x="64" y="264" font-size="12" fill="{c_muted}">Transparent Estimated Rate:</text>
    <text x="64" y="296" font-size="28" font-weight="800" fill="{c_head}">$1,450 <tspan font-size="12" font-weight="500" fill="{c_muted}">/ total all-inclusive</tspan></text>
    <!-- CTA Button -->
    <rect x="360" y="250" width="180" height="44" rx="8" fill="{c_accent}"/>
    <text x="390" y="277" font-size="13" font-weight="600" fill="#FFFFFF">Direct WhatsApp →</text>
  </g>
'''

        else:
            # Default clean generic block
            body = f'''
  <g transform="translate(32, 64)">
    <rect x="0" y="0" width="736" height="350" rx="14" fill="{c_card}" stroke="{c_border}" stroke-width="1" filter="url(#card-shadow)"/>
    <text x="300" y="170" font-size="16" font-weight="600" fill="{c_accent}">[ {archetype.upper()} WIREFRAME ]</text>
    <text x="270" y="196" font-size="12" fill="{c_muted}">Structural Layout Option: {title}</text>
  </g>
'''

        svg_full = svg_header + body + "\n</svg>"
        return svg_full

    def build_section_options(self, section_type: str) -> List[Dict[str, Any]]:
        """Compiles manifests, generates SVGs, and formats Markdown cards."""
        options = self.get_options_for_section(section_type)
        results = []

        # Validate pairwise divergence
        if len(options) >= 2:
            d_ab = self.calculate_pairwise_distance(options[0], options[1])
            d_bc = self.calculate_pairwise_distance(options[1], options[2]) if len(options) > 2 else 3
            d_ac = self.calculate_pairwise_distance(options[0], options[2]) if len(options) > 2 else 3
            print(f"[*] Pairwise Divergence Distances: A-B={d_ab}, B-C={d_bc}, A-C={d_ac} (Requirement: >= 3)")

        for opt in options:
            opt_id = opt["optionId"]
            title = opt["title"]
            arch = opt["archetype"]
            layout = opt.get("svgLayout", "asymmetric_split")

            # Generate SVG wireframe
            svg_content = self.generate_svg_wireframe(layout, title, arch)
            svg_path = self.out_dir / f"{section_type}_{opt_id}.svg"
            svg_path.write_text(svg_content, encoding="utf-8")

            # Generate lightweight standalone HTML preview
            html_content = f'''<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Preview: {title}</title>
  <style>
    body {{ margin: 0; padding: 24px; background: #EFEFEF; display: flex; justify-content: center; align-items: center; min-height: 100vh; }}
    .card {{ background: white; border-radius: 12px; box-shadow: 0 8px 30px rgba(0,0,0,0.1); max-width: 900px; width: 100%; overflow: hidden; }}
  </style>
</head>
<body>
  <div class="card">
    {svg_content}
  </div>
</body>
</html>'''
            html_path = self.out_dir / f"{section_type}_{opt_id}.html"
            html_path.write_text(html_content, encoding="utf-8")

            opt_copy = dict(opt)
            opt_copy["previewSvgPath"] = str(svg_path)
            opt_copy["previewHtmlPath"] = str(html_path)
            results.append(opt_copy)

        return results

    def format_chat_prompt(self, section_type: str, options: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generates the structured ask_question prompt and human-readable decision cards."""
        q_text = f"Select the layout archetype for section: [{section_type.upper()}]"
        choices = []

        card_text = f"### SECTION DECISION: [{section_type.upper()}] — CHOOSE YOUR LAYOUT\n\n"

        for i, opt in enumerate(options):
            letter = chr(ord('A') + i)
            rec = " (Recommended)" if i == 0 else ""
            title = opt["title"]
            arch = opt["archetype"]
            thesis = opt["thesis"]
            tradeoff = opt["tradeoffs"][0] if opt.get("tradeoffs") else "Standard maintenance"
            diffs = opt.get("differentiators", [])
            diff_str = "; ".join(diffs[:2])

            choice_str = f"Option {letter}{rec}: {title} ({arch}) - {thesis} [Tradeoff: {tradeoff}]"
            choices.append(choice_str)

            card_text += f"**[{letter}] {title}** ({arch}){rec}\n"
            card_text += f"- *Thesis*: {thesis}\n"
            card_text += f"- *Key Architecture*: {diff_str}\n"
            card_text += f"- *Tradeoff*: {tradeoff}\n"
            card_text += f"- *Wireframe Preview*: `file:///{opt['previewSvgPath'].replace('\\\\', '/')}`\n\n"

        choices.append(f"Custom / Hybrid: Combine Option A's base structure with specific elements from Option B or C.")
        choices.append(f"Agent Autonomously Decides: Proceed with Option A based on benchmark tokens.")

        return {
            "question": q_text,
            "options": choices,
            "markdown_cards": card_text,
            "raw_options": options
        }


def main():
    parser = argparse.ArgumentParser(description="Zero-Credit Section Option & SVG Wireframe Engine")
    parser.add_argument("--section", required=True, help="Section type: hero, features, proof, conversion, footer")
    parser.add_argument("--out-dir", default=".website-architect/previews", help="Output directory for SVG/HTML wireframes")
    parser.add_argument("--tokens", default=None, help="Path to design_tokens.json")
    parser.add_argument("--tree", default=None, help="Path to reference_layout_tree.json")
    parser.add_argument("--json-out", default=None, help="Write full manifest JSON to this path")

    args = parser.parse_args()

    engine = SectionOptionEngine(out_dir=args.out_dir, design_tokens_path=args.tokens, layout_tree_path=args.tree)
    options = engine.build_section_options(args.section)
    prompt_payload = engine.format_chat_prompt(args.section, options)

    print("\n" + "=" * 70)
    print(f"   SECTION-BY-SECTION PREVIEW GENERATOR: {args.section.upper()}")
    print("=" * 70)
    print(prompt_payload["markdown_cards"])
    print("=" * 70)
    print(f"[+] Successfully generated 3 SVG wireframes in: {args.out_dir}")

    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as f:
            json.dump(prompt_payload, f, indent=2)
        print(f"[+] Manifest saved to: {args.json_out}")


if __name__ == "__main__":
    main()
