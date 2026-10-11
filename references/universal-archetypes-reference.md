# Universal Business Archetype Classification & Feature Matrices

This reference document defines the ten universal commercial and institutional operational archetypes for the `/website-architect` engine. Each archetype is anchored to its **scarce operational resource** — the fundamental operational constraint that dictates all information architecture, conversion funnels, and component requirements.

---

## 1. Master Archetype Matrix

| # | Archetype | Representative Commercial Verticals | Core Revenue Model | Scarce Operational Resource | Dominant User Persona & Arrival State | North-Star Conversion Event (CTA) |
|---|---|---|---|---|---|---|
| **1** | **Local Food & Beverage / Hospitality** | Full-Service Restaurants, Cafes, Highway Rest Stops, Cloud Kitchens, Gastropubs, Bakeries | Per-cover dine-in spend, takeaway margins, delivery ticket volume | **Table turnover rate / Kitchen throughput capacity** | Mobile traveler/commuter seeking immediate food, parking, or clean amenities; local family planning dinner | **WhatsApp Order (Curbside Pickup)** / **Instant Table Reservation** / **Online Cart Checkout** |
| **2** | **Local Physical Services & Trade Contractors** | Emergency Plumbing, HVAC Services, Electrical Contractors, Roofing, Collision Centers, Landscaping | Field service call-out fee, time-and-materials, fixed-bid contracts | **Qualified technician hours / Service van dispatch slots** | Distressed property owner facing emergency (water leak, AC failure) or homeowner seeking quote | **Direct Hotline (Click-to-Call)** / **Emergency Dispatch Request** / **Instant Quote Calculator** |
| **3** | **High-Trust Professional Services** | Corporate Law Firms, CPA & Tax Advisory, Wealth Management, Management Consulting, Architecture | Retainer agreements, billable advisory hours, project milestones | **Billable partner hours / Senior advisor calendar availability** | C-suite executive or private client seeking authoritative expertise with low tolerance for sales fluff | **Scheduled Discovery Consultation (Calendly)** / **RFP Scoping Submission** / **Confidential Case Review** |
| **4** | **Healthcare, Wellness & Medical Practices** | Dental Clinics, Specialist Physicians, Physiotherapy, Med Spas, Mental Health Practices, Gyms | Fee-for-service, private insurance claims, recurring membership dues | **Practitioner appointment slots / Treatment room occupancy** | Patient in physical distress, elective patient researching safety, or individual seeking wellness membership | **HIPAA-Compliant Appointment Booking** / **Patient Portal Access** / **Free Consultation Booking** |
| **5** | **Direct-to-Consumer (D2C) & E-Commerce** | Single-Product Hero Brands, Niche DTC Catalogs, Multi-Brand Retailers, Curated Subscriptions | Product margin × volume, recurring subscription LTV | **SKU inventory velocity / Checkout funnel conversion rate** | Social media impulse buyer, specification researcher, or repeat customer restocking essentials | **Instant Stripe Checkout** / **Slide-Out Add-to-Cart** / **1-Click Bundle Upsell** |
| **6** | **B2B Software, SaaS & Digital Platforms** | Enterprise SaaS, Developer Infrastructure, AI Tooling, API Platforms, B2B Marketplaces | Recurring subscriptions (seat-based, usage-based), platform fees | **Qualified sales pipeline / Trial-to-paid conversion rate** | Technical evaluator (CTO, engineer) inspecting docs or business leader evaluating ROI and compliance | **Self-Service Trial Signup** / **Interactive Product Demo Booking** / **Instant API Key Provisioning** |
| **7** | **Real Estate & Property Developments** | Luxury Developments, Residential Brokerages, Commercial Leasing, Boutique Vacation Rentals | Transaction commissions, capital property sales, nightly booking yield | **Listing inventory velocity / Agent showing bandwidth / Calendar occupancy** | High-intent property investor, homebuyer analyzing floorplans, or vacation traveler booking dates | **Private Property Viewing Request** / **Direct Nightly Booking** / **VIP Floorplan & Spec Download** |
| **8** | **Creative Agencies, Studios & Portfolios** | Brand Strategy Studios, Commercial Production Houses, Freelance Directors, 3D Artists | Project retainers, production day-rates, creative licensing | **Creative director bandwidth / Studio production capacity** | Brand CMO or agency producer scouting elite creative talent and verifying aesthetic alignment | **Project Inquiry Brief Submission** / **Introductory Call Booking** / **Showreel Screen Access** |
| **9** | **Education, Courses & Community Organizations** | Tech Bootcamps, Executive Masterclasses, Private Academies, Non-Profit Foundations, Conferences | Cohort tuition, course sales, donor contributions, event ticketing | **Cohort seat capacity / Instructor hours / Venue ticket allocation** | Career-changer evaluating curriculum, parent assessing school credentials, or conference attendee | **Cohort Application Submission** / **Instant Course Enrollment** / **Event Ticket Checkout** |
| **10** | **Industrial, Manufacturing & B2B Supply** | Precision OEM Suppliers, Custom Metal Fabrication, Contract Packaging, Wholesale Distributors | High-volume supply contracts, wholesale margin, custom fabrication bids | **CNC/Machine shop capacity / Tooling lead times / Minimum order quantity (MOQ)** | Procurement engineer evaluating ISO tolerances, plant manager needing custom parts | **Formal RFQ (Request for Quote) with CAD Upload** / **Sample Kit Request** / **Wholesale Account Application** |

