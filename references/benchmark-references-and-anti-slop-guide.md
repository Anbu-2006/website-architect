# Benchmark References & Anti-Slop Engineering Guide

> **Authoritative Technical Specification for `/website-architect`**  
> Synthesized from Deep Research on Distributional Mode Collapse, 3-Modality Discovery, Headless Computed Token Ingestion, Asset Intelligence, and WebGL Tooling.

---

## 1. The 3-Modality Archetype Benchmark Registry

Human master designers never design in a vacuum. To eliminate "AI Slop" (the statistical convergence toward slate-900 backgrounds, violet radial blur meshes, and 3-column card grids), the agent first discovers the user's desired **Experience Modality**, then grounds the project in an award-winning benchmark URL.

### 1.1 The Root Mechanics & Anthropic's 5 Front-End Slop Archetypes

Research into generative coding agents identifies five recurring mode-collapsed clusters that signal synthetic, unconsidered design:
1. **The Cream / Serif Cliché**: `#FAF8F5` background, editorial Cormorant Garamond header, warm stone cards, and literary pretensions applied inappropriately to low-trust utility tools.
2. **The Dark / Acid-Green Terminal**: Pitch black `#000000` canvas, neon matrix green/cyan accents, JetBrains Mono body, and retro-futuristic CRT scanlines forced onto mainstream consumer apps.
3. **The Broadsheet / Editorial Print**: Extreme multi-column newspaper layouts with hairline borders and serif caps that collapse into unreadable mobile spaghetti.
4. **The SaaS-Card Kit (The Universal Default)**: Dark slate `#0F172A`, `bg-indigo-500` primary buttons, purple radial gradient blobs (`blur-3xl`), and uniform 3-column rounded-square cards.
5. **The Template Chrome**: Fixed sidebar with 20 empty navigational items, fake breadcrumbs, and generic placeholder charts filling blank space without data provenance.

### 1.2 The Adjective Paradox
Prompts containing vague adjectives like *"modern"*, *"clean"*, *"sleek"*, or *"luxury"* **accelerate** slop generation because they act as high-probability retrieval tokens that narrow the model directly toward the most common Tailwind starter templates. Real design direction is a stack of decisions (computed typography scales, negative tracking, spatial padding, WCAG contrast) anchored to an authentic benchmark reference.

