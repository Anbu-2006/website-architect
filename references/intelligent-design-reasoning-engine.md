# Intelligent Design Reasoning Engine & Cognitive Architecture Protocol

> **Core Cognitive Brain for `/website-architect`**  
> Synthesized from User Directive: "The AI has to think in an intelligent way, not random... which style is best, which color grading, which text, whether to use simple photos, interactive elements, or 3D canvas, and recommend 3 grounded benchmark examples to compile the site."

---

## 1. The 6-Dimension Architectural Thinking Framework

When given any business concept, URL, or Google Maps profile, the AI agent **must not** emit generic boilerplate or make arbitrary visual choices. The AI must activate its **Architectural Thinking Brain** across 6 explicit dimensions:

```
┌────────────────────────────────────────────────────────────────────────┐
│               THE 6-DIMENSION ARCHITECTURAL THINKING BRAIN             │
├────────────────────────────────────────────────────────────────────────┤
│ 1. VISUAL STYLE & THESIS       │ Editorial / Swiss / Brutalist / Luxe │
├────────────────────────────────┼──────────────────────────────────────┤
│ 2. SPATIAL GEOMETRY & LAYOUT   │ 60/40 Split / Bento / Index / Canvas │
├────────────────────────────────┼──────────────────────────────────────┤
│ 3. COLOR GRADING & PSYCHOLOGY  │ Warm Stone / Espresso / Amber / Deep │
├────────────────────────────────┼──────────────────────────────────────┤
│ 4. TYPOGRAPHY PAIRING & SCALE  │ Display Serif + Clean Grotesque      │
├────────────────────────────────┼──────────────────────────────────────┤
│ 5. MEDIA & IMMERSION STRATEGY  │ 35mm Photo vs. Interactive vs. 3D    │
├────────────────────────────────┼──────────────────────────────────────┤
│ 6. CONVERSION & FRICTION FLOW  │ Sticky Hotbar / Calculator / Drawer  │
└────────────────────────────────┴──────────────────────────────────────┘
```

---

### Dimension 1: Visual Style & Aesthetic Direction
The AI evaluates customer psychology and market positioning to select the single best aesthetic direction:

| Archetype / Domain | Recommended Style Direction | Rationale | Banned Defaults |
|---|---|---|---|
| **Luxury Farmstay / Boutique Hotel** | **Warm Architectural Editorial** | Evokes heritage, tranquility, and organic terroir through large whitespace (112px–140px) and asymmetric full-bleed visuals. | Dark slate-900, purple gradients, generic SaaS kits. |
| **Highway Dining / Express Food** | **High-Contrast Express Utility** | Customer arrives hungry or traveling; needs sub-1s load time, bold item pricing, and instant click-to-order WhatsApp. | Heavy 3D canvas, tiny unreadable serif text, un-priced menus. |
| **B2B SaaS / Developer Tool** | **Minimalist High-Density Monolith** | Users value operational clarity, keyboard shortcuts, code tabs, and interactive ROI calculators. | Cliché cream palettes, faux-literary prose, generic 3-card kits. |
| **Artisanal D2C E-Commerce** | **Tactile Editorial Craft** | Sensory product focus with compounding typography, ingredient callouts, and slide-out cart drawers. | Wholesale discount banners, cluttered popups, ungrounded cards. |
| **High-Trust Advisory / Law Firm** | **Restrained Corporate Prestige** | Projects authority and discretion through disciplined Swiss grids, verified case studies, and zero fluff. | Flashy particle animations, cartoon icons, consumer chat popups. |
| **Medical / Aesthetics Clinic** | **Empathetic Clinical Warmth** | Combines clinical sterility with human warmth (terracotta/sage), HIPAA-safe booking, and doctor credentials. | High-pressure urgency timers, unverified health claims. |

---

