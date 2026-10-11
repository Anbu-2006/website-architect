---
name: website-architect
description: Universal interactive website architecture, information scoping, asset intelligence, and production web building engine. ALWAYS activate this skill whenever the user asks to build, create, design, code, plan, architect, or redesign ANY website, landing page, portfolio, web app, or commercial web page, or when providing a business URL, reference recording, or Google Maps link. Enforces 1:1 reference structural replication, multi-page Next.js App Router routing without anchor-hash jumps, eliminates generic AI slop, mandates multi-skill orchestration (ui-ux-pro-max, design-system, taste-skill, ui-styling, impeccable), and validates via automated AST and layout fidelity gates.
---

# Universal Website Architect Engine

## 0. MANDATORY EXECUTION GATE: THE ANTI-SLOP IRON LAW (Pre-Generation Contract)

> [!CAUTION]
> **STRICT PROHIBITION ON SPECULATIVE CODING & AI SLOP**
> An AI agent executing `website-architect` is **STRICTLY PROHIBITED** from generating ungrounded JSX/TSX or defaulting to generic Tailwind component templates (dark navy/slate background, uniform 3-card grids, Inter typography, glowing purple blur blobs, hollow marketing prose).
> Before ANY UI component or page file is authored, the agent **MUST** satisfy this 11-point execution contract:

1. **Unified Master Skill Architecture (Progressive Disclosure)**:
   The agent operates as a **Unified Master Web Architect**, eliminating "skill soup" and instruction dilution from juggling 7+ competing skills. It natively embeds the core rules from:
   - `ui-ux-pro-max` (WCAG AA design tokens, typography math, and product palettes).
   - `design-system` (three-layer `:root` CSS custom properties, 8dp spatial scales).
   - `taste-skill` / `soft-skill` (editorial layout geometry, 60/40 asymmetric splits, Doppelrand nested containers, generous 96px–128px section breathing room).
   - `ui-styling` (accessible shadcn/Radix primitives, semantic HTML).
   - `impeccable` (61-point craft audit, compositor-only motion, zero layout shifts).
   Progressive loading loads lightweight metadata initially (~250 tokens), then triggers full scripts and schemas on demand.

2. **1:1 Structural DNA Preservation (Reference Replication Protocol)**:
   When given a reference website (URL or video recording, e.g. Blackberry Farm, Loyola University Maryland):
   - **PRESERVE 1:1**:
     - Exact section sequence and vertical viewport heights.
     - Exact layout geometry: If the reference uses a 100vw full-bleed media/video hero, preserve the full-bleed hero; if it uses centered single-column editorial manifestos, preserve centered editorial; if it uses asymmetric multi-column bento, preserve that exact structure. Defaulting to generic 60/40 splits or 3-card SaaS templates when the reference has a full-bleed hero is strictly forbidden!
     - Exact bespoke image treatments: If the reference has arched / ogee photo masks, the code MUST implement the curved mask via `clip-path` or SVG mask. Substituting standard rounded rectangular cards is strictly forbidden!
     - Exact typography pairing: If the reference uses high-contrast display serif headlines, the code MUST use a display serif face. Defaulting to Inter/Roboto is strictly forbidden!
     - Ambient video hero loops: If the reference uses full-bleed video heroes, the code MUST implement a full-bleed looping video.
     - **Animation & Motion Parity**: If the reference has WAAPI tracks, CSS `@keyframes`, or GSAP ScrollTrigger animations, the generated code MUST implement equivalent motion with matching easing curves and durations.
   - **SOURCE FRESH FOR TARGET**:
     - Client's authentic photography, real verified specifications, and brand colors are mapped 1:1 into these structural slots.

### 0.1 The 5-Subagent Autonomous Finite State Machine (Zero Manual User Assignment)

> [!IMPORTANT]
> **AUTONOMOUS AGENT HANDOFF: ZERO MANUAL USER ASSIGNMENT REQUIRED**
> The user **NEVER** has to manually assign, trigger, or prompt separate subagents. The orchestrator coordinates and executes all five specialist personas across deterministic state locks and spatial file-system fences:
> **Agent 1 (Scout & Harvester)** $\to$ **Agent 2 (Creative Art Director)** $\to$ **Agent 3 (3D & Kinetic Specialist)** $\to$ **Agent 4 (Master Production Builder)** $\to$ **Agent 5 (Forensic QA Auditor)**.
> Alternatively, the pipeline can be executed via the master orchestration script:
> ```bash
> python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/orchestrate.py" --benchmark <benchmark_url> --query "<business_name_or_maps_url>" --domain "<domain>" --out-dir .
> ```
> Consult [multi-agent-orchestration-and-fencing.md](references/multi-agent-orchestration-and-fencing.md) and [3d-webgl-r3f-and-scroll-engineering.md](references/3d-webgl-r3f-and-scroll-engineering.md) for complete mathematical and spatial fencing specifications.

#### The 5 Specialist Subagent Personas:

1. **Agent 1: Deep Internet Scout & Benchmark Harvester (Read-Only Privilege)**
   - Executes headless Playwright Chromium with native 60fps hardware video recording (`reference_walkthrough_60fps.webm`).
   - Runs **MonkeyCrawler Heuristics**: Automatically scrolls the full height, hovers over cards, and exercises interactive components (`button`, `[role="tab"]`, `[data-state]`, accordions, carousel arrows, gallery sliders).
   - Traverses primary subroutes (e.g. `/accommodations`, `/dining`, `/about`).
   - Scrapes official brand vector SVGs, high-res photography, and verified customer telemetry.
   - Emits and signs `reference_layout_tree.json` and `assets_manifest.json` (validating against `schemas/assets_manifest.schema.json`).

2. **Agent 2: Creative Art Director (Read-Only Privilege)**
   - Ingests `business_profile.json` and competitive layout trees.
   - Derives intentional design vectors: typographic pairings (e.g., Canela/Ogg + Maison Neue), APCA-calibrated OKLCH color palettes (anti-halation), and fluid typography clamping `clamp(2.5rem, 1.571rem + 3.81vw, 5rem)`.
   - Solves damped harmonic oscillator equations ($m\ddot{x} + c\dot{x} + kx = 0$) for CSS `linear()` spring tokens.
   - Emits and signs `creative_thesis.json` (validating against `schemas/creative_thesis.schema.json`).

3. **Agent 3: 3D & Kinetic Motion Specialist (Spatial Fence: `src/components/canvas/`, `src/lib/motion/`)**
   - Evaluates whether spatial 3D interaction clarifies product value.
   - Scaffolds leak-free `InteractiveSceneCanvas.tsx` with React Three Fiber (< 3MB Draco geometry, max 25 draw calls per frame, DPR clamped to `[1, 2]`, WebGL context loss disposal on unmount, and high-res static image fallback).
   - Scaffolds `useUnifiedScrollEngine.ts` uniting Lenis smooth scroll inertia with GSAP ScrollTrigger ticker.
   - Emits and signs `scene_graph.json` (validating against `schemas/scene_graph.schema.json`).

4. **Agent 4: Master Production Builder (Spatial Fence: `src/app/`, `src/components/sections/`)**
   - Consumes `reference_layout_tree.json`, `creative_thesis.json`, `assets_manifest.json`, and `scene_graph.json`.
   - Executes structural cloning via `clone_reference_structure.py` to produce authentic Next.js 15 App Router pages and section components.
   - Emits Asymmetric Bento Grid 2.0 (8-column primary cell + 4-column secondary vertical telemetry stack).
   - Emits Zero-JS CSS Grid auto-height accordions (0fr $\to$ 1fr).
   - Emits Enterprise Footer with live `Intl.DateTimeFormat` local office status indicators and embedded `schema.org/LocalBusiness` JSON-LD.
   - Generates full subpages (`/about`, `/accommodations`, `/contact`) with $\ge 4$ to 6 rich sections per page.

5. **Agent 5: Forensic Quality Gate Auditor (Read & Headless Exec Privilege)**
   - Executes `anti_slop_gate.py` enforcing all **22+ deterministic AST checks**: zero 3-card kits, zero card-ception, zero ungrounded blur blobs, zero anchor illusions, 16px mobile inputs, 44px touch targets, sticky hover isolation, reduced-motion reset, and WebGL context cleanup.
   - Runs headless browser checks (`playwright-mcp`, `chrome-devtools-mcp`): zero console errors, zero layout shifts ($\text{CLS} < 0.05$), and $\text{LCP} < 1.2\text{s}$.
   - Approves completion only when all gates pass with exit code 0.

3. **Multi-Page Architecture Contract (Zero Hash-Jump Illusion)**:
   - For all Multi-Page Architecture (MPA) builds, the agent MUST write `route_manifest.json` and generate >= 3 distinct Next.js App Router subpages (`page.tsx`).
   - Primary navigation MUST use Next.js `<Link href="/route">`.
   - Single-page anchor jumps (`href="#schools"`, `href="#programs"`) in primary navigation are strictly banned.
   - The AST checker `python skills/website-architect/scripts/check_no_anchor_illusion.py <path_to_src_app>` MUST be executed and MUST pass with code 0.

4. **Monoculture Ratio Limit (<= 0.40)**:
   $$\text{Monoculture Ratio} = \frac{\text{Count of most common section signature}}{\text{Total sections in page}} \le 0.40$$
   If > 40% of sections on any route share the same layout signature (e.g. repeating icon-in-chip cards), the code is rejected for pattern collapse. Every route must exhibit visual pacing: full-bleed visual anchors, asymmetric editorial splits, index strips, and varied interaction modules.

5. **Structural Layout Fidelity Gate (F >= 0.85 across 8 vectors)**:
   - `python skills/website-architect/scripts/layout_fidelity_score.py <ref_wireframe> <target_wireframe>`
   - Scores across 8 vectors: primitive sequence, column ratios, mask fidelity, section count, animation signatures, micro-interactions, responsive breakpoints, and fluid math compliance.
   - Requires composite fidelity score F >= 0.85 before pre-delivery sign-off.

6. **Fluid Typography & Responsive Units (No Pixel-Freeze)**:
   - The extraction engine captures **declared** CSS rules via Chrome DevTools Protocol `CSS.getMatchedStylesForNode`, preserving `clamp()`, `calc()`, `rem`, and `vw` fluid values.
   - Generated code MUST use the declared fluid values, NOT the resolved static desktop pixels from `getComputedStyle()`.
   - Layout fidelity scorer penalizes static `px` values where the reference extracted `clamp()` or `rem`.

