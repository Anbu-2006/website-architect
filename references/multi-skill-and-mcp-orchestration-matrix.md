# Multi-Skill & MCP Orchestration Matrix: Cognitive Architecture Guide

> **Authoritative Technical Specification for `/website-architect`**  
> Synthesized from Deep Research on Specialized Frontend Skills, Model Context Protocol (MCP) Capabilities, and Vercel Web Interface Guidelines.

---

## 1. Core Operating Philosophy: Intelligence Over Tool-Stuffing

A common failure mode in AI engineering is "tool stuffing" — indiscriminately throwing a dozen tools and skills into a prompt without clear boundaries or reasoning. This leads to instruction dilution, conflicting patterns, and erratic code.

`/website-architect` operates as a **Senior Solutions Architect and General Contractor**. It treats skills and MCP servers as **specialized subcontractors**, engaging each one strictly:
1. **At the right lifecycle phase** (Planning $\to$ Visual Direction $\to$ Component Sourcing $\to$ AST Gates $\to$ Dual-Browser Verification).
2. **With clear cognitive criteria** (Why this tool? What decision does it inform? What is the expected output?).
3. **With deterministic fallbacks** (If an MCP times out or is offline, seamless fallback to local scripts and CDNs ensures zero broken builds).

```
┌────────────────────────────────────────────────────────────────────────────────────────────────┐
│                         COGNITIVE DECISION & ORCHESTRATION PIPELINE                            │
├────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                │
│   PHASE A: COGNITIVE PLANNING & TOPOLOGY                                                       │
│   └── sequential-thinking (MCP) ➔ Hypothesize ADS score, route tree, and layout hierarchy      │
│                                                                                                │
│   PHASE B: VISUAL ART DIRECTION & DESIGN SYSTEM                                                │
│   ├── ui-ux-pro-max (Skill)     ➔ Calibrated product palettes, WCAG AA contrast (>= 4.5:1)    │
│   ├── Archetype Style Skill     ➔ soft-skill / minimalist-skill / brutalist-skill / gpt-taste  │
│   ├── design-system (Skill)     ➔ 3-layer CSS custom properties (:root primitive ➔ semantic)  │
│   └── shadcn-ui (MCP)           ➔ list_themes / get_theme for theme presets                   │
│                                                                                                │
│   PHASE C: COMPONENT & ASSET SOURCING (The 4-Tier Sourcing Protocol)                           │
│   ├── Tier 1: Functional Controls & Forms ➔ shadcn-ui (MCP: get_component, get_block)          │
│   ├── Tier 2: Animated Showcases & Bento  ➔ magicuidesign-mcp (getRegistryItem)                │
│   ├── Tier 3: Production Vector Icons     ➔ lucide-icons (MCP: search_icons)                   │
│   ├── Tier 4: Brand Logos & Technology    ➔ 21st-magic (search_logo) + resilient_sourcing.py   │
│   └── Photography & Visual Media          ➔ Native generate_image (FREE) / harvest_assets.py   │
│                                                                                                │
│   PHASE D: PRE-DELIVERY AST QUALITY GATES (Deterministic Python Scripts)                       │
│   ├── check_no_anchor_illusion.py ➔ Validates >= 3 Next.js App Router subpages (zero # jumps)  │
│   ├── anti_slop_gate.py           ➔ Enforces zero raw hex, zero emojis, zero uniform 3-cards   │
│   └── verify_orchestration.py     ➔ Asserts physical existence of imported components & SVGs   │
│                                                                                                │
│   PHASE E: DUAL-BROWSER RUNTIME VALIDATION                                                     │
│   ├── playwright-mcp (MCP)        ➔ High-level accessibility tree navigation & form validation │
│   └── chrome-devtools-mcp (MCP)   ➔ Low-level CDP inspection (0 console errors, CLS < 0.05)    │
│                                                                                                │
└────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Phase-by-Phase Cognitive Decision Tree

When building or architecting a website, follow this step-by-step decision tree. Never invoke tools outside their dedicated phase.

### Phase A: Architecture, Scoping & Topology (Thinking First)
- **Goal**: Deconstruct user prompt or URL, formulate hypotheses, calculate the Architecture Decision Score (ADS), and design the route manifest before touching JSX or CSS.
- **Primary Tool**: `sequential-thinking` (`sequentialthinking` MCP).
- **When & Why to Use**:
  - Complex architectural choices require course correction and branching. Use `sequentialthinking` to debate:
    1. Is this a Single-Page (SPA) or Multi-Page Architecture (MPA)? (Calculate $\text{ADS} = \text{Catalog Depth} + \text{Search Specificity} + \text{Journey Deliberation} - \text{Immediacy Need}$).
    2. What are the $\ge 3$ distinct Next.js App Router routes needed to eliminate anchor-hash illusions?
    3. What is the scarce operational resource of this business?
- **Invocation Contract**:
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

---

### Phase B: Visual Art Direction & Design Tokens
- **Goal**: Establish a distinct visual thesis, eliminate generic AI defaults (no dark navy `#0B0F19` with purple glowing blobs), and build a production design token architecture.
- **Specialist Routing Rules**:
  - **Color & Typography Intelligence**: Run `ui-ux-pro-max`:
    ```bash
    python "C:/Users/anbua/.gemini/config/skills/ui-ux-pro-max/scripts/search.py" "<archetype> <stack>" --design-system
    ```
    Retrieves WCAG AA contrast-checked hex tokens and font pairings.
  - **Archetype-Specific Aesthetic Direction**:
    | Business Profile | Specialist Skill to Read | Signature Architectural Patterns |
    | :--- | :--- | :--- |
    | **Luxury, Hospitality, High-End Agency** | `soft-skill` | Doppelrand nested bezels (`p-2 rounded-[2rem]` wrapping `rounded-[calc(2rem-0.5rem)]`), button-in-button CTAs, `cubic-bezier(0.32, 0.72, 0, 1)` spring curves, macro-whitespace (`py-24` to `py-40`). |
    | **Developer Tools, Clean SaaS, Documentation** | `minimalist-skill` | Warm bone canvas (`#F7F6F3`), desaturated spot pastels, ultra-flat 1px borders, zero heavy shadows, `<kbd>` keystrokes, macOS window chrome. |
    | **Industrial, CNC, Defense, Tactical Telemetry** | `brutalist-skill` | Rigid 0px geometry, documentation paper `#F4F4F0` or CRT black `#0A0A0A`, monolithic uppercase clamp headers, ASCII telemetry (`[ STATUS: ACTIVE ]`, crosshairs `+`). |
    | **High-Motion Showcases, Studios, Bento Portfolios** | `gpt-tasteskill` | 2-line hero rule (H1 never wraps > 2 lines), gapless bento grid with `grid-flow-dense`, GSAP ScrollTrigger pinning and scrubbed text reveals. |
    | **Existing Codebase Modernization** | `redesign-skill` | 6-dimension non-breaking audit, surgical style upgrades preserving business logic. |
  - **Token Integration**: Run `design-system` scripts or ingest via `extract_tokens.py` to establish 3-layer CSS custom properties in `src/app/globals.css`.
  - **Theme Presets (MCP)**:
    ```python
    call_mcp_tool(ServerName="shadcn-ui", ToolName="get_theme", Arguments={"themeName": "zinc"})
    ```

