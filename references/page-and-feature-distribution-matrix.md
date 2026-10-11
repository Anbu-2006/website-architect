# Universal Page-by-Page & Feature Distribution Matrix

This reference provides the authoritative specification for **site topology (SPA vs. MPA)**, **canonical routes**, and **exact section-by-section component anatomy** across all 10 universal digital archetypes.

---

## 1. Master Archetype Topology & Routing Overview

| # | Archetype | Default Topology | Primary Routing Engine | Minimum Canonical Pages (MPA) | When Compressed to Single-Page (SPA) |
|---|---|---|---|---|---|
| **1** | **Local Food & Beverage** | **Single-Page (SPA)** *(Express/Highway)* or **MPA** *(Multi-Location/Fine Dining)* | Modern HTML5 or Vite + React | `/`, `/menu`, `/locations/[city]`, `/catering`, `/contact` | Single-location restaurant or highway stop with menu, curbside takeaway, and WhatsApp cart on one fast page. |
| **2** | **Trade Contractors & Local Physical Services** | **Single-Page (SPA)** *(Single Trade)* or **MPA** *(Multi-Service/Commercial)* | Modern HTML5 or Vite + React | `/`, `/services/[trade]`, `/service-area/[zip]`, `/estimate`, `/contact` | Single residential trade (e.g. emergency plumber) with 24/7 hotline, territory map, and quote calculator on one page. |
| **3** | **High-Trust Professional Services (Law, Wealth, Advisory)** | **Multi-Page (MPA)** | Next.js (App Router) or Astro | `/`, `/practices/[slug]`, `/attorneys/[slug]`, `/case-results`, `/insights`, `/contact` | Solo advisory practitioner or boutique consultancy with a single core retainer offering. |
| **4** | **Healthcare, Wellness & Medical Clinics** | **Multi-Page (MPA)** | Next.js (App Router) or Astro | `/`, `/specialties/[id]`, `/doctors/[id]`, `/insurance`, `/patient-portal`, `/book` | Single-practitioner wellness studio or local dental office with online booking modal. |
| **5** | **E-Commerce & DTC Retail** | **Multi-Page (MPA)** *(Catalog)* or **SPA** *(Single-Product Hero)* | Next.js (App Router) or Vite + React | `/`, `/collections/[category]`, `/products/[slug]`, `/cart`, `/checkout`, `/account` | Single revolutionary hero product (1 SKU) with 1-click bundle upsells and slide-out checkout drawer. |
| **6** | **B2B Software & SaaS Platforms** | **Multi-Page (MPA)** | Next.js (App Router) | `/`, `/features/[capability]`, `/pricing`, `/integrations`, `/docs`, `/blog`, `/login` | Early-stage pre-launch waitlist or single micro-tool with demo video and email capture. |
| **7** | **Luxury Farmstays, Resorts & Event Grounds** | **Single-Page (SPA)** *(Single Estate)* or **MPA** *(Resort Chain)* | Vite + React (TypeScript) | `/`, `/villas/[slug]`, `/weddings-events`, `/dining`, `/virtual-tour`, `/reserve` | Single private farmstay/estate (e.g. Krishi Farms) with 3D virtual tour, stay rate calculator, and WhatsApp booking on one cohesive page. |
| **8** | **Creative Agencies & Portfolios** | **Single-Page (SPA)** or **Hybrid MPA** | Vite + React + GSAP/R3F | `/`, `/work/[project-slug]`, `/capabilities`, `/agency`, `/contact` | Boutique motion studio or director showcase with video showreel, client marquee, and project brief form. |
| **9** | **Education, Bootcamps & Community** | **Multi-Page (MPA)** | Next.js (App Router) or Astro | `/`, `/curriculum/[track]`, `/outcomes`, `/tuition-financing`, `/apply`, `/campus` | Single masterclass, weekend conference, or single-cohort summit landing page. |
| **10** | **Industrial, Manufacturing & B2B Supply** | **Multi-Page (MPA)** | Next.js (App Router) | `/`, `/capabilities/[process]`, `/materials`, `/equipment-list`, `/certifications`, `/rfq` | Single custom fabrication shop focusing purely on CAD file uploads and quote generation. |

---

## 2. In-Depth Page-by-Page Component Breakdown