---

## 2. In-Depth Archetype Profiles & Component Specifications

### 2.1 Local Food & Beverage / Hospitality

#### 2.1.1 Highway Express Dining & Takeaway (e.g. Oasis Restaurant Archetype)
- **Customer Arrival Mindset:** Traveler or commuter on the highway seeking immediate sustenance, parking availability, clean restrooms, or express takeaway. Latency tolerance is zero.
- **Speed & Stack Target:** <0.6s FCP on 3G/4G. Recommended Stack: **Modern HTML5 + Vanilla CSS + ES6** (zero build step, instant load).
- **Core Architecture:**
  - Delivery partner aggregator links (Swiggy, Zomato, UberEats) positioned immediately in the hero/quick-actions.
  - Express WhatsApp Takeaway Order generator with slide-out cart bag drawer.
  - Highway quick-action strip: Parking space capacity, clean washrooms indicator, express curbside pickup window.
  - Direct click-to-call phone hotline and 1-tap Google Maps GPS navigation embed.

#### 2.1.2 Destination Dining & Fine Gastronomy
- **Customer Arrival Mindset:** Guests planning a celebratory dinner or business lunch; evaluating culinary ambiance, signature chef credentials, and seating availability.
- **Speed & Stack Target:** <1.4s LCP. Recommended Stack: **Vite + React** or **Next.js**.
- **Core Architecture:**
  - Curated visual menu with ingredient provenance and dietary badges.
  - Interactive table reservation modal with party size and time slot selection.
  - Private dining room (PDR) event inquiry pipeline.

### 2.2 Local Physical Services & Trade Contractors
- **Operational Reality:** Inquiries are often urgent (broken pipe, AC failure in summer) or price-sensitive. Users demand immediate proof of legitimacy and fast technician dispatch.
- **Must-Have Core Features:**
  - Prominent emergency dispatch hotline above the fold with 24/7 availability status.
  - Service territory coverage map or postal code checker.
  - State contractor license number and insurance verification badge.
  - Transparent pricing tiers or diagnostic dispatch fee disclosure.
- **High-Conversion Accelerators:**
  - Instant Job Estimate Calculator: parametric inputs (service type, square footage, urgency) producing a transparent price range.
  - Diagnostic photo/video upload tool allowing homeowners to attach images of the fault.
  - Dual-action CTAs: "Emergency Call Now" (red/high urgency) vs "Schedule Free Inspection" (secondary).
  - Before/after interactive image comparison slider for completed projects.
- **Trust Signals:** State license number, Google Guaranteed badge, BBB accreditation, verified Google/Yelp customer reviews with job type tags.
- **Back-Office Hub:** Field service software (Jobber, ServiceTitan), Twilio call tracking, or instant SMS technician notification.

### 2.3 High-Trust Professional Services
- **Operational Reality:** Client engagements represent significant financial or legal commitments. Visitors are risk-averse and actively scrutinizing partner credentials, precedent cases, and peer recognition.
- **Must-Have Core Features:**
  - Comprehensive partner/advisor biographies with verified academic background, bar/board admissions, and headshots.
  - Detailed practice area pages explaining methodology, legal precedent, and client criteria.
  - Secure, confidential inquiry form with strict privacy disclosures.
  - Direct office locations, phone lines, and calendar booking links.
- **High-Conversion Accelerators:**
  - Interactive Scoping / Settlement / Tax Savings Calculator.
  - Practice-specific consultation booking wizard (routes inquiry to the specialized partner).
  - Client portal preview showing institutional security and communication standards.
  - Gated whitepapers, executive briefings, and regulatory impact analyses.