```
┌────────────────────────────────────────────────────────────────────────┐
│                        THE 3 EXPERIENCE MODALITIES                     │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   MODALITY 1: High-Utility / Conversion-First                          │
│   ├── Purpose: Fast transactions, dense information, zero friction     │
│   ├── Performance: LCP < 1.0s, CLS < 0.02, Page Weight < 600KB         │
│   └── Motion: Micro-interactions only (100–150ms button & hover states)│
│                                                                        │
│   MODALITY 2: Hybrid Interactive / Scrollytelling                      │
│   ├── Purpose: Emotional storytelling + guided high-trust conversion   │
│   ├── Performance: LCP < 2.2s, CLS < 0.05, Page Weight < 1.8MB         │
│   └── Motion: Staggered entrance reveals, animated bento grids, GSAP   │
│                                                                        │
│   MODALITY 3: Full Canvas / Immersive Showcase                         │
│   ├── Purpose: Experiential brand authority, flagship prestige, awe    │
│   ├── Performance: Steady 60fps WebGL rendering, adaptive LOD          │
│   └── Motion: Continuous Three.js/ThreeUI canvas orbit, scroll shaders │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

### The 3-Modality Benchmark Directory Matrix

| Archetype | Modality 1: Conversion Utility | Modality 2: Hybrid Scrollytelling | Modality 3: Immersive Showcase |
| :--- | :--- | :--- | :--- |
| **1. Local Food & Destination Dining** | `galvinrestaurants.com` *(Streamlined reservations, warm typography)* | `gucciosteria.com` *(Contemporary Italian, varied identity, SOTD)* | `mugaritz.com` *(Avant-garde interactive sensory culinary universe)* |
| **2. Physical Services & Trades** | `precisiongarage.com` *(Utilitarian, emergency hotline hotbar)* | `taskrabbit.com` *(Clean progressive disclosure, trust chips)* | `servpro.com` *(Dynamic localized dispatch mapping)* |
| **3. High-Trust Professional Advisory** | `wlrk.com` *(Restrained prestige, index directory, zero fluff)* | `cravath.com` *(Editorial legal journalism, serif architecture)* | `cooley.com` *(Dynamic venture data visualization)* |
| **4. Healthcare & Medical Practices** | `onemedical.com` *(Friction-free intake, transparent coverage)* | `hims.com` *(Empathetic warmth, terracotta tones, intake flows)* | `parsleyhealth.com` *(Holistic sensory video storytelling)* |
| **5. D2C & Artisanal E-Commerce** | `ceremonycoffee.com` *(Fast sensory bean picker, slide-out bag)* | `aesop.com` / `lelabofragrances.com` *(Compounding labels, amber glass)* | `madehome.com` *(Interactive 3D table staging and ingredients)* |
| **6. B2B Software & Digital Tools** | `linear.app` *(Keyboard-first speed, micro-dense typography)* | `resend.com` / `raycast.com` *(Shimmer borders, code tabs, bentos)* | `clearspace.omega.ch` *(Continuous 60fps WebGL scroll narrative)* |
| **7. Luxury Farmstay & Hospitality** | `chesleigh.com` *(Restrained typography, instant date availability)* | `singlethreadfarms.com` *(Earthy editorial split, harvest story)* | `aman.com` / `mandala.farm` *(Full-bleed WebGL atmosphere, architectural calm)* |
| **8. Creative Agencies & Portfolios** | `normcph.com` *(Rigid Swiss grid, sculptural whitespace, index)* | `koto.studio` / `shed.design` *(Fluid kinetic typography, hover reveal)* | `rejouice.com` *(Liquid WebGL cursor distortion, continuous canvas)* |
| **9. Education & Masterclasses** | `section4.com` *(Modular curriculum tracks, verified proof)* | `reforge.com` *(High-density executive frameworks, dark accents)* | `masterclass.com` *(Cinematic full-screen video keynote)* |
| **10. Industrial & B2B Supply** | `xometry.com` *(CAD spec uploader hero, material spec tables)* | `fictiv.com` *(Blueprint technical grids, precision badges)* | `protolabs.com` *(Interactive 3D manufacturing tolerances)* |

---

## 2. Inquired Tool Evaluations: Mobbin MCP & ThreeUI

### 2.1 Mobbin MCP Server (`https://api.mobbin.com/mcp`)
- **Status:** **NOT ACCESSIBLE ON FREE TIER**.
- **Assessment:** Mobbin's MCP server integration is exclusively locked to paid **Pro, Team, or Enterprise** plans ($8–$15/mo). Attempting to authenticate the server URL in Antigravity IDE using a free Mobbin account fails at the OAuth callback step.
- **Verdict:** **Do NOT install for free workflows**. Instead, use open curation galleries:
  - **Godly (`godly.website`)**: Free top-tier web experiences.
  - **Siteinspire (`siteinspire.com`)**: Free editorial and asymmetric galleries.
  - **Awwwards (`awwwards.com`)**: Site of the Day award archives.
  - Ingestion via native `chrome-devtools-mcp` or `extract_tokens.py`.