### Archetype 1: Local Food, Beverage & Highway Hospitality

#### Scenario A: Highway Takeaway / Fast Dining (Single-Page SPA)
*Optimized for travelers moving at 80 km/h needing instantaneous menu decisions, curbside parking, and frictionless ordering.*
* **Hero Banner Section**:
  - Live Highway Mile Marker / Distance badge (e.g., *"5 mins before Bidadi Flyover"*)
  - High-impact visual of signature hot dish with steam micro-animation
  - Dual Primary CTAs: `[ Order Ahead on WhatsApp ]` and `[ Open in Google Maps ]`
  - Floating Live Status: "Open Now • Closes at 11:00 PM • Valet Parking Available"
* **Instant Curbside & Drive-Thru Ordering Module**:
  - Quick-toggle category filter tabs (`Mandis & Biryanis`, `Starters & Grills`, `Beverages`)
  - Item cards with zero-latency `+ Add` counter, spice indicator, dietary badge (Halal/Veg)
  - Sticky bottom floating summary bar with total cost and `[ Order via WhatsApp Dispatch ]`
* **Highway Traveler Amenities Grid**:
  - 4-column icon badge matrix: Clean Restrooms (Checked Hourly), AC Family Dining Hall, EV Fast Charging (60kW), Ample Car Parking
* **Verified Social Proof & Google Reviews Strip**:
  - Live Google Review Rating badge (4.2★ from 2,300+ travelers)
  - Carousel of high-intent highway traveler quotes emphasizing speed and hygiene
* **Interactive Geo-Location & Highway Route Directions**:
  - Static Leaflet/Mapbox embed with highway entry slip-road highlighted
  - Clickable navigation triggers for Google Maps, Apple Maps, and Waze
* **Micro-Footer & Contact**:
  - One-tap phone dialer, WhatsApp direct chat, FSSAI license badge, and operating hours

#### Scenario B: Multi-Location Dining Brand / Fine Gastronomy (Multi-Page MPA)
* **Page 1: Homepage (`/`)**:
  - Cinematic ambient video hero of culinary craftsmanship, kitchen plating, and architectural dining space
  - Brand heritage narrative & executive chef introduction
  - Signature tasting menu highlights with high-res editorial photography
  - Multi-location selector cards with real-time table availability
  - Press accolades strip (Michelin Guide, 50 Best, Conde Nast Traveler)
* **Page 2: Full Menu (`/menu`)**:
  - Tabbed sub-menus: Lunch Prix-Fixe, Evening Degustation, Wine & Sommelier Pairing, Artisanal Cocktails
  - Dietary filtration (Vegan, Gluten-Free, Nut Allergies, Halal)
  - Detailed ingredient origins and farm sourcing notes
  - Explicit rule: *No downloadable raw PDF files; all menus rendered as semantic, crawlable HTML with Schema.org Restaurant schema.*
* **Page 3: Locations & Ambience (`/locations/[city]`)**:
  - Dedicated SEO landing page per municipal district
  - Architectural photography of private dining rooms, patio, and chef's counter
  - Specific address, valet instructions, transit access, and direct private concierge line
* **Page 4: Private Events & Catering (`/private-dining`)**:
  - Seating capacity charts (Cocktail reception vs. Seated banquet)
  - Event inquiry form with date picker, party size, AV requirements, and budget tier selector
  - Past corporate & wedding gala gallery with downloadable event prospectus
* **Page 5: Reservation Engine (`/reserve`)**:
  - Embedded SevenRooms / OpenTable widget or custom calendar selector
  - Cancellation policy disclosure, dress code guidelines, and instant SMS confirmation

---

### Archetype 2: Local Physical Services & Trade Contractors

#### Scenario A: Emergency Trade / Single Service (e.g. 24/7 Plumber) (Single-Page SPA)
* **Sticky Emergency Dispatch Header**:
  - Prominent pulsating red badge: "24/7 Rapid Emergency Dispatch • On-Site in < 45 Mins"
  - Click-to-Call Primary CTA with phone number pre-loaded: `[ Call (555) 019-2834 ]`
* **Emergency Hero Section**:
  - Clear value proposition: Licensed, Insured, Zero Dispatch Fee with repair
  - Instant dispatch form: ZIP code input + emergency issue selector (`Burst Pipe`, `Water Heater Flooding`, `Drain Clog`)