7. **60fps Video Walkthrough & Motion Transfer Protocol (WAAPI + CSS @keyframes + GSAP)**:
   - **Live 60fps Video Walkthrough**: Playwright Chromium records a full 60fps WebM video (`reference_walkthrough_60fps.webm` in `.website-architect/reference_recordings/`) while executing a programmatic smooth scroll through the benchmark site to trigger all entrance animations, parallax, and video elements.
   - **Visual Section Slices**: Captures 10 individual high-resolution section screenshot slices (`.website-architect/reference_slices/section_01.png` - `section_10.png`) for section-by-section optical alignment.
   - **Mathematical Motion Tokens**: Concurrently extracts exact Web Animations API (WAAPI) tracks (`duration`, `delay`, `easing` curves like `cubic-bezier(0.25, 1, 0.5, 1)`), declared CSS `@keyframes`, and GSAP `ScrollTrigger` instances.
   - **Dual-Source Code Synthesis**: The AI model uses the visual video/slices as ground truth for pacing and feel, and uses the extracted tokens to inject exact mathematical easing curves into Framer Motion (`whileInView`, `viewport`, `transition`) and CSS keyframes.
   - **AST Verification**: `scripts/anti_slop_gate.py` and `scripts/verify_orchestration.py` test the codebase to ensure animations and motion dependencies (`framer-motion`) are actively imported and rendered, failing if motion is missing or faked.

8. **Micro-Interaction Profiling (Hover/Active CDP Extraction)**:
   - The extraction engine uses CDP `CSS.forcePseudoState` to force `:hover` and capture elevation deltas (`transform`, `box-shadow`, `background-color`, `opacity`).
   - Extracted `transitionDuration` and `transitionTimingFunction` are codified for buttons, cards, and navigation links.

9. **Multi-Viewport Responsive Matrix (Desktop / Tablet / Mobile)**:
   - The extraction engine profiles layout restructuring across 3 standard breakpoints: Desktop (1440×900), Tablet (768×1024), Mobile (390×844).
   - Detects mobile hamburger drawer menus, column count changes, and padding rhythm adjustments.
   - Generated code MUST implement responsive behavior matching the extracted matrix.

10. **The Section-by-Section Option Protocol & Low-Cost Visual Previews**:
    - **NEVER** build the entire website in a monolithic, unguided black-box dump.
    - The durable unit of construction is the **section**.
    - For each planned section in `page_blueprint.json`, the agent **MUST** run:
      `python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/section_option_previewer.py" --section <type> --tokens design_tokens.json`
    - Produces exactly 3 structurally divergent options differing across $\ge 3$ axes (Composition, Density, Media, Reading direction, Interaction).
    - Renders zero-credit programmatic SVG wireframe previews or local headless Playwright micro-component snapshots (ZERO image-gen API credits burned).
    - Presents the options via the interactive `ask_question` tool modal, halting execution until the user selects Option A, B, C, or a Custom Hybrid.

11. **Machine-Verifiable Tool Receipts & Resilient 3-Tier Sourcing**:
    - **Zero Tolerance for Pretend Orchestration**: The agent must never claim in chat text that a tool was called or an asset was installed without physical file evidence.
    - All claimed MCP primitives (Magic UI, 21st blocks) and brand vector SVGs MUST physically exist on disk and be verified by `scripts/verify_orchestration.py`.
    - Automated 3-tier fallback hierarchy (MCP $\rightarrow$ Direct HTTP/CDN $\rightarrow$ Offline bundled cache) via `scripts/resilient_sourcing.py` guarantees zero missing asset or timeout failures.

12. **Multi-Page Route Depth Contract (Zero 1-Section Skeleton Stubs)**:
    - **NEVER** leave any route as a 1-section skeleton or empty placeholder stub (e.g. `/about`, `/accommodations`, `/offerings`, `/contact`).
    - Every canonical route in a Multi-Page Architecture (MPA) build **MUST import and render at least 4 to 6 distinct, robust, purposeful section components**.
    - Example for `/about`: `AboutHero`, `HeritageStory`, `PillarsAndValues`, `LeadershipAndCustodians`, `EditorialManifesto`, `SubpageCTA`.
    - Example for `/accommodations`: `OfferingsHero`, `FacetedFilterBar`, `OfferingsCatalogGrid`, `IncludedAmenitiesBento`, `BookingPoliciesAccordion`, `CatalogCTA`.
    - Enforced deterministically by `scripts/anti_slop_gate.py` (Check 9: `STUB_PAGE_SLOP`).

13. **Generic Dummy Button Prohibition (`GENERIC_BUTTON_SLOP`)**:
    - **STRICTLY PROHIBIT** generic dummy button copy ("Click Here", "Button", "Submit Button", "Learn More" or "Read More" without a valid non-empty `href` or action).
    - **STRICTLY PROHIBIT** dead click handlers (`onClick={() => {}}` or mock `alert()` calls).
    - All interactive triggers MUST feature contextual, high-intent action copy ("Reserve Cottage", "View Tasting Menu", "Get GPS Route", "Explore Suites") and be bound to authentic routing or interactive modal/drawer state.
    - Enforced deterministically by `scripts/anti_slop_gate.py` (Check 10: `GENERIC_BUTTON_SLOP`).

## Overview & Core Operating Mechanics
The **Website Architect** is an enterprise-grade cognitive engine and master general contractor that turns any business concept, client project, or commercial URL into a production-grade, validated web architecture, authoritative Product Requirements Document (PRD), and fully implemented, high-craft web application.

### Why "AI Slop" Occurs (The Statistical Median Trap)
"AI Slop" in web design is not a failure of coding ability; it is a **distributional mode collapse**. Autoregressive language models minimize cross-entropy loss by predicting the statistical center of their training data. Because the 2019–2024 web corpus is dominated by Tailwind boilerplate, component starter templates, and SaaS landing pages, unconstrained generation converges on a predictable median: dark navy/slate backgrounds (`#0B0F19`), glowing purple/indigo radial blur meshes, three-column feature cards, Inter typography, and hollow marketing prose.

Furthermore, prompting with subjective adjectives like *"modern"*, *"sleek"*, or *"clean"* creates the **Adjective Paradox**: these adjectives act as high-probability retrieval tokens that narrow the model directly toward standard Tailwind boilerplate rather than bespoke craftsmanship.

### The 4 Architectural Countermeasures
To force generation off the statistical median onto a human-caliber distribution, Website Architect enforces four strict mechanisms:
1. **The Modality Gate (Utility, Hybrid, Immersive)**: Constrains the search space and interaction budget before visual work begins.
2. **Dynamic Live Benchmark Grounding**: Anchors design decisions to verified award-winning sites from Awwwards, Godly, and Siteinspire.
3. **Headless Visual DNA Extraction**: Ingests computed styles (`window.getComputedStyle()`) post-hydration via Playwright, producing a mathematical `DESIGN.md` specification.
4. **15 Greppable Negative Guardrails**: Binary, mechanically-checkable constraints that ban known AI signatures before code generation starts.

It handles all 10 universal commercial archetypes:
1. **Local Food & Beverage / Hospitality** (Highway Express vs. Destination Dining)
2. **Local Physical Services & Trade Contractors** (Emergency Trades vs. Commercial Contractors)
3. **High-Trust Professional Services** (Boutique Advisory vs. Corporate Law Firms)
4. **Healthcare, Wellness & Medical Practices** (Solo Aesthetic Clinics vs. Multi-Specialty Networks)
5. **Direct-to-Consumer (D2C) & E-Commerce** (Single-Product Hero vs. Multi-Category Catalogs)
6. **B2B Software, SaaS & Digital Platforms** (Micro-SaaS Tools vs. Enterprise PLG Platforms)
7. **Real Estate, Luxury Hospitality & Destination Grounds** (Private Farmstays/Resorts vs. Brokerages)
8. **Creative Agencies, Studios & Portfolios** (Boutique Motion Studios vs. Full-Service Agencies)
9. **Education, Courses & Community Organizations** (Cohort Masterclasses vs. Technology Academies)
10. **Industrial, Manufacturing & B2B Supply** (Custom CNC Job Shops vs. Multi-Division OEM Manufacturers)

---

## Authoritative Skill & MCP Execution Matrix (Concrete Tool Calls)

To guarantee that the AI agent **actually executes** the required skills, scripts, and MCP tools rather than superficially mentioning them, all invocations must follow these concrete tool-call contracts:

### 0. Native Developer-Grade Internet Research & Scouting Tools (`search_web`, `read_url_content`)

A real developer does not build websites from assumptions or generic marketing hallucinations. When given any business name, URL, or brief, the agent **MUST** actively scour the live internet using these native tools:

| Tool Name | Lifecycle Phase | Developer-Grade Research Purpose | Mandatory Tool Call Syntax |
| :--- | :--- | :--- | :--- |
| **`search_web`** | **Stage 1.5 & Stage 4** | • Discover official client website, verified phone, address, and social channels.<br>• Uncover real products, menu items, pricing, founders, and verified reviews.<br>• Scout top 3 live award-winning benchmarks on Awwwards, Godly, and Siteinspire. | `search_web(query="<business_name> official website menu pricing reviews")`<br>`search_web(query="<commercial_archetype> award winning websites awwwards godly")` |
| **`read_url_content`** | **Stage 1.5** | Ingest raw HTML-to-markdown text from official client websites, press releases, or competitor pages to extract 100% authentic brand voice, mission copy, and customer proof. | `read_url_content(Url="<client_or_competitor_url>")` |

### 1. Concrete Skill Invocations (`view_file`)
Whenever a specialist skill is required, the agent **MUST** call `view_file` using its absolute filesystem path:

| Skill Name | Purpose in Website Architect | Mandatory Tool Call Syntax |
| :--- | :--- | :--- |
| **`ui-ux-pro-max`** | Design system intelligence, palettes, typography pairings | `view_file(AbsolutePath="C:/Users/anbua/.gemini/config/skills/ui-ux-pro-max/SKILL.md")` |
| **`design-system`** | Three-layer token architecture, CSS variable generation | `view_file(AbsolutePath="C:/Users/anbua/.gemini/config/skills/design-system/SKILL.md")` |
| **`taste-skill`** | Editorial layout geometry, variance dials, anti-slop rules | `view_file(AbsolutePath="C:/Users/anbua/.gemini/config/skills/taste-skill/SKILL.md")` |
| **`ui-styling`** | shadcn/ui primitives, Tailwind CSS utilities, accessible themes | `view_file(AbsolutePath="C:/Users/anbua/.gemini/config/skills/ui-styling/SKILL.md")` |
| **`impeccable`** | 61-point design craft, responsive polish, and audit gate | `view_file(AbsolutePath="C:/Users/anbua/.gemini/config/skills/impeccable/SKILL.md")` |
| **`21st-ui`** | Component discovery, curated Tailwind blocks, logo extraction | `view_file(AbsolutePath="C:/Users/anbua/.gemini/config/skills/21st-ui/SKILL.md")` |
| **`a11y-debugging`**| Accessibility auditing (WCAG AA, focus rings, reduced motion) | `view_file(AbsolutePath="C:/Users/anbua/.gemini/config/plugins/chrome-devtools-plugin/skills/a11y-debugging/SKILL.md")` |
| **`soft-skill`** | High-end $150k luxury agency craft, Doppelrand, button-in-button | `view_file(AbsolutePath="C:/Users/anbua/.gemini/config/skills/soft-skill/SKILL.md")` |
| **`minimalist-skill`**| Utilitarian document minimalism, warm bone `#F7F6F3`, `<kbd>` shortcuts | `view_file(AbsolutePath="C:/Users/anbua/.gemini/config/skills/minimalist-skill/SKILL.md")` |
| **`brutalist-skill`** | Industrial brutalism, 0px radius, Swiss print & tactical telemetry | `view_file(AbsolutePath="C:/Users/anbua/.gemini/config/skills/brutalist-skill/SKILL.md")` |
| **`gpt-tasteskill`**| Advanced GSAP ScrollTriggers, gapless bento, 2-line hero rule | `view_file(AbsolutePath="C:/Users/anbua/.gemini/config/skills/gpt-tasteskill/SKILL.md")` |
| **`redesign-skill`**| Diagnostic scan & surgical non-breaking codebase upgrade | `view_file(AbsolutePath="C:/Users/anbua/.gemini/config/skills/redesign-skill/SKILL.md")` |
| **`image-to-code`** | Image-first design-to-code workflow for flagship heroes | `view_file(AbsolutePath="C:/Users/anbua/.gemini/config/skills/image-to-code-skill/SKILL.md")` |

### 2. Concrete Python Script Invocations (`run_command`)
All automated scripts must be run via `run_command` using absolute paths. Scripts use `asyncio` and Playwright:

- **Design Intelligence Query (`ui-ux-pro-max`):**
  ```bash
  python "C:/Users/anbua/.gemini/config/skills/ui-ux-pro-max/scripts/search.py" "<archetype> <stack>" --design-system
  ```
- **Production CDP+WAAPI Token & Layout DNA Extraction (`extract_tokens.py` — async Playwright + CDP):**
  Extracts fluid `clamp()`/`rem` via CDP, WAAPI tracks, CSS `@keyframes`, GSAP ScrollTrigger metadata, hover deltas, responsive viewport matrix, captures high-resolution reference section screenshot slices, and outputs `reference_layout_tree.json`:
  ```bash
  python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/extract_tokens.py" --url "<benchmark_url>" --out DESIGN.md --tokens-out design_tokens.json --layout-tree-out reference_layout_tree.json --slices-dir .website-architect/reference_slices --assets assets/
  ```
  Outputs: `DESIGN.md`, `design_tokens.json`, `reference_layout_tree.json`, `.website-architect/reference_slices/section_*.png`.

- **Multi-Channel Asset Intelligence Harvester (`harvest_assets.py`):**
  Deep harvesting across Google Maps (ratings, reviews, NAP, photos), official client domain (vector logos, SVGs, press photography), social media channels (Instagram, Facebook), Pinterest aesthetic fallbacks, and ambient background looping videos (< 8MB):
  ```bash
  python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/harvest_assets.py" --source multi --query "<query_or_maps_url>" --domain "<official_domain>" --out public/assets --max 12 --video
  ```
  Outputs: `public/assets/assets_manifest.json`, `public/assets/maps_photo_*.jpg`, `public/assets/domain_photo_*.jpg`, `public/assets/brand_logo.svg`, `public/assets/*_loop_1.mp4`.

- **Universal Reference Structural Cloner (`clone_reference_structure.py`):**
  Consumes `reference_layout_tree.json` and `assets_manifest.json` to generate authentic Next.js 15 section components and `page.tsx` skeletons cloning the benchmark's exact layout geometry (full-bleed media, centered editorial, or multi-column grids) with zero generic SaaS template defaults:
  ```bash
  python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/clone_reference_structure.py" --tree reference_layout_tree.json --manifest public/assets/assets_manifest.json --out-dir src/components/sections --page-out src/app/page.tsx --business-name "<name>"
  ```

- **Section-by-Section Option & Wireframe Engine (`section_option_previewer.py`):**
  Derives 3 structurally divergent layout options aligned with the cloned reference DNA at $0 credit cost:
  ```bash
  python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/section_option_previewer.py" --section <hero|features|proof|conversion|footer> --tokens design_tokens.json --tree reference_layout_tree.json
  ```
- **Multi-Viewport Recursive Sitemap Crawler (`crawl_sitemap.py` — async Playwright):**
  Handles virtual scroll (Lenis/GSAP) via synthetic mouse wheel delta. Explores mobile hamburger drawer menus at 390px viewport.
  ```bash
  python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/crawl_sitemap.py" <reference_url> [out_file]
  ```
- **Video-to-Wireframe IR Decomposition (`video_to_wireframe.py`):**
  Extracts keyframes via ffmpeg, tracks optical flow scroll displacement, detects GSAP scroll-pinning dwell states, analyzes contours for arched masks, and synthesizes `wireframe_ir.json`.
  ```bash
  python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/video_to_wireframe.py" <video.mp4> --out wireframes/
  ```
- **8-Vector Structural Layout Fidelity Scorer (`layout_fidelity_score.py`):**
  Scores: primitive sequence, column ratios, mask fidelity, section count, animation signatures, micro-interactions, responsive breakpoints, and fluid math compliance.
  ```bash
  python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/layout_fidelity_score.py" <ref_ir.json> <gen_ast.json>
  ```
- **Multi-Page Anti-Anchor-Illusion AST Gate (`check_no_anchor_illusion.py`):**
  ```bash
  python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/check_no_anchor_illusion.py" <path_to_app_dir>
  ```
- **Automated Anti-Slop AST Gate (`anti_slop_gate.py` — MANDATORY PRE-DELIVERY):**
  Scans JSX/TSX AST for repetitive 3-card/4-card grids, text-only partner placards, structural emojis, and token divergence from `design_tokens.json`.
  ```bash
  python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/anti_slop_gate.py" <path_to_project_root>
  ```
- **Multi-Skill & MCP Orchestration Verifier (`verify_orchestration.py` — MANDATORY PRE-DELIVERY):**
  Verifies that claimed MCP components exist with authentic registry code, vector brand SVGs exist in `assets/logos/`, and required dependencies are installed.
  ```bash
  python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/verify_orchestration.py" <path_to_project_root>
  ```
- **Resilient Multi-Tier Asset & Component Sourcing Engine (`resilient_sourcing.py`):**
  Guarantees zero MCP connection errors or missing asset failures via automatic 3-tier fallback (MCP -> Direct CDN/API -> Bundled Offline Registry):
  ```bash
  python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/resilient_sourcing.py" batch-logos "<brand1,brand2,...>" --out public/assets/logos
  python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/resilient_sourcing.py" component "<component_name>" --out src/components/ui/<component_name>.tsx
  ```

### 3. Concrete MCP Tool Invocations (`call_mcp_tool`) & Exact Verified Schemas
All MCP tool calls must use exact parameter keys verified against their local schema specifications. Invoke each tool strictly within its dedicated lifecycle phase:

#### Phase A: Cognitive Planning & Route Topology (`sequential-thinking`)
- **Tool**: `call_mcp_tool(ServerName="sequential-thinking", ToolName="sequentialthinking", Arguments=...)`
- **When to Use**: Stage 1-2 & Stage 6. Use before creating files to calculate the Architecture Decision Score (ADS), plan multi-page App Router topology, and evaluate route boundaries.
- **Contract Example**:
  ```python
  call_mcp_tool(
    ServerName="sequential-thinking",
    ToolName="sequentialthinking",
    Arguments={
      "thought": "Analyzing client business model: Destination boutique farmstay. ADS score calculation: Catalog Depth=3, Search Specificity=2, Deliberation=5, Immediacy=1 => ADS=9 (Strict MPA required). Planned routes: '/', '/cottages', '/dining', '/experiences', '/reserve'.",
      "thoughtNumber": 1,
      "totalThoughts": 3,
      "nextThoughtNeeded": True
    }
  )
  ```

#### Phase B & C: UI Primitives, Blocks & Themes (`shadcn-ui`)
- **100% Free & Unmetered** (No API key required).
- **When to Use**: Sourcing accessible Radix-based primitives (accordions, sheets, dialogs, dropdowns, forms, data tables) and themes.
- **Contract Examples**:
  ```python
  # Fetch full accessible component source code (v4)
  call_mcp_tool(
    ServerName="shadcn-ui",
    ToolName="get_component",
    Arguments={"componentName": "accordion"}
  )
  # Fetch pre-built layout block (dashboard, login, calendar, sidebar)
  call_mcp_tool(
    ServerName="shadcn-ui",
    ToolName="get_block",
    Arguments={"blockName": "dashboard-01", "includeComponents": True}
  )
  # Inspect or apply tweakcn theme presets
  call_mcp_tool(
    ServerName="shadcn-ui",
    ToolName="get_theme",
    Arguments={"themeName": "zinc"}
  )
  ```

#### Phase C: Animated Hero Primitives & Bento Grids (`magicuidesign-mcp`)
- **100% Free & Unmetered** (No API key required).
- **When to Use**: Building visual showcase anchors: animated bento grids, marquee logo tickers, shimmer buttons, and border beams.
- **Contract Examples**:
  ```python
  # Search registry items
  call_mcp_tool(
    ServerName="magicuidesign-mcp",
    ToolName="searchRegistryItems",
    Arguments={"query": "bento-grid", "limit": 5}
  )
  # Retrieve component source code
  call_mcp_tool(
    ServerName="magicuidesign-mcp",
    ToolName="getRegistryItem",
    Arguments={"name": "bento-grid", "includeSource": True}
  )
  ```

#### Phase C: Production Vector Icons (`lucide-icons`)
- **100% Free & Unmetered** (Runs via `npx -y lucide-icons-mcp@latest --stdio`).
- **When to Use**: Sourcing ALL structural UI icons (navigation, status pills, actions, controls). Strictly ban emojis for structural icons.
- **Contract Examples**:
  ```python
  # Search 1,500+ vector icons by keyword or category
  call_mcp_tool(
    ServerName="lucide-icons",
    ToolName="search_icons",
    Arguments={"query": "calendar", "limit": 5}
  )
  # Get React usage examples
  call_mcp_tool(
    ServerName="lucide-icons",
    ToolName="get_icon_usage_examples",
    Arguments={"name": "calendar"}
  )
  ```

#### Phase C: Community Blocks & Brand Logos (`21st-magic` + Resilient Fallback)
- **When to Use**: Discovering community React blocks, color themes, and fetching tech/brand vector SVGs.
- **Contract Examples**:
  ```python
  # Search community blocks
  call_mcp_tool(ServerName="21st-magic", ToolName="search", Arguments={"query": "pricing table", "type": "component"})
  # Search brand logo
  call_mcp_tool(ServerName="21st-magic", ToolName="search_logo", Arguments={"query": "stripe"})
  ```
