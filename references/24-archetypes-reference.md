# Enterprise Architecture Reference for 24 Operating Models

This reference provides the technical, operational, and data-consistency baseline across the 8 Commercial Macro-Archetypes and 24 Operating Sub-Types.

---

## The 3 Data Consistency Tiers

* **Tier A — Strict Transactional Authority (ACID / Row-Level Locks):**
  * *Applies to:* Money movement, ledger balances, unique serialized inventory, appointment slot reservations, lease execution, contract signing, clinical records.
  * *Mechanisms:* PostgreSQL `SELECT ... FOR UPDATE`, atomic Redis locks with TTL, idempotency keys on mutating endpoints, transactional outbox pattern.
* **Tier B — Bounded Staleness (Brief Cache + Revalidation):**
  * *Applies to:* Catalog browsing prices, day-level appointment availability previews, account usage totals, estimated delivery dates.
  * *Mechanisms:* Edge caching with short TTLs (10–60s); mandatory revalidation against Tier A prior to checkout or commitment.
* **Tier C — Eventual Consistency (Global Edge & Search Indexes):**
  * *Applies to:* Editorial content, marketing copy, search indexes (Algolia/Elasticsearch), customer reviews, case studies, public documentation.
  * *Mechanisms:* Static Site Generation (SSG), global CDN edge caching, asynchronous background index updates.

---

## Macro-Archetype 1: Direct Transactional & Commerce
*Core Mandate: Own salable inventory, pricing, order/return states, customer identity, and post-purchase economics.*

### C1: D2C Replenishment Retail
* **Canonical Page Scope:** 14 MVP / 2,500 Mature Scale.
* **Scarce Resource:** Salable warehouse stock, promotional pricing, subscription state.
* **North-Star CTA:** "Add to Cart" / "Subscribe Now" (Instant 1-Click Checkout).
* **Critical Engine:** Variant/bundle selector, recurring delivery cadence picker, slide-out dynamic cart, address autocomplete.
* **Data Consistency:** Tier A for stock decrement and payments; Tier C for catalog browsing.
* **Integrations:** Headless commerce engine (Shopify Plus, Commercetools), ERP/WMS (NetSuite, ShipBob), Stripe/Payment Gateways, Klaviyo.
* **Failure Modes:** Overselling from non-atomic stock holds during flash sales; hiding subscription recurring renewal terms.

### C2: Curated Luxury & Artisanal Commerce
* **Canonical Page Scope:** 16 MVP / 900 Mature Scale.
* **Scarce Resource:** Serialized one-of-a-kind (1-of-1) pieces, bespoke maker hours.
* **North-Star CTA:** "Request Private Viewing" / "Reserve This Piece".
* **Critical Engine:** High-resolution zoom viewer, serialized temporary reservation hold, concierge inquiry drawer, provenance verifier.
* **Data Consistency:** Strict row-level lock on unique piece availability; Tier C for editorial provenance stories.
* **Integrations:** Specialized luxury OMS, CRM, private bank transfer/escrow APIs, digital certificate of authenticity registries.
* **Failure Modes:** Selling the same serialized item twice across showroom POS and website; applying cheap discount-store countdown urgency timers.

### C3: Multi-Vendor Marketplace
* **Canonical Page Scope:** 22 MVP / 100,000+ Mature Scale.
* **Scarce Resource:** Multi-seller catalog synchronization, platform buyer trust, escrow fund state.
* **North-Star CTA:** "Secure Order" / "Start Selling".
* **Critical Engine:** Vendor KYB/KYC verification, split-order cart checkout, escrow payout engine, automated dispute handling.
* **Data Consistency:** ACID double-entry ledger for wallet/escrow balances; eventual consistency for global search indexes.
* **Integrations:** Stripe Connect / marketplace payouts, automated sales tax (Avalara/TaxJar), identity verification, shipping rate APIs.
* **Failure Modes:** Ledger and payout calculation drift; blending buyer and seller permission boundaries in the database.

---

## Macro-Archetype 2: Capacity & Asset-Constrained Services
*Core Mandate: Prevent double-booking and encode duration, buffers, deposits, and cancellation rules.*