* **Emergency Service Cards**:
  - 3-column grid of common emergencies with standard diagnostic pricing transparency
* **Verified Credentials & Insurance Strip**:
  - Master Plumber License # displayed, BBB A+ rating, $2M General Liability Insurance badge
* **Live Service Radius Map**:
  - Interactive coverage area boundary showing response time tiers (< 30 min, < 45 min, < 60 min)
* **Emergency Step-by-Step Dispatch Workflow**:
  - 3-step visual tracker: 1. Instant Call -> 2. Tech Dispatched with Live GPS -> 3. Upfront Fixed Price Repair
* **Customer Reviews & Before/After Gallery**:
  - Slider showing burst pipe repair, clean work area, and 5-star customer feedback

#### Scenario B: Multi-Trade / Commercial & Residential Contractor (Multi-Page MPA)
* **Page 1: Homepage (`/`)**:
  - Corporate contractor hero featuring fleet, master technicians, and major commercial projects
  - Dual conversion paths: Residential Homeowners vs. Commercial Property Managers
  - Comprehensive service directory cards linking to dedicated trade pages
  - Lifetime workmanship warranty badge and industry accreditation logos
* **Page 2: Trade Service Pages (`/services/[trade-slug]`)**:
  - Dedicated SEO pages for HVAC, Commercial Plumbing, Electrical Rewiring, Roofing
  - Problem identification diagnostic guide for homeowners/facility managers
  - Equipment brands serviced (Carrier, Trane, Lennox, Kohler)
  - Transparent tiered service packages (Standard Tune-up vs. Complete System Replacement)
* **Page 3: Service Territory & Municipal Hubs (`/service-area/[city]`)**:
  - Localized municipal landing pages optimized for localized search intent
  - Local building code compliance statements and municipal permit handling services
* **Page 4: Instant Project Estimate Calculator (`/estimate`)**:
  - Interactive multi-step estimator: Property square footage, project type, material tier
  - Dynamic estimated cost range with options to schedule on-site verification visit
* **Page 5: Commercial Contracts & Facility Maintenance (`/commercial`)**:
  - Preventative maintenance retainer agreements, SLA response guarantees (e.g., 2-hour SLA)
  - Dedicated commercial account representative intake form

---

### Archetype 3: High-Trust Professional Services (Law, Wealth, Advisory)

#### Scenario A: Boutique Specialist / Solo Advisory Partner (Single-Page SPA)
* **Executive Authority Hero**:
  - Black/slate high-craft palette with executive partner portrait
  - Clear specialization statement (e.g. *"M&A and Cross-Border Tax Counsel for Tech Founders"*)
  - Dispassionate proof metrics: $450M+ Transaction Volume Closed • 22 Years Experience
* **Core Retainer & Advisory Offerings**:
  - 3 structured engagement packages with scope boundaries, deliverable timelines, and fee frameworks
* **Transaction Track Record / Tombstone Gallery**:
  - Anonymized deal summaries, enterprise valuations, and regulatory clearances
* **Partner Biography & Credentials**:
  - Bar admissions, prestigious clerkships, published treatises, speaking appearances
* **Confidential Consultation Intake**:
  - Secure intake form with conflict-of-interest pre-screening questions and NDA checkbox

#### Scenario B: Multi-Partner Corporate Law Firm (Multi-Page MPA)
* **Page 1: Firm Overview (`/`)**:
  - Strategic institutional positioning statement and global reach metrics
  - Practice area taxonomy grid leading into dedicated department pages
  - Recent high-profile regulatory victories and landmark litigation outcomes
  - Institutional thought leadership banner
* **Page 2: Practice Areas (`/practices/[practice-slug]`)**:
  - In-depth legal analysis of current regulatory landscape (e.g., Antitrust, IP Litigation)
  - Representative matters and case studies with legal precedence citations
  - Assigned practice group leaders and cross-functional team bios
* **Page 3: Partner Directory (`/attorneys/[partner-slug]`)**:
  - Comprehensive partner curriculum vitae: Education, Bar Admissions, Court Appearances, Publications
  - Direct vCard download, verified contact information, and assistant liaison
