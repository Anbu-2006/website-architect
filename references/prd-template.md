# Standardized Enterprise Website PRD & Technical Architecture Template

When Stage 4 confirmation is received, instantiate this exact template using the specific business details gathered during discovery.

---

# Product Requirements Document (PRD) & Technical Architecture

**Project Entity:** [Client / Business Name]  
**Operating Sub-Type:** [Code & Sub-Type Name, e.g., B3: MRO Wholesale Distributor]  
**Authoritative System of Record:** [Primary Hub: ERP / CRM / EHR / Custom DB]  
**Data Consistency Standard:** [Tier A / Tier B / Tier C]  

---

## 1. Executive Strategy & Operational Model
* **The Commercial Mandate:** [Explain why an owned website is mandatory for this business vs. third-party aggregators].
* **The Scarce Resource:** [Identify the finite resource being managed: stock, clinician hours, partner judgment, machine time, crew labor, etc.].
* **North-Star Conversion Action (CTA):** [Primary CTA label and operational outcome].
* **User Personas & Friction Tolerance:** [Detail the primary buyer mindset, urgency level, and what triggers an immediate exit].

---

## 2. Canonical Sitemap & Route Hierarchy

### Public Canonical Routes (MVP: [X] Pages / Scale: [Y] Pages)
* `/`: Root homepage and brand value proposition.
* `/[core-catalog-or-services]`: Master taxonomy index.
* `/[core-catalog-or-services]/[slug]`: Specific detail pages.
* `/[conversion-funnel-entry]`: Dedicated conversion path (e.g., `/quote`, `/book`, `/checkout`).
* `/about`, `/team`, `/contact`: Core trust and verification surfaces.
* `/legal/privacy`, `/legal/terms`, `/legal/compliance`: Regulatory disclosures.

### Authenticated & Gated Routes
* `/portal/login`: Authentication portal (OAuth / SAML / Magic Links).
* `/portal/dashboard`: Core operational overview.
* `/portal/[records]`: Sub-type specific records (e.g., `/portal/orders`, `/portal/matters`, `/portal/work-orders`).
* `/portal/settings`: Account, team, and security preferences.

### System & Edge Routes
* `/404`: Branded not-found handler with contextual search and fallback navigation.
* `/500`: System failure handler configured to suppress stack traces and log telemetry.
* `/api/webhooks/[provider]`: Inbound asynchronous webhook handlers.
* `/consent/preferences`: Dynamic cookie and data privacy consent manager.

---

## 3. Page-Level Component & Interaction Matrix
*(Detail the top 3–4 critical conversion pages for this sub-type)*

### Page 1: [Page Name, e.g., Homepage / Product Detail / Booking Wizard]
* **Above-the-Fold Zone:**
  * Hero composition, layout, and background asset rules.
  * Primary value proposition formula.
  * Primary and secondary CTA configuration.
* **Body Modules & Dynamic Engines:**
  * [Itemize specific technical engines: e.g., real-time calendar picker, parametric SKU table, CAD uploader, usage slider].
* **Form Field & Input Validation Schema:**
  * Step-by-step fields, client-side format regex, server-side sanitization, and database constraints.
  * File upload constraints: allowed MIME types, size limits, antivirus quarantine rules.
* **Trust & Proof Modules:**
  * Specific industry accreditations, certifications, badges, and verified testimonial blocks.

---

## 4. Operational State Machine & Backend Workflows

### Primary Conversion State Machine

```text
[User Action] ──► [Preliminary Verification] ──► [Authoritative Locking (Tier A)] ──► [Commit & Dispatch]
```

* **Step-by-step state transitions:** Explicitly define state labels (e.g., `Anonymous` → `Soft Hold (TTL)` → `Payment Authorized` → `Committed Order`).
* **Concurrency & Race Condition Handling:** [Explain the exact mechanism: PostgreSQL row locks, Redis Lua scripts, composite unique constraints].
* **Automated Asynchronous Hand-Offs:**
  * CRM / ERP ingestion payloads.
  * Transactional email/SMS notifications.
  * Automated document compilation (PDF invoices, contracts, or CoAs).
* **Back-Office Modules & Role-Based Access Control (RBAC):**
  * Matrix defining permissions for Admin, Operations Staff, and Client/Viewer roles.

---

## 5. Technical Stack & Failure Mode Safeguards

### Recommended Architecture
* **Frontend & Edge Layer:** [e.g., Next.js App Router with SSG for marketing and SSR for dynamic routes; Cloudflare Edge CDN].
* **Application & API Layer:** [e.g., Node.js / Go microservices; REST / GraphQL / gRPC].
* **Database & Concurrency Tier:** [e.g., PostgreSQL for relational ACID state; Redis for distributed locks and session caches; ClickHouse for time-series logs].
* **Third-Party API Dependency Checklist:** [Identity providers, payment processors, ERP connectors, messaging relays].

### Anti-Patterns & Vulnerability Defense
* **Top 3 Anti-Patterns to Avoid:** [Specific architectural or design mistakes common to this business type].
* **Primary Technical Vulnerability:** [The single most dangerous failure point—e.g., double-booking, cross-tenant data leak, price drift—and how this architecture neutralizes it].

---

## 6. Asset Manifest & Media Mapping Table

Every visual asset (user-uploaded or generated) must be mapped to its exact component target, aspect ratio, and accessibility metadata:

| Asset Source Path | Semantic Role | Target Component Slot | Target Dimensions & Aspect | Alt Text & Accessibility Tag |
| :--- | :--- | :--- | :--- | :--- |
| `assets/logo.svg` | `BrandLogoPrimary` | `HeaderNavbar`, `Footer` | Scalable Vector / 240×60px | "Official Oasis Restaurant Logo" |
| `assets/hero-dish.webp` | `HeroVisual` | `HomepageHeroBackground` | 1920×1080 (16:9) | "Freshly prepared signature Chicken Dum Biryani with aromatic spices" |
| `assets/mandi.webp` | `FeaturedDish_1` | `PopularDishesGrid[0]` | 800×600 (4:3) | "Traditional Arab Chicken Mandi Platter" |
| `assets/tandoori.webp` | `FeaturedDish_2` | `PopularDishesGrid[1]` | 800×600 (4:3) | "Charcoal roasted Tandoori Chicken with lemon garnish" |
| `assets/ambiance.webp` | `AmbiancePhoto` | `AboutSectionAmbiance` | 1200×800 (3:2) | "Spacious family dining hall at Oasis Restaurant" |
