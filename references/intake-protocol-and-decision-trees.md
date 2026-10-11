# Autonomous Multi-Path Intake Protocol & Cognitive Decision Trees

This reference guide specifies the autonomous data extraction pipelines, intake scenarios, and friction-free decision flow for `/website-architect`.

---

## 1. The Two-Step Intake Protocol & Asset Sourcing Gate

To ensure both data accuracy and maximum aesthetic quality, the intake operates in two deterministic steps:

### Step 1: Link & Reference Collection
The AI requests the primary business URL (Google Maps listing, website, or pitch description) and optional benchmark reference website URL.

### Step 2: Interactive Asset Sourcing Gate (via `ask_question`)
The AI prompts the user to select how media assets (photos, videos, brand logos) should be sourced:
```json
{
  "question": "How would you like to source visual and media assets (photos, videos, logos) for this website build?",
  "options": [
    "(Recommended) Hybrid: Combine assets I place in the project folder with scraped Google Maps photos, reviews, and vectors.",
    "User-Provided Assets Only: Exclusively scan and curate high-res photos and videos I have placed in the project folder.",
    "Google Maps & Scraped Only: Autonomously harvest all photography, customer reviews, and vectors from Google Maps & web sources."
  ]
}
```

```text
┌──────────────────────────────────────────────────────────────────────────────────┐
│                             STAGE 0: INTAKE SEQUENCE                             │
├──────────────────────────────────────────────────────────────────────────────────┤
│ Step 1: Collect Target Business URL / Maps Link & Benchmark Reference URL        │
│ Step 2: Ask Asset Sourcing Gate (Hybrid vs. User Assets vs. Scraped Maps)        │
└───────────────────────────────────────┬──────────────────────────────────────────┘
                                        │
             ┌──────────────────────────┼──────────────────────────┐
             ▼                          ▼                          ▼
      [Hybrid Mode]             [User Assets Only]        [Maps Scraped Only]
   • User Hero & Videos       • Scan user_assets/        • Playwright harvest
   • Maps Reviews & Vectors   • Vision inspection        • 5-tier video stream
   • Curate into Sections     • Keyframe extraction      • Ken-Burns fallback
             │                          │                          │
             └──────────────────────────┴──────────────────────────┘
                                        │
                                        ▼
                  [Visual Media & Keyframe Inspection]
                  • Pillow aspect ratio / orientation analysis
                  • ffmpeg video duration, fps, & keyframe extraction
                  • Vision evaluation (view_file) for section fit
                  • Video generation recipes (Higgsfield / fallback)
                                        │
                                        ▼
                  [Business Intelligence & ADS Scoring]
                  • 10-Archetype taxonomy classification
                  • Topology lock: SPA vs. MPA (Zero 1-section stubs)
                  • Pre-flight Enterprise PRD -> Stage 9 Build
```

---

## 2. Customer Arrival Mindset Taxonomy

Every customer visits a website with a specific cognitive state and tolerance for latency:

1. **Urgent / Convenience Focus (Highway, Emergency Trades, Fast Dining)**:
   - *Mindset:* "I am hungry / I need immediate help / I am driving right now."
   - *Tolerance for Latency:* Zero. Must load in <0.8s on 3G/4G.
   - *Critical Architecture:* Delivery partner links (Swiggy, Zomato), one-tap calling, live opening hours, express curbside pickup, parking directions.
   - *Prohibited:* Heavy 3D, long video intros, forced animations.
   - *Inferred Modality:* **Modality 1 (High-Utility / Conversion-First)**.

2. **High-Ticket Experiential Focus (Luxury Farmstays, Boutique Resorts, Wedding Grounds)**:
   - *Mindset:* "I am planning an expensive family vacation, corporate offsite, or wedding. Does this place have the right ambiance and quality?"
   - *Tolerance for Latency:* Moderate (<2.0s). Dwell time is high.
   - *Critical Architecture:* Visual scrollytelling tour (pool, lawn, luxury suites), verified guest reviews, transparent date & guest pricing calculator, direct WhatsApp reservation.
   - *Inferred Modality:* **Modality 2 (Hybrid Interactive / Scrollytelling)**.

3. **High-Volume Transactional Focus (E-Commerce, Apparel, Gadgets)**:
   - *Mindset:* "I want to find a specific product, check reviews, and buy."
   - *Tolerance for Latency:* Very Low. Every 100ms delay drops conversions by 7%.
   - *Critical Architecture:* Instant search, category filters, slide-out cart drawer, 1-click checkout.
   - *Prohibited:* Forced 3D canvas scrolling (causes 28–42% cart abandonment).
   - *Inferred Modality:* **Modality 1 or 2 with Server Components**.

4. **B2B Investigative Focus (Enterprise Software, High-Trust Advisory)**:
   - *Mindset:* "Will this software solve our workflow problem, scale securely, and comply with regulations?"
   - *Tolerance for Latency:* Low-to-Moderate.
   - *Critical Architecture:* Clear outcome-based value proposition, interactive ROI calculator, SOC 2 / GDPR badges, transparent pricing, developer docs.
   - *Inferred Modality:* **Modality 2 (Hybrid Interactive)**.

---

## 3. High-Intelligence Autonomous Operation

### ⛔ Anti-Fatigue Directives
- **NEVER** ask the user to pick frontend frameworks or styling libraries. Next.js 15 (App Router) + TypeScript + Tailwind CSS v4 + Motion is locked in universally.
- **NEVER** ask the user to select experience modalities, conversion features, or back-office integrations. The AI infers these autonomously based on the business archetype.
- **NEVER** dump numbered question lists in chat (e.g. `1. What is your goal? 2. What is your budget?`).
- **RESTRICT** interactive prompts (`ask_question`) strictly to essential human checkpoints:
  1. **Intake Initialization (Stage 1)**: Maps link or business pitch.
  2. **Benchmark Selection (Stage 4B)**: Confirming or providing visual design reference (skipped if provided upfront).
  3. **Build Authorization (Stage 8)**: Approving the verified `PRD.md` before launching the production build.