* **Page 4: Case Results & Track Record (`/case-results`)**:
  - Filterable litigation and transactional database by industry, deal size, and jurisdiction
  - Explicit legal ethics disclaimers (*"Past results do not guarantee future outcomes"*)
* **Page 5: Thought Leadership & Legal Insights (`/insights`)**:
  - Whitepapers, client alerts, supreme court brief breakdowns, and podcast episodes
* **Page 6: Office Locations & Consultation (`/contact`)**:
  - Global office directory with security check-in protocols, transit directions, and secure encrypted messaging portal

---

### Archetype 4: Healthcare, Wellness & Medical Practices

#### Scenario A: Solo Wellness Studio / Boutique Aesthetic Clinic (Single-Page SPA)
* **Serene Aesthetic Hero**:
  - Warm neutral, clinical elegance visual tone with ambient interior video
  - Core specialization headline: "Board-Certified Dermatology & Non-Invasive Aesthetics"
  - Primary CTA: `[ Book Initial Consultation ]` with real-time calendar picker
* **Treatment Offerings Grid**:
  - Visual cards with treatment duration, downtime expectations, and target skin/health outcomes
* **Medical Director Credentials**:
  - Medical board certifications, fellowship credentials, hospital affiliations, and philosophy of care
* **Clinical Before & After Visual Slider**:
  - Standardized medical lighting before/after case studies with treatment specifications and patient consent
* **Patient Experience & Clinic Tour**:
  - Photography of state-of-the-art sterile suites, calming recovery lounges, and hygiene standards
* **FAQ & Pre-Treatment Protocols**:
  - Accordion addressing contraindications, preparation instructions, and aftercare

#### Scenario B: Multi-Specialty Clinic / Medical Network (Multi-Page MPA)
* **Page 1: Medical Network Portal (`/`)**:
  - Multi-facility search bar: Find a Doctor by Specialty, Insurance Provider, or Clinic Location
  - Urgent care wait-time counter with real-time triage status
  - Department highlights (Cardiology, Orthopedics, Pediatrics, Oncology)
  - Patient safety accreditations (Joint Commission, Magnet Recognition)
* **Page 2: Clinical Specialties (`/specialties/[specialty-slug]`)**:
  - Comprehensive disease and condition index with clinical treatment pathways
  - Minimally invasive surgical capabilities and diagnostic technology inventory (e.g., 3T MRI)
* **Page 3: Physician Directory (`/doctors/[doctor-slug]`)**:
  - Verified medical license numbers, medical school, residency, board certifications
  - Clinical research papers, accepted insurance plans, and patient satisfaction ratings
  - Direct appointment scheduling integration (Epic MyChart / Cerner / Zocdoc)
* **Page 4: Insurance & Billing Transparency (`/insurance`)**:
  - In-network HMO/PPO provider search tool
  - Good Faith Estimate price transparency sheets complying with healthcare price transparency mandates
* **Page 5: Patient Resource Center & Portal (`/patient-portal`)**:
  - Pre-appointment registration forms, medical record request workflows, telehealth check-in room

---

### Archetype 5: Direct-to-Consumer (D2C) & E-Commerce

#### Scenario A: Catalog Storefront (>50 SKUs) (Multi-Page MPA)
* **Page 1: Storefront Homepage (`/`)**:
  - Hero campaign promoting seasonal collection with lifestyle photography
  - Category navigation cards (Apparel, Footwear, Accessories, Best Sellers)
  - Best-seller product carousel with instant hover quick-view and swatch selectors
  - Social proof UGC Instagram feed with shoppable tags
  - Sustainability and materials transparency badge strip
* **Page 2: Collection Listing Page (`/collections/[category]`)**:
  - Multi-faceted sticky sidebar filters: Price Range, Size, Color Swatch, Material, In-Stock
  - Sort dropdown: Featured, Newest, Price Low-to-High, Customer Rating
  - Infinite scroll or pagination with persistent grid view toggles (2-col vs 4-col)
* **Page 3: Product Detail Page (PDP) (`/products/[product-slug]`)**:
  - High-resolution zoomable image gallery with model measurements and fit guide
  - Live inventory scarcity indicator (*"Only 3 left in Size M"*)
  - Variant pickers with disabled states for out-of-stock sizes
  - One-click express checkout buttons (Shop Pay, Apple Pay, PayPal)
  - Collapsible product specifications: Materials, Care Instructions, Ethical Manufacturing
  - Verified customer reviews with photo uploads and body type metrics