- **Mandatory Zero-Cost Fallback (`resilient_sourcing.py`)**:
  When unauthenticated or offline, use `scripts/resilient_sourcing.py` to batch-pull authentic brand vector SVGs from Simple-Icons and SVGL CDNs at **$0.00 cost**:
  ```bash
  python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/resilient_sourcing.py" batch-logos "stripe,google,aws,apple" --out public/assets/logos
  ```

#### Phase D: MotionSites AI Design Prompts & Recipes (`motionsites` + `motionsites_prompts.py`)
- **When to Use**: Grounding hero sections, asymmetric bento grids, dual-tier liquid glassmorphism, and luxury dark-mode aesthetics in real, curated AI website prompt recipes (500+ templates).
- **Contract Examples**:
  ```python
  # Search 500+ design prompts via MCP or local script
  call_mcp_tool(ServerName="motionsites", ToolName="search_prompts", Arguments={"query": "liquid glass", "type": "hero"})
  # Retrieve complete design prompt specification
  call_mcp_tool(ServerName="motionsites", ToolName="get_prompt", Arguments={"prompt_id": "bloom-ai-hero"})
  ```
- **Autonomous Zero-Cost Bridge (`motionsites_prompts.py`)**:
  Access 183 free design prompts, exact CSS glass tokens, and CDN videos instantly with $0.00 cost:
  ```bash
  python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/motionsites_prompts.py" search "fintech" --type hero
  python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/motionsites_prompts.py" get "bloom-ai-hero"
  python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/motionsites_prompts.py" recipes
  ```

#### Phase E: High-Level User Journey & Route Testing (`playwright-mcp`)
- **100% Free & Unmetered** (Microsoft official Playwright MCP).
- **When to Use**: Testing multi-page navigation across routes, validating form inputs, clicking drawers, and inspecting accessibility tree elements.
- **Contract Examples**:
  ```python
  # Navigate to running application
  call_mcp_tool(ServerName="playwright-mcp", ToolName="browser_navigate", Arguments={"url": "http://localhost:3000"})
  # Click multi-page route link (verifying no hash-jump illusion)
  call_mcp_tool(ServerName="playwright-mcp", ToolName="browser_click", Arguments={"selector": "nav a[href='/cottages']"})
  # Test form inputs
  call_mcp_tool(ServerName="playwright-mcp", ToolName="browser_fill_form", Arguments={"selector": "input[name='guests']", "value": "4"})
  # Take verification screenshot
  call_mcp_tool(ServerName="playwright-mcp", ToolName="browser_take_screenshot", Arguments={})
  ```

#### Phase E: Low-Level CDP Telemetry & Performance Audit (`chrome-devtools-mcp`)
- **100% Free & Unmetered** (Local Chrome DevTools Protocol).
- **When to Use**: Live console error audits (assert 0 errors), Cumulative Layout Shift ($CLS < 0.05$), and WCAG AA color contrast math.
- **Contract Examples**:
  ```python
  # Step 1: Discover active page ID (pageId is REQUIRED)
  call_mcp_tool(ServerName="chrome-devtools-mcp", ToolName="list_pages", Arguments={})
  # Step 2: Navigate to target URL
  call_mcp_tool(ServerName="chrome-devtools-mcp", ToolName="navigate_page", Arguments={"pageId": 1, "url": "http://localhost:3000"})
  # Step 3: Assert ZERO runtime console exceptions
  call_mcp_tool(ServerName="chrome-devtools-mcp", ToolName="list_console_messages", Arguments={"pageId": 1})
  # Step 4: Capture high-resolution visual screenshot
  call_mcp_tool(ServerName="chrome-devtools-mcp", ToolName="take_screenshot", Arguments={"pageId": 1, "format": "png"})
  ```

#### Zero-Credit Visual Media & Procedural 3D Policy
- **Zero Paid Credits**: Do NOT consume external paid credits (e.g. Higgsfield) for static mockups or videos when native and local alternatives exist.
- **Local API Gateway & Key Bridge (`scripts/get_gateway_key.py`)**: Automatically connects to the local gateway at `E:\Antigravity_to_api` (port 20128) to retrieve active API keys (`sk-...`) and leverage 15 frontier models with automatic Google OAuth quota failover (`429 RESOURCE_EXHAUSTED` auto-jump).
- **Procedural 3D Instead of Video (`img2threejs`)**: For hero objects, products, and characters, activate the `img2threejs` skill to rebuild 2D reference images into interactive, code-only Three.js models with a 6-stage sculpting pipeline. Eliminates video streaming overhead with silky 60fps real-time WebGL rendering at ZERO credit cost.
- **74 Curated Brand Design Systems (`references/design-systems/INDEX.md`)**: Ingest verified `DESIGN.md` tokens (Stripe, Linear, Apple, Vercel, Porsche, etc.) from the curated `awesome-design-md` registry to guarantee authentic aesthetics.
- **Headless 60fps Video Capture (`playwright-cli`)**: Use `playwright-cli video-start` and `playwright-cli video-stop` to record live browser walkthroughs and WebGL animations to high-definition WebM/MP4 locally on Windows at 0 cost.
- **Free Static Photography**: Scrape uncompressed Google Maps photos (`=s1600`) or Pinterest editorial boards (`/736x/`) via `harvest_assets.py`, or use native Antigravity IDE `generate_image` at zero credit cost.
- **Free Ambient Video Loops**: Harvest royalty-free web video loops via `harvest_assets.py --source video` (Pexels/Wikimedia, < 5MB) or use native 60fps CSS Ken-Burns animations (`animate-ken-burns`).


---

## Strict Operating Directives & Anti-Pattern Rules

1. **NO Static Plain-Text Question Dumps:**
   - **NEVER** output numbered lists of questions in markdown chat text (e.g. `1. What is your goal? 2. What color do you want?`).
   - **MANDATORY Interactive UI Tool Modals (`ask_question`):** All stage progression, discovery questions, and user decisions MUST be prompted via the native `ask_question` tool so that the user receives an interactive dialog modal with selectable buttons and a write-in input box.
2. **Step-by-Step Halts:**
   - Always halt execution and yield control after triggering an `ask_question` modal. Never combine questions from different stages into a single dump.
3. **Contextual Recommendation Framing:**
   - When calling `ask_question`, always place `(Recommended)` on the optimal option based on the business archetype, customer mindset, and performance budgets.
4. **Reference-Grounded Design Token Ingestion (Ban AI Slop Defaults):**
   - **NEVER** design in a vacuum or fall back on generic AI defaults: dark slate backgrounds (`#0B0F19`), glowing purple/indigo radial blur blobs, uniform 3-card grids, Inter-only typography, or hollow SaaS buzzwords.
   - Every project must be grounded in an award-winning benchmark reference website (proactively offered by the agent in Stage 4, or provided by the user).
   - Ingest computed styles via `scripts/extract_tokens.py` or native `chrome-devtools-mcp` to generate `DESIGN.md`.
   - Strictly enforce the 15 Greppable Negative Guardrails across layout, color, typography, copywriting, and media.
5. **Surgical, Intentional Asset Sourcing & Photo Re-Framing:**
   - **NEVER** randomly scrape or bulk download mismatched assets from multiple random websites.
   - Sourcing must be **strictly section-by-section and intentional**:
     - Exactly 1 signature hero image matching domain, aspect ratio, and lighting.
     - Section-specific feature/product visuals (only the exact items described in the copy).
     - Static images and photography MUST be extracted via `scripts/harvest_assets.py` from Google Maps (`=s1600`) or Pinterest editorial boards (`/736x/`) at zero credit cost.
     - When Google Maps photos are crooked, poorly lit, or goofy, use AI vision diagnosis + 8-Dimension De-AI photo synthesis via native `generate_image` (35mm film grain, directional natural window light, straight architectural framing) to preserve authentic venue identity.
6. **MANDATORY Multi-Skill & MCP Execution Gate:**
   - **NEVER** stop after generating `PRD.md` (planning paralysis).
   - **NEVER** jump directly to generating ungrounded, monolithic UI code in a single file with hardcoded hex colors, magic spacing, or emoji icons.
   - During **Stage 9**, the agent **MUST ACTUALLY CALL** the specialist skills and MCP tools via concrete tool calls (`view_file`, `run_command`, `call_mcp_tool`) following the exact 8-step build sequence.
7. **Progressive Disclosure Reference Library:**
   - [benchmark-references-and-anti-slop-guide.md](references/benchmark-references-and-anti-slop-guide.md): 3-Modality benchmark directory, computed JavaScript extraction payloads, ThreeUI guidelines, and 15 Greppable Negative Guardrails.
   - [page-and-feature-distribution-matrix.md](references/page-and-feature-distribution-matrix.md): Authoritative page-by-page breakdown, canonical routes, section anatomy, and mandatory vs. prohibited features for all 10 archetypes across SPA & MPA architectures.
   - [universal-archetypes-reference.md](references/universal-archetypes-reference.md): 10 universal archetypes, scarce resources, and feature matrices.
   - [information-architecture-guide.md](references/information-architecture-guide.md): Above-the-fold geometry, 55/45 hero grid, mid-funnel flow, persistent ambient mobile hotbars, and SPA vs. MPA rules.
   - [intake-protocol-and-decision-trees.md](references/intake-protocol-and-decision-trees.md): Bifurcated intake, customer mindset taxonomy, and psychological question sequencing.
   - [color-palettes-reference.md](references/color-palettes-reference.md): Curated design themes with WCAG AA compliant HEX tokens.
   - [tech-stack-and-gui-guide.md](references/tech-stack-and-gui-guide.md): Customer intent to tech stack matrix, LCP safety posters, and canvas memory management.
   - [enterprise-prd-template.md](references/enterprise-prd-template.md): 6-domain universal PRD blueprint, Asset Manifest Table, and Schema.org JSON-LD.
   - [intelligent-design-reasoning-engine.md](references/intelligent-design-reasoning-engine.md): 6-Dimension cognitive design reasoning framework (style, geometry, color grading, typography, media/3D strategy, and 3-benchmark grounding protocol).
   - [asset-and-media-intelligence-guide.md](references/asset-and-media-intelligence-guide.md): 8-Dimension de-AI photo synthesis framework, commercial archetype prompt templates, video generation via Higgsfield (generate_video), ambient web loop video performance (< 5MB, poster fallbacks), and automated media harvesting.
   - [multi-skill-and-mcp-orchestration-matrix.md](references/multi-skill-and-mcp-orchestration-matrix.md): Master routing matrix, aesthetic specialist selection table, verified MCP integration specs, and 5-phase engineering pipeline.
   - [reference-grounded-replication-engine.md](references/reference-grounded-replication-engine.md): The authoritative 6-vector specification for video-to-code decomposition, headless visual DNA extraction, decoupled IR schemas, and anti-median guardrails.
   - [universal-benchmark-catalog.md](references/universal-benchmark-catalog.md): Verified award-winning benchmark catalog across all 10 universal archetypes, specifying domain leaders, typography pairings, color grading, and unique spatial choreography.
   - [web-interface-guidelines.md](references/web-interface-guidelines.md): Vercel Web Interface Guidelines, MUST/SHOULD/NEVER rules, interaction affordances, form hydration, animation compositor constraints, and dark-mode theming.