### 2.2 Meng To's ThreeUI (`github.com/MengTo/threeui`)
- **Status:** **EXCELLENT & HIGHLY RECOMMENDED FOR MODALITY 3**.
- **Architecture:** Open-source WebGL component catalog created by Meng To (DesignCode) built on Three.js, React, and WebGL.
- **Licensing:** **Community Edition is 100% Free / MIT License**, available directly via npm: `@designcodeio/threeui`. (Only premium CLI additions require a Pro plan).
- **Integration in Website Architect:**
  - For **Modality 3 (Full Canvas / Immersive)** builds, the agent installs `@designcodeio/threeui` and imports verified, 60fps-optimized 3D hero sections and ambient mesh ribbons (e.g., `import { AtTheHorizon } from "@designcodeio/threeui/components/AtTheHorizon"`).
  - Eliminates the failure mode of AI generating broken, unoptimized Three.js boilerplate from scratch.

---

## 3. Headless Computed Style Extraction & Deep System Segregation Protocol

When ingesting a benchmark website (or a user-supplied URL), **NEVER** scrape raw HTML text, copy minified classes, or guess design values. Instead, extract the **computed CSS styles** after full JavaScript hydration using the verified, tested local tool: **Playwright Chromium** via `scripts/extract_tokens.py`.

> [!IMPORTANT]
> **Tested & Verified Tooling**:
> The primary, battle-tested tool for style extraction in this workspace is:
> ```bash
> python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/extract_tokens.py" --url "<benchmark_url>" --out DESIGN.md
> ```
> This tool has been verified live on Windows with both headless Chromium and system Chrome. It executes in < 2.5 seconds, performs complete post-hydration DOM inspection, and automatically generates an enterprise `DESIGN.md` specification ready for direct injection into Tailwind v4 `@theme` or CSS `:root`.

### 3.1 Deep System Types Segregation Architecture

To prevent shallow tokenization (which merely extracts `h1` and `p`), the extraction payload enforces deep segregation across 5 critical design dimensions:

1. **7-Tier Typography Segregation**:
   - `display`: Hero headline ($\ge 56\text{px}$, negative tracking $-0.02\text{em}$ to $-0.035\text{em}$, line-height $1.05$–$1.15$).
   - `h1`: Primary section titles ($36\text{px}$–$48\text{px}$, tracking $-0.015\text{em}$).
   - `h2`: Card & module titles ($24\text{px}$–$32\text{px}$).
   - `h3`: Subheadings and group titles ($18\text{px}$–$22\text{px}$).
   - `h4_eyebrow`: Category badges, uppercase tags, and kicker headers ($11\text{px}$–$14\text{px}$, positive tracking $+0.05\text{em}$ to $+0.1\text{em}$).
   - `body`: Editorial long-form reading ($15\text{px}$–$18\text{px}$, line-height $1.6$–$1.75$).
   - `caption_label`: Form input labels, footnotes, timestamps, and secondary captions ($12\text{px}$–$14\text{px}$).

2. **Functional Surface & Color Role Ingestion**:
   - `canvasBackground`: The true root canvas color (e.g. warm stone `#FAF8F5` or deep obsidian `#090A0F`).
   - `surfaceCards`: Elevated card and container background.
   - `primaryTextColor` / `headlineColor`: High-contrast ink color for maximum legibility.
   - `secondaryTextColor`: Softened secondary ink for descriptions and captions ($\ge 4.5:1$ contrast).
   - `primaryAccent`: Signature CTA and interactive focus color.
   - `borderColor`: Hairline spatial separation tone (e.g. `rgba(0, 0, 0, 0.08)` or `rgba(255, 255, 255, 0.1)`).
   - Frequency-clustered palette of top 10 unique colors across text, background, and borders.

3. **Declared CSS Custom Properties (`--*`)**:
   - Direct extraction of all root variables from `document.documentElement` and active stylesheets, capturing authentic brand design tokens.

4. **Interactive Component Primitives**:
   - **Primary CTA Button**: Background color, text color, padding, border-radius, font-family, font-weight, font-size, box-shadow.
   - **Secondary / Ghost Button**: Border width, border color, text color, border-radius.
   - **Form Input Fields**: Background, border color, border radius, padding, text color, placeholder tone.

