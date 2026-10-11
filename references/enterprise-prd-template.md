# Universal Enterprise Product Requirements Document (PRD) Template

This document provides the standard architectural specification blueprint delivered in Stage 8 of `/website-architect`. 

Every generated PRD must follow this comprehensive 6-domain structure, adapting cleanly to either **Single-Page Architecture (SPA)** or **Multi-Page Architecture (MPA)** based on the calculated **Architecture Decision Score (ADS)**:

---

```markdown
# Product Requirements Document & Technical Architecture Specification

**Project Name:** [Business Name]  
**Universal Archetype:** [Archetype #1-10: e.g., Local Food & Hospitality / Luxury Farmstay / E-Commerce / B2B SaaS]  
**Site Topology:** [Single-Page Architecture (SPA) vs. Multi-Page Architecture (MPA)]  
**Architecture Decision Score (ADS):** [Score / 15: e.g. ADS = 4 (SPA) or ADS = 11 (MPA)]  
**Primary North-Star CTA:** [e.g. Instant WhatsApp Curbside Takeaway / Stay Reservation / 1-Click Checkout / Scheduled Consultation]  
**Runtime Tech Stack:** [Modern HTML5 + CSS3 + ES6 / Vite + React (TypeScript) + Tailwind / Next.js (App Router)]  
**Date:** [Date] | **Status:** Approved for Implementation  

---

## 1. Executive Summary & Strategic Value Proposition
- **Business Capability:** [Concise statement of commercial offerings and market category]
- **Target Persona & Arrival State:** [e.g., Highway traveler seeking hot food and clean restrooms OR tech executive seeking enterprise cloud observability]
- **Scarce Operational Resource:** [e.g., Table turnover / Villa calendar availability / Senior partner consultation hours]
- **Primary Conversion Metric:** [Target conversion action and expected user completion velocity]

---

## 2. Grounded Benchmark Reference & Extracted Design System Tokens
- **Selected Experience Modality:** [Modality 1: High-Utility / Modality 2: Hybrid Interactive / Modality 3: Full Canvas Immersive]
- **Award-Winning Benchmark URL:** [e.g. `https://singlethreadfarms.com` or `https://linear.app`]
- **Extracted Visual DNA (`DESIGN.md`):**
  - **Headline Typography:** [e.g. Cormorant Garamond / Playfair Display: font-size 56px, weight 600, letter-spacing -0.025em]
  - **Body Typography:** [e.g. Plus Jakarta Sans / Satoshi: font-size 16px, line-height 1.65, weight 400]
  - **Canvas Surface & Ink:** [e.g. Background `#FAF8F5`, Ink `#1A1816`, Accent `#8B6F4E`, Border `rgba(0,0,0,0.08)`]
  - **Spatial Scale:** [e.g. Container max-width 1280px, section padding 112px desktop / 64px mobile]
- **Anti-Slop Color Rule:** Zero default indigo/violet gradients, zero generic slate-900 backgrounds.

---

## 3. Architecture Topology, Routing & Spatial Wireframe Hierarchy

### 2.1 Architectural Decision Score (ADS) Justification
$$\text{ADS} = \text{Catalog Depth} (1-5) + \text{Search Specificity} (1-5) + \text{Journey Deliberation} (1-5) - \text{Immediacy Need} (1-5)$$
- **Calculated ADS:** [Score]
- **Decision:** [If ADS <= 5: Single-Page Architecture (SPA) | If ADS >= 6: Multi-Page Architecture (MPA)]
- **Topology Rationale:** [Why SPA or MPA is mathematically optimal for this customer journey and catalog scale]

### 2.2 Sitemap & Route Topology

#### Option A: If Single-Page Architecture (SPA)
- **Primary Route:** `/` (Continuous High-Conversion Journey)
  - **Section 1.0: Global Utility Header** (Sticky, Operational Status Badge, Direct Hotline, Action Trigger)
  - **Section 2.0: Contextual Hero Viewport** (55/45 Grid, H1 Proposition, Dual CTAs, Live Social Proof Strip)
  - **Section 3.0: High-Urgency / Value Strip** (Fast Amenities, Diagnostic Guarantee, or Scarcity Notice)
  - **Section 4.0: Core Offering / Signature Showcase** (Interactive Menu, Room Suites, or Service Tiers)
  - **Section 5.0: Sensory Immersion / Visual Tour** (3D Grounds Tour Scrubber, Video Reel, or Before/After Slider)
  - **Section 6.0: Interactive Dynamic Engine** (Stay Rate Calculator, Instant Estimate Tool, or Order Cart)
  - **Section 7.0: Verified Social Proof & Reviews** (Google Reviews Rating Counter, Verified Customer Quotes)
  - **Section 8.0: Friction-Mitigation FAQ Accordion** (Policies, Inclusions, Logistics, Guarantees)
  - **Section 9.0: Physical Location, Route & Logistics** (Interactive Map Embed, Mile-Marker Directions, Plus Code)
  - **Section 10.0: Global Footer & Legal** (Operating Hours, Licenses, Direct Contact, Copyright)