---

### Phase C: Component & Asset Sourcing (Intentional Archetype Sourcing)
- **Goal**: Author high-craft Next.js components using authentic, accessible primitives while maintaining a strict **100% free / zero-credit cost** default boundary.
- **The Golden Rule of MCP Selection**:
  > **STRICTLY BAN RANDOM RETRIEVALS**. Never query an MCP server for arbitrary components. Every MCP call must be grounded in the business archetype, the section's functional intent, and the design thesis.

- **Intentional Archetype-to-MCP Selection Matrix**:
  | Business Archetype | `magicuidesign-mcp` Primitives | `shadcn-ui` Primitives | `lucide-icons` Semantic Clusters |
  | :--- | :--- | :--- | :--- |
  | **Luxury Hospitality, Farmstays, Resorts** | `blur-fade`, `carousel`, `text-reveal`, `shimmer-button` | `accordion` (policies), `tabs` (cottage tiers), `dialog` (stay calculator modal) | `Sparkles`, `Trees`, `Utensils`, `Waves`, `MapPin`, `Compass`, `Bed`, `Users` |
  | **B2B SaaS, Developer Tools, AI Platforms** | `bento-grid`, `border-beam`, `marquee`, `terminal`, `dock` | `sheet` (slide-out docs), `table` (telemetry/pricing), `command` (quick search) | `Terminal`, `Cpu`, `ShieldCheck`, `Layers`, `Zap`, `GitBranch`, `Activity` |
  | **High-Volume E-Commerce & Retail** | `marquee` (brand social proof), `blur-fade` (catalog reveal) | `dialog` (quick buy), `sheet` (slide-out cart), `slider` (price filter) | `ShoppingBag`, `Filter`, `Star`, `Truck`, `ShieldCheck`, `CreditCard` |
  | **High-Trust Advisory, Law, Finance** | `blur-fade`, `number-ticker` (verified metrics) | `tabs` (practice areas), `accordion` (legal FAQs), `dialog` (consultation) | `Scale`, `Building`, `Award`, `FileText`, `PhoneCall`, `Lock` |
  | **Healthcare, Clinics, Wellness** | `blur-fade`, `animated-shiny-text` | `calendar` (appointment picker), `tabs` (specialties), `dialog` (portal) | `Heart`, `Activity`, `Calendar`, `Clock`, `Stethoscope`, `UserCheck` |