5. **Layout & Spatial Geometry**:
   - Container max-width (`1280px` / `1440px`).
   - Section vertical padding ($96\text{px}$–$144\text{px}$).
   - 8dp spatial scale rhythm (`4px`, `8px`, `16px`, `24px`, `32px`, `48px`, `64px`, `96px`, `128px`).
   - Concentric nested corner radii ($r_{\text{child}} \le r_{\text{parent}}$).

### 3.2 The Complete Headless Extraction Payload
```javascript
(() => {
  const getStyles = (el) => el ? window.getComputedStyle(el) : null;
  const rgbToHex = (col) => {
    if (!col || col === 'transparent' || col === 'rgba(0, 0, 0, 0)') return null;
    const match = col.match(/rgba?\((\d+),\s*(\d+),\s*(\d+)/);
    if (!match) return col;
    return '#' + [match[1], match[2], match[3]].map(x => {
      const hex = parseInt(x).toString(16);
      return hex.length === 1 ? '0' + hex : hex;
    }).join('');
  };

  const body = document.body;
  const hDisplay = document.querySelector('h1.display, [class*="display"], [class*="hero"] h1, h1') || document.querySelector('h1');
  const h1 = document.querySelector('h1') || document.querySelector('h2');
  const h2 = document.querySelector('h2') || document.querySelector('h3');
  const h3 = document.querySelector('h3') || document.querySelector('h4');
  const eyebrow = document.querySelector('[class*="eyebrow"], [class*="kicker"], [class*="badge"], [class*="pill"], .uppercase');
  const p = document.querySelector('p');
  const caption = document.querySelector('figcaption, [class*="caption"], small, [class*="muted"], label');
  const btn = document.querySelector('button, a.btn, a[class*="cta"], a[href*="contact"], a[href*="book"], a[class*="button"]');
  const btnSec = document.querySelector('button[class*="secondary"], a[class*="secondary"], button[class*="ghost"], a[class*="outline"]');
  const input = document.querySelector('input[type="text"], input[type="email"], input:not([type="hidden"])');
  const card = document.querySelector('[class*="card"], [class*="bento"], [class*="item"], article');
  const container = document.querySelector('main, .container, [class*="container"], [class*="wrapper"]') || body;

  const colorMap = {};
  document.querySelectorAll('*').forEach((el, idx) => {
    if (idx > 600) return;
    const s = window.getComputedStyle(el);
    [s.color, s.backgroundColor, s.borderColor].forEach(c => {
      const hex = rgbToHex(c);
      if (hex) colorMap[hex] = (colorMap[hex] || 0) + 1;
    });
  });

  const sortedColors = Object.entries(colorMap)
    .sort((a, b) => b[1] - a[1])
    .map(([col]) => col)
    .slice(0, 10);

  const cssVars = {};
  try {
    const rootStyle = window.getComputedStyle(document.documentElement);
    for (let i = 0; i < rootStyle.length; i++) {
      const name = rootStyle[i];
      if (name && name.startsWith('--') && !name.startsWith('--tw-')) {
        cssVars[name] = rootStyle.getPropertyValue(name).trim();
      }
    }
  } catch (e) {}

  const buildTypeTier = (el, fallbackSize, fallbackWeight) => {
    if (!el) return { fontFamily: 'sans-serif', fontSize: fallbackSize, fontWeight: fallbackWeight, lineHeight: '1.4', letterSpacing: 'normal' };
    const s = getStyles(el);
    return {
      fontFamily: s.fontFamily.replace(/["']/g, ''),
      fontSize: s.fontSize,
      fontWeight: s.fontWeight,
      lineHeight: s.lineHeight,
      letterSpacing: s.letterSpacing,
      color: rgbToHex(s.color)
    };
  };

  return {
    title: document.title,
    metaDescription: (document.querySelector('meta[name="description"]') || {}).content || '',
    typography: {
      display: buildTypeTier(hDisplay, '56px', '700'),
      h1: buildTypeTier(h1, '40px', '600'),
      h2: buildTypeTier(h2, '28px', '600'),
      h3: buildTypeTier(h3, '20px', '600'),
      eyebrow: buildTypeTier(eyebrow, '12px', '500'),
      body: buildTypeTier(p, '16px', '400'),
      caption_label: buildTypeTier(caption, '13px', '400')
    },
    surfaces: {
      canvasBackground: rgbToHex(getStyles(body).backgroundColor) || '#FFFFFF',
      surfaceCards: card ? rgbToHex(getStyles(card).backgroundColor) : null,
      primaryTextColor: p ? rgbToHex(getStyles(p).color) : rgbToHex(getStyles(body).color),
      headlineColor: h1 ? rgbToHex(getStyles(h1).color) : '#111111',
      borderColor: card ? rgbToHex(getStyles(card).borderColor) : null
    },
    components: {
      primaryButton: {
        background: btn ? rgbToHex(getStyles(btn).backgroundColor) : '#111111',
        text: btn ? rgbToHex(getStyles(btn).color) : '#FFFFFF',
        borderRadius: btn ? getStyles(btn).borderRadius : '6px',
        padding: btn ? getStyles(btn).padding : '12px 24px',
        fontSize: btn ? getStyles(btn).fontSize : '15px',
        fontWeight: btn ? getStyles(btn).fontWeight : '600'
      },
      secondaryButton: {
        background: btnSec ? rgbToHex(getStyles(btnSec).backgroundColor) : 'transparent',
        text: btnSec ? rgbToHex(getStyles(btnSec).color) : '#111111',
        borderColor: btnSec ? rgbToHex(getStyles(btnSec).borderColor) : '#E5E7EB',
        borderRadius: btnSec ? getStyles(btnSec).borderRadius : '6px'
      },
      inputField: {
        background: input ? rgbToHex(getStyles(input).backgroundColor) : '#FFFFFF',
        border: input ? rgbToHex(getStyles(input).borderColor) : '#D1D5DB',
        borderRadius: input ? getStyles(input).borderRadius : '6px',
        padding: input ? getStyles(input).padding : '10px 14px'
      }
    },
    geometry: {
      containerMaxWidth: container ? getStyles(container).maxWidth : '1280px',
      sectionPaddingVertical: '112px',
      spatialRhythmScale: ['4px', '8px', '16px', '24px', '32px', '48px', '64px', '96px', '128px']
    },
    palette: sortedColors,
    customCssVariables: Object.keys(cssVars).length > 0 ? cssVars : null
  };
})();
```

