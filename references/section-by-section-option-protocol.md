# Section-by-Section Option Protocol & Low-Cost Visual Preview Specification

This reference codifies the **Section-by-Section Option Protocol** for `website-architect`, synthesized from industry research across v0 (composite pipelines, AST autofixers), Bolt.new (in-browser WebContainer execution), Lovable.dev (persistent design knowledge systems), and Claude/Antigravity Agentic IDE architectures.

---

## 1. The Core Problem with Monolithic Single-Shot Generation

Single-shot, end-to-end page generation suffers from three compounding architectural failure modes:

1. **Hallucination Amplification**: Maintaining global consistency across 8+ sections simultaneously creates exponential context degradation. Small prompt drifts early in generation cascade into severe architectural errors downstream.
2. **Template Mode Collapse ("AI Slop Fingerprint")**: Without explicit, granular decision gates, autoregressive language models sample from the statistical center of their training distribution—yielding the familiar cliché: dark navy background, glowing purple radial blur blobs, centered hero, identical 3-card feature grid, Inter typography, and emoji UI icons.
3. **User Disempowerment & Approval Fatigue**: When a system dumps 1,500 lines of code in a single turn, the user cannot easily steer individual section aesthetics. The only remediation is full-page re-generation (expensive, non-deterministic) or manual coding.

---

## 2. The Section-by-Section State Machine

Page construction is modeled as a deterministic, event-sourced state machine where the durable unit of state is the **section**, not the entire page:

```text
PROJECT_INTAKE
  │
  ▼
REFERENCE_INGESTED (URL or Video DNA via extract_tokens.py / video_to_wireframe.py)
  │
  ▼
DESIGN_CONTRACT_LOCKED (DESIGN.md + design_tokens.json)
  │
  ▼
PAGE_BLUEPRINT_APPROVED (Ordered Section Anatomy & Narrative Jobs)
  │
  ▼
┌────────────────────────────────────────────────────────┐
│ SECTION-BY-SECTION ITERATION LOOP                      │
│                                                        │
│ 1. SECTION_BRIEF_READY                                 │
│ 2. OPTIONS_PLANNED (3 structurally divergent manifests)│
│ 3. PREVIEWS_RENDERED (Zero-credit SVG / micro-HTML)   │
│ 4. USER_SELECTION_PENDING (ask_question modal)         │
│ 5. OPTION_SELECTED (A / B / C / Hybrid / Revise)       │
│ 6. PRODUCTION_PATCHED (Scoped component code authored) │
│ 7. AST_AND_SLOP_AUDITED (anti_slop_gate.py)            │
│ 8. SECTION_COMMITTED & ADVANCED                        │
└────────────────────────┬───────────────────────────────┘
                         │ (All sections complete)
                         ▼
PAGE_INTEGRATION_AUDIT (verify_orchestration.py + chrome-devtools-mcp)
  │
  ▼
RELEASE_CANDIDATE_DELIVERED
```

---

## 3. The Divergence Contract ($\ge 3$ Axes of Variation)

Offering "3 options" where all three share the same layout geometry and differ only in background color or button radius is **prohibited**. Every candidate set must diverge across at least **3 independent structural axes**:

| Structural Axis | Dimension Choices |
| :--- | :--- |
| **1. Composition** | Asymmetric Split (60/40 or 5/7), Full-Bleed Stage, Bento Grid (8-col + 4-col), Numbered Index Strip, Editorial Stack, Tabular Matrix. |
| **2. Information Density** | Sparse (air, breathing room, whitespace), Balanced (editorial rhythm), Dense (specifications, metrics, technical telemetry). |
| **3. Media Behavior** | Framed Portrait (4:5), 100vw Ambient Web Loop, Contained Interface Window, 21:9 Horizon Bar, Interactive Canvas Preview. |
| **4. Reading Direction** | Lateral F-Pattern, Vertical Downward Narrative, Anchor-to-Actions, Matrix Scanning. |
| **5. Interaction Mode** | Dual CTAs + Floating Proof Chip, Sound/Video Toggle, Scroll-Scrubbed Stage, Tabbed Switcher, Reactive Client Slider. |
| **6. Typography Role** | Type-Led Display Serif, Media-Dominant, Data-Led Monospace Telemetry, Action-Oriented. |
| **7. Spatial Rhythm** | Uncompressed Breathing (`py-32`), Stepped Chapters, Gapless Grid, Compact Focus (`py-16`). |