- **Visual Media & Video Generation Protocols**:
  1. **User Asset Intake & Inspection (`curate_user_assets.py`)**:
     - Run `curate_user_assets.py --mode {hybrid|user_only|maps_only}`.
     - Pillow analyzes dimensions and classifies assets into `hero_wide`, `suite_gallery`, `culinary_gastronomy`.
     - ffmpeg extracts `*_first_frame.jpg`, `*_mid_frame.jpg`, and `*_last_frame.jpg`.
  2. **Frame-Directed Video Creation & Enhancement**:
     - When external video generation is requested, use Higgsfield MCP:
       ```python
       call_mcp_tool(
         ServerName="higgsfield",
         ToolName="generate_video",
         Arguments={
           "prompt": "Slow cinematic drone orbit over property, lush trees and morning mist, 4k ultra-detailed, ambient loop",
           "medias": [{"role": "image", "url": "/assets/hero_first_frame.jpg"}],
           "aspect_ratio": "16:9",
           "duration": 5
         }
       )
       ```
     - *Zero-Credit Fallback (Free, Instant, 0-Latency)*:
       - YouTube B-Roll extraction via `yt-dlp`.
       - High-res still with 60fps GPU Ken-Burns pan (`animate-ken-burns`) with zero layout shift.

---

### Phase D: Automated AST Quality Gates (Pre-Delivery Verification)
Before launching a browser or presenting code to the user, run these automated verification gates:

1. **Anti-Anchor Illusion AST Gate (`check_no_anchor_illusion.py`)**:
   ```bash
   python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/check_no_anchor_illusion.py" <path_to_app_dir>
   ```
   *Pass Criteria*: All MPA builds have $\ge 3$ distinct Next.js App Router subpages (`page.tsx`) and primary navigation uses `<Link href="/route">`. Zero `#` single-page hash jumps.

2. **Automated Anti-Slop AST Gate (`anti_slop_gate.py`)**:
   ```bash
   python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/anti_slop_gate.py" <path_to_project_root>
   ```
   *Pass Criteria (10 Comprehensive Checks)*:
   - Check 1: Zero structural emojis in UI (must use Lucide vector SVGs).
   - Check 2: Zero text-only partner placards (must use real brand SVGs from 21st-magic/SVGL).
   - Check 3: Zero generic decorative blur blobs (`blur-3xl rounded-full`).
   - Check 4: Zero uniform card syndromes (monoculture ratio $\le 0.40$).
   - Check 5: Zero aggressive hero booking widgets in luxury benchmarks (keep hero cinematic).
   - Check 6: Zero generic SaaS 4-stat metric strips in hospitality heroes.
   - Check 7: Hero section must feature authentic motion (`<video>`, `animate-ken-burns`, or `motion.div`).
   - Check 8: 60fps GPU Compositor Rule (bans transitions on `width`, `height`, `top`, `left`, `margin`, `padding`, and structural `transition: all`).
   - Check 9: **Multi-Page Route Depth Check (`STUB_PAGE_SLOP`)**: Every route (`page.tsx`) must import and render **$\ge 4$ distinct, purposeful section components**. Zero 1-section skeleton stubs!
   - Check 10: **Generic Button Ban (`GENERIC_BUTTON_SLOP`)**: Zero dummy button text ("Click Here", "Button", "Read More" without href); zero empty `onClick={() => {}}` handlers.

3. **Orchestration Verification Gate (`verify_orchestration.py`)**:
   ```bash
   python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/verify_orchestration.py" <path_to_project_root>
   ```
   *Pass Criteria*: All claimed components, vector SVGs in `public/assets/logos/`, and package dependencies exist physically on disk. Eliminates hallucinated tool claims.

---

### Phase E: Dual-Browser Runtime Validation
Once dev server is running (`npm run dev`), validate the application using the dual-browser strategy:

```
Dual-Browser Validation Flow:
┌────────────────────────────────────────────────────────────────────────┐
│ 1. High-Level User Journey Test (playwright-mcp)                       │
│    • Navigate across all routes (/about, /services, /contact)          │
│    • Click interactive buttons, toggle mobile drawer, fill forms      │
│    • Verify accessibility tree elements and keyboard operability       │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 2. Low-Level Performance & Console Audit (chrome-devtools-mcp)         │
│    • Inspect console messages: MUST HAVE 0 ERRORS                      │
│    • Verify Cumulative Layout Shift: CLS < 0.05                        │
│    • Check WCAG AA contrast ratio: >= 4.5:1 on all text                │
│    • Capture final high-resolution visual screenshot                   │
└────────────────────────────────────────────────────────────────────────┘
```

