# Reference-Grounded Web Replication & Domain Transposition Engine
### The Authoritative Technical Architecture for 1:1 Structural Fidelity, True Multi-Page Routing, and Anti-Slop Execution

---

## 1. The Core Problem: Why AI Agents Produce "AI Slop" Instead of Replicas

When an AI coding assistant is asked to replicate an award-winning reference website (or a screen recording of one, such as Loyola University Maryland), the agent almost universally fails in two distinct ways:

1. **Routing Collapse (The Single-Page Hash Illusion)**:
   - The reference site is an expansive, authoritative Multi-Page Architecture (MPA) with distinct routes (`/`, `/visit/`, `/programs/`, `/admissions/`, `/placements/`).
   - The AI agent condenses the entire institutional scope into a single `page.tsx` file and wires the primary navigation to anchor jumps (`href="#schools"`, `href="#programs"`, `href="#placements"`).
   - **Root Cause**: Autoregressive models optimize for local coherence in a single context window. Writing one large file is the path of least resistance unless a rigid pre-generation route manifest contract is enforced.

2. **Pattern Collapse & Monoculture (The Statistical Median Trap)**:
   - The reference site features rich spatial variety: full-bleed ambient video heroes, organic arched (ogee-curved) photo masks, high-contrast serif display headlines, asymmetric 60/40 editorial splits, and generous whitespace.
   - The AI agent flattens the entire visual vocabulary into a **single repeating unit**: uniform 3-column card grids with rounded icon-in-chip badges, centered sans-serif headlines, and green/slate recoloring.
   - **Root Cause**: The 2019–2024 web training corpus is dominated by SaaS starter kits and component libraries. Prompting with subjective adjectives like "modern" or "clean" triggers high-probability retrieval tokens that pull generation directly toward this statistical median.

---

## 2. The 6-Vector Reference Replication Architecture

To achieve genuine 1:1 structural fidelity without falling into the median trap, `website-architect` enforces the 6 engineering vectors:

```
┌────────────────────────────────────────────────────────────────────────┐
│ VECTOR 1: Video-to-Code & Screen-Recording Decomposition              │
│ Optical flow scroll tracking ──▶ Keyframe extraction ──▶ Wireframe IR  │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ VECTOR 2: Headless Scraping & Visual DNA Ingestion via MCP             │
│ Playwright getComputedStyle() ──▶ clipPath, fonts, grid, spacing tokens│
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ VECTOR 3: True Multi-Page Architecture Generation Engine               │
│ route_manifest.json ──▶ Next.js App Router ──▶ check_no_anchor AST gate│
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ VECTOR 4: Reference-to-Target Domain Transposition Engine              │
│ Preserved 1:1 (Structure, Grids, Masks) ⊗ Fresh Target Copy & Media    │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ VECTOR 5: Anti-Median Negative Guardrails & Monoculture Gates          │
│ Monoculture Ratio <= 0.40 ──▶ Layout Fidelity F >= 0.85 ──▶ Hard Bans   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ VECTOR 6: Concrete Multi-Skill & MCP Orchestration Pipeline            │
│ ui-ux-pro-max + design-system + taste-skill + ui-styling + impeccable   │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Vector 1: Video-to-Code Decomposition Pipeline

When the user supplies an MP4/WebM screen recording (e.g. desktop walkthrough of a benchmark site):

1. **Shot/Scroll Segmentation**:
   - **Route Transition Detector**: Diff consecutive frames at 1 fps. If pixel difference exceeds 85% within 2 frames, classify as a page navigation event (corroborate with OCR on URL bar).
   - **Optical Flow Scroll Tracker**: Use Farneback dense optical flow or cross-correlation on horizontal strips to calculate cumulative vertical scroll displacement:
     $$v_{\text{cum}} = \sum_{t} \Delta y_t$$
     This reconstructs virtual document height even though the video only shows a single viewport window.
2. **Keyframe Extraction**:
   - Sample keyframes at every viewport-height boundary crossing ($y \equiv 0 \pmod{H_{\text{viewport}}}$) and during user dwell pauses (velocity $\approx 0$ for $\ge 500\text{ms}$).
3. **Per-Frame Semantic Labeling**:
   - Extract semantic section types (`full_bleed_hero_video`, `organic_mask_gallery`, `asymmetric_split`, `stat_strip`, `card_grid`, `testimonial`, `footer`).
   - Identify image treatment: `arched_mask` (ogee / semicircular clip path), `rectangular`, `circular`.
   - Identify typography: `serif_display` vs `sans_display`.
4. **Assembly into `wireframe_ir.json`**:
   - Export an ordered layout AST per route representing the exact physical geometry and component sequence.

---

## 4. Vector 2: Headless Visual DNA Extraction (`scripts/extract_tokens.py`)

When the user supplies a live reference URL:

1. **DOM Geometry & Computed Style Harvest**:
   - Execute in headless browser (Playwright or `chrome-devtools-mcp`):
     ```javascript
     const computed = window.getComputedStyle(element);
     const rect = element.getBoundingClientRect();
     ```
2. **Token Ingestion Targets**:
   - `typography`: `fontFamily`, `fontSize`, `fontWeight`, `lineHeight`, `letterSpacing` for both display headers and body copy.
   - `surfaces`: Canvas background, ink color, primary CTA fill, border contrast.
   - `masks & shapes`: Exact `clipPath` (`clip-path: path(...)` or `clip-path: polygon(...)`), border-radii, layered shadows.
   - `layout`: `display`, `gridTemplateColumns`, `flexDirection`, `gap`, section vertical padding rhythm (`paddingTop`, `paddingBottom`).
3. **Storage**: Output directly to `design_tokens.json` and `DESIGN.md`.

---

## 5. Vector 3: Multi-Page App Router Architecture & AST Gates

### The Multi-Page Manifest Contract
Before any component code is written, the agent MUST write `route_manifest.json`:
```json
{
  "framework": "next-app-router",
  "min_routes_required": 4,
  "routes": [
    { "path": "/", "file": "src/app/page.tsx", "nav_label": "Home" },
    { "path": "/programs", "file": "src/app/programs/page.tsx", "nav_label": "Academic Programs" },
    { "path": "/admissions", "file": "src/app/admissions/page.tsx", "nav_label": "Admissions & Aid" },
    { "path": "/visit", "file": "src/app/visit/page.tsx", "nav_label": "Visit Campus" },
    { "path": "/placements", "file": "src/app/placements/page.tsx", "nav_label": "Placements & Careers" }
  ],
  "shared_components": ["Navigation", "LocationAndFooter", "AdmissionsModal"]
}
```

### The Anti-Anchor-Illusion Gate (`scripts/check_no_anchor_illusion.py`)
Run before and after generation:
```bash
python skills/website-architect/scripts/check_no_anchor_illusion.py <path_to_src_app>
```
**Strict AST Enforcement Rules**:
1. Number of distinct route files (`page.tsx`) MUST be $\ge \text{min\_routes\_required}$ (minimum 3–5).
2. Primary navigation MUST use Next.js `<Link href="/route">` or `<a>`.
3. **Zero Hash Jumps**: If a nav item points to `#something` (e.g. `href="#programs"`), the AST validator immediately fails the build.

---

## 6. Vector 4: Reference-to-Target Domain Transposition

To preserve structural craftsmanship without infringing copyright or confusing client identity, strictly decouple **Structural DNA** from **Target Business Content**:

| Structural DNA (Preserved 1:1 from Reference) | Target Content Entity (Sourced Fresh for Target) |
| :--- | :--- |
| Section sequence & physical viewport height | Client's authentic value proposition |
| Asymmetric layout ratios (e.g. 60/40 splits) | Target business's real product/service offerings |
| Image treatment (e.g. arched clip-path masks) | Target business's authentic photography |
| Typography pairing (Display Serif + Clean Sans) | Target business's verified factual copy |
| Spacing rhythm & container max-width | Target brand color palette & vector logos |
| Full-bleed ambient video hero loop behavior | Target's own licensed/shot drone footage |

### Intermediate Representation Node Schema
```json
{
  "section_id": "home.arched_showcase",
  "structural_dna": {
    "section_type": "organic_mask_gallery",
    "columns": 4,
    "image_treatment": {
      "mask": "arched",
      "clip_path": "rounded-t-[100px] sm:rounded-t-[130px] rounded-b-2xl",
      "aspect_ratio": "3/4"
    },
    "typography": "serif_display",
    "pacing_padding": "py-20 md:py-28"
  },
  "target_content": {
    "headline": "A Living Campus Designed For Discovery & Leadership",
    "items": [
      { "title": "Neoclassical Central Portico", "image": "/assets/campus_central_quad.jpg" },
      { "title": "Applied Technology & Research Labs", "image": "/assets/hero_campus_engineering.jpg" },
      { "title": "Dr. Chandramma Medical Institute", "image": "/assets/medical_hospital_cdsimer.jpg" },
      { "title": "Vibrant Residential Quad Life", "image": "/assets/hostel_residence_towers.jpg" }
    ]
  }
}
```