* **Page 4: Interactive Cart Drawer (`/cart`)**:
  - Slide-out side drawer with free shipping progress bar (*"Add $18 for Free Express Shipping"*)
  - Cross-sell bundle recommendations based on cart contents
* **Page 5: Checkout Funnel (`/checkout`)**:
  - Distraction-free one-page or accordion checkout with address autocomplete
  - Guest checkout option (never force mandatory account creation prior to purchase)

#### Scenario B: Revolutionary Single-Product Hero (1 SKU) (Single-Page SPA)
* **Unboxing / Hero Showcase Section**:
  - 360-degree interactive product rotation or high-definition exploding CAD diagram
  - Bold proposition headline, award badges (CES Innovation Award, Red Dot), and direct `[ Buy Now - $199 ]` CTA
* **Engineering Anatomy & Material Deep-Dive**:
  - Micro-zoom hotspots detailing medical-grade titanium casing, custom acoustic drivers, 40-hr battery cell
* **Scientific Benchmark / Comparison Table**:
  - Direct head-to-head comparison chart contrasting the hero product against traditional generic alternatives
* **Influencer & Press Unboxing Carousel**:
  - Embedded short-form video testimonials (MKBHD, Wirecutter, The Verge)
* **Sticky Bottom Conversion Drawer**:
  - Persistent sticky footer showing product thumbnail, quantity selector, price, and instant checkout button

---

### Archetype 6: B2B Software, SaaS & Digital Platforms

#### Scenario A: Enterprise PLG / Multi-Feature SaaS (Multi-Page MPA)
* **Page 1: Platform Homepage (`/`)**:
  - Value proposition hero with interactive product UI sandbox or self-playing interactive video
  - Marquee of Fortune 500 customer logos (SOC2 certified, GDPR ready)
  - Key capability bento grid highlighting developer APIs, enterprise security, and team collaboration
  - Quantified enterprise ROI metrics (*"42% reduction in sprint cycle times"*)
* **Page 2: Feature & Capability Breakdown (`/features/[feature-slug]`)**:
  - Deep-dive into technical architecture, schema diagrams, and workflow automation triggers
  - Before/After efficiency comparison illustrating the platform workflow vs legacy manual work
* **Page 3: Solutions by Industry / Role (`/solutions/[vertical]`)**:
  - Tailored messaging for FinTech, Healthcare, E-Commerce engineering teams
  - Industry-specific compliance badges (HIPAA, PCI-DSS Level 1, ISO 27001)
* **Page 4: Transparent Pricing & ROI Calculator (`/pricing`)**:
  - Monthly vs Annual billing toggle (highlighting 20% annual discount)
  - 3-tier pricing matrix: Starter ($29/mo), Pro ($99/mo), Enterprise (Custom Contact Sales)
  - Feature entitlement comparison matrix with tooltips explaining limits
  - Interactive ROI slider estimating cost savings based on team headcount
* **Page 5: Security, Trust & Compliance (`/security`)**:
  - Live status page embed showing 99.99% uptime history
  - Real-time downloadable SOC2 Type II, ISO 27001 certifications, penetration testing executive summary
* **Page 6: Developer Documentation (`/docs`)**:
  - Multi-language API code snippets (cURL, Python, TypeScript, Go) with sandbox copy buttons
  - Interactive API playground with response schemas

#### Scenario B: Micro-SaaS / Developer Tool / Waitlist (Single-Page SPA)
* **Problem-Agitation Hero**:
  - Terminal-style animated code block demonstrating the command-line pain vs. 1-line solution
  - Email waitlist input with immediate referral queue position generator
* **Live Interactive Demo Playground**:
  - Zero-signup interactive playground running WebAssembly or mock API response in real-time
* **Founder Manifesto & Open-Source Commitment**:
  - GitHub stars badge, roadmap kanban board, and Discord developer community invite
* **Transparent Lifetime / Early-Adopter Pricing**:
  - Single founder lifetime deal card with countdown timer and limited seat availability counter

---

### Archetype 7: Luxury Farmstay, Boutique Resort & Event Grounds