- **Persistent Mobile Hotbar / Slide-Out Drawers:**
  - Slide-Out Order Bag / Booking Drawer (WhatsApp Encoder / Instant Form)
  - Sticky Bottom Action Hotbar on mobile devices (< 768px)

#### Option B: If Multi-Page Architecture (MPA)
- **Canonical Routing Map:**
  - **Page 1: `/` (Platform / Brand Homepage)**: Hero value proposition, marquee client/partner logos, core offerings grid, commercial impact proof, testimonials.
  - **Page 2: `/[catalog-or-services]` (e.g. `/menu`, `/services/[trade]`, `/collections/[category]`, `/features/[slug]`, `/practices/[slug]`)**: Category taxonomy, multi-faceted filtering, deep-dive technical specs, pricing packages.
  - **Page 3: `/[product-or-attorney-slug]` (PDP / Bio)**: High-res zoomable gallery, live inventory status, bar admissions/certifications, direct booking/purchase.
  - **Page 4: `/pricing` or `/estimate` or `/case-results`**: Interactive cost calculator, tier comparison matrix, ROI estimation, anonymized track record.
  - **Page 5: `/checkout` or `/contact` or `/reserve`**: Distraction-free conversion funnel, address autocomplete, guest checkout, secure consultation intake.

---

## 3. Page & Component Specification (Section-by-Section)

*(Adapts to the specific archetype chosen: e.g. Restaurant, Farmstay, Law Firm, E-Commerce, SaaS, Clinic, or Contractor)*

### Component 1.0: Global Utility Header
- **Container:** Sticky top bar, `height: 72px`, backdrop blur `16px`, `z-index: 50`.
- **Brand Identifier:** Vector SVG mark + Business Name + Municipal Sub-Badge.
- **Operational Status Badge:** Real-time pulse indicator checking local client time against operational hours (e.g., "🟢 Open Now • Closes 11:00 PM").
- **Direct Hotline:** `tel:` protocol link with raw phone number displayed.
- **Action Triggers:** Primary North-Star CTA button + Drawer trigger with badge counter.

### Component 2.0: Contextual Hero Viewport
- **Grid Layout:** Asymmetric 55/45 desktop grid; single-column mobile stack.
- **H1 Headline:** 8–12 words declaring core specialization, location, and key outcome.
- **Subheadline:** 24–36 words detailing speed, quality differentiators, and guarantees.
- **Dual CTAs:** Primary conversion button + Secondary orientation/route button.
- **Verified Proof Strip:** Star rating (`4.2 ★`), verified review volume, and category authority badge.
- **Visual Anchor:** High-resolution authentic photograph (`assets/...`) with ambient depth shadow.

### Component 3.0: Core Offering / Interactive Engine
- **Search & Filter:** Instant zero-latency search matching item names, tags, and specifications.
- **Category Tabs:** Horizontal pill buttons for rapid browsing without page reload.
- **Offering Cards:** High-res image, pricing tier, key specs, and instant action trigger (`+ Add`, `Select`, `Book`).
- **Interactive Calculator (if applicable):** Dynamic date range, guest count, or square-footage sliders updating live totals.

### Component 4.0: Social Proof & Credibility Validation
- **Verified Ratings:** Direct Google Review embed or verified third-party audit badge.
- **Regulatory / License Display:** License numbers, bar admissions, medical board certifications, or ISO compliance.

### Component 5.0: Location, Logistics & Contact
- **Physical Address & NAP:** Full street address, landmark notes, Plus Code, and direct hotline.
- **Route Navigation:** Instant triggers opening Google Maps, Apple Maps, and Waze with coordinates pre-loaded.

---

## 4. Page & Component Specification (Section-by-Section)

*(Adapts to the specific archetype chosen: e.g. Restaurant, Farmstay, Law Firm, E-Commerce, SaaS, Clinic, or Contractor)*

---

## 5. Anti-Slop Quality Gate & 15 Greppable Negative Constraints

Before final build delivery, verify compliance against the 15 mechanically-checkable anti-slop rules:

| # | Guardrail Name | Mechanically Greppable Test | Status |
|---|---|---|---|
| 1 | **No Default Inter/Sans** | Grep `font-family: 'Inter'`, `Roboto` without pairing | ✅ PASSED (Bespoke Display + Body pairing) |
| 2 | **No Indigo/Violet Defaults** | Hex search `#8b5cf6`, `#7c3aed`, `#6366f1` | ✅ PASSED (Domain-calibrated palette) |
| 3 | **No Radial Blur Blobs** | Class search `blur-3xl bg-purple-500/20` | ✅ PASSED (Crisp architectural surfaces) |
| 4 | **No 3-Column Card Grids** | DOM selector `grid-cols-1 md:grid-cols-3` | ✅ PASSED (Asymmetric 60/40 & bento layouts) |
| 5 | **No Icon-in-Rounded-Square**| DOM query `div.rounded-2xl > svg` top-left | ✅ PASSED (Editorial numbering / typography) |
| 6 | **No Emoji Structural Marks**| Unicode search for emojis in buttons/headers | ✅ PASSED (Cohesive vector SVGs) |
| 7 | **No Gradient Text on Headers**| Search `bg-clip-text text-transparent` on `<h1>`–`<h3>` | ✅ PASSED (Solid high-contrast ink) |
| 8 | **No Cards-Inside-Cards** | DOM search `[class*="card"] [class*="card"]` | ✅ PASSED (Flat spatial planes & dividers) |
| 9 | **No Hollow Buzzwords** | Regex `(?i)(unleash|seamlessly|elevate|supercharge)` | ✅ PASSED (Factual, domain-specific copy) |
| 10| **No Fake Precision Metrics** | Regex `(?i)(\b99\.9%\b|\b4\.8x\b|\b94%\b)` unverified | ✅ PASSED (Verifiable facts & real reviews) |
| 11| **Negative Display Tracking** | CSS check: `letter-spacing: 0` on headers $\ge 40\text{px}$ | ✅ PASSED (Negative tracking `-0.02em`) |
| 12| **No Glassmorphism Defaults**| Class search `backdrop-blur-md bg-white/10` | ✅ PASSED (Grounded tactile surfaces) |
| 13| **No Staccato One-Liners** | Copy check: Consecutive 3-word sentences | ✅ PASSED (Balanced informative sentences) |
| 14| **Zero Raw Hex in Components**| Grep: Inline `#xxxxxx` inside component files | ✅ PASSED (100% tokenized CSS variables) |
| 15| **No Plastic AI Imagery** | Asset check: Cartoon 3D renders, neon stock | ✅ PASSED (Authentic 35mm photography) |

---

## 6. Technical Architecture, State Management & Back-Office Protocols
- **Frontend Stack:** [e.g. Modern HTML5 + CSS3 + ES6 OR Vite + React + Tailwind OR Next.js]
- **State Store:** Client-side reactive state tracking selection, pricing, and inputs.
- **Back-Office Dispatch Pipeline:** Encodes line-item details, quantities, subtotal, and special notes into a clean `wa.me/` URI or webhook payload.
- **Zero-Credit Media Pipeline:** Real-world assets sourced from Google Maps CDN (`=s1600`) and Pinterest editorial CDN (`/736x/`) at zero credit cost.

---

## 7. Authoritative Asset Manifest Table

| Asset ID | Filename | Source | Resolution | Placement on Site | Alt Text & Accessibility Tag | Status |
|---|---|---|---|---|---|---|
| AST-01 | `assets/hero_primary.jpg` | Google Maps CDN | 1600×1066 | Hero Visual Anchor | [Descriptive alt text] | Verified |
| AST-02 | `assets/showcase_01.jpg` | Pinterest Editorial | 736×980 | Offering Card / Gallery | [Descriptive alt text] | Verified |
| AST-03 | `assets/showcase_02.jpg` | Pinterest Editorial | 736×920 | Offering Card / Gallery | [Descriptive alt text] | Verified |

---

## 8. Schema.org Structured Data & Performance Budgets

### JSON-LD Implementation
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "[LocalBusiness / Restaurant / Resort / MedicalBusiness / LegalService / Product]",
  "name": "[Business Name]",
  "image": "[Hero Image URL]",
  "telephone": "[Phone Number]",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[Street Address]",
    "addressLocality": "[Locality]",
    "addressRegion": "[State]",
    "postalCode": "[Postal Code]",
    "addressCountry": "[Country]"
  }
}
</script>
```

### Technical Performance Budgets
- **Largest Contentful Paint (LCP):** < 1.0s on 4G mobile networks.
- **Cumulative Layout Shift (CLS):** < 0.05.
- **First Input Delay (FID) / INP:** < 100ms.
- **WCAG AA Compliance:** Text contrast ratio ≥ 4.5:1 across both dark and light modes.
- **Touch Target Ergonomics:** All interactive buttons and mobile hotbar links ≥ 48×48dp.
```