---

## 9-Stage Architecture & Build Lifecycle

### The Interactive User Experience & Question Flow

> [!IMPORTANT]
> **STRICT CHRONOLOGICAL QUESTION SEQUENCE (NEVER ASK FOR BENCHMARK IN STAGE 1)**:
> 1. **Step 1 (Question 1: Business Intake ONLY)**: 
>    The AI asks **ONLY** for the client's business information (Google Maps listing OR business description/pitch). The AI **MUST NEVER** ask the user for a reference or benchmark website in this step, because the AI does not yet know what the business is!
> 2. **Step 2 (AI Autonomous Analysis & Benchmark Discovery)**:
>    The AI analyzes the business, classifies its commercial archetype, determines needed features, and automatically discovers the **top-rated, most beautiful, award-winning benchmark websites** specifically tailored to that exact business type.
> 3. **Step 3 (Question 2: User Selects from AI-Suggested Benchmarks)**:
>    The AI presents 3–4 stunning, curated benchmark websites tailored to the business (with live URLs and visual styles, plus a write-in option). The user picks their favorite. **THAT** becomes the reference website!
> 4. **Step 4 (AI Token Ingestion & PRD Blueprint Compilation)**:
>    The AI extracts tokens from the selected benchmark and compiles the full authoritative Product Requirements Document (`PRD.md`).
> 5. **Step 5 (Question 3: PRD Sign-Off)**:
>    The user reviews the PRD blueprint and confirms to begin the build.
> 6. **Step 6 (Questions 4+: Section-by-Section Design Options)**:
>    For each planned section (Hero, Story, Amenities, Dynamic Calculator, Contact), the AI generates 3 distinct design options (A, B, C) with visual SVG wireframe previews. The user selects their favorite option for each section.
> 7. **Step 7 (Autonomous Multi-Agent Build & Verification)**:
>    The 4-agent subnetwork builds the Next.js App Router project, harvests high-res photos and free ambient video, runs anti-slop AST gates, and verifies the site in the browser.

---

### Stage 1: The Two-Step Intake Protocol & Asset Sourcing Gate

When `/website-architect` is invoked (or a website project is started):

#### Step 1: Link & Business Intake
- The AI requests the client's business information (Google Maps listing, website URL, or business pitch) and optional benchmark reference URL.
- If the user's initial prompt **already contains** these links, the AI proceeds immediately to Step 2 without asking redundant questions.

#### Step 2: Interactive Asset Sourcing Gate (via `ask_question`)
The AI prompts the user to declare how visual media (photos, videos, brand marks) should be sourced:
- **Tool Call**:
  ```python
  ask_question(
    questions=[{
      "question": "How would you like to source visual and media assets (photos, videos, brand logos) for this website build?",
      "options": [
        "(Recommended) Hybrid: Combine assets I place in the project folder with scraped Google Maps photos, reviews, and vectors.",
        "User-Provided Assets Only: Exclusively scan and curate high-res photos and videos I have placed in the project folder.",
        "Google Maps & Scraped Only: Autonomously harvest all photography, customer reviews, and vectors from Google Maps & web sources."
      ],
      "is_multi_select": False
    }],
    toolSummary="Asset sourcing preference",
    toolAction="Asking user asset sourcing preference"
  )
  ```

#### Step 2.5: Forensic Media Curation & Vision Inspection (`curate_user_assets.py`)
Once the sourcing mode is confirmed:
1. **Execute Curation Engine**:
   ```bash
   python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/curate_user_assets.py" --mode <hybrid|user_only|maps_only> --user-dir user_assets --maps-manifest public/assets/assets_manifest.json --public-dir public/assets
   ```
2. **Vision Inspection Protocol (`view_file`)**:
   - The AI inspects each user-provided photo or extracted video frame using `view_file`.
   - Analyzes subject matter (exterior grounds, interior suite, culinary plating, staff portrait), aspect ratio (16:9, 4:3, 1:1, 9:16), and lighting quality.
   - Maps each image to its optimal candidate section (`Section01Hero`, `Section02Story`, `Section04Accommodations`, `Section05Gastronomy`).
3. **Keyframe Video Extraction & Generation**:
   - `ffmpeg` automatically extracts `*_first_frame.jpg` (used as video poster and LCP anchor), `*_mid_frame.jpg`, and `*_last_frame.jpg`.
   - If an ambient hero video is missing or the provided video has an awkward angle:
     - **Higgsfield MCP `generate_video` (When Authorized)**: Feed the extracted first-frame image to `generate_video` with cinematic camera direction.
     - **Zero-Credit Fallback (Free & Instant)**: YouTube B-Roll extraction via `yt-dlp` or 60fps GPU Ken-Burns animation applied to the highest-resolution still photograph.

---

### Stage 1.5: Developer-Grade Web Intelligence & Competitor Scouting Engine

> [!IMPORTANT]
> **GROUNDING IN REALITY: ZERO HALLUCINATED COPY OR SPECIFICATIONS**
> Senior software engineers never invent fake products, placeholder menus, or mock pricing when live data exists on the web.
> Before classifying the business in Stage 2, the agent **MUST** run active internet reconnaissance:

#### Step 1.5A: Entity & Brand Footprint Discovery (`search_web`)
- If the user provides a business name, brand, or concept without a direct URL:
  Execute `search_web` to discover:
  1. The business's official website domain.
  2. Official Google Maps listing or physical venue address.
  3. Active social channels (Instagram, LinkedIn, X, YouTube).
  4. Real founders, founding year, key team members, and notable press mentions.
  - Example: `search_web(query="<business_name> official website locations menu story")`

#### Step 1.5B: Authentic Copywriting & Spec Ingestion (`read_url_content`)
- If an official website or public page is discovered:
  Execute `read_url_content` on key routes (`/about`, `/menu`, `/pricing`, `/services`):
  - Extract authentic brand voice, taglines, and core value propositions.
  - Capture real product names, item descriptions, and transparent pricing.
  - Capture verified customer testimonials and review ratings.
  - Ingest raw text directly into the project scratchpad (`assets/raw_scouted_data.txt`).

#### Step 1.5C: Live Award-Winning Benchmark Scouting (`search_web`)
- Rather than relying solely on static catalog examples, query the live internet for recent award-winning sites in the exact commercial archetype:
  - Example: `search_web(query="best <commercial_archetype> website design awwwards godly siteinspire")`
  - Identify 3 live, visually breathtaking benchmark URLs with distinct visual DNA to present to the user in Stage 4.

#### Step 1.5D: Synthesized Profile Ingestion into `classify_business.py`
- Consolidate all verified facts into a comprehensive synthesized brief:
  ```bash
  python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/classify_business.py" --pitch "<synthesized_scouted_data>" --name "<business_name>" --out assets/business_profile.json
  ```
- This ensures Stage 2 and all subsequent section blueprints are 100% grounded in authentic commercial reality.

---

### Stage 2: Autonomous Business Classification & 'Needed Things' Blueprint

Once input is received (either via Google Maps link or business pitch):
1. **Autonomous Intelligence Execution (`classify_business.py` & `harvest_assets.py`):**
   - **If a Google Maps URL is provided:**
     Run `harvest_assets.py` to scrape full place metadata (name, category, rating, reviews count, address, phone, hours, photos) and immediately run `classify_business.py`:
     ```bash
     python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/harvest_assets.py" --source maps --query "<url>" --out assets/
     python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/classify_business.py" --maps-data assets/maps_data.json --out assets/business_profile.json
     ```
   - **If a Business Description / Pitch is provided:**
     Run `classify_business.py` directly with the pitch text:
     ```bash
     python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/classify_business.py" --pitch "<pitch>" --out assets/business_profile.json
     ```

2. **Present Exhaustive Business Intelligence & 'Needed Things' Summary:**
   Output the structured classification directly to the user:
   - **Identified Archetype & Commercial Sub-Type:** State the matched archetype (1 of 10) and specific commercial sub-type (e.g., *Archetype 1: Local Food & Beverage / Hospitality -> Luxury Farmstay, Resort & Destination Event Grounds*).
   - **Primary Revenue Model & Scarce Operational Resource:** State the revenue mechanism and core operational bottleneck (e.g., *Weekend calendar dates & private cottage booking slots*).
   - **Customer Arrival Mindset & Performance Budget:** State customer psychology and Core Web Vitals target (e.g., *High-Ticket Experiential Deliberator; Target LCP < 1.2s, CLS < 0.02*).
   - **Architecture Decision Score (ADS) & Topology:** State the computed formula:
     $$\text{ADS} = \text{Catalog Depth} (1-5) + \text{Search Specificity} (1-5) + \text{Journey Deliberation} (1-5) - \text{Immediacy Need} (1-5)$$
     Confirm topology: **Single-Page Architecture (SPA)** if $\text{ADS} \le 5$, or **Multi-Page Architecture (MPA)** if $\text{ADS} \ge 6$.
   - **Needed Things: Complete Canonical Page / Section Anatomy:**
     Present the exact section sequence (1.0 to N.0) or canonical routes with layout types and content purposes.
   - **Needed Things: Interactive Conversion Modules (Must-Haves):**
     List the exact dynamic interactive modules required (e.g., Dynamic Stay Rate Calculator with guest slider, Zero-Commission WhatsApp Payload Dispatcher, Persistent Mobile Action Hotbar, 60fps Grounds Video Scrubber, Accessible FAQ Accordion).
   - **Needed Things: North-Star Conversion Event (CTA):**
     State the primary conversion mechanism with the exact pre-filled WhatsApp message payload template.
   - **Needed Things: Back-Office Hub:**
     State the operational dispatch schema (Direct WhatsApp URL encoder, webhook to Google Sheets / CRM).
   - **Needed Things: Aesthetic Thesis & Modality:**
     State inferred modality (Modality 1, 2, or 3), selected specialist skill (`soft-skill`, `minimalist-skill`, `brutalist-skill`, `gpt-tasteskill`, `redesign-skill`), spatial geometry (e.g., 60/40 Asymmetric Split), color palette tokens, and typography pairing.
   - **Needed Things: 3 Curated Live Human-Crafted Benchmark References:**
     List 3 award-winning live websites with URLs and visual DNA matching this exact category.