#### Scenario A: Single Private Estate / Farmstay (e.g. Krishi Farms Archetype) (Single-Page SPA)
* **Atmospheric Welcome Hero**:
  - Lush cinematic video hero of rolling estate grounds, organic orchard, and private villa architecture
  - Floating Live Weather / Sunset Tracker (e.g., *"Bidadi, KA • 26°C Sunny • Sunset at 6:18 PM"*)
  - Primary Booking CTA: `[ Check Estate Availability ]`
* **Estate Master Overview & Curated Grounds**:
  - Interactive property layout map highlighting private cottages, swimming pool, organic farm, and campfire lawn
* **Bespoke Accommodations & Villa Specifications**:
  - Card carousel of villa suites detailing king bedding, open-air rainforest showers, private verandas, and guest capacity
* **Farm-to-Table Gastronomy & Agrarian Dining**:
  - Menu story detailing 100% estate-grown vegetables, wood-fired clay oven, and authentic regional culinary heritage
* **Curated Farm Experiences & Activities Bento**:
  - 6-tile bento grid: Organic farming workshops, night stargazing by campfire, tractor estate rides, nature trails
* **Dynamic Stay Rate Calculator & Booking Concierge**:
  - Interactive date range selector, weekend vs. weekday pricing tier calculation, extra guest multiplier
  - Automated deposit calculation and instant `[ Reserve via WhatsApp Concierge ]` dispatch with pre-filled booking details
* **Location & Road Trip Route Guide**:
  - Mile marker transit directions from major highway slip-roads and Bangalore metropolitan center
* **Host Heritage & Sustainable Agrarian Story**:
  - Family heritage chronicle, rainwater harvesting, solar self-sufficiency metrics

#### Scenario B: Multi-Property Luxury Resort Collection (Multi-Page MPA)
* **Page 1: Hospitality Brand Homepage (`/`)**:
  - Global destination portfolio selector (Coastal Villas, Mountain Retreats, Vineyard Sanctuaries)
  - Editorial brand magazine showcasing bespoke concierge experiences and culinary residencies
* **Page 2: Property Deep-Dives (`/properties/[destination-slug]`)**:
  - High-res architectural photography, climate guide, local airport transfer logistics, and estate history
* **Page 3: Weddings & Celebrations (`/weddings-events`)**:
  - Lawn capacities, bridal suite specifications, catering minimums, and preferred vendor directories
  - Interactive 3D floorplan viewer for event planners
* **Page 4: Centralized Booking Engine (`/reserve`)**:
  - Live availability calendar, room add-ons (Spa package, private chef tasting, helicopter charter), secure PCI checkout

---

### Archetype 8: Creative Agencies, Studios & Production Houses

#### Scenario A: Boutique Motion / Design Studio (Single-Page SPA Showcase)
* **Immersive Video Showreel Hero**:
  - Full-viewport ambient 4K showreel with audio mute/unmute control
  - Bold typography statement: "We craft category-defining digital experiences and kinetic brand identities"
* **Selected Work Showcase Grid**:
  - High-impact case study cards featuring video hover previews, client names (Nike, Apple, Spotify), and deliverables
* **Capabilities & Disciplines Marquee**:
  - Kinetic typography ticker: 3D Motion Design • Creative Direction • WebGL Development • Brand Strategy
* **Studio Culture & Leadership**:
  - Candid behind-the-scenes photography of team, awards shelf (Cannes Lions, D&AD, Awwwards), and studio manifesto
* **Project Inquiry & Brief Form**:
  - Interactive project budget slider ($25k, $50k, $100k+), timeline selector, and instant calendar booking link

#### Scenario B: Full-Service Digital Agency (Multi-Page MPA)
* **Page 1: Agency Homepage (`/`)**:
  - Dynamic client case study showcase with quantified commercial impact metrics
  - Services overview leading into dedicated practice area pages
* **Page 2: Deep-Dive Case Studies (`/work/[client-slug]`)**:
  - Full project post-mortem: The Challenge, Strategic Hypothesis, Creative Execution, and Business Impact (e.g. +310% ARR)
  - High-resolution design system artifact embeds, mobile prototypes, and design sprint documentation
* **Page 3: Services & Methodologies (`/capabilities`)**:
  - Detailed agency process breakdown: Discovery Sprint, Brand Positioning, Rapid Prototyping, Production Build