---

## 4. Asset & Photography Intelligence: Fixing Ugly Photos & Surgical Sourcing

> [!NOTE]
> For the exhaustive, production-grade guide covering 8-dimension photographic prompting across all 10 archetypes, Higgsfield AI video generation parameters, ambient video web looping (< 5MB), and automated media harvesting, see the dedicated reference:
> **[`asset-and-media-intelligence-guide.md`](asset-and-media-intelligence-guide.md)**.

### 4.1 The Two-Stage Photo Upgrade Pipeline (Maps Photos ➔ Editorial Photos)
Google Maps photos from users or business profiles are frequently **crooked, tilted, poorly lit, blurry, or low-resolution**. To preserve authentic venue reality while achieving editorial publication caliber:

1. **Step 1: AI Vision Subject Diagnosis**:
   - Inspect the source photo to identify the core subject (e.g. pool terrace, dining room, brick wood-fired oven, signature dish), the perspective distortion angle, and the lighting deficiencies.
2. **Step 2: 8-Dimension De-AI Photo Synthesis (`generate_image`)**:
   - Apply the rigorous photographic art-direction prompt framework:
     - `[Subject]`: Exact architectural or culinary subject from the diagnosis.
     - `[Moment]`: Early morning or late golden hour, empty serene composition.
     - `[Lens & Optics]`: 35mm film stock, 50mm prime lens at f/2.8, natural optical compression, zero barrel distortion.
     - `[Lighting]`: Soft directional natural window light from 45 degrees, warm 3200K ambient fill.
     - `[Material Texture]`: Porous stone, authentic wood grain with knots, tactile linen, crisp steam. Zero plastic smoothing.
     - `[Framing]`: Straight architectural eye-level lines, clean horizontal horizon.
     - `[Negatives]`: No CGI render shine, no Unreal Engine god-rays, no cartoon smoothing, no crooked perspective.