### S1: Urgent Care / Diagnostic Clinic
* **Canonical Page Scope:** 15 MVP / 220 Mature Scale.
* **Scarce Resource:** Clinician hours, diagnostic room availability, triage priority.
* **North-Star CTA:** "Book Urgent Visit" / "Check Live Wait Times".
* **Critical Engine:** Symptom triage filter, real-time availability slot picker with pessimistic database locking, EHR calendar synchronization.
* **Data Consistency:** Row lock on appointment slots; strict zero-trust object authorization for medical records.
* **Integrations:** Practice Management / EHR (Epic, Cerner, AthenaHealth), HIPAA-compliant messaging, Twilio SMS.
* **Failure Modes:** Firing third-party marketing tracking pixels on intake forms (HIPAA violation); double-booking clinicians due to cache lag.

### S2: Exclusive Event Venue
* **Canonical Page Scope:** 18 MVP / 180 Mature Scale.
* **Scarce Resource:** Physical ballroom/grounds capacity, date availability, event turnover hours.
* **North-Star CTA:** "Check Date Availability" / "Schedule Venue Tour".
* **Critical Engine:** Date/space composite uniqueness lock, interactive floorplan capacity calculator, proposal generator, multi-stage deposit schedule.
* **Data Consistency:** Composite date-space unique locks; eventual consistency for photo galleries.
* **Integrations:** Venue CRM, Google/Outlook Calendar APIs, DocuSign / e-signature, Stripe deposit hold engine.
* **Failure Modes:** Allowing instant bookings without mandatory cleaning/turnaround buffers; CRM and public calendar maintaining separate date states.

### S3: Heavy-Machinery & Equipment Rental Hub
* **Canonical Page Scope:** 20 MVP / 12,000 Mature Scale.
* **Scarce Resource:** Serialized machinery fleet, transport trailers, delivery logistics capacity.
* **North-Star CTA:** "Reserve Fleet Asset" / "Request Rental Quote".
* **Critical Engine:** Equipment spec filter, serialized branch fleet allocator, jobsite freight delivery calculator, damage waiver e-sign.
* **Data Consistency:** Range/row locking on serialized equipment IDs; distributed saga across inter-branch transfers.
* **Integrations:** Rental ERP, telematics/GPS fleet tracking, carrier routing APIs, credit verification bureaus.
* **Failure Modes:** Treating serialized heavy machinery as fungible retail SKUs; quoting deliveries without validating jobsite dimensional clearances.

---

## Macro-Archetype 3: High-Trust Advisory & Consulting
*Core Mandate: Establish domain authority before capture, route sensitive matters, and protect confidentiality.*

### A1: Corporate Law Firm
* **Canonical Page Scope:** 16 MVP / 650 Mature Scale.
* **Scarce Resource:** Partner billable capacity, conflict clearance status, attorney-client privilege.
* **North-Star CTA:** "Schedule Confidential Consultation" / "Submit Matter Inquiry".
* **Critical Engine:** Partner directory with credential filtering, guarded intake questionnaire with automated conflict-of-interest checks.
* **Data Consistency:** Strict matter-level Access Control Lists (ACL) and immutable audit logging; Tier C for legal whitepapers.
* **Integrations:** Legal Practice Management (Clio, MyCase), Enterprise CRM (Salesforce Financial Services Cloud), secure client document vaults.
* **Failure Modes:** Soliciting confidential matter narratives before running an automated conflict check; displaying consumer-grade chat popups.

### A2: Wealth Management & Private Capital Advisory
* **Canonical Page Scope:** 18 MVP / 350 Mature Scale.
* **Scarce Resource:** Fiduciary advisory capacity, mandate suitability, investor capital allocation.
* **North-Star CTA:** "Request Confidential Consultation" / "Access Investor Portal".
* **Critical Engine:** Investor suitability sequence, accreditation verification check, phishing-resistant MFA client vault.
* **Data Consistency:** ACID ledgers for capital reporting; strict immutable access audit trails.
* **Integrations:** Portfolio accounting systems, institutional custodians (Schwab, Fidelity), KYC/AML screening engines, Box Governance.
* **Failure Modes:** Collecting unencrypted net worth or tax data on public marketing forms; sending wire instructions over standard email.

### A3: Specialized Medical Practice / Surgery Center
* **Canonical Page Scope:** 17 MVP / 300 Mature Scale.
* **Scarce Resource:** Specialized surgical theater time, multidisciplinary physician evaluation hours.
* **North-Star CTA:** "Request Specialist Consultation" / "Submit Physician Referral".
* **Critical Engine:** Condition-to-specialist routing engine, secure medical records & DICOM image upload portal, referral intake tracker.
* **Data Consistency:** Strict clinical record states; regulated diagnostic image transfer logs.
* **Integrations:** Hospital EHR/PACS systems via FHIR/HL7 interfaces, secure patient portals, encrypted cloud storage (AWS S3 with BAA).
* **Failure Modes:** Storing medical imaging in public CMS asset libraries; confusing educational content with individualized medical advice.