---

### Stage 3: Autonomous Universal Tech Stack Architecture Lock (Zero User Prompt)

> [!IMPORTANT]
> **THE UNIVERSAL OMNIPOTENT TECHNOLOGY STACK (PRODUCTION STANDARD)**
> To deliver maximum interactivity, instantaneous load times, robust multi-page SEO, and full-stack API capabilities without requiring user deliberation, `website-architect` locks in one universal, production-grade foundation:
> 
> **Next.js 15 (App Router) + TypeScript + Tailwind CSS v4 + Motion (Framer Motion) + Lucide React + Radix UI Primitives**
> 
> **Why this single universal stack is capable of everything:**
> 1. **Infinite Interactivity & Client State**: Feature modules use `"use client"` for real-time stay rate calculators, slide-out cart drawers, 60fps spring animations, interactive bento grids, and filters without hydration bugs.
> 2. **Full Multi-Page Architecture (MPA) & SEO**: Complete App Router routing (`/`, `/about`, `/services/[slug]`, `/pricing`, `/contact`) with React Server Components (RSC), dynamic metadata (`generateMetadata`), OpenGraph images, and automated sitemaps. Zero hash-jump illusion.
> 3. **Full-Stack Backend & Server Actions**: Edge API routes (`app/api/*`), Server Actions for zero-JS form submissions, direct database connections (Supabase, Prisma), and webhook processing (Stripe, WhatsApp, n8n).
> 4. **Universal Component Ecosystem**: Drop-in compatibility with `magicuidesign-mcp` (bento grids, marquees), `21st-magic` (brand vector SVGs), `@designcodeio/threeui`, Three.js WebGL canvas, Lucide icons, and Radix UI.
> 5. **Universal Deployment**: Instantly exportable to static HTML (`output: 'export'`) for sub-0.6s FCP edge CDN delivery, or deployed to Vercel/Node.js/Docker with zero configuration changes.
>
> The agent logs this universal stack directly into the project architecture and `PRD.md` without prompting the user.

---

### Stage 4: Autonomous Modality & Live Benchmark Token Ingestion

To eliminate generic "AI Slop" and ground the website in human-crafted design, Stage 4 executes autonomous modality assignment and deep token extraction:

#### Step 4A: Autonomous Experience Modality Inference (The AI Decides)
The agent autonomously infers the optimal experience modality from the business archetype and customer psychology:
- **Modality 1: High-Utility / Conversion-First**:
  - *Assigned For*: Local Physical Services & Trades (Plumbing, HVAC, Roofing, Towing), Express Food & Takeaway Dining, High-Volume E-Commerce Catalogs, B2B Industrial Supply.
  - *Signature*: Sub-0.8s FCP, zero scroll-jacking, persistent ambient mobile hotbar (direct WhatsApp/Call dispatch), friction-free sticky CTAs, instant tabbed pricing.
- **Modality 2: Hybrid Interactive / Scrollytelling**:
  - *Assigned For*: Luxury Farmstays, Resorts & Boutique Hotels, Destination Dining, High-Trust Professional Advisory (Boutique Law/Finance), Aesthetic Medical Clinics, Creative Agencies, Cohort Masterclasses.
  - *Signature*: Awwwards-caliber entrance reveals, Doppelrand nested containers, animated bento grids via Magic UI, dynamic rate/stay calculators, kinetic typography, 60fps micro-interactions.
- **Modality 3: Full Canvas / Immersive Showcase**:
  - *Assigned For*: Flagship Hardware, Luxury Automotive, Avant-Garde Fashion, High-End Web3 Platforms, Boutique Motion Studios.
  - *Signature*: Continuous 60fps ThreeUI / Three.js WebGL canvas background, interactive 3D model orbit/manipulation, shader fluid effects, audio-visual ambiance.

The agent logs the inferred modality and reasoning into `PRD.md` with zero modal friction.

#### Step 4B: Benchmark Grounding & Reference Selection
- **If the user already provided a reference URL in Stage 1**:
  Immediately proceed to Step 4C to extract tokens directly from that URL.
- **If no reference URL was provided**:
  Consult [benchmark-references-and-anti-slop-guide.md](references/benchmark-references-and-anti-slop-guide.md) to retrieve the **3 award-winning benchmark reference websites** matching the Category + Modality combination.
  Call `ask_question`:
  - **Question:** "Select an award-winning benchmark reference website (or enter your own URL) to ground the visual design tokens:"
  - **Options:**
    - `1. (Recommended) Benchmark Option A: <Name> (<URL>) - <Visual DNA: e.g. Earthy luxury, high-contrast serif headlines, warm stone background (#FAF8F5), generous 120px whitespace, zero card borders.>`
    - `2. Benchmark Option B: <Name> (<URL>) - <Visual DNA: e.g. Minimalist architectural calm, full-bleed cinematic imagery, asymmetric 60/40 layouts, deep espresso ink typography.>`
    - `3. Benchmark Option C: <Name> (<URL>) - <Visual DNA: e.g. High-density Swiss grid, tactile amber surfaces, interactive sensory elements.>`
    - `4. Custom Reference Website URL: Enter any live public URL whose aesthetic, layout, colors, or typography you love.`
  - **Action:** STOP AND WAIT FOR USER SELECTION.

#### Step 4C: Automated 60fps Deep Token Extraction (`extract_tokens.py`)
Once the benchmark is selected (or user supplies a URL):
- Run the automated token extraction engine via `run_command`:
  ```bash
  python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/extract_tokens.py" --url "<selected_url>" --out DESIGN.md --tokens-out design_tokens.json --assets assets/
  ```
- The engine executes with GPU acceleration (`--use-gl=angle`, `--enable-webgl`, `--enable-gpu-rasterization`):
  - Captures declared fluid typography (`clamp()`, `rem`, `@media`) via CDP `CSS.getMatchedStylesForNode`.
  - Captures active WAAPI animation tracks and CSS `@keyframes`.
  - Captures tree-shaken GSAP ScrollTrigger pins and triggers.
  - Records WebGL/2D canvas streams at **60fps / 6 Mbps** as background WebM loops.
  - Profiles micro-interaction `:hover` deltas and transition curves.
  - Profiles responsive layout matrices across Desktop (1440), Tablet (768), and Mobile (390).
- Automatically saves `DESIGN.md` in the project root.

#### Step 4D: Video Recording Reference Decomposition (`video_to_wireframe.py`)
When the user provides a video recording (`.mp4`, `.mov`, `.webm`) of a reference site:
- Run: `python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/video_to_wireframe.py" --video "<video_file>" --out wireframes/`
- Extracts keyframe visual wireframes, detects layout transitions, isolates arched photo masks, and generates reference layout schemas.

#### Step 4E: Multi-Page Recursive Sitemap Crawling (`crawl_sitemap.py`)
When the user provides a multi-page reference website URL:
- Run: `python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/crawl_sitemap.py" --url "<reference_url>" --out sitemap.json`
- Ingests the real route hierarchy (e.g., `/visit/`, `/programs/`, `/admissions/`), capturing subpage topologies to replicate true multi-page depth.

---

### Stage 5: Autonomous Conversion Engine & Interactive Accelerators (The AI Decides)
Consult [universal-archetypes-reference.md](references/universal-archetypes-reference.md) and [page-and-feature-distribution-matrix.md](references/page-and-feature-distribution-matrix.md) to autonomously assign:
1. **North-Star Conversion Action**:
   - *Hospitality / Destination Dining*: Direct Structured WhatsApp Date Reservation (zero commission, instant confirmation).
   - *Emergency Trades / Physical Services*: Direct Click-to-Call Emergency Hotline + 1-Tap WhatsApp Dispatch.
   - *E-Commerce & Retail*: 1-Click Express Checkout + Slide-Out Sticky Cart Drawer.
   - *B2B Software & SaaS*: Interactive Product Sandbox / 14-Day Self-Serve Trial.
   - *High-Trust Advisory & Healthcare*: Confidential Case Assessment Sheet / Provider Booking Slot.
2. **Interactive Accelerators & Feature Modules**:
   - Autonomously configure category-specific modules: Dynamic Stay Rate Calculator, Reactive Menu Search with dietary tags, Delivery Partner Links (Swiggy/Zomato), Before/After Interactive Comparison Slider, CAD Spec Uploader.
   - Strictly prohibit destructive anti-patterns (NO raw PDF menus, NO heavy WebGL on transactional checkouts, NO un-priced booking forms).

---

### Stage 6: Autonomous Systems of Record & Back-Office Hub (The AI Decides)
Autonomously determine the back-office dispatch and settlement pipeline:
1. **Lead & Order Routing**:
   - Configure zero-commission structured WhatsApp URL encoder with formatted order/booking summaries (`Name`, `Date/Guests`, `Package/Items`, `Total Estimate`).
   - Configure webhook schema for cloud databases (Supabase / Firebase / Google Sheets) and automated workflows (`n8n`).
2. **Settlement Architecture**:
   - Hybrid payment model: Instant Online UPI / Card processing + Pay on Arrival / Cash on Delivery (COD) for physical venues, or prepaid Stripe Elements for SaaS/e-commerce.

---

### Stage 7: Autonomous Asset Intelligence & Photo Sourcing Pipeline
1. **Surgical Asset Inventory Assessment**:
   - Scan `assets/` using `list_dir`.
   - Identify exact section slots: 1 Signature Hero ($\ge 1600\text{px}$), specific item photos matching copy, and verified brand vector marks.
2. **Two-Stage Photo Upgrade Pipeline (Fixing Ugly Maps Photos)**:
   - For crooked, blurry, or poorly lit Google Maps photos:
     - Perform AI visual diagnosis (subject, tilt angle, lighting flaws).
     - Synthesize photo-real replacements using the **8-Dimension De-AI Photo Framework** via native `generate_image` (35mm film stock, 50mm f/2.8 lens, directional natural window light, straight horizontal horizon, porous textures, zero plastic smoothing) at **zero credit cost**.
3. **Automated Media Harvesting**:
   - Editorial photography: `python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/harvest_assets.py" --source pinterest --query "<item>" --out assets/`
   - Ambient video loops: `python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/harvest_assets.py" --source video --query "<topic>" --out assets/`
   - AI cinematic video: For high-prestige hero loops, invoke `higgsfield` (`generate_video`) with 5-second slow-glide prompts at 60fps.
4. **Autonomous Asset Tagging & Manifest Generation**:
   - The AI inspects detected images and videos in `assets/`, autonomously classifies each asset by role (`Signature Hero`, `Brand Logo`, `Grounds Ambiance`, `Service Card`, `Gallery Photo`), and records every entry in the **Authoritative Asset Manifest Table** (`Asset ID`, `Filename`, `Type`, `Source`, `Placement`, `Alt/Poster`, `Status`) without pestering the user with repetitive questions per file.