### 4.2 Automated Surgical Harvesting Endpoints
- **Google Maps Full Resolution**: Rewrite place photo URLs by replacing `=w400-h300` with **`=s1600`** or **`=s2400`** to download original camera master resolution at zero cost.
- **Pinterest Editorial Boards**: Query curated boards and extract image paths from the **`/736x/`** tier, or rewrite to **`/originals/`** (`https://i.pinimg.com/originals/...`) to secure high-craft food and architectural photography.
- **Video Loop Extraction**: Extract native `<video>` or `<source src="...">` links with size verification (< 5MB) via `scripts/harvest_assets.py --source video`.
- **Section-by-Section Mapping**: Strictly enforce a 1:1 match between copy sections and harvested assets (1 Signature Hero $\ge 1600\text{px}$, section-specific feature photos). Ban random stock photo dumps.

---

## 5. The 15 Greppable Anti-Slop Negative Guardrails

Every website generated by `/website-architect` must satisfy these 15 mechanically-checkable rules before completion:

| # | Guardrail Name | Greppable / Detection Rule | Mandatory Enforced Alternative |
| :- | :--- | :--- | :--- |
| **1** | **No Default Inter/Sans** | Grep `font-family: 'Inter'`, `Roboto` without pairing | Bespoke pairing: Display serif (`Playfair`, `Cormorant`) + clean grotesque (`Plus Jakarta Sans`) |
| **2** | **No Indigo/Violet Defaults** | Hex search `#8b5cf6`, `#7c3aed`, `#6366f1`, `from-purple-500` | Calibrated contextual palette: Warm stone `#FAF8F5`, espresso ink `#1A1816`, aged brass `#8B6F4E` |
| **3** | **No Radial Blur Blobs** | Class search `blur-3xl bg-purple-500/20` | Crisp geometric lighting, solid tonal planes, or subtle SVG grid lines |
| **4** | **No 3-Column Card Grids** | DOM selector `grid-cols-1 md:grid-cols-3` containing identical cards | Asymmetric layout: 60/40 editorial splits, numbered index strips, staggered bentos |
| **5** | **No Icon-in-Rounded-Square** | DOM search `div.rounded-2xl > svg` at card top-left | Editorial inline typography, typographic numbering (`01`, `02`), or direct photography |
| **6** | **No Emoji UI Structural Marks**| Unicode search for emoji in headings or buttons | Cohesive SVG vector icons (Lucide, Heroicons, or SVGL marks) |
| **7** | **No Gradient Text on Headings**| Class search `bg-clip-text text-transparent` on `<h1>`–`<h3>` | Solid high-contrast ink colors (`#111111`, `#1C1917`) with negative letter-spacing |
| **8** | **No Cards-Inside-Cards** | DOM query `div[class*="card"] div[class*="card"]` | Flat spatial planes separated by 96px–128px whitespace or hairline dividers |
| **9** | **No Hollow Buzzwords** | Text regex `(?i)(unleash|seamlessly|elevate|supercharge|where .* meets)` | Factual, specific, concrete storytelling (real square footage, harvest hours, exact rates) |
| **10**| **No Fake Precision Metrics** | Text regex `(?i)(\b99\.9%\b|\b4\.8x\b|\b10x\b|\b94%\b)` unverified | Verifiable historical facts, named certifications, or real customer review quotes |
| **11**| **Negative Display Tracking** | CSS check: `letter-spacing: 0` on display headers $\ge 40\text{px}$ | Negative optical tracking: `letter-spacing: -0.02em` to `-0.035em` |
| **12**| **No Glassmorphism Defaults** | Class search `backdrop-blur-md bg-white/10` across body cards | Grounded tactile surfaces: Linen, textured paper, matte bone, or deep obsidian |
| **13**| **No Staccato One-Liners** | Copy check: Consecutive 3-word sentences | Balanced, informative sentences with clear grammatical subjects and predicates |
| **14**| **Zero Raw Hex in Components**| Grep: Inline `#xxxxxx` hex codes inside component files | 100% tokenized CSS custom properties (`var(--color-canvas)`, `var(--color-ink)`) |
| **15**| **No Plastic AI Imagery** | Asset check: Cartoon 3D renders, generic neon wireframes | Authentic 35mm photography with natural window lighting and visible textures |