---

## Macro-Archetype 4: Industrial, Supply Chain & B2B Distribution
*Core Mandate: Support custom RFQ/CPQ, contract pricing, lot traceability, and enterprise ERP truth.*

### B1: Raw-Material Supplier
* **Canonical Page Scope:** 18 MVP / 15,000 Mature Scale.
* **Scarce Resource:** Manufacturing run capacity, chemical/alloy lot compliance, bulk inventory.
* **North-Star CTA:** "Request Material Sample" / "Submit Volume RFQ".
* **Critical Engine:** Parametric property/grade filter, Certificate of Analysis (CoA) search by lot number, technical data sheet (TDS/SDS) library.
* **Data Consistency:** Versioned master specification data; immutable lot traceability.
* **Integrations:** Enterprise ERP (SAP, Oracle), LIMS (Laboratory Information Management System), CRM/CPQ, freight calculation APIs.
* **Failure Modes:** Publishing superseded SDS/TDS documents with outdated safety ratings; performing engineering unit conversions only in client-side JavaScript.

### B2: Contract Manufacturer / Custom Fabrication
* **Canonical Page Scope:** 17 MVP / 500 Mature Scale.
* **Scarce Resource:** Machine tooling envelopes, factory capacity, engineering quoting hours.
* **North-Star CTA:** "Upload CAD for Quoting" / "Prequalify Manufacturing Run".
* **Critical Engine:** NDA gatekeeper, 2 GB multipart CAD/BOM uploader, automated Design for Manufacturability (DFM) analyzer, revision manager.
* **Data Consistency:** Immutable file revision hashes; Attribute-Based Access Control (ABAC) on proprietary client drawings.
* **Integrations:** CAD viewing engines, ERP/MES (Manufacturing Execution Systems), CPQ pricing engines, secure cloud file vaults.
* **Failure Modes:** Distributing unversioned CAD drawings; emailing sensitive engineering blueprints through unprotected SMTP mail.

### B3: MRO Wholesale Distributor
* **Canonical Page Scope:** 20 MVP / 250,000+ Mature Scale.
* **Scarce Resource:** Regional warehouse distribution stock, contracted buyer credit lines.
* **North-Star CTA:** "Submit Purchase Order" / "Request Contract Pricing".
* **Critical Engine:** Exact MPN/SKU search, bulk CSV order entry matrix, customer-specific contract pricing engine, cXML PunchOut gateway.
* **Data Consistency:** Real-time ERP stock and pricing verification at checkout commit; eventual consistency for catalog search.
* **Integrations:** ERP (SAP S/4HANA, NetSuite), PunchOut gateways (TradeCentric, Coupa, Ariba), EDI (850/855/810), Net-30 credit engines.
* **Failure Modes:** Forcing wholesale procurement buyers through consumer-style 1-item checkouts; exposing retail list prices to authenticated enterprise buyers.

---

## Macro-Archetype 5: Product-Led Software & Digital Infrastructure
*Core Mandate: Join user acquisition, activation, billing, documentation, and product telemetry into one lifecycle.*

### P1: Developer API Platform
* **Canonical Page Scope:** 15 MVP / 2,000 Mature Scale.
* **Scarce Resource:** Server infrastructure capacity, API rate limits, compute quotas.
* **North-Star CTA:** "Get API Key" / "Read Documentation".
* **Critical Engine:** Interactive API sandbox/playground, scoped API key generator, append-only usage metering console, interactive documentation.
* **Data Consistency:** Scoped token authorization; append-only time-series usage ledgers (ClickHouse/TimescaleDB).
* **Integrations:** API Gateways (Kong, Envoy), Stripe Billing / metered usage webhooks, Auth0/OIDC, telemetry pipelines.
* **Failure Modes:** Calculating customer invoices from sampled marketing telemetry; binding API keys to individual employee emails rather than organization tenants.

### P2: Enterprise B2B SaaS
* **Canonical Page Scope:** 18 MVP / 700 Mature Scale.
* **Scarce Resource:** Workspace tenant instances, user seat entitlements, enterprise licensing limits.
* **North-Star CTA:** "Start Free Trial" / "Book Enterprise Demo".
* **Critical Engine:** Self-serve tenant provisioner, SAML 2.0 / SSO configuration wizard, SCIM user directory sync, role-based access control (RBAC).
* **Data Consistency:** Strict multi-tenant isolation via PostgreSQL Row-Level Security (RLS); eventual consistency for aggregated reporting.
* **Integrations:** Enterprise IdPs (Okta, Azure AD), Stripe/Paddle subscription engines, CRM (HubSpot, Salesforce), PostHog/Segment.
* **Failure Modes:** Blending public marketing CMS sessions with authenticated tenant state; allowing cross-tenant data leakage via un-scoped SQL queries.