- **Trust Signals:** Chambers & Partners / Legal 500 / Super Lawyers badges, State Bar / CPA license verification, representative case results, corporate client logos.
- **Back-Office Hub:** Clio, HubSpot, Salesforce CRM, or encrypted DMS (NetDocuments).

### 2.4 Healthcare, Wellness & Medical Practices
- **Operational Reality:** Patients balance vulnerability with high skepticism regarding physician competence, insurance coverage, and facility hygiene.
- **Must-Have Core Features:**
  - HIPAA-compliant appointment scheduling and contact forms.
  - Comprehensive accepted insurance provider directory with search/filter.
  - Physician credentials, board certifications, and clinical specialty breakdowns.
  - Location access instructions including parking, ADA accessibility, and public transit links.
- **High-Conversion Accelerators:**
  - Multi-step appointment booking wizard: Specialty → Provider → Date/Time → Insurance → Confirmation.
  - Symptom-to-specialist triage selector.
  - Telehealth virtual consultation scheduling module.
  - Digital new-patient intake form download or online completion portal.
- **Trust Signals:** Board certification logos, hospital affiliations, patient reviews (compliant with healthcare privacy standards), sanitization/safety protocols.
- **Back-Office Hub:** EHR/EMR platforms (Epic, Cerner, Dentrix), HIPAA-compliant messaging services (Klara).

### 2.5 Direct-to-Consumer (D2C) & E-Commerce
- **Operational Reality:** Success depends on minimizing checkout friction, maximizing Average Order Value (AOV), and accelerating SKU inventory velocity.
- **Must-Have Core Features:**
  - High-velocity product catalog with instant faceted search, tag filtering, and sorting.
  - Rich Product Detail Pages (PDP) with multi-angle photography, video demos, and specifications.
  - Persistent shopping cart drawer with live subtotal and free-shipping progress meter.
  - Frictionless checkout supporting Apple Pay, Google Pay, UPI, and credit cards.
- **High-Conversion Accelerators:**
  - 1-Click Post-Purchase Upsell / Bundle Builder ("Complete the look" or "Add protection plan").
  - Interactive Shade Finder / Size Predictor Quiz reducing return rates.
  - Postal code delivery date estimator directly on the PDP.
  - Real-time inventory urgency counter ("Only 3 left in stock").
- **Trust Signals:** Verified buyer review badges with customer-uploaded photos, payment provider trust marks (Visa, Mastercard, Stripe, PayPal), 30-day money-back guarantee seal.
- **Back-Office Hub:** Shopify, WooCommerce, Stripe Payments, Klaviyo marketing automation, ShipStation.

### 2.6 B2B Software, SaaS & Digital Platforms
- **Operational Reality:** Must simultaneously convince two distinct personas: the technical practitioner evaluating developer ergonomics and the executive buyer evaluating business ROI and compliance.
- **Must-Have Core Features:**
  - Feature taxonomy grouped by business outcome or persona capability.
  - Transparent pricing page with Monthly/Annual billing toggle, feature comparison matrix, and FAQ.
  - Self-service free trial signup or guided product demonstration booking.
  - Security, compliance, and uptime status transparency (SOC 2, GDPR, ISO 27001).
- **High-Conversion Accelerators:**
  - Interactive ROI / Cost-Savings Calculator based on team size and current tooling spend.
  - Interactive sandboxed product tour or embedded Loom product walkthrough.
  - Direct API documentation and code snippet switcher (cURL, Python, TypeScript, Go).
  - Competitor comparison landing pages ("Why [Product] vs [Competitor]").
- **Trust Signals:** SOC 2 Type II badge, enterprise client logo marquee, G2 / Capterra badges, live uptime monitor link (99.99%).
- **Back-Office Hub:** Salesforce, HubSpot, Stripe Billing, Segment, Vitally customer success.

### 2.7 Real Estate, Luxury Hospitality & Destination Grounds