1. **`playwright-mcp` (High-Level Interaction Testing)**:
   ```python
   # Navigate to local server
   call_mcp_tool(
     ServerName="playwright-mcp",
     ToolName="browser_navigate",
     Arguments={"url": "http://localhost:3000"}
   )
   # Click navigation link to verify real multi-page routing
   call_mcp_tool(
     ServerName="playwright-mcp",
     ToolName="browser_click",
     Arguments={"selector": "nav a[href='/cottages']"}
   )
   # Test form input interaction
   call_mcp_tool(
     ServerName="playwright-mcp",
     ToolName="browser_fill_form",
     Arguments={"selector": "input[name='guests']", "value": "4"}
   )
   ```

2. **`chrome-devtools-mcp` (Low-Level CDP Telemetry & Verification)**:
   ```python
   # Step 1: List active pages to get pageId
   call_mcp_tool(ServerName="chrome-devtools-mcp", ToolName="list_pages", Arguments={})

   # Step 2: Navigate to target URL
   call_mcp_tool(ServerName="chrome-devtools-mcp", ToolName="navigate_page", Arguments={"pageId": 1, "url": "http://localhost:3000"})

   # Step 3: Assert ZERO runtime console errors
   call_mcp_tool(ServerName="chrome-devtools-mcp", ToolName="list_console_messages", Arguments={"pageId": 1})

   # Step 4: Capture visual verification screenshot
   call_mcp_tool(ServerName="chrome-devtools-mcp", ToolName="take_screenshot", Arguments={"pageId": 1, "format": "png"})
   ```

---

## 3. Verified MCP Server Fleet Summary

| MCP Server | Package / Command | Cost / Auth | Core Function in Web Architecture |
| :--- | :--- | :--- | :--- |
| **`sequential-thinking`** | `npx -y @modelcontextprotocol/server-sequential-thinking@latest` | **100% Free** (No API Key) | Multi-step reasoning, hypothesis testing, route topology planning, ADS calculation. |
| **`shadcn-ui`** | `npx -y @jpisnice/shadcn-ui-mcp-server@latest` | **100% Free** (No API Key) | Authoritative source code for accessible Radix UI primitives, blocks, forms, and themes. |
| **`magicuidesign-mcp`** | `npx -y @magicuidesign/mcp@latest` | **100% Free** (No API Key) | Animated visual components: Bento grids, Marquees, Shimmer buttons, Border beams. |
| **`lucide-icons`** | `npx -y lucide-icons-mcp@latest --stdio` | **100% Free** (No API Key) | Searchable catalog of 1,500+ Lucide vector icons. Eliminates emojis as structural UI icons. |
| **`21st-magic`** | `npx -y @21st-dev/magic@latest API_KEY=...` | **Free Tier** + Fallback | Community blocks and brand logos. Supported by offline zero-cost `resilient_sourcing.py`. |
| **`playwright-mcp`** | `npx -y @playwright/mcp@latest` | **100% Free** (No API Key) | High-level accessibility tree navigation, multi-page link clicking, form filling, user journey tests. |
| **`chrome-devtools-mcp`** | `npx -y chrome-devtools-mcp@latest ...` | **100% Free** (No API Key) | Low-level CDP inspection, runtime console error audit (0 errors required), layout shift checks. |

---

## 4. Anti-Patterns & Banned Behaviors

1. **NO Tool Stuffing**: Do not call `shadcn-ui`, `magicuidesign-mcp`, and `21st-magic` all for the same component. Use `shadcn-ui` for base functional primitives, `magicuidesign-mcp` for animated visual anchors, and `lucide-icons` for icons.
2. **NO Hallucinated Orchestration**: Never write in chat "I fetched the component from Magic UI" if you didn't run the tool call or script. `verify_orchestration.py` strictly checks this.
3. **NO Emojis as UI Icons**: Structural icons must always be SVGs from `lucide-icons` or `assets/`.
4. **NO Hash-Jump Navigation**: Primary navigation must use real Next.js `<Link>` to separate route pages (`/services`, `/pricing`). Single-page anchor jumps (`#services`) fail the `check_no_anchor_illusion.py` gate.
5. **NO Paid Credits for Video or Images**: Strictly ban consuming paid external credits (e.g. Higgsfield API) in free mode. Use the 4-Tier Free Ambient Video Engine (Direct benchmark MP4 stream extraction via Playwright, Public HD royalty-free loops via Pexels/Pixabay, Free native `generate_image` + GPU-accelerated CSS Ken-Burns cinematic motion, or WebGL/Three.js shaders) and Antigravity native `generate_image` at 100% zero cost.
6. **NO Manual Agent Assignment**: The multi-agent subnetwork runs autonomously via the lead AI model or the single master command `python scripts/orchestrate.py`. Never burden the user with assigning or coordinating subagents.