### P3: Consumer Digital Service / App Portal
* **Canonical Page Scope:** 12 MVP / 300 Mature Scale.
* **Scarce Resource:** Subscriber access entitlements, active device sessions.
* **North-Star CTA:** "Download App" / "Start Free Membership".
* **Critical Engine:** Passwordless magic-link/social auth, web-to-app deep-linking handler, store receipt validator, self-service cancellation desk.
* **Data Consistency:** Canonical user account identity; idempotent subscription entitlement ledger.
* **Integrations:** Apple App Store / Google Play billing webhooks, Stripe, push notification relays (Firebase), customer support desks.
* **Failure Modes:** Maintaining separate subscription entitlement truth between web and native mobile apps; enforcing complex password walls before demonstrating value.

---

## Macro-Archetype 6: Knowledge, Media & Creator Academies
*Core Mandate: Monetize audience attention, protect intellectual property, and track learning progress.*

### K1: Digital Publication & Media Brand
* **Canonical Page Scope:** 14 MVP / 100,000+ Mature Scale.
* **Scarce Resource:** Editorial attention, premium subscriber article archive.
* **North-Star CTA:** "Subscribe for Full Access" / "Join Free Newsletter".
* **Critical Engine:** Edge-metered paywall worker (Cloudflare/Vercel Edge), newsletter preference center, lightweight distraction-free reader mode.
* **Data Consistency:** Strong edge JWT entitlement checks; Tier C global edge caching for public articles.
* **Integrations:** Ghost / Headless CMS, Stripe / Memberful subscriptions, email distribution engines (ConvertKit, Beehiiv).
* **Failure Modes:** Enforcing client-side paywalls that can be bypassed by disabling JavaScript or using browser Inspect Element; running heavy ad scripts that destroy Core Web Vitals.

### K2: Cohort-Course Academy
* **Canonical Page Scope:** 17 MVP / 600 Mature Scale.
* **Scarce Resource:** Live cohort seats, mentor grading capacity, workshop time slots.
* **North-Star CTA:** "Apply for Cohort" / "Enroll Now".
* **Critical Engine:** Admissions application workflow, cohort-seat reservation ledger, LMS lesson progression tracker, assignment submission desk.
* **Data Consistency:** ACID cohort-seat reservation ledger; atomic enrollment confirmation.
* **Integrations:** Video conferencing APIs (Zoom), LMS platforms, Stripe payment plans, Discord/Circle community webhooks.
* **Failure Modes:** Oversubscribing cohort capacity beyond mentor grading bandwidth; using evergreen self-paced video UI patterns for synchronous live cohorts.

### K3: Independent Creator & Research Syndicate
* **Canonical Page Scope:** 13 MVP / 2,000 Mature Scale.
* **Scarce Resource:** Proprietary research reports, specialized advisory access.
* **North-Star CTA:** "Become a Member" / "Download Research Brief".
* **Critical Engine:** Tiered membership paywall, expiring signed download URLs, automated watermarked PDF generator.
* **Data Consistency:** Tier entitlement validation; Tier C caching for public editorial content.
* **Integrations:** Stripe recurring billing, private podcast RSS generation, cloud storage (AWS S3 signed URLs), community platforms.
* **Failure Modes:** Providing un-expiring public download links to premium research PDFs; locking all research samples behind an opaque paywall without proving credibility.

---

## Macro-Archetype 7: Asset-Heavy & Real Estate Operations
*Core Mandate: Present verified property inventory, qualify leads, and manage tenant operations.*

### R1: Residential Brokerage / Property Portal
* **Canonical Page Scope:** 18 MVP / 50,000+ Mature Scale.
* **Scarce Resource:** Verified property listings, licensed agent response time.
* **North-Star CTA:** "Schedule Property Tour" / "Request Home Valuation".
* **Critical Engine:** Geospatial map search, automated MLS/IDX feed normalizer, tour scheduling picker, agent routing engine.
* **Data Consistency:** MLS feed-authoritative listing state; pessimistic locking on tour time slots.
* **Integrations:** MLS/RETS/RESO Web API feeds, Google Maps API, Real Estate CRM (Follow Up Boss), DocuSign.
* **Failure Modes:** Displaying sold or off-market listings as active inventory; silently distributing a single buyer lead to competing agents.