*Automated Gate*: `section_option_previewer.py` calculates pairwise axis distance between candidate options and requires $\Delta \ge 3$ across all pairs.

---

## 4. Zero-Credit Low-Cost Visual Preview Ladder

To prevent burning expensive image generation credits during section deliberation, `website-architect` uses a tiered preview hierarchy:

### Tier 1: Programmatic SVG Wireframes (Primary Standard — Zero Credit)
- Executed via `scripts/section_option_previewer.py`.
- Generates 16:9 vectorized SVG diagrams illustrating exact element geometries, column ratios, media frames, button placements, and token colors.
- Renders directly in the browser or chat without network latency or external model API costs.

### Tier 2: Temporary HTML Micro-Component + Headless Playwright Screenshot (Secondary — Zero API Cost)
- For sections where typography rendering and micro-spacing must be seen in a real browser engine:
  - Generates minimal standalone HTML file with Tailwind CSS CDN and Google Fonts.
  - Takes a headless WebP snapshot at Desktop (1440×900) and Mobile (390×844) viewports.
  - Cost: 0 tokens, 0 credits (local compute only).

### Tier 3: Interactive Sandbox iframe (For Complex Interactive Calculators)
- Used when client-side reactivity (e.g. dynamic guest/rate calculation, date picker) is the primary decision factor.

---

## 5. Machine-Verifiable Tool Receipts (Eliminating Pretend Orchestration)

Agents must never output conversational claims like *"I have fetched the bento grid from Magic UI and installed brand logos"* without verifiable receipts. Every action requires a `ToolReceipt`:

```json
{
  "receiptId": "rcpt_7f8a9b2c",
  "runId": "run_website_build_01",
  "step": "9.4_component_sourcing",
  "tool": "resilient_sourcing.py",
  "args": {
    "command": "batch-logos",
    "brands": ["stripe", "google", "apple"]
  },
  "status": "ok",
  "artifactUris": [
    "public/assets/logos/stripe.svg",
    "public/assets/logos/google.svg",
    "public/assets/logos/apple.svg"
  ],
  "outputSha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "timestamp": "2026-09-27T22:45:00Z"
}
```

*Verification Enforcement*: The AST gate script `scripts/verify_orchestration.py` scans physical disk storage before pre-delivery sign-off. If a component or SVG is claimed in code but absent on disk, the build is immediately rejected.

---

## 6. Three-Tier Resilient Sourcing Hierarchy

When fetching external assets or components, network timeouts or upstream registry gaps must never break the build:

| Tier | Component Sourcing | Brand Vector Marks | Photography / Media |
| :--- | :--- | :--- | :--- |
| **Tier 1: Primary MCP** | `magicuidesign-mcp` / `21st-magic` | `21st-magic` `search_logo` | Local `assets/` harvested from Maps/Pinterest |
| **Tier 2: Direct HTTP/CDN** | Raw GitHub Registry CDN / shadcn CLI | Simple-Icons jsDelivr CDN / SVGL API | 8-Dimension De-AI synthesis via native `generate_image` |
| **Tier 3: Offline Bundled Cache** | Bundled MIT primitives in `resilient_sourcing.py` | Local pre-cached brand SVGs in `assets/logos/` | Deliberate neutral geometric frame with labeled metadata |

*Hard Rule*: Never replace a missing logo with an emoji, and never use text-only placards for authentic partner showcases.