---

### Stage 8: Enterprise PRD Delivery & Build Authorization (Turn 2 — Interactive Checkpoint)
Generate an exhaustive, production-grade Product Requirements Document saved to `PRD.md` in the project root:
1. **Executive Strategy & Operational Model** (Capability, Target Persona, Scarce Resource, North-Star Metric)
2. **Grounded Benchmark Reference & Design System** (Reference URL, Visual DNA, Extracted Typography & Color Tokens from `DESIGN.md`)
3. **Architecture Topology & Canonical Sitemap** (Universal Next.js App Router stack, SPA vs MPA ADS score justification, exact URL routing tree)
4. **Exact Page & Component Specification** (Section-by-section anatomy for EVERY canonical page with 60/40 splits and interactive modules)
5. **Anti-Slop Compliance & Quality Gate Checklist** (Verification against all 15 Greppable Negative Guardrails)
6. **Technical Architecture & Back-Office Protocols** (Client state stores, WhatsApp URL encoder, webhook schemas)
7. **Authoritative Asset Manifest Table** (All media mapped with ID, Source, Placement, Alt Text, and Verification Status)
8. **Schema.org Structured Data & Core Web Vitals Performance Budgets** (JSON-LD script payload, LCP < 1.2s, CLS < 0.05)

**Build Authorization Checkpoint:**
Call `ask_question`:
- **Question:** "PRD successfully compiled and verified against all architecture standards. How would you like to proceed with the build?"
- **Options:**
  - `1. (Recommended) Proceed to Production Build: Launch Stage 9 autonomous implementation pipeline across all UI skills and MCPs.`
  - `2. Refine PRD Specifications: Adjust architecture, section anatomy, or integrations before code generation.`
- **Action:** STOP AND WAIT FOR THE USER'S SELECTION.

---

### Stage 9: Production Website Building: The Section-by-Section Option Protocol & Master Multi-Skill Pipeline (Active Code Construction)

> [!IMPORTANT]
> **THE SECTION-BY-SECTION HUMAN-IN-THE-LOOP REVOLUTION (ZERO BLACK-BOX CODE DUMPS)**
> Traditional AI web builders fail because they treat page generation as an unguided, monolithic "black-box" prompt. This causes **hallucination amplification**, **template mode collapse ("AI slop")**, and **user disempowerment**.
> In `website-architect`, the durable unit of construction is the **section**, not the entire page.
> Before ANY section code is committed, the agent **MUST** execute the Section-by-Section Option Protocol:
> 1. **Divergent Option Planning**: Propose exactly 3 structurally divergent options differing across $\ge 3$ structural axes (Composition, Density, Media, Reading direction, Interaction, Typography role, Rhythm).
> 2. **Zero-Credit Visual Preview**: Generate programmatic SVG wireframe diagrams and lightweight HTML previews via `section_option_previewer.py` (ZERO image-gen API credits burned).
> 3. **Human Choice Modal**: Present structured decision cards via the interactive `ask_question` tool modal, halting execution until the user selects Option A, B, C, or a Custom Hybrid.
> 4. **Scoped Mutation**: Author ONLY the approved section component (`src/components/sections/<section_id>.tsx`), pulling verified primitives via 3-tier resilient sourcing (`resilient_sourcing.py`).
> 5. **AST Verification**: Audit the section against anti-slop rules before advancing.
> 6. **Full Integration Audit**: At page completion, run `anti_slop_gate.py`, `verify_orchestration.py`, and live browser verification via `chrome-devtools-mcp`.

```
┌────────────────────────────────────────────────────────────────────────┐
│ 9.0 GLOBAL DESIGN SYSTEM & FOUNDATION SETUP                            │
│     • Ingest tokens from DESIGN.md & design_tokens.json                │
│     • Inject :root CSS variables & Tailwind @theme in globals.css      │
│     • Establish 8dp spatial rhythm, concentric radii, Google Fonts     │
│     • Build application layout shell (Header, Nav, Footer placeholder) │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 9.LOOP: SECTION-BY-SECTION ITERATIVE APPROVAL LIFECYCLE                │
│                                                                        │
│ For each planned section (Hero, Features, Proof, Conversion, Footer):   │
│                                                                        │
│ ┌──────────────────────────────────────────────────────────────────┐   │
│ │ 9.N.1 RUN ZERO-CREDIT PREVIEW ENGINE                             │   │
│ │       Command: python section_option_previewer.py                │   │
│ │                --section <type> --tokens design_tokens.json      │   │
│ │       Generates 3 divergent manifests & 16:9 SVG wireframe cards │   │
│ └─────────────────────────────────┬────────────────────────────────┘   │
│                                   │                                    │
│                                   ▼                                    │
│ ┌──────────────────────────────────────────────────────────────────┐   │
│ │ 9.N.2 HUMAN-IN-THE-LOOP CHOICE MODAL (ask_question)              │   │
│ │       Display Option A (Recommended), Option B, Option C, Hybrid │   │
│ │       Embed SVG wireframe previews & design trade-offs           │   │
│ │       HALT EXECUTION & AWAIT USER SELECTION                      │   │
│ └─────────────────────────────────┬────────────────────────────────┘   │
│                                   │                                    │
│                                   ▼                                    │
│ ┌──────────────────────────────────────────────────────────────────┐   │
│ │ 9.N.3 SCOPED COMPONENT CONSTRUCTION & RESILIENT SOURCING         │   │
│ │       Fetch primitives via resilient_sourcing.py (Magic UI / SVGs│   │
│ │       Author ONLY src/components/sections/<section_id>.tsx       │   │
│ │       Strictly consume semantic tokens (ZERO raw hex codes)      │   │
│ └─────────────────────────────────┬────────────────────────────────┘   │
│                                   │                                    │
│                                   ▼                                    │
│ ┌──────────────────────────────────────────────────────────────────┐   │
│ │ 9.N.4 SECTION AST CHECK & CHECKPOINT COMMIT                      │   │
│ │       Run section-level anti-slop check                          │   │
│ │       Record ToolReceipt and advance to next section             │   │
│ └──────────────────────────────────────────────────────────────────┘   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ (All sections approved)
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 9.FINAL: FULL-PAGE INTEGRATION & QUALITY VERIFICATION GATES            │
│     • Automated Anti-Slop AST Gate (anti_slop_gate.py)                 │
│     • Multi-Skill & MCP Orchestration Verifier (verify_orchestration.py│
│     • Anti-Anchor-Illusion MPA Gate (check_no_anchor_illusion.py)      │
│     • Live In-Browser Dev Server Verification (chrome-devtools-mcp)    │
│       Assert zero console errors, zero layout shifts, capture snapshot │
└────────────────────────────────────────────────────────────────────────┘
```

---

#### Detailed Execution Contracts:

### Phase 9.0: Global Design System & Foundation Setup

1. **Step 9.0.1: Design Intelligence & Token Ingestion (`DESIGN.md` & `ui-ux-pro-max`)**:
   - Ingest the extracted `DESIGN.md` and `design_tokens.json` created during Stage 4.
   - Query `ui-ux-pro-max` search script for palette math and typography pairing:
     ```bash
     python "C:/Users/anbua/.gemini/config/skills/ui-ux-pro-max/scripts/search.py" "<archetype> <stack>" --design-system
     ```
   - Extract Google Fonts `@import` URL, WCAG-tested color tokens, and section composition guidelines.

2. **Step 9.0.2: Production Design Tokens & Primitives (`design-system` & `ui-styling`)**:
   - Create or update global stylesheet (`src/app/globals.css` or `src/index.css`) with three-layer semantic tokens directly mapped from `DESIGN.md`:
     ```css
     :root {
       /* Benchmark Extracted Typography */
       --font-display: var(--font-display, "Playfair Display", serif);
       --font-body: var(--font-body, "Plus Jakarta Sans", sans-serif);

       /* Benchmark Extracted Surfaces & Ink */
       --color-canvas: <benchmark-canvas-bg>;
       --color-ink: <benchmark-ink-color>;
       --color-headline: <benchmark-headline-color>;
       --color-accent: <benchmark-accent-color>;
       --color-accent-foreground: <benchmark-accent-fg>;
       --color-border: rgba(0, 0, 0, 0.08);

       /* Spatial Scale */
       --space-1: 4px;
       --space-2: 8px;
       --space-4: 16px;
       --space-8: 32px;
       --space-16: 64px;
       --space-24: 96px;
       --space-32: 128px;
       --radius-sm: 6px;
       --radius-md: 10px;
       --radius-lg: 16px;

       /* Vercel Web Interface Guidelines: Layered Shadows & Crisp Borders */
       --shadow-ambient: 0 1px 2px rgba(0, 0, 0, 0.04);
       --shadow-direct: 0 8px 24px -4px rgba(0, 0, 0, 0.08);
       --shadow-layered: var(--shadow-ambient), var(--shadow-direct);
     }

     /* Dark Mode & OS Theming */
     :root[data-theme="dark"], html.dark {
       color-scheme: dark;
     }

     /* Windows <select> Contrast Bug Fix */
     select, option {
       background-color: var(--color-canvas);
       color: var(--color-ink);
     }
     ```
   - Enforce: **Strictly ZERO raw hex codes inside component files**. All styling must consume semantic design tokens.
   - Enforce Concentric Nested Radii: $r_{child} \le r_{parent} - \text{padding}$.
   - Ensure `<meta name="theme-color">` aligns with the canvas background.

3. **Step 9.0.3: Layout Shell & Navigation**:
   - Construct `src/components/layout/Header.tsx` with logo, desktop navigation links using Next.js `<Link>`, and mobile responsive drawer trigger.
   - Construct layout shell (`src/app/layout.tsx`) injecting font links, metadata, and persistent ambient mobile hotbar.

---

### Phase 9.Loop: The Section-by-Section Iterative Approval Lifecycle

For each section declared in `PRD.md` / `page_blueprint.json` (typically: **Hero**, **Proof/Marquee**, **Features/Bento**, **Intermission/Story**, **Conversion/Calculator**, **Footer**):

#### Sub-Step 9.N.1: Divergent Option Planning & Zero-Credit SVG Rendering
- Run the automated preview engine:
  ```bash
  python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/section_option_previewer.py" --section <section_type> --tokens design_tokens.json --out-dir .website-architect/previews
  ```