### R2: Commercial Property Management Portal
* **Canonical Page Scope:** 16 MVP / 4,000 Mature Scale.
* **Scarce Resource:** Leasable commercial square footage, facility maintenance staff hours, rent ledger state.
* **North-Star CTA:** "Submit Work Order" / "View Available Suites".
* **Critical Engine:** Tenant/owner portal, emergency maintenance triage engine, lease document vault, CAM/rent invoice ledger.
* **Data Consistency:** Property-scoped tenant access controls; strict double-entry accounting for rent and common-area maintenance (CAM).
* **Integrations:** Property management accounting (Yardi, AppFolio), CMMS maintenance systems, building access control APIs.
* **Failure Modes:** Routing emergency life-safety repairs (e.g., gas leaks, structural flooding) into general non-urgent maintenance queues; cross-tenant document exposure.

### R3: Coworking & Flexible Workspace
* **Canonical Page Scope:** 17 MVP / 1,500 Mature Scale.
* **Scarce Resource:** Desk/office capacity, meeting room calendar hours, building physical access credentials.
* **North-Star CTA:** "Book Day Pass" / "Reserve Meeting Room".
* **Critical Engine:** Real-time meeting room calendar lock, monthly membership credit ledger, rotating digital door access pass generator.
* **Data Consistency:** ACID room reservation locks; real-time physical access credential synchronization and instant revocation.
* **Integrations:** Coworking software (OfficeRnD, Nexudus), IoT door access controllers (Kisi, Brivo), Stripe billing.
* **Failure Modes:** Allowing web calendar bookings without synchronizing with physical room access systems; issuing static unrevocable QR codes for building doors.

---

## Macro-Archetype 8: Field Services & Local Contracting
*Core Mandate: Triage urgency, verify territory, dispatch certified crews, and maintain job records.*

### F1: Emergency Trades (HVAC, Plumbing, Electrical)
* **Canonical Page Scope:** 14 MVP / 1,200 Mature Scale.
* **Scarce Resource:** On-call technician hours, truck parts inventory, geofenced dispatch territory.
* **North-Star CTA:** "Request Emergency Dispatch" / "Call Now".
* **Critical Engine:** Geofenced territory validator, life-safety symptom triage filter, live technician ETA tracking link.
* **Data Consistency:** Atomic crew assignment; idempotent dispatch ingestion from web forms.
* **Integrations:** Field Service Management (ServiceTitan, Housecall Pro), Twilio programmable voice/SMS, Google Maps Geocoding API.
* **Failure Modes:** Promising arrival windows during severe weather without checking live crew availability; presenting lengthy 10-field forms during water/gas emergencies.

### F2: Commercial Construction Contractor
* **Canonical Page Scope:** 16 MVP / 800 Mature Scale.
* **Scarce Resource:** Corporate bonding capacity, project manager bandwidth, qualified subcontractor trades.
* **North-Star CTA:** "Submit Project Opportunity" / "Access Subcontractor Bid Room".
* **Critical Engine:** Subcontractor prequalification intake, permissioned digital bid room, 5 GB drawing/addenda uploader, bonded project showcase.
* **Data Consistency:** Immutable bid submission timestamps and file hashes; strict bid deadline locking.
* **Integrations:** Construction management platforms (Procore, Autodesk Construction Cloud), e-signature engines, secure file storage.
* **Failure Modes:** Accepting official subcontractor bids via unauthenticated email; distributing outdated drawing revisions without addenda tracking.

### F3: Industrial Maintenance & Reliability Provider
* **Canonical Page Scope:** 18 MVP / 3,500 Mature Scale.
* **Scarce Resource:** Certified reliability engineers, vibration/oil diagnostic tools, SLA response windows.
* **North-Star CTA:** "Request Plant Assessment" / "Log 24/7 SLA Service Call".
* **Critical Engine:** Plant asset hierarchy registry, IoT condition-monitoring telemetry stream, technician skill-matching filter, SLA timer.
* **Data Consistency:** Strong asset and work-order state machines; streaming sensor telemetry data ingestion.
* **Integrations:** Enterprise Asset Management (IBM Maximo, SAP PM), IoT gateways, time-series databases, customer SLA portals.
* **Failure Modes:** Exposing real-time industrial plant telemetry on public CMS pages; allowing offline field app updates to overwrite newer database records.