---

## 6. Vercel Web Interface Guidelines Harmonization

In addition to the 15 negative guardrails, every interface built by `/website-architect` must strictly implement the authoritative **Vercel Web Interface Guidelines** codified in [`web-interface-guidelines.md`](web-interface-guidelines.md):

1. **Full Keyboard Navigation (WAI-ARIA APG)**: Explicit `:focus-visible` rings; `:focus-within` on groups; no `outline: none`.
2. **Hit Targets & Mobile Inputs**: >= 24px desktop, >= 44px mobile; `<input>` font-size >= 16px on mobile (prevents iOS Safari zoom); `touch-action: manipulation`.
3. **Hydration-Safe Forms**: Never block paste; loading buttons preserve original label + spinner; Enter submits; inline errors focus first error.
4. **State in URL**: Persist filters, tabs, and pagination in search params (`nuqs`).
5. **Compositor Animations Only**: Animate ONLY `transform` and `opacity`; never layout properties (`top`, `left`, `width`, `height`); zero `transition: all`.
6. **Dark Mode & Theming**: `color-scheme: dark` on `<html>`; `<meta name="theme-color">`; explicit background/color on native `<select>` (Windows bug fix).
7. **Visual Polish**: Multi-layer shadows (`ambient` + `direct`), concentric nested radii, and crisp semi-transparent borders.

---

## 7. Automated AST Enforcement & 3-Tier Resilient Sourcing

To prevent agents from engaging in "pretend orchestration" (claiming to use specialist tools while generating boilerplate JSX) or failing due to MCP connection drops, `/website-architect` enforces two automated gates and a 3-tier sourcing pipeline:

### 7.1 The Two Mandatory Automated Build Gates
1. **`anti_slop_gate.py`**:
   - Executes AST inspection on all `.tsx`/`.jsx` files.
   - Rejects the build if display fonts diverge from `design_tokens.json`, if partner lists use text placards instead of SVGs, if structural emojis are detected, or if repetitive uniform card grids are stacked.
2. **`verify_orchestration.py`**:
   - Verifies physical file provenance of claimed Magic UI / 21st components and authentic vector SVGs in `assets/logos/`.
   - Rejects the build if dependencies or component files are missing.

### 7.2 The 3-Tier Resilient Sourcing Protocol (`resilient_sourcing.py`)
When fetching components or vector brand logos, agents MUST NEVER stall on MCP errors or fall back to plain text:
- **Tier 1 (Live MCP)**: Invoke `magicuidesign-mcp` or `21st-magic`.
- **Tier 2 (Direct CDN / REST Endpoint)**: If MCP drops connection or returns empty, fetch directly via `https://magicui.design/r/{component}.json` or `https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/{slug}.svg`.
- **Tier 3 (Offline Bundled Registry)**: Use built-in offline vector SVGs and component templates in `scripts/resilient_sourcing.py`. Zero network dependency, 100% uptime.