---

## 7. Vector 5: Anti-Median Negative Guardrails & Monoculture Penalties

### The Monoculture Ratio Formula
To eliminate pattern collapse (where the AI makes every section look like a card grid):
$$\text{Monoculture Ratio} = \frac{\text{Count of most common section layout signature}}{\text{Total sections in page}} \le 0.40$$

If $>40\%$ of sections on any route share the same layout signature, the code is rejected.

### The 7 Greppable Negative Guardrails (Mechanical Bans)
1. `[BAN]` **Uniform 3-Column Card Grids**: Prohibited unless the reference explicitly uses that exact component.
2. `[BAN]` **Defaulting to Inter/System Sans**: Prohibited when the reference or archetype specifies display serif (Playfair, Cormorant, Garamond) or geometric display.
3. `[BAN]` **Replacing Arched / Bespoke Masks with Rectangles**: If the reference uses arched photo masks, the code MUST implement the curved mask via `clip-path` or SVG mask.
4. `[BAN]` **Glowing Purple/Indigo Gradient Blobs**: Strictly forbidden on dark backgrounds.
5. `[BAN]` **Primary Navigation Hash Jumps (`href="#..."`)**: Strictly forbidden in MPA projects.
6. `[BAN]` **Emojis as Structural UI Icons**: Strictly forbidden. Use Lucide, Heroicons, or SVGL vector marks.
7. `[BAN]` **Hollow Marketing Fluff**: All copy must contain concrete domain nouns, actual specifications, and transparent figures.

---

## 8. Vector 6: Multi-Skill & MCP Concrete Execution Protocol

The agent MUST actively execute specialized skills and MCP tools in this exact ordered sequence:

1. **Design System & Intelligence (`ui-ux-pro-max`)**:
   - `view_file(AbsolutePath="C:/Users/anbua/.gemini/config/skills/ui-ux-pro-max/SKILL.md")`
   - Run design search: `python "C:/Users/anbua/.gemini/config/skills/ui-ux-pro-max/scripts/search.py" "<archetype>" --design-system`
2. **Three-Layer Token Generation (`design-system`)**:
   - `view_file(AbsolutePath="C:/Users/anbua/.gemini/config/skills/design-system/SKILL.md")`
   - Create `:root` CSS custom properties (surfaces, ink, borders, shadows, spacing scale).
3. **Editorial Layout Geometry (`taste-skill` or `soft-skill`)**:
   - `view_file(AbsolutePath="C:/Users/anbua/.gemini/config/skills/taste-skill/SKILL.md")`
   - Enforce asymmetric 60/40 splits, typographic index strips, and generous section pacing.
4. **Animated Components via MCP (`magicuidesign-mcp` & `21st-magic`)**:
   - Call `call_mcp_tool(ServerName="magicuidesign-mcp", ToolName="getRegistryItem", Arguments={"name": "bento-grid", "includeSource": true})`
5. **Component Primitives & Accessibility (`ui-styling`)**:
   - `view_file(AbsolutePath="C:/Users/anbua/.gemini/config/skills/ui-styling/SKILL.md")`
6. **Pre-Delivery Craft Audit (`impeccable` & `a11y-debugging`)**:
   - `view_file(AbsolutePath="C:/Users/anbua/.gemini/config/skills/impeccable/SKILL.md")`
   - Verify touch targets $\ge 44\text{px}$, WCAG AA contrast $\ge 4.5:1$, and reduced motion.
7. **Automated Verification Gates**:
   - Run `check_no_anchor_illusion.py`
   - Run `layout_fidelity_score.py`
8. **Dev Server Runtime Validation (`chrome-devtools-mcp`)**:
   - `navigate_page(url="http://localhost:3000")`
   - `list_console_messages()` -> assert 0 errors
   - `take_screenshot()` -> visual sign-off