#### 2.7.1 Luxury Farmstays, Private Villa Resorts & Destination Event Grounds (e.g. Krishi Farms Archetype)
- **Customer Arrival Mindset:** High-intent guests planning an expensive weekend getaway, destination wedding, family celebration, or corporate offsite ($300 to $5,000+ booking value). High dwell time; visitors demand sensory desire, visual reassurance of ambiance, and transparent date/guest pricing.
- **Recommended Modality:** **Hybrid Interactive / Scrollytelling Website** (Cinematic virtual tour scrubber + clean, accessible utility booking and pricing sections).
- **Recommended Stack:** **Vite + React (TypeScript) + Tailwind CSS** (rich client state for dynamic rate calculations, 60fps canvas virtual tour scrubbing, zero SSR hydration mismatches, fast static CDN deployment).
- **Core Architecture:**
  - 5-Stop Virtual Grounds Tour (Private Swimming Pool, 5+ Acre Celebration Lawn, Traditional Wedding Mandap, Illuminated Night Farmhouse, Luxury AC Bedroom Suite).
  - Dynamic Stay & Event Rate Calculator: Real-time price calculation updating as guest count changes (e.g., ₹950/head Day Outing vs. ₹18,000 Overnight Villa vs. Destination Wedding).
  - Direct WhatsApp Date Reservation: Pre-formats package, date, guest count, and customer contact into an instant 1-tap WhatsApp booking message.
  - Highway route embed from major metro junctions (e.g. Kanakapura Road from Bangalore).

#### 2.7.2 Residential Brokerages & Commercial Property Developments
- **Customer Arrival Mindset:** High-value property investors and homebuyers analyzing floorplans, square footage, neighborhood amenities, and financing options.
- **Recommended Stack:** **Next.js (App Router / SSR)** for deep listing SEO or **Vite + React**.
- **Core Architecture:**
  - Interactive Matterport 3D virtual tour embed or aerial drone video.
  - Mortgage / Monthly Payment Calculator with interest rate and down payment sliders.
  - Gated VIP Floorplan & Development Investor Deck download form.

### 2.8 Creative Agencies, Studios & Portfolios
- **Operational Reality:** Evaluated primarily on visual craft, taste, and proof of tier-one client execution. Typography and motion must reflect world-class aesthetic standards.
- **Must-Have Core Features:**
  - Full-screen project case studies with visual showreels, client objectives, and measurable deliverables.
  - Core service capabilities breakdown (Brand Identity, Web Development, Film Production).
  - Transparent project inquiry form capturing timeline, budget tier, and scope.
  - Studio leadership team bios and award recognitions.
- **High-Conversion Accelerators:**
  - Asymmetric, editorial bento grids and smooth micro-interactions.
  - Interactive video showreel modal with zero loading latency.
  - Client roster marquee with interactive project previews on hover.
- **Trust Signals:** Industry awards (Awwwards, Cannes Lions, D&AD, FWA), tier-one client logos, press features.
- **Back-Office Hub:** Notion client pipeline, HubSpot, direct email dispatch.

### 2.9 Education, Courses & Community Organizations
- **Operational Reality:** Prospects require proof of career transformation, curriculum rigor, and community support before committing time and tuition.
- **Must-Have Core Features:**
  - Detailed syllabus and module breakdown with learning outcomes and project deliverables.
  - Instructor credentials and industry background.
  - Cohort calendar with upcoming start dates, application deadlines, and tuition pricing.
  - Formal student application or enrollment checkout module.
- **High-Conversion Accelerators:**
  - Instant Syllabus Download Form with automated email nurturing.
  - Interactive Graduate Outcome & Salary Growth Calculator.
  - Free sample lesson video or interactive code challenge.
  - Student alumni video testimonials and hiring company logo marquee.
- **Trust Signals:** Accreditation badges, CIRR-verified employment statistics, alumni LinkedIn placement links.
- **Back-Office Hub:** Teachable, Kajabi, Thinkific, Stripe, Airtable admissions CRM.

### 2.10 Industrial, Manufacturing & B2B Supply
- **Operational Reality:** Buyers are technical procurement managers and engineers seeking exact technical tolerances, compliance standards, and reliable lead times.
- **Must-Have Core Features:**
  - Parametric product catalog with searchable technical specification tables and tolerance charts.
  - Material capabilities directory (CNC aluminum, injection molding, sheet metal).
  - Formal Request for Quote (RFQ) module with CAD/STEP file upload.
  - Facility machinery inventory and manufacturing certifications (ISO 9001, AS9100).
- **High-Conversion Accelerators:**
  - Instant CAD File Analysis & Preliminary Pricing Calculator.
  - Free Material Sample Kit Request Form.
  - Downloadable engineering spec sheets, 2D technical drawings, and compliance certificates.
- **Trust Signals:** ISO 9001 / AS9100 / IATF 16949 certification badges, ITAR registration, enterprise defense/aerospace client logos.
- **Back-Office Hub:** ERP/MES systems (SAP, NetSuite), Paperless Parts, secure engineering file storage.