* **Page 4: Team, Leadership & Careers (`/agency`)**:
  - Leadership bios, diversity metrics, open engineering and design roles, and remote work culture guidelines

---

### Archetype 9: Education, Bootcamps & Community Platforms

#### Scenario A: Specialized Cohort Masterclass (Single-Page SPA)
* **Cohort Urgency Hero**:
  - Next cohort start date counter: *"Spring Cohort Begins Oct 12 • 4 Seats Remaining"*
  - Syllabus headline, instructor credentials (ex-Google, ex-Stanford), and `[ Apply for Cohort ]` CTA
* **Curriculum Roadmap & Weekly Sprint Modules**:
  - Accordion breakdown: Week 1 Foundation -> Week 4 Real-World Project -> Week 8 Capstone Pitch to Investors
* **Instructor & Guest Mentor Showcase**:
  - Industry veteran headshots, current corporate roles, and guest office hour schedules
* **Graduate Career Outcomes & Alumni Logos**:
  - Median graduate salary increase metrics (+45%), hiring companies (Amazon, Stripe, Meta)
* **Tuition & Guaranteed Refund Policy**:
  - Upfront tuition vs. monthly installment plans, 14-day 100% money-back guarantee terms

#### Scenario B: Multi-Track Technology Academy (Multi-Page MPA)
* **Page 1: Academy Homepage (`/`)**:
  - Track directory: Software Engineering, Data Science, AI & Machine Learning, UX Design
  - Enterprise corporate upskilling partnerships and government accreditation badges
* **Page 2: Track Curriculum Pages (`/curriculum/[track-slug]`)**:
  - 24-week day-by-day syllabus, prerequisites checklist, software tools mastered, and sample capstone projects
* **Page 3: Career Outcomes & Placement Report (`/outcomes`)**:
  - Audited third-party CIRR employment statistics, placement rates within 180 days, and alumni testimonials
* **Page 4: Tuition, Scholarships & Financing (`/tuition`)**:
  - Income Share Agreements (ISAs), zero-interest loan partners, women-in-tech scholarship applications
* **Page 5: Student Admissions & Application Portal (`/apply`)**:
  - Multi-step technical assessment and admissions interview scheduler

---

### Archetype 10: Industrial, Manufacturing & B2B Supply

#### Scenario A: Custom Job Shop / CNC Machining (Single-Page Fast RFQ SPA)
* **Industrial Capability Hero**:
  - Clean engineering palette with high-speed 5-axis CNC machining video background
  - Tolerance guarantee headline: *"Precision CNC Milling & Turning to ±0.0002 Inches • Quotes in 2 Hours"*
  - Primary CTA: `[ Upload CAD File for Instant RFQ ]`
* **Manufacturing Capabilities Grid**:
  - 4-column matrix: CNC Milling, CNC Turning, Sheet Metal Fabrication, Wire EDM
* **Materials & Finishing Inventory**:
  - Searchable materials table: Aerospace Aluminum, Stainless 316, Titanium Grade 5, PEEK, Delrin
  - Surface finishing options: Anodizing Type II/III, Bead Blasting, Passivation, Powder Coating
* **Facility Equipment Manifest & Inspection Standards**:
  - Exact CNC machine count (Haas VF-4, Mazak Integrex), CMM inspection arms, and ISO 9001:2015 certification badge
* **Rapid CAD Upload & RFQ Form**:
  - Drag-and-drop STEP/IGES/DXF file upload with NDA confirmation and delivery deadline picker

#### Scenario B: Multi-Division Industrial Equipment & OEM Supply (Multi-Page MPA)
* **Page 1: Corporate Manufacturing Portal (`/`)**:
  - Global manufacturing footprint (6 international ISO-certified facilities, 250,000 sq ft)
  - Division links: Heavy Defense Equipment, Medical Diagnostics, Energy & Power Systems
  - Global supply chain resilience statement and sustainability metrics
* **Page 2: Engineering Process & Capabilities (`/capabilities/[process]`)**:
  - Deep-dive into automated robotic welding, vacuum heat treating, and high-volume stamping
  - Engineering design-for-manufacturing (DFM) guidelines and tolerance whitepapers
* **Page 3: Quality Assurance & Testing Lab (`/quality-assurance`)**:
  - Non-Destructive Testing (NDT), X-ray spectrometry, ultrasonic flaw detection, and calibration certificates