- Generates exactly 3 structurally divergent options with validated pairwise divergence distance ($\ge 3$ axes):
  - **Hero Options**: Asymmetric 60/40 Split vs. Full-Bleed Media Stage vs. Editorial Stack.
  - **Features Options**: Asymmetric Bento Grid (8-col + 4-col) vs. Tabular Index Strip with Sticky Stage vs. 5/7 Capability Stage.
  - **Proof Options**: Infinite SVG Marquee + 3 Hard Metrics vs. Tabbed Case Study Carousel vs. Asymmetric Pull-Quote with Audited ROI Card.
  - **Conversion Options**: Dynamic Parameter Calculator Stage vs. Transparent Tier Comparison Matrix vs. Asymmetric 60/40 Reservation Funnel.
  - **Footer Options**: Oversized Brand Mark with 4-Col Directory vs. Conversion Pre-Footer Stage vs. High-Density Utility Directory.
- Automatically writes 16:9 vectorized SVG wireframes to `.website-architect/previews/<section>_<optionId>.svg` at **zero credit cost**.

#### Sub-Step 9.N.2: Human-in-the-Loop Decision Modal (`ask_question`)
- Prompt the user with the structured decision modal:
  ```python
  ask_question(
    questions=[{
      "question": "Select the layout archetype for section: [HERO]",
      "options": [
        "(Recommended) Option A: Asymmetric 60/40 Editorial Split (asymmetric-split) - High-impact narrative pairing display serif copy against framed photography with proof badge. [Tradeoff: Requires high-resolution vertical photography]",
        "Option B: Full-Bleed Media Stage with Anchor Block (full-bleed-stage) - Cinematic visual immersion with bottom-left anchored typography and live operational status pill. [Tradeoff: Heavier media requirement < 5MB]",
        "Option C: Type-Led Editorial Stack with Landscape Horizon (editorial-stack) - Oversized typographic manifesto with centered proof strip and wide landscape showcase below. [Tradeoff: Higher vertical scroll space]",
        "Custom / Hybrid: Combine Option A's base structure with specific elements from Option B or C.",
        "Agent Autonomously Decides: Proceed with Option A based on benchmark tokens."
      ]
    }],
    toolAction="Presenting section layout options",
    toolSummary="Section layout selection modal"
  )
  ```
- **Action**: STOP AND WAIT FOR USER SELECTION. Never proceed without user decision.

#### Sub-Step 9.N.3: Scoped Component Construction & Resilient Sourcing
- Author **ONLY** the approved section component inside `src/components/sections/<section_id>.tsx`.
- Strictly prohibit modifying files outside the active section boundary.
- **Resilient 3-Tier Sourcing (`resilient_sourcing.py`)**:
  - If the section requires animated UI primitives (bento grid, marquee, shimmer button):
    Fetch verified code via:
    ```bash
    python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/resilient_sourcing.py" component "bento-grid" --out src/components/ui/bento-grid.tsx
    python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/resilient_sourcing.py" component "shimmer-button" --out src/components/ui/shimmer-button.tsx
    ```
  - If the section displays client/partner marks:
    Batch-fetch genuine brand vector SVGs via:
    ```bash
    python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/resilient_sourcing.py" batch-logos "stripe,google,amazon,intel,apple" --out public/assets/logos
    ```
    *Strictly Banned*: Text-only placards or emoji icons for partner showcases.
  - Link authentic imagery from `assets/` matching the Asset Manifest from Stage 7.
  - Enforce Vercel Web Interface Guidelines:
    - Visible `:focus-visible` rings on all interactive elements.
    - Touch targets $\ge 44\times 44\text{px}$ on desktop and $\ge 48\times 48\text{dp}$ on mobile.
    - All links use Next.js `<Link>`.
    - Compositor-only animations (`transform`, `opacity`). Zero `transition: all`.
    - Negative display letter-spacing (`-0.02em` to `-0.035em`) on display headlines.

#### Sub-Step 9.N.4: Section-Level AST & Anti-Slop Audit
- Run immediate static scan on the section:
  ```bash
  python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/anti_slop_gate.py" <path_to_project_root>
  ```
- If violations are detected (e.g. raw hex color, missing token, emoji icon), repair immediately before advancing.

#### Sub-Step 9.N.5: Section Commit & Advance
- Record tool receipt in execution history, commit the section component, and advance to the next section in `page_blueprint.json`.

---

### Phase 9.Final: Full-Page Integration & Quality Verification Gates (v2.3.0)

Once all sections are constructed and assembled into the page route:

1. **Gate 2: Static Anti-Slop & Token Integrity (`anti_slop_static_patch.py` — MANDATORY PRE-DELIVERY GATE)**:
   ```bash
   python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/anti_slop_static_patch.py" <path_to_project_root>
   ```
   Enforces:
   - **Dual-Layer Color Science**:
     * *Layer 1 (CIEDE2000 Math)*: Evaluates $\Delta E_{00}$ against the 5-point generic slate cluster (`#0B0F19`, `#0F172A`, `#020617`, `#111827`, `#030712`): Hard fail $\le 3.5$, warning $3.5 - 5.0$.
     * *Layer 2 (Continuous Dark Slate-Space Filter)*: Detects any cool blue-gray tone ($L^* \le 30.0$, $b^* \le -3.0$, $\text{Hue} \in [240^\circ, 285^\circ]$). Catches slate-800 (`#1E293B`), gray-800 (`#1F2937`), slate-700 (`#334155`), `#1B2027`, and `#0E1420`, while mathematically sparing neutral charcoal (`#121212`) and warm stone (`#1C1917`).
   - **Modern CSS Color Parser**: Automatically parses and converts `oklch()`, `hsl()`, bare HSL triplets (`--background: 222.2 47.4% 11.2%;`), and `color(display-p3)` in `globals.css` and tokens.
   - **Alpha Compositing**: 8-digit translucent hex codes are composited over dark canvas (`#000000`) before $\Delta E$ checks.
   - **Balanced Tag Parser**: Uses quote- and brace-balanced parsing for `<Image>` and `<img>` tags, immune to `>` inside arrow functions (`onLoad={() => ...}`) or classNames.
   - **Case-Insensitive Anchor Lookahead**: Lookahead `(?![0-9a-zA-Z_-])` protects camelCase anchors like `#addToCart` from matching `#add`.
   - **Rule-Scoped Pragmas**: Requires explicit rule and justification (`// anti-slop-allow: <rule-name> reason: <justification>`). Unscoped pragmas are rejected.
   - **Full File Coverage**: Scans `.tsx`, `.jsx`, `.ts`, `.css`, `.scss`, and `.svg` files across `app`, `components`, `lib`, `src`, `styles`, and `hooks`.
   - **Fail-Closed Guarantee**: Exits with code 1 if 0 source files are scanned or 0 pages exist.

2. **Gate 2.Receipts: Multi-Skill & Asset Orchestration Gate (`verify_orchestration.py` — MANDATORY PRE-DELIVERY GATE)**:
   ```bash
   python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/verify_orchestration.py" <path_to_project_root>
   ```
   Checks `.arch/receipts/stage-<n>-<skill>.json` cryptographically. Guarantees:
   - Claimed Magic UI or 21st components physically exist with verified registry implementations.
   - Authentic brand vector SVGs exist in `public/assets/logos/` for partner showcases.
   - Design tokens are verified as consumed, supporting both `var(--token)` and compiled Tailwind v4 utility classes (`bg-brand-primary`).

3. **Gate 3: Rendered Runtime & Accessibility Gate (`runtime_gate.py` — MANDATORY GATE)**:
   ```bash
   python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/runtime_gate.py" http://localhost:3000 --min-routes 4
   ```
   Dual-viewport testing: Mobile (Pixel 7 emulation, touch, DPR 2.625) and Desktop (1440x900):
   - **Visually Hidden Skip Link Exemption**: Exempts `.sr-only`, `clip: rect(0,0,0,0)`, and 1x1px skip anchors from tap-target size violations.
   - **Intelligent In-Sentence Link Heuristic**: Distinguishes inline prose links from mobile navigation items by checking parent text volume. Strictly enforces $\ge 44\times 44\text{px}$ targets on solitary navigation links (`<li><a>`).
   - **Inner Scroll Container Discovery**: Detects scrolling `<main>` or documentElement when body has `overflow: hidden`.
   - **Deterministic Hydration Readiness**: Awaits `document.readyState === 'complete'`, `document.fonts.ready`, and all lazy images before auditing.
   - **Dynamic Full-Page Step-Scrolling**: Steps through scroll height in 50% viewport increments with instant behavior, triggering dynamic imports and scroll observers.
   - **Official Session-Window CLS**: Measures maximum session window (shifts with $<1\text{s}$ gap up to $5\text{s}$ max window).
   - **Windows Sub-Pixel Tolerance**: `scrollWidth > clientWidth + 1.5` prevents false-positive overflows from 0.5px rounding quirks.
   - **Non-Swallowing 404 Probe**: Asserts `/__synthetic_test_route_404__` returns HTTP 404 without swallowing exceptions.

4. **Gate 4: Stage 10 Performance, Core Web Vitals & Lighthouse Gate (`lighthouse_gate.py` — MANDATORY GATE)**:
   ```bash
   python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/lighthouse_gate.py" <path_to_project_root> --build-prod
   ```
   Enforces:
   - **Fail-Closed by Default**: Server offline, missing `npx`, or failed audits exit non-zero (Code 1).
   - **Authentic Production Server Isolation (`--build-prod`)**: Runs `next build && next start -p 3001`, verifies server health, audits production bundle, and cleanly terminates the process.
   - **Full Route Coverage**: Audits all discovered routable templates; cleans Next.js route groups (`(marketing)` -> `/`).
   - **Modality-Specific CWV Budgets & WebGL Canvas Enforcement**:
     * *Modality C (Cinematic 3D / WebGL)*: LCP $\le 3800\text{ms}$, TBT $\le 350\text{ms}$ **ONLY IF** non-zero area WebGL `<canvas>` is verified; otherwise reverts to strict default budgets. Removes `--disable-gpu` to allow real hardware WebGL execution.
     * *Modality A/B/D*: LCP $\le 2500\text{ms}$, TBT $\le 200\text{ms}$.
     * *Non-waivable across ALL modalities*: CLS $\le 0.10$, TTFB $\le 600\text{ms}$, Google Green Accessibility $\ge 90$, SEO $\ge 90$.
   - **5-Run Median-Run Aggregation**: Statistically reduces CI and Windows throttling variance by >50%.

5. **Automated Layout Fidelity Scoring Gate (`layout_fidelity_score.py`)**:
   For reference-grounded builds (video or URL):
   ```bash
   python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/layout_fidelity_score.py" --ref <ref_wireframe> --target <target_wireframe>
   ```
   Requires structural fidelity score $F \ge 0.85$ before pre-delivery sign-off.

6. **Adversarial Mutation Suite Verification (`test_gate_mutations.py`)**:
   ```bash
   python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/test_gate_mutations.py"
   ```
   Requires 100% pass rate across 15 adversarial defect mutations before autonomous client deployment.