### Dimension 2: Spatial Geometry & Layout Variance
The AI decides how content breathes and flows:
* **The Asymmetric 60/40 Hero**: Replaces the centered AI cliché with an anchor headline/CTA on the left (60%) and an authentic architectural visual on the right (40%).
* **Staggered Bento Grids**: Instead of 3 equal-sized cards, the AI uses an asymmetric layout with one dominant anchor card (spanning 2 columns) and two supporting micro-cards.
* **Numbered Index Strips**: For services, amenities, or process steps, uses clean typographic index rows (`01`, `02`, `03`) with subtle hairline dividers instead of cards-inside-cards.
* **Breathing Room Scale**: Sections breathe with `96px–140px` vertical padding on desktop, collapsing to `64px` on mobile.

---

### Dimension 3: Color Grading & Palette Psychology
The AI selects a cohesive, domain-calibrated color palette:
* **Warm Terracotta & Stone (Hospitality / Culinary)**: Canvas `#FAF8F5`, Surface `#F0EDE8`, Primary Ink `#1C1917`, Accent `#8B6F4E` (aged brass) or `#B8422E` (terracotta).
* **Deep Obsidian & Amber (Creative / DevTool / Dark Tech)**: Canvas `#090A0F`, Surface `#12151E`, Ink `#EDEDED`, Accent `#F59E0B` (technical amber).
* **Alpine Crisp & Slate (Healthcare / Enterprise)**: Canvas `#FFFFFF`, Surface `#F8FAFC`, Ink `#0F172A`, Accent `#0284C7` (deep sky).
* **Strict Rule**: Strictly **ZERO default indigo/violet gradients** (`#8b5cf6`, `#7c3aed`), and **ZERO raw hex codes in components** (all styling consumes `:root` tokens).

---

### Dimension 4: Typography Pairing & Text Hierarchy
The AI formulates a bespoke typographic hierarchy:
* **Primary Headline Display**: High-character serif or geometric display font (e.g. `Cormorant Garamond`, `Playfair Display`, `Syne`, or `Cabinet Grotesk`). Display headers $\ge 40\text{px}$ always receive **negative optical tracking** (`letter-spacing: -0.02em` to `-0.035em`).
* **Clean Grotesque Body**: Highly legible body font (e.g. `Plus Jakarta Sans`, `Satoshi`, `Inter` *only when paired with a serif display*, or `Geist`). Body copy has a relaxed line-height of `1.6–1.7`.
* **Tabular Numbers**: Any numeric metric, pricing tier, or counter uses `font-variant-numeric: tabular-nums`.

---

### Dimension 5: Media & Immersion Strategy (Photo vs. Interactive vs. 3D Canvas)
The AI explicitly evaluates which media layer best serves the user experience:

```
┌────────────────────────────────────────────────────────────────────────┐
│                     MEDIA & IMMERSION DECISION TREE                    │
├────────────────────────────────────────────────────────────────────────┤
│ • HIGH-RES AUTHENTIC PHOTOGRAPHY (Modality 1 & 2):                     │
│   When the business has real-world physical reality (rooms, dishes,    │
│   craftsmanship). Harvested via `=s1600` or reframed using 8-dimension │
│   35mm film grain prompts. No cartoon 3D renders.                      │
│                                                                        │
│ • INTERACTIVE MICRO-MODULES (Modality 2):                              │
│   When customers deliberate on price or options (dynamic stay rate     │
│   calculator, reactive menu search, slide-out drawer, bento reveals).  │
│                                                                        │
│ • FULL 3D / WEBGL CANVAS (Modality 3):                                 │
│   Only when experiential awe is the primary conversion driver (e.g.    │
│   flagship automotive, luxury creative portfolio, Web3). Implemented   │
│   using verified 60fps MIT ThreeUI (@designcodeio/threeui) components. │
│                                                                        │
│ • AMBIENT VIDEO LOOPS:                                                 │
│   Looping <video autoplay muted loop playsinline> with Safari H.264    │
│   fallback, poster image, and prefers-reduced-motion pause control.    │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. The 3-Benchmark Grounding Protocol

To eliminate AI slop, the AI **never designs from scratch**. In Stage 4, the AI executes this exact 3-step benchmark recommendation and grounding workflow:

### Step 1: AI Design Reasoning Presentation
The AI outputs a concise **Architectural Thesis** summarizing:
1. Recommended Style Direction & Spatial Layout.
2. Recommended Color Grading & Typography Pairing.
3. Recommended Immersion Strategy (Photo vs. Interactive vs. 3D).

### Step 2: 3 Curated Benchmark Website Recommendations
The AI presents **3 real-world, award-winning benchmark reference websites** matching the business category and modality. For example, for a Luxury Farmstay / Hospitality project:
1. **Benchmark A (Earthy Editorial Craft)**: `https://singlethreadfarms.com` — *Visual DNA: Warm stone canvas (#FAF8F5), serif headlines, 120px section breathing room, authentic harvest imagery, slide-out booking.*
2. **Benchmark B (Minimalist Architectural Calm)**: `https://chesleigh.com` — *Visual DNA: Restrained Swiss typography, instant date availability hotbar, full-bleed landscape photography.*
3. **Benchmark C (Sensory Scrollytelling)**: `https://mandala.farm` — *Visual DNA: Fluid kinetic reveals, animated bento cards, dynamic room rate calculator.*