* **Page 4: Industry Solutions (`/industries/[industry-slug]`)**:
  - Aerospace (AS9100D), Medical Devices (ISO 13485), Automotive (IATF 16949) compliance documentation
* **Page 5: Request for Proposal / Enterprise RFQ (`/rfq`)**:
  - Multi-part enterprise specification submission portal with export control (ITAR) compliance checks

---

## 3. Mandatory vs. Prohibited Features by Archetype

| Archetype | MUST-HAVE Conversion Features | STRICTLY PROHIBITED Anti-Patterns |
|---|---|---|
| **1. Local Food & Highway Hospitality** | Live Open/Closed indicator, instant WhatsApp order cart, verified Google review rating badge, highway mile-marker directions, mobile click-to-call. | Raw PDF menus requiring download, un-priced generic food stock photos, forced user login before viewing menu. |
| **2. Physical Services & Contractors** | 24/7 hotline click-to-call in sticky header, emergency dispatch territory map, upfront diagnostic pricing, license & insurance badges. | Hiding phone number behind contact form, generic unverified 5-star claims without municipal context. |
| **3. High-Trust Professional Services** | Partner credentials and bar admissions, anonymized transaction/case track record, dispassionate tone, secure consultation intake. | Flashy cartoon animations, fake countdown timers, exaggerated "Get Rich" claims, emoji-filled headlines. |
| **4. Healthcare & Medical Clinics** | Board certification proofs, verified insurance accepted search, online appointment scheduling, clinic sterility tour. | Prescribing medical advice on marketing pages, non-HIPAA compliant open contact text areas. |
| **5. E-Commerce & DTC Retail** | Express 1-click checkout (Shop Pay/Apple Pay), zoomable product gallery, live inventory status, transparent returns policy. | Heavy 3D canvas that lags mobile checkout, mandatory account registration before cart view, hidden shipping costs. |
| **6. B2B Software & SaaS** | Interactive product sandbox/demo video, transparent multi-tier pricing with annual toggle, security compliance badges (SOC2/GDPR). | "Contact Us for Pricing" on entry-level tiers, marketing buzzwords without real UI screenshots, fake client logos. |
| **7. Luxury Farmstays & Resorts** | Dynamic stay rate calculator with weekend tiers, virtual tour/aerial drone video, farm-to-table dining menu, direct WhatsApp concierge. | Static text-only room descriptions without square footage or bedding details, un-priced booking forms. |
| **8. Creative Agencies & Portfolios** | High-definition video showreel, quantifiable commercial client metrics (+% ARR), verified client roster, interactive brief form. | Generic stock agency templates, broken video embeds, autoplay audio without user interaction. |
| **9. Education & Bootcamps** | Week-by-week actionable syllabus, verified instructor credentials, audited graduate placement statistics, money-back guarantee. | Promising guaranteed $200k jobs, hiding tuition costs behind high-pressure sales calls. |
| **10. Industrial & Manufacturing** | Tolerances specifications (±0.0002"), drag-and-drop CAD file upload (STEP/IGES), ISO 9001 certs, machine equipment manifest. | Stock photos of smiling office workers instead of real factory floor machinery, vague "high quality" claims. |

---

## 4. The SPA vs. MPA Architectural Decision Engine

When evaluating any incoming business request, calculate the **Architecture Decision Score (ADS)**:

$$\text{ADS} = \text{Catalog Depth} (1-5) + \text{Search Specificity} (1-5) + \text{Journey Deliberation} (1-5) - \text{Immediacy Need} (1-5)$$

* **ADS $\le 5$ $\rightarrow$ Single-Page Architecture (SPA)**:
  - Examples: Highway restaurant, emergency plumber, boutique farmstay, single-product hero, waitlist.
  - Runtime: Vite + React or Modern HTML5. All sections on one fast, high-converting scroll journey.
* **ADS $\ge 6$ $\rightarrow$ Multi-Page Architecture (MPA)**:
  - Examples: E-commerce catalog (>10 SKUs), multi-specialty clinic, corporate law firm, enterprise SaaS, multi-campus academy.
  - Runtime: Next.js (App Router) or Astro. Dedicated URLs for deep search indexing, distinct intent routing, and analytics funnel isolation.