### Step 3: Selection & Token Compilation
- The user selects one benchmark (or the AI selects the optimal fit).
- The AI runs `scripts/extract_tokens.py` to capture the computed CSS values (`window.getComputedStyle`).
- The extracted tokens are synthesized into `DESIGN.md`.
- The AI **compiles the website grounded in that reference**, replicating its layout geometry and whitespace rhythm while generating 100% fresh, factual content and assets.

---

## 3. Concrete Design Reasoning Archetype Playbook

### Scenario A: Luxury Farmstay / Eco-Resort (e.g., Krishi Farms)
* **AI Design Reasoning**:
  - *Style*: Warm Architectural Editorial.
  - *Layout*: Asymmetric 60/40 hero grid + 4-stop sensory visual tour + numbered amenity index strip.
  - *Color*: Warm stone `#FAF8F5`, deep espresso `#1A1816`, aged brass `#8B6F4E`.
  - *Typography*: Playfair Display / Cormorant Garamond display + Plus Jakarta Sans body.
  - *Immersion*: High-res 35mm photography (pool, villas, orchards) + **Interactive Stay Rate Calculator** with guest/date sliders + direct WhatsApp reservation hotbar.
  - *Benchmark*: `singlethreadfarms.com` / `mandala.farm`.

### Scenario B: Highway Dining & Takeaway (e.g., Kanakapura Highway Food Court)
* **AI Design Reasoning**:
  - *Style*: High-Contrast Express Utility.
  - *Layout*: Sticky operational status header ("🟢 Open Now") + 55/45 hero with live distance counter + tabbed reactive digital menu.
  - *Color*: Warm charcoal `#111827`, saffron gold `#F59E0B`, crisp white `#FFFFFF`.
  - *Typography*: Space Grotesk / Outfit display + Inter/System body with `tabular-nums`.
  - *Immersion*: High-resolution food styling photography + **Slide-Out Takeaway Bag Drawer** + 1-click WhatsApp Curbside dispatch. Zero heavy 3D.
  - *Benchmark*: `galvinrestaurants.com` / `sweetgreen.com`.

### Scenario C: High-Tech B2B SaaS / Observability Platform
* **AI Design Reasoning**:
  - *Style*: Minimalist High-Density Monolith.
  - *Layout*: Asymmetric bento grid with Magic UI shimmer borders + terminal command tabs + interactive ROI calculator.
  - *Color*: Deep obsidian `#090A0F`, slate `#1E293B`, technical cyan/amber `#06B6D4`.
  - *Typography*: Geist / Syne display + Geist Mono for metrics and code blocks.
  - *Immersion*: Interactive code execution tabs + live metric charts (Chart.js) + SOC 2 Type II trust badges.
  - *Benchmark*: `linear.app` / `raycast.com` / `resend.com`.
