#!/usr/bin/env python3
"""
Autonomous Business Classifier & Requirements Engine for Website Architect.
Decomposes either a Google Maps URL, scraped maps_data.json, or raw business pitch
into the exact commercial archetype, ADS score, and complete 'Needed Things' specification.
"""

import os
import re
import sys
import json
import argparse
import urllib.parse

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Comprehensive 10-Archetype Knowledge Base with 24 Sub-Types
ARCHETYPES_DB = {
    "hospitality_resort": {
        "id": 1,
        "archetype": "Local Food & Beverage / Hospitality",
        "sub_type": "Luxury Farmstay, Resort & Destination Event Grounds",
        "keywords": ["farmstay", "resort", "hotel", "retreat", "cottage", "villa", "homestay", "farmhouse", "glamping", "estate", "destination", "event grounds"],
        "revenue_model": "Per-night cottage/villa stay, weekend event buyouts, experiential farm/culinary tours",
        "scarce_resource": "Weekend calendar dates & private cottage booking slots",
        "customer_mindset": "High-Ticket Experiential Deliberator (planning family celebration, luxury getaway; high sensory scrutiny)",
        "target_lcp": "< 1.2s",
        "target_cls": "< 0.02",
        "ads_components": {"catalog": 2, "search": 1, "deliberation": 5, "immediacy": 4},
        "modality": "Modality 2: Hybrid Interactive / Scrollytelling",
        "specialist_skill": "soft-skill (High-End Visual Design: Warm Editorial)",
        "spatial_geometry": "Full-Bleed Viewport Media + Editorial Minimalist Cadence (Grounded in Reference)",
        "palette": {
            "background": "#FAF8F5",
            "foreground": "#1A1816",
            "accent": "#8B6F4E",
            "secondary": "#2D3B2D",
            "surface": "#F2EFE9"
        },
        "typography": {"display": "Cormorant Garamond (Serif)", "body": "Plus Jakarta Sans (Sans-Serif)"},
        "sections": [
            {"id": "1.0", "title": "Signature Hero", "type": "Hero", "description": "Ambient 60fps looping grounds video with headline, luxury badge, and check-in date scrubber"},
            {"id": "2.0", "title": "Estate & Grounds Ambiance", "type": "Editorial Story", "description": "Doppelrand nested photography showcasing organic acres, pool, and sunset lawn"},
            {"id": "3.0", "title": "Interactive Stay Rate Calculator", "type": "Interactive Module", "description": "Dynamic guest slider x nights picker x cottage tier with live total and instant WhatsApp payload"},
            {"id": "4.0", "title": "Accommodations & Luxury Suites", "type": "Tabbed Catalog", "description": "Curated cottage cards with square footage, bed configuration, private deck, and amenity pills"},
            {"id": "5.0", "title": "Farm-to-Table Gastronomy & Coffee Estate", "type": "Sensory Grid", "description": "Culinary heritage, estate-grown coffee tasting, organic garden harvests"},
            {"id": "6.0", "title": "Verified Guest Reviews & Social Proof", "type": "Trust Strip", "description": "Verified Google Maps 4.6+ star quotes and celebration photo carousel"},
            {"id": "7.0", "title": "Estate Directions & Route Navigation", "type": "Map Embed", "description": "1-tap Google Maps GPS navigation, road advisory, nearby landmarks"},
            {"id": "8.0", "title": "Instant Concierge WhatsApp Reservation", "type": "Modal / CTA", "description": "Structured zero-commission direct WhatsApp dispatch modal with pre-filled guest details"}
        ],
        "interactive_modules": [
            "Real-time stay rate calculator with guest slider ($Rate = Base x Guests x Nights)",
            "Direct zero-commission structured WhatsApp reservation generator",
            "60fps ambient grounds video scrubber / carousel",
            "Interactive FAQ accordion with keyboard focus management"
        ],
        "north_star_cta": "Direct Structured WhatsApp Reservation",
        "whatsapp_template": "Hi {business_name}, I want to reserve a stay at your property. Guests: [X] adults, [Y] kids. Check-in: [Date], Check-out: [Date]. Preferred accommodation: [Cottage/Villa]. Please confirm availability and rates.",
        "back_office": "Direct WhatsApp Dispatch + Webhook into Google Sheets / Reservation CRM",
        "benchmarks": [
            {"name": "SingleThread Farm", "url": "https://www.singlethreadfarms.com", "dna": "Ultra-luxury hospitality, high-contrast serif headlines, warm stone background (#FAF8F5), generous 120px whitespace."},
            {"name": "Blackberry Farm", "url": "https://www.blackberryfarm.com", "dna": "Heritage estate calm, full-bleed cinematic imagery, asymmetric 60/40 layouts, deep espresso ink typography."},
            {"name": "Soho Farmhouse", "url": "https://www.sohohouse.com/houses/soho-farmhouse", "dna": "Refined rustic luxury, tactile olive & amber surfaces, bespoke private cabin booking flow."}
        ]
    },
    "hospitality_dining_express": {
        "id": 1,
        "archetype": "Local Food & Beverage / Hospitality",
        "sub_type": "Highway Express Dining, Casual Restaurant & Takeaway Counter",
        "keywords": ["restaurant", "cafe", "dhaba", "fast food", "takeaway", "biryani", "mandi", "bakery", "diner", "tiffin", "bistro", "eatery"],
        "revenue_model": "Per-cover dine-in spend, express curbside takeaway, delivery partner orders",
        "scarce_resource": "Table turnover rate & kitchen order throughput capacity",
        "customer_mindset": "Urgent / Convenience Mindset (traveler on highway or hungry diner; zero tolerance for latency)",
        "target_lcp": "< 0.6s",
        "target_cls": "< 0.01",
        "ads_components": {"catalog": 2, "search": 1, "deliberation": 1, "immediacy": 5},
        "modality": "Modality 1: High-Utility / Conversion-First",
        "specialist_skill": "minimalist-skill (High Speed, Instant Action Strip)",
        "spatial_geometry": "Compact Fluid Grid + Persistent Bottom Mobile Hotbar",
        "palette": {
            "background": "#FFFFFF",
            "foreground": "#111827",
            "accent": "#DC2626",
            "secondary": "#D97706",
            "surface": "#F9FAFB"
        },
        "typography": {"display": "Outfit (Bold Sans)", "body": "Inter (Sans-Serif)"},
        "sections": [
            {"id": "1.0", "title": "Express Hero", "type": "Hero", "description": "Instant 1-tap call, Swiggy/Zomato delivery aggregator buttons, and curbside takeaway CTA"},
            {"id": "2.0", "title": "Highway Traveler Quick Strip", "type": "Utility Strip", "description": "Parking capacity, clean restrooms indicator, live opening hours, AC family dining badge"},
            {"id": "3.0", "title": "Signature Menu & Popular Dishes", "type": "Categorized Menu", "description": "Visual menu with dietary tags (Veg/Non-Veg, Halal, Jain), transparent pricing, and 1-tap order buttons"},
            {"id": "4.0", "title": "Customer Reviews & Topic Chips", "type": "Social Proof", "description": "Review topic chips (Biryani, Mandi, Service) and verified Google review quotes"},
            {"id": "5.0", "title": "Live GPS Route & Location", "type": "Map Embed", "description": "1-tap Google Maps directions for commuters and highway travelers"},
            {"id": "6.0", "title": "Persistent Mobile Hotbar", "type": "Sticky Action Bar", "description": "Fixed mobile footer: Call Hotline | WhatsApp Takeaway | Get Directions"}
        ],
        "interactive_modules": [
            "Persistent mobile quick-action hotbar (Call Hotline, WhatsApp Order, Google Maps GPS)",
            "Delivery partner aggregator links (Swiggy, Zomato, UberEats)",
            "Visual dietary toggle (Pure Veg vs All, Halal badge)",
            "Express slide-out takeaway bag generator with WhatsApp checkout"
        ],
        "north_star_cta": "1-Tap Phone Call / WhatsApp Curbside Takeaway",
        "whatsapp_template": "Hi {business_name}, I would like to place an express takeaway order: Items: [Dishes with quantities]. Pickup time: [approximate time/minutes]. Please confirm order total.",
        "back_office": "Direct WhatsApp Order Dispatch + Kitchen Tablet Display",
        "benchmarks": [
            {"name": "Shake Shack", "url": "https://shakeshack.com", "dna": "High-velocity food ordering, bold typography, instant menu tabs, zero friction."},
            {"name": "Sweetgreen", "url": "https://www.sweetgreen.com", "dna": "Clean modern fast-casual, clear dietary categorization, crisp appetizing photography."},
            {"name": "In-N-Out", "url": "https://www.in-n-out.com", "dna": "Utilitarian clarity, iconic red/yellow palette, straightforward highway navigation."}
        ]
    },
    "trade_contractor": {
        "id": 2,
        "archetype": "Local Physical Services & Trade Contractors",
        "sub_type": "Emergency Plumbing, HVAC, Electrical & Roofing Services",
        "keywords": ["plumbing", "plumber", "hvac", "air conditioning", "electrician", "roofing", "contractor", "drain cleaning", "pest control", "towing", "mechanic", "renovation"],
        "revenue_model": "Emergency call-out fee, diagnostic inspection fee, time-and-materials, project contracts",
        "scarce_resource": "Qualified technician hours & emergency service van dispatch slots",
        "customer_mindset": "Distressed / High-Urgency Mindset (facing water leak, broken heater, power failure; demands proof of speed & legitimacy)",
        "target_lcp": "< 0.6s",
        "target_cls": "< 0.01",
        "ads_components": {"catalog": 2, "search": 1, "deliberation": 1, "immediacy": 5},
        "modality": "Modality 1: High-Utility / Conversion-First",
        "specialist_skill": "minimalist-skill (Utilitarian Authority)",
        "spatial_geometry": "Single-Column Focused Flow + Emergency Banner",
        "palette": {
            "background": "#FFFFFF",
            "foreground": "#0F172A",
            "accent": "#DC2626",
            "secondary": "#2563EB",
            "surface": "#F1F5F9"
        },
        "typography": {"display": "Inter (Bold Display)", "body": "Inter (Sans-Serif)"},
        "sections": [
            {"id": "1.0", "title": "Emergency Dispatch Hero", "type": "Hero", "description": "24/7 hotline button, 15-minute emergency response guarantee, state license & insured badge"},
            {"id": "2.0", "title": "Service Territory & Radius Checker", "type": "Interactive Checker", "description": "Postal code validator confirming immediate van availability in user's zip code"},
            {"id": "3.0", "title": "Core Emergency Trade Services", "type": "Service Cards", "description": "Burst pipe, sewer backup, water heater replacement, AC repair with flat diagnostic rates"},
            {"id": "4.0", "title": "Transparent Diagnostic Pricing", "type": "Pricing Table", "description": "Zero hidden fees guarantee, upfront diagnostic quote, warranty terms"},
            {"id": "5.0", "title": "Verified Credentials & Trust Badges", "type": "Trust Strip", "description": "State Master License #, Google Guaranteed badge, $2M liability insurance proof"},
            {"id": "6.0", "title": "Verified Homeowner Emergency Reviews", "type": "Reviews", "description": "Real customer quotes highlighting arrival speed and professional cleanliness"},
            {"id": "7.0", "title": "Persistent Mobile Hotline Bar", "type": "Sticky Header/Footer", "description": "Sticky tap-to-call button with live 'Techs Available Now' indicator"}
        ],
        "interactive_modules": [
            "Persistent mobile click-to-call hotline bar with live online status badge",
            "Instant postal code / ZIP code service area validator",
            "Diagnostic photo upload form (allows homeowner to snap pic of leak/fault)",
            "Instant repair cost estimate calculator"
        ],
        "north_star_cta": "Direct Emergency Phone Hotline (Click-to-Call)",
        "whatsapp_template": "EMERGENCY: Hi {business_name}, I have an urgent issue at my property: [Address/Zip]. Issue: [Water leak / AC broken / Electrical outage]. Are technicians available for immediate dispatch?",
        "back_office": "Direct Twilio Call Routing + Field Service Dispatch (Jobber / ServiceTitan) Webhook",
        "benchmarks": [
            {"name": "Roto-Rooter", "url": "https://www.rotorooter.com", "dna": "High-urgency emergency dispatch, persistent hotline, zero-friction local booking."},
            {"name": "One Hour Heating & AC", "url": "https://www.onehourheatandair.com", "dna": "On-time guarantee badges, technician tracking, transparent service tiering."},
            {"name": "Mr. Electric", "url": "https://www.mrelectric.com", "dna": "Safety-first authority, upfront pricing disclosures, licensed technician trust."}
        ]
    },
    "professional_services": {
        "id": 3,
        "archetype": "High-Trust Professional Services",
        "sub_type": "Boutique Corporate Law, Tax & Wealth Management Advisory",
        "keywords": ["law firm", "attorney", "lawyer", "legal", "cpa", "tax", "accounting", "wealth management", "consulting", "financial advisor", "architecture firm"],
        "revenue_model": "Monthly retainer agreements, billable advisory hours, fixed milestone fees",
        "scarce_resource": "Senior partner billable hours & advisory calendar availability",
        "customer_mindset": "Risk-Averse Deliberator (corporate executive or private client seeking authoritative expertise with zero tolerance for fluff)",
        "target_lcp": "< 0.9s",
        "target_cls": "< 0.01",
        "ads_components": {"catalog": 3, "search": 2, "deliberation": 5, "immediacy": 2},
        "modality": "Modality 2: Hybrid Interactive / Scrollytelling",
        "specialist_skill": "minimalist-skill (Swiss Typographic Authority)",
        "spatial_geometry": "Authoritative Single-Column & Asymmetric Editorial + High Whitespace",
        "palette": {
            "background": "#0F172A",
            "foreground": "#F8FAFC",
            "accent": "#D97706",
            "secondary": "#64748B",
            "surface": "#1E293B"
        },
        "typography": {"display": "Cinzel / Playfair Display (Serif)", "body": "Inter / Plus Jakarta Sans (Sans-Serif)"},
        "sections": [
            {"id": "1.0", "title": "Authoritative Hero", "type": "Hero", "description": "High-impact value proposition, Chambers/Legal 500 credentials, and confidential consultation CTA"},
            {"id": "2.0", "title": "Specialized Practice Areas", "type": "Practice Grid", "description": "M&A, Cross-border tax, Private wealth structuring, Regulatory defense with detailed briefs"},
            {"id": "3.0", "title": "Senior Partner Biographies", "type": "Team Dossier", "description": "Verified bar admissions, landmark case outcomes, academic credentials, and direct email"},
            {"id": "4.0", "title": "Representative Case Precedents", "type": "Track Record", "description": "Anonymized transaction values ($50M+ exits, tax structuring savings, arbitration wins)"},
            {"id": "5.0", "title": "Institutional Trust Badges", "type": "Trust Strip", "description": "State Bar certifications, Legal 500, Best Lawyers, Big-4 alumni credentials"},
            {"id": "6.0", "title": "Confidential Engagement Inquiry", "type": "Secure Form", "description": "Strict attorney-client privilege notice, conflict-of-interest check, Calendly consultation scheduler"}
        ],
        "interactive_modules": [
            "Confidential consultation booking wizard with practice-area routing",
            "Interactive tax liability or transaction scoping calculator",
            "Filterable precedent transaction / case result database",
            "Gated executive briefing / whitepaper PDF download"
        ],
        "north_star_cta": "Scheduled Confidential Discovery Consultation",
        "whatsapp_template": "Confidential Inquiry: Dear {business_name}, I am seeking legal/financial advisory regarding [Practice Area/Matter]. Please connect me with the appropriate senior partner for an initial consultation.",
        "back_office": "Clio / Salesforce CRM Webhook + Encrypted PGP/Email Delivery",
        "benchmarks": [
            {"name": "Wachtell, Lipton, Rosen & Katz", "url": "https://www.wlrk.com", "dna": "Pure typographic authority, zero generic fluff, declassified institutional elegance."},
            {"name": "Cravath, Swaine & Moore", "url": "https://www.cravath.com", "dna": "Historic legal prestige, crisp serif type hierarchy, landmark case documentation."},
            {"name": "Latham & Watkins", "url": "https://www.lw.com", "dna": "Global corporate practice taxonomy, thought leadership research engine, polished dark accents."}
        ]
    },
    "healthcare_medical": {
        "id": 4,
        "archetype": "Healthcare, Wellness & Medical Practices",
        "sub_type": "Specialized Dental, Aesthetic Dermatology & Medical Clinics",
        "keywords": ["dental", "dentist", "clinic", "dermatology", "plastic surgery", "physiotherapy", "doctor", "medical", "orthopedic", "psychology", "medspa", "wellness clinic"],
        "revenue_model": "Fee-for-service, elective treatment packages, private insurance claims, recurring wellness memberships",
        "scarce_resource": "Physician clinical appointment slots & specialized treatment room occupancy",
        "customer_mindset": "Vulnerable yet Skeptical Patient (balancing physical concern with strict scrutiny of practitioner credentials and hygiene)",
        "target_lcp": "< 0.8s",
        "target_cls": "< 0.01",
        "ads_components": {"catalog": 3, "search": 2, "deliberation": 4, "immediacy": 3},
        "modality": "Modality 1: High-Utility / Conversion-First",
        "specialist_skill": "soft-skill (Clinical Calm & Warmth)",
        "spatial_geometry": "Clean Airy Bento Grid + Generous Whitespace",
        "palette": {
            "background": "#F8FAFC",
            "foreground": "#0F172A",
            "accent": "#0D9488",
            "secondary": "#0284C7",
            "surface": "#FFFFFF"
        },
        "typography": {"display": "Plus Jakarta Sans (Medium Display)", "body": "Inter (Sans-Serif)"},
        "sections": [
            {"id": "1.0", "title": "Clinical Hero", "type": "Hero", "description": "Welcoming clinic ambiance, board certification badges, next available appointment indicator"},
            {"id": "2.0", "title": "Specialized Clinical Treatments", "type": "Service Cards", "description": "Dental implants, aesthetic lasers, orthodontics with procedure duration and recovery times"},
            {"id": "3.0", "title": "Physician Credentials & Education", "type": "Doctor Profiles", "description": "Board certifications, medical school fellowship, years of clinical experience, patient reviews"},
            {"id": "4.0", "title": "Before / After Clinical Results", "type": "Comparison Slider", "description": "Interactive before/after clinical slider with patient consent and treatment timeline"},
            {"id": "5.0", "title": "Accepted Insurance & Transparent Pricing", "type": "Insurance Checker", "description": "Searchable list of in-network insurance providers, financing plans (CareCredit, EMI)"},
            {"id": "6.0", "title": "Patient Reviews & Safety Protocols", "type": "Social Proof", "description": "HIPAA-compliant verified patient reviews, hospital-grade sterilization protocol badges"},
            {"id": "7.0", "title": "Clinic Location, Parking & Booking Modal", "type": "Map & Booking", "description": "Direct appointment calendar booking, wheelchair accessibility notes, driving directions"}
        ],
        "interactive_modules": [
            "Interactive Before/After clinical result slider",
            "In-network health insurance provider search/filter",
            "Multi-step HIPAA appointment booking wizard (Select Treatment -> Select Doctor -> Pick Date/Time)",
            "Online patient intake questionnaire download"
        ],
        "north_star_cta": "Book Clinical Consultation / Appointment",
        "whatsapp_template": "Hi {business_name}, I would like to schedule an appointment for [Treatment/Checkup]. Preferred doctor: [Doctor Name / Any]. Preferred day: [Weekday/Weekend, Morning/Evening].",
        "back_office": "EMR/EHR Webhook (Epic / Dentrix / Kareo) + SMS Confirmation (Twilio)",
        "benchmarks": [
            {"name": "Tend Dental", "url": "https://www.hellotend.com", "dna": "Modern hospitality-grade dental experience, transparent pricing, sub-minute booking."},
            {"name": "Parsley Health", "url": "https://www.parsleyhealth.com", "dna": "Holistic medical calm, soft teal accents, doctor biography depth."},
            {"name": "Forward Health", "url": "https://goforward.com", "dna": "High-tech preventive clinic, clean metrics, seamless app-like interface."}
        ]
    },
    "ecommerce_d2c": {
        "id": 5,
        "archetype": "Direct-to-Consumer (D2C) & E-Commerce",
        "sub_type": "Curated Niche Storefront & Single-Product Hero Brand",
        "keywords": ["shop", "store", "ecommerce", "brand", "d2c", "apparel", "clothing", "skincare", "cosmetics", "jewelry", "ceramics", "furniture", "electronics"],
        "revenue_model": "Product margin x transaction volume, recurring subscription replenishment",
        "scarce_resource": "SKU inventory velocity & checkout conversion funnel rate",
        "customer_mindset": "Impulse / Specification Researcher (scouting product aesthetics, shipping dates, return policy, verified buyer reviews)",
        "target_lcp": "< 1.2s",
        "target_cls": "< 0.02",
        "ads_components": {"catalog": 4, "search": 4, "deliberation": 3, "immediacy": 2},
        "modality": "Modality 2: Hybrid Interactive / Scrollytelling",
        "specialist_skill": "soft-skill (Tactile Product Elegance)",
        "spatial_geometry": "Asymmetric Product Grid + Persistent Slide-out Cart Drawer",
        "palette": {
            "background": "#FDFBF7",
            "foreground": "#18181B",
            "accent": "#99582A",
            "secondary": "#6F1D1B",
            "surface": "#F4EFE6"
        },
        "typography": {"display": "Editorial Serif / Syne", "body": "Inter (Sans-Serif)"},
        "sections": [
            {"id": "1.0", "title": "Hero Product Launch", "type": "Hero", "description": "High-res tactile product photography, key benefit pills, instant Add-to-Bag CTA"},
            {"id": "2.0", "title": "Material Provenance & Craftsmanship", "type": "Split Story", "description": "Artisanal materials, sustainable sourcing, durability guarantee"},
            {"id": "3.0", "title": "Curated Collection Grid", "type": "Product Catalog", "description": "Faceted product cards with hover video loops, variant color pickers, and quick add"},
            {"id": "4.0", "title": "Interactive Product Spec & Size Guide", "type": "Tabs / Drawer", "description": "Dimensional specs, materials breakdown, interactive fit/size calculator"},
            {"id": "5.0", "title": "Verified Customer Reviews & Photo UGC", "type": "Photo Reviews", "description": "5-star rating filter, verified buyer badges, Instagram customer unboxing gallery"},
            {"id": "6.0", "title": "Risk-Free Commerce Guarantee", "type": "Trust Strip", "description": "30-day money-back guarantee, free carbon-neutral shipping, secure 256-bit checkout"}
        ],
        "interactive_modules": [
            "Persistent slide-out cart drawer with live subtotal and free shipping progress meter",
            "Interactive product variant switcher (colors, sizes, bundles)",
            "1-Click express checkout (Apple Pay, Google Pay, UPI)",
            "Postal code delivery date estimator on product page"
        ],
        "north_star_cta": "Add to Cart / 1-Click Express Checkout",
        "whatsapp_template": "Hi {business_name}, I am interested in purchasing [Product Name - Variant]. Do you offer express delivery to [City/Postal Code]?",
        "back_office": "Shopify / Stripe Checkout + Inventory Management Webhook",
        "benchmarks": [
            {"name": "Aesop", "url": "https://www.aesop.com", "dna": "World-class editorial e-commerce, warm muted stone surfaces, philosophical copy."},
            {"name": "Our Place", "url": "https://fromourplace.com", "dna": "Vibrant product storytelling, color variant mastery, high-converting bundle cart."},
            {"name": "Bellroy", "url": "https://bellroy.com", "dna": "Interactive product comparison, slimness slider, clean technical layout."}
        ]
    },
    "b2b_saas": {
        "id": 6,
        "archetype": "B2B Software, SaaS & Digital Platforms",
        "sub_type": "Developer Infrastructure, Enterprise Workflow SaaS & AI Platforms",
        "keywords": ["saas", "software", "api", "cloud", "developer", "platform", "b2b", "workflow", "ai", "security", "database", "analytics", "infrastructure"],
        "revenue_model": "Recurring subscriptions (seat-based, usage-based, compute tiering), enterprise contracts",
        "scarce_resource": "Qualified enterprise sales pipeline & self-serve trial conversion rate",
        "customer_mindset": "Technical Evaluator (engineer inspecting APIs) or Business Leader (evaluating ROI, SOC 2 compliance, and time-to-value)",
        "target_lcp": "< 0.8s",
        "target_cls": "< 0.01",
        "ads_components": {"catalog": 3, "search": 2, "deliberation": 4, "immediacy": 2},
        "modality": "Modality 2: Hybrid Interactive / Scrollytelling",
        "specialist_skill": "minimalist-skill (Engineering Precision / Dark Mode Tech)",
        "spatial_geometry": "Strict 8dp Bento Grid + Animated Terminal/Dashboard Previews",
        "palette": {
            "background": "#090A0F",
            "foreground": "#F8FAFC",
            "accent": "#6366F1",
            "secondary": "#10B981",
            "surface": "#12141D"
        },
        "typography": {"display": "Geist / Plus Jakarta Sans", "body": "Inter / Geist Mono"},
        "sections": [
            {"id": "1.0", "title": "Value Proposition Hero", "type": "Hero", "description": "Outcome-focused headline, 1-click install command (`npm i`), interactive UI preview, and Start Free Trial CTA"},
            {"id": "2.0", "title": "Customer Logos & Social Proof", "type": "Marquee", "description": "Enterprise trust strip featuring leading engineering teams using the product"},
            {"id": "3.0", "title": "Interactive Product Tour / Bento Grid", "type": "Feature Bento", "description": "Animated feature cards showcasing real code, workflow automation, and telemetry"},
            {"id": "4.0", "title": "Interactive ROI & Compute Calculator", "type": "Calculator", "description": "Slider for monthly events/seats calculating cost savings vs legacy solutions"},
            {"id": "5.0", "title": "Transparent Multi-Tier Pricing Table", "type": "Pricing Table", "description": "Monthly/Annual toggle, feature comparison checklist, Free/Pro/Enterprise tiers"},
            {"id": "6.0", "title": "Enterprise Security & Compliance", "type": "Trust Strip", "description": "SOC 2 Type II, GDPR, HIPAA, 99.99% uptime SLA badges and security whitepaper"},
            {"id": "7.0", "title": "Developer Documentation Strip", "type": "Code Preview", "description": "Syntax-highlighted SDK examples in Python, TypeScript, Go with copy-to-clipboard"}
        ],
        "interactive_modules": [
            "Interactive animated product tour / code sandbox tab switcher",
            "Dynamic ROI & compute cost slider calculator",
            "Monthly vs Annual billing toggle with animated price transitions",
            "1-Click command copy buttons (`npm install ...`) with toast feedback"
        ],
        "north_star_cta": "Start Free Trial / Book Enterprise Architecture Demo",
        "whatsapp_template": "Enterprise Inquiry: Hi {business_name}, our team is evaluating your platform for [Use Case]. We have [X] developers. Please connect us with a solutions architect for a technical demo.",
        "back_office": "HubSpot / Stripe Billing / Segment Webhook + Slack Notification",
        "benchmarks": [
            {"name": "Linear", "url": "https://linear.app", "dna": "Awwwards gold standard, keyboard-first ethos, subtle dark obsidian layers, micro-springs."},
            {"name": "Vercel", "url": "https://vercel.com", "dna": "Pure Swiss typographic clarity, geometric monochrome, instant interactive previews."},
            {"name": "Supabase", "url": "https://supabase.com", "dna": "Developer-first architecture, emerald green accents, syntax-highlighted code tabs."}
        ]
    },
    "real_estate": {
        "id": 7,
        "archetype": "Real Estate & Property Developments",
        "sub_type": "Luxury Residential Developments & Boutique Vacation Portfolios",
        "keywords": ["real estate", "realtor", "apartments", "condos", "villas", "property development", "brokerage", "residential", "leasing", "penthouse"],
        "revenue_model": "Transaction commissions, capital property sales, nightly villa yield",
        "scarce_resource": "Exclusive listing inventory & private showing consultation slots",
        "customer_mindset": "High-Capital Investor / Homebuyer (analyzing architectural floorplans, neighborhood yields, and finishing specs)",
        "target_lcp": "< 1.2s",
        "target_cls": "< 0.02",
        "ads_components": {"catalog": 3, "search": 3, "deliberation": 5, "immediacy": 2},
        "modality": "Modality 2: Hybrid Interactive / Scrollytelling",
        "specialist_skill": "soft-skill (Architectural Grandeur)",
        "spatial_geometry": "Full-Bleed Architectural Media + Editorial Spatial Cadence",
        "palette": {
            "background": "#F7F5F0",
            "foreground": "#1C1917",
            "accent": "#92400E",
            "secondary": "#44403C",
            "surface": "#EFECE6"
        },
        "typography": {"display": "Cinzel / Cormorant Garamond", "body": "Plus Jakarta Sans"},
        "sections": [
            {"id": "1.0", "title": "Architectural Vision Hero", "type": "Hero", "description": "Full-bleed drone footage, architectural pedigree, VIP showing request CTA"},
            {"id": "2.0", "title": "The Residences & Penthouses", "type": "Floorplan Grid", "description": "Interactive floorplans, square footage, solar orientation, finish packages"},
            {"id": "3.0", "title": "Interactive Mortgage & Yield Calculator", "type": "Calculator", "description": "Down payment x interest rate x rental yield modeling tool"},
            {"id": "4.0", "title": "Building Amenities & Lifestyle", "type": "Photo Story", "description": "Private infinity pool, concierge, wellness spa, private dining lounge"},
            {"id": "5.0", "title": "Neighborhood Map & Cultural Proximity", "type": "Interactive Map", "description": "Walking times to Michelin dining, top private schools, and transit"},
            {"id": "6.0", "title": "Private Viewing & Floorplan Dossier", "type": "Modal / Form", "description": "Gated architectural brochure download + confidential private appointment request"}
        ],
        "interactive_modules": [
            "Interactive architectural floorplan viewer with zoom and unit specs",
            "Mortgage and estimated rental yield calculator",
            "Private showing consultation booking calendar",
            "Gated architectural prospectus / brochure PDF download"
        ],
        "north_star_cta": "Schedule Private Property Viewing / Download VIP Floorplans",
        "whatsapp_template": "Property Inquiry: Hi {business_name}, I am interested in viewing available units at [Development Name]. Please send floorplan specifications and private showing availability.",
        "back_office": "HubSpot / Follow Up Boss CRM Webhook + Direct Agent SMS Alert",
        "benchmarks": [
            {"name": "The Henderson", "url": "https://thehenderson.com.hk", "dna": "Zaha Hadid architectural elegance, fluid glass curves, high-prestige typography."},
            {"name": "One Beverly Hills", "url": "https://onebeverlyhills.com", "dna": "Lush botanical luxury, cinematic aerial video, curated residence specifications."},
            {"name": "Aman Residences", "url": "https://www.aman.com/residences", "dna": "Extreme minimalism, transcendent serenity, discreet ultra-HNW inquiry flow."}
        ]
    },
    "creative_agency": {
        "id": 8,
        "archetype": "Creative Agencies, Studios & Portfolios",
        "sub_type": "Brand Strategy Studios, Motion Houses & Digital Production Agencies",
        "keywords": ["agency", "design studio", "branding agency", "creative agency", "production house", "portfolio", "art director", "motion studio"],
        "revenue_model": "Project retainers, production day-rates, creative IP licensing",
        "scarce_resource": "Creative director bandwidth & studio production quarterly slots",
        "customer_mindset": "Brand CMO / Creative Producer (evaluating aesthetic vision, past client roster, and cultural relevance)",
        "target_lcp": "< 1.4s",
        "target_cls": "< 0.02",
        "ads_components": {"catalog": 3, "search": 1, "deliberation": 4, "immediacy": 1},
        "modality": "Modality 2: Hybrid Interactive / Scrollytelling",
        "specialist_skill": "taste-skill (Anti-Generic Editorial Craft)",
        "spatial_geometry": "Asymmetric Case Study Index + Hover Video Canvas",
        "palette": {
            "background": "#000000",
            "foreground": "#FFFFFF",
            "accent": "#FF4500",
            "secondary": "#A1A1AA",
            "surface": "#121212"
        },
        "typography": {"display": "Syne / Monument Extended", "body": "Inter / Geist"},
        "sections": [
            {"id": "1.0", "title": "Manifesto & Showreel Hero", "type": "Hero", "description": "High-velocity 60fps showreel video grid with bold creative thesis and project inquiry CTA"},
            {"id": "2.0", "title": "Selected Case Studies", "type": "Case Study Index", "description": "Numbered typographic project list with hover thumbnail reveal and deep dive links"},
            {"id": "3.0", "title": "Disciplines & Studio Philosophy", "type": "Text Bento", "description": "Brand identity, kinetic design, 3D world-building, digital flagship engineering"},
            {"id": "4.0", "title": "Client Recognition & Awwwards Badges", "type": "Trust Strip", "description": "Awwwards Site of the Year, Cannes Lions, D&AD pencils, Fast Company Innovation"},
            {"id": "5.0", "title": "Project Inquiry & Brief Submission", "type": "Inquiry Form", "description": "Structured scoping modal: Budget range ($50k-$200k+), launch timeline, brief uploader"}
        ],
        "interactive_modules": [
            "60fps hover video preview across project index strip",
            "Fullscreen showreel video overlay with keyboard ESC / spacebar controls",
            "Interactive project scoping brief uploader with budget selector",
            "Custom cursor / magnetic button micro-interactions"
        ],
        "north_star_cta": "Submit Project Brief / Initiate Collaboration",
        "whatsapp_template": "Studio Inquiry: Hi {business_name}, we are looking to partner with your team on a new project: [Branding / Website / Campaign]. Target launch: [Q3/Q4]. Budget tier: [$50k+]. Let's discuss.",
        "back_office": "Notion / Slack Webhook + Direct Partner Calendar Scheduler",
        "benchmarks": [
            {"name": "Active Theory", "url": "https://activetheory.net", "dna": "Interactive motion benchmark, sound design, fluid WebGL transitions."},
            {"name": "Locomotive", "url": "https://locomotive.ca", "dna": "Scroll-driven kinetic typography, bold contrast, distinctive French-Canadian craft."},
            {"name": "Basic Agency", "url": "https://basicagency.com", "dna": "High-contrast editorial grid, raw agency culture, prominent client wins."}
        ]
    },
    "education_bootcamp": {
        "id": 9,
        "archetype": "Education, Courses & Community Organizations",
        "sub_type": "Executive Masterclasses, Tech Bootcamps & Private Academies",
        "keywords": ["bootcamp", "academy", "masterclass", "course", "education", "school", "training", "workshop", "coaching", "cohort", "curriculum"],
        "revenue_model": "Cohort tuition, self-paced course sales, enterprise team training",
        "scarce_resource": "Cohort seat capacity & senior instructor mentorship bandwidth",
        "customer_mindset": "Career-Changer or Professional (scrutinizing graduate job placement, mentor credentials, and curriculum rigor)",
        "target_lcp": "< 0.8s",
        "target_cls": "< 0.01",
        "ads_components": {"catalog": 3, "search": 2, "deliberation": 5, "immediacy": 2},
        "modality": "Modality 2: Hybrid Interactive / Scrollytelling",
        "specialist_skill": "minimalist-skill (Structured Educational Clarity)",
        "spatial_geometry": "Syllabus Timeline + Graduate Proof Bento",
        "palette": {
            "background": "#F8FAFC",
            "foreground": "#0F172A",
            "accent": "#4F46E5",
            "secondary": "#059669",
            "surface": "#FFFFFF"
        },
        "typography": {"display": "Plus Jakarta Sans (Display)", "body": "Inter (Sans-Serif)"},
        "sections": [
            {"id": "1.0", "title": "Outcome Hero", "type": "Hero", "description": "Career outcome headline ($125k avg graduate salary), cohort start countdown, Apply Now CTA"},
            {"id": "2.0", "title": "Alumni Placement Marquee", "type": "Trust Strip", "description": "Logos of companies hiring graduates (Google, Stripe, Airbnb, Apple)"},
            {"id": "3.0", "title": "Interactive Week-by-Week Curriculum", "type": "Accordion Timeline", "description": "Interactive syllabus modules, project deliverables, live coding sessions"},
            {"id": "4.0", "title": "Instructor Roster & Mentors", "type": "Faculty Dossier", "description": "Industry practitioner bios, former engineering leads, direct office hours"},
            {"id": "5.0", "title": "Interactive Salary Increase & ROI Calculator", "type": "Calculator", "description": "Current salary vs target role calculating tuition payback timeline"},
            {"id": "6.0", "title": "Tuition Options & ISA Terms", "type": "Pricing Table", "description": "Upfront discount, monthly installments, Income Share Agreement terms"},
            {"id": "7.0", "title": "Cohort Application & Syllabus Download", "type": "Application Modal", "description": "Instant syllabus PDF download + multi-step cohort application form"}
        ],
        "interactive_modules": [
            "Interactive week-by-week syllabus accordion with preview lessons",
            "Career ROI and salary increase payback calculator",
            "Cohort registration countdown timer with remaining seat counter",
            "Instant syllabus PDF generator sent directly to email/WhatsApp"
        ],
        "north_star_cta": "Apply for Next Cohort / Download Complete Syllabus",
        "whatsapp_template": "Admissions Inquiry: Hi {business_name}, I am interested in applying for the upcoming [Course/Bootcamp Name] cohort. Please share the syllabus and scholarship details.",
        "back_office": "HubSpot Admissions Pipeline + Stripe Tuition Checkout",
        "benchmarks": [
            {"name": "Reforge", "url": "https://www.reforge.com", "dna": "Executive education benchmark, rigorous frameworks, high-contrast dark accents."},
            {"name": "Springboard", "url": "https://www.springboard.com", "dna": "Job-guarantee trust signals, clear student journey timeline, transparent tuition."},
            {"name": "Designlab", "url": "https://designlab.com", "dna": "Clean modern learning UX, student portfolio showcase, mentor access."}
        ]
    },
    "industrial_manufacturing": {
        "id": 10,
        "archetype": "Industrial, Manufacturing & B2B Supply",
        "sub_type": "Precision OEM Suppliers, CNC Machining & Custom Metal Fabrication",
        "keywords": ["manufacturing", "factory", "machining", "cnc", "fabrication", "oem", "industrial", "sheet metal", "wholesale supplier", "tooling", "injection molding"],
        "revenue_model": "High-volume OEM contracts, custom machining bids, materials wholesale margin",
        "scarce_resource": "CNC spindle hours, tooling lead time, minimum order quantity (MOQ) slots",
        "customer_mindset": "Procurement Engineer / Plant Manager (evaluating ISO certifications, tolerance specs (±0.005mm), and production capacity)",
        "target_lcp": "< 0.7s",
        "target_cls": "< 0.01",
        "ads_components": {"catalog": 3, "search": 2, "deliberation": 4, "immediacy": 2},
        "modality": "Modality 1: High-Utility / Conversion-First",
        "specialist_skill": "brutalist-skill (Raw Industrial Blueprint / Telemetry)",
        "spatial_geometry": "Rigid Grid + Technical Telemetry & Tolerance Tables",
        "palette": {
            "background": "#0B0F19",
            "foreground": "#E2E8F0",
            "accent": "#F59E0B",
            "secondary": "#64748B",
            "surface": "#1E293B"
        },
        "typography": {"display": "Chivo / Space Grotesk (Bold)", "body": "JetBrains Mono / Inter"},
        "sections": [
            {"id": "1.0", "title": "Precision Capabilities Hero", "type": "Hero", "description": "ISO 9001:2015 certified, 5-axis CNC tolerance telemetry (±0.002mm), instant RFQ CTA"},
            {"id": "2.0", "title": "Machining Capabilities & Machine Fleet", "type": "Spec Grid", "description": "Haas/Mazak spindle counts, maximum part dimensions (X/Y/Z), materials supported"},
            {"id": "3.0", "title": "Material Compatibility Matrix", "type": "Technical Table", "description": "Aerospace Aluminum (6061/7075), Titanium Grade 5, Stainless Steel 316L, Inconel"},
            {"id": "4.0", "title": "Quality Inspection & CMM Reports", "type": "Certification Strip", "description": "Zeiss CMM inspection reports, AS9100D aerospace compliance, mill test certificates"},
            {"id": "5.0", "title": "Industries Served & Case Studies", "type": "Bento Grid", "description": "Aerospace, Medical devices, Automotive robotics, Semiconductor tooling"},
            {"id": "6.0", "title": "Secure CAD Upload & Request for Quote (RFQ)", "type": "Secure RFQ Form", "description": "STEP/IGES file uploader with NDA guarantee and 24-hour engineering quote SLA"}
        ],
        "interactive_modules": [
            "Interactive CAD file uploader (STEP, IGES, DXF) with automated NDA agreement",
            "Material tolerance and turnaround time parametric estimator",
            "Filterable machine fleet specification directory",
            "Instant downloadable ISO certification and quality manual"
        ],
        "north_star_cta": "Request Formal Engineering Quote (Upload CAD)",
        "whatsapp_template": "RFQ Inquiry: Dear {business_name}, we require a quotation for precision machining: Material: [Aluminum/Steel/Titanium]. Quantity: [X parts]. Target delivery: [Date]. CAD attached.",
        "back_office": "Paperless Parts / ERP Webhook + Direct Engineering Team Email",
        "benchmarks": [
            {"name": "Fictiv", "url": "https://www.fictiv.com", "dna": "Digital manufacturing gold standard, instant quote interface, telemetry clarity."},
            {"name": "Protolabs", "url": "https://www.protolabs.com", "dna": "Rapid prototyping precision, automated DFM analysis, comprehensive material specs."},
            {"name": "Xometry", "url": "https://www.xometry.com", "dna": "Instant quoting engine, global supplier network, rigid industrial engineering typography."}
        ]
    }
}

def clean_string(s):
    if not s:
        return ""
    return re.sub(r'[\ue000-\uf8ff]', '', str(s)).strip()

def score_match(text, keywords):
    """Computes keyword match score against a normalized text string."""
    text_lower = text.lower()
    score = 0
    for kw in keywords:
        # Give higher weight to multi-word phrases or exact word matches
        if re.search(r'\b' + re.escape(kw) + r'\b', text_lower):
            score += 3
        elif kw in text_lower:
            score += 1
    return score

def classify(input_data):
    """
    Classifies business data (from Google Maps or raw pitch) into the exact archetype.
    """
    title = clean_string(input_data.get("title", ""))
    category = clean_string(input_data.get("category", ""))
    overview = clean_string(input_data.get("overview", ""))
    reviews = " ".join([clean_string(r) for r in input_data.get("customer_reviews", [])])
    tags = " ".join([clean_string(t) for t in input_data.get("popular_dishes_tags", [])])
    pitch = clean_string(input_data.get("pitch", ""))

    combined_corpus = f"{title} {category} {overview} {tags} {reviews} {pitch}".lower()

    best_key = None
    best_score = -1

    for key, spec in ARCHETYPES_DB.items():
        score = 0
        # If category directly matches sub_type or keywords, massive boost
        if category:
            for kw in spec["keywords"]:
                if kw in category.lower():
                    score += 10
        # Check title
        score += score_match(title, spec["keywords"]) * 2
        # Check combined corpus
        score += score_match(combined_corpus, spec["keywords"])

        if score > best_score:
            best_score = score
            best_key = key

    # Fallback to general hospitality if still unmatched
    if not best_key or best_score <= 0:
        best_key = "hospitality_resort"

    matched = ARCHETYPES_DB[best_key].copy()
    
    # Calculate Feature-Driven ADS Score & Topology
    comps = matched["ads_components"].copy()
    features_detected = []
    text_to_check = f"{pitch} {overview} {title}".lower()

    if re.search(r'\b(blog|articles|news|insights|stories)\b', text_to_check):
        features_detected.append("Dedicated Blog / Editorial Hub (/blog)")
        comps["catalog"] += 2
        comps["search"] += 1
    if re.search(r'\b(individual pages|separate pages|subpages|detail pages|per room|per service|dedicated pages)\b', text_to_check):
        features_detected.append("Dedicated Item / Service Detail Sub-Routes (/items/[slug])")
        comps["catalog"] += 2
    if re.search(r'\b(portal|dashboard|login|account|member area)\b', text_to_check):
        features_detected.append("Client Portal & Authentication Area (/portal)")
        comps["catalog"] += 2
    if re.search(r'\b(careers|jobs|team page|press)\b', text_to_check):
        features_detected.append("Institutional & Careers Subpages (/careers, /about)")
        comps["catalog"] += 1
    if re.search(r'\b(multi-category|catalog|storefront|shop|ecommerce)\b', text_to_check):
        features_detected.append("Multi-Tier E-Commerce Catalog (/catalog, /cart, /checkout)")
        comps["catalog"] += 2

    ads_score = comps["catalog"] + comps["search"] + comps["deliberation"] - comps["immediacy"]

    # Explicit user preference or feature-driven override
    user_top_pref = input_data.get("topology")
    if user_top_pref == "spa" or re.search(r'\b(single page|one page|landing page only|single-page)\b', text_to_check):
        topology = "Single-Page Architecture (SPA)"
        topology_reason = "User Preference / Focused Scope: Consolidated into a high-density, continuous scroll journey with slide-out drawers."
    elif user_top_pref == "mpa" or re.search(r'\b(multi-page|multipage|multiple pages|separate pages|multi page)\b', text_to_check):
        topology = "Multi-Page Architecture (MPA)"
        topology_reason = "User Preference / Multi-Page Scope: Decomposed into canonical Next.js App Router sub-routes."
    elif ads_score <= 5:
        topology = "Single-Page Architecture (SPA)"
        topology_reason = f"ADS Score ({ads_score}/15 <= 5): Optimal for high-speed conversion, focused brand storytelling, and mobile retention."
    else:
        topology = "Multi-Page Architecture (MPA)"
        topology_reason = f"ADS Score ({ads_score}/15 >= 6): Driven by high catalog depth, extensive feature set, or dedicated subpage requirements."

    # Determine Canonical Route Map vs Single-Page Section Flow
    if topology == "Multi-Page Architecture (MPA)":
        # Dynamic naming based on archetype
        is_hospitality = "hospitality" in matched_key or "resort" in matched_key
        offerings_name = "Accommodations & Suites" if is_hospitality else "Offerings & Directory"
        offerings_path = "/accommodations" if is_hospitality else "/offerings"
        
        canonical_routes = [
            {
                "path": "/",
                "name": "Flagship Home",
                "purpose": "Signature hero, capability highlights, proof marquee, direct CTA",
                "required_sections": matched["sections"]
            },
            {
                "path": "/about",
                "name": "Story & Philosophy",
                "purpose": "Brand heritage, grounds/studio tour, founder manifesto, team credentials",
                "required_sections": [
                    {"id": "about-1.0", "title": "AboutHero", "type": "Subpage Hero", "description": "Atmospheric wide header with breadcrumbs, establishment origins, and narrative mission", "mcp": "magicuidesign-mcp:blur-fade"},
                    {"id": "about-2.0", "title": "HeritageStory", "type": "Asymmetric Split", "description": "Founders' journey, historical provenance, and architectural philosophy with high-res photography", "mcp": "lucide-icons"},
                    {"id": "about-3.0", "title": "PillarsAndValues", "type": "Bento Grid", "description": "Craftsmanship, ecological stewardship, sustainability, and quality commitments with Lucide icons", "mcp": "magicuidesign-mcp:bento-grid"},
                    {"id": "about-4.0", "title": "LeadershipAndCustodians", "type": "Card Grid", "description": "Founding artisans, master chefs, or key directors with portraits and credentials", "mcp": "shadcn-ui:avatar"},
                    {"id": "about-5.0", "title": "EditorialManifesto", "type": "Centered Editorial", "description": "Full-bleed quote statement and dedication to exceptional guest/client outcomes", "mcp": "magicuidesign-mcp:text-reveal"},
                    {"id": "about-6.0", "title": "SubpageCTA", "type": "Conversion Banner", "description": "Direct inquiry and reservation trigger linking to contact/offerings", "mcp": "shadcn-ui:button"}
                ]
            },
            {
                "path": offerings_path,
                "name": offerings_name,
                "purpose": "Faceted filterable catalog of cottages, services, or products with zero 1-section stubs",
                "required_sections": [
                    {"id": "catalog-1.0", "title": "OfferingsHero", "type": "Subpage Hero", "description": "Immersive catalog header with live availability status indicator", "mcp": "magicuidesign-mcp:blur-fade"},
                    {"id": "catalog-2.0", "title": "FacetedFilterBar", "type": "Filter Controls", "description": "Interactive category pills, tier selector, and sorting controls", "mcp": "shadcn-ui:tabs"},
                    {"id": "catalog-3.0", "title": "OfferingsCatalogGrid", "type": "Faceted Catalog", "description": "Comprehensive cards with dimensions, occupancy/specs, pricing, amenity tags, and photo carousels", "mcp": "magicuidesign-mcp:carousel"},
                    {"id": "catalog-4.0", "title": "IncludedAmenitiesBento", "type": "Bento Grid", "description": "Everyday perks, exclusive access, grounds privileges, and concierge support", "mcp": "magicuidesign-mcp:bento-grid"},
                    {"id": "catalog-5.0", "title": "BookingPoliciesAccordion", "type": "Accordion", "description": "Deposit terms, check-in schedules, cancellation windows, and guest policies", "mcp": "shadcn-ui:accordion"},
                    {"id": "catalog-6.0", "title": "CatalogCTA", "type": "Conversion Banner", "description": "Direct reservation dispatcher with instant WhatsApp payload pre-loaded", "mcp": "shadcn-ui:button"}
                ]
            },
            {
                "path": "/contact",
                "name": "Inquiry & Logistics",
                "purpose": "Interactive booking wizard, GPS directions, emergency hotline",
                "required_sections": [
                    {"id": "contact-1.0", "title": "ContactHero", "type": "Subpage Hero", "description": "Inquiry header with live availability status and rapid response promise", "mcp": "magicuidesign-mcp:blur-fade"},
                    {"id": "contact-2.0", "title": "DirectConciergeGrid", "type": "Contact Grid", "description": "Direct hotline, WhatsApp instant chat, email concierge, and operational hours", "mcp": "lucide-icons"},
                    {"id": "contact-3.0", "title": "InteractiveInquiryForm", "type": "Form Module", "description": "Accessible inquiry form with date pickers, service selector, and WhatsApp dispatch payload", "mcp": "shadcn-ui:dialog"},
                    {"id": "contact-4.0", "title": "GPSDirectionsAndMap", "type": "Map Embed", "description": "1-tap navigation coordinates, driving instructions from transit hubs, and parking notes", "mcp": "lucide-icons"},
                    {"id": "contact-5.0", "title": "FAQAccordion", "type": "Accordion", "description": "Essential logistics, directions, accessibility, and booking FAQs", "mcp": "shadcn-ui:accordion"}
                ]
            }
        ]
        if any("Blog" in f for f in features_detected):
            canonical_routes.append({
                "path": "/blog",
                "name": "Editorial & Insights",
                "purpose": "SEO articles, stories, guides, and updates",
                "required_sections": [
                    {"id": "blog-1.0", "title": "BlogHero", "type": "Subpage Hero", "description": "Editorial journal header with featured story showcase", "mcp": "magicuidesign-mcp:blur-fade"},
                    {"id": "blog-2.0", "title": "TopicFilterBar", "type": "Filter Controls", "description": "Topic filter chips (Heritage, Nature, Gastronomy, Local Guides)", "mcp": "shadcn-ui:tabs"},
                    {"id": "blog-3.0", "title": "ArticleIndexGrid", "type": "Article Grid", "description": "3-column editorial cards with read time, publication date, and author attribution", "mcp": "lucide-icons"},
                    {"id": "blog-4.0", "title": "NewsletterSubscription", "type": "Newsletter Bar", "description": "Private seasonal gazette and dispatch email capture", "mcp": "shadcn-ui:button"}
                ]
            })
        if any("Portal" in f for f in features_detected):
            canonical_routes.append({
                "path": "/portal",
                "name": "Client Portal / Dashboard",
                "purpose": "Authenticated customer bookings, orders, and documents",
                "required_sections": [
                    {"id": "portal-1.0", "title": "PortalHero", "type": "Dashboard Header", "description": "Customer welcome header with account status and active bookings", "mcp": "shadcn-ui:avatar"},
                    {"id": "portal-2.0", "title": "ActiveReservationsList", "type": "Data Table", "description": "Upcoming stay dates, invoice downloads, and check-in QR code", "mcp": "shadcn-ui:table"},
                    {"id": "portal-3.0", "title": "PreferencesManager", "type": "Settings Panel", "description": "Dietary requirements, room configuration, and billing contact management", "mcp": "shadcn-ui:form"}
                ]
            })
    else:
        canonical_routes = [
            {
                "path": "/",
                "name": "Consolidated Continuous Scroll Journey",
                "purpose": "All 1.0 to N.0 sections on canonical root route with off-canvas slide-out drawers for details",
                "required_sections": matched["sections"]
            }
        ]
    
    # Replace business name in templates
    b_name = title or input_data.get("business_name") or "Business"
    matched["whatsapp_template"] = matched["whatsapp_template"].replace("{business_name}", b_name)

    result = {
        "business_name": b_name,
        "input_source": input_data.get("source", "raw_pitch"),
        "raw_category_detected": category or "Not specified",
        "identified_archetype": matched["archetype"],
        "identified_sub_type": matched["sub_type"],
        "primary_revenue_model": matched["revenue_model"],
        "scarce_operational_resource": matched["scarce_resource"],
        "customer_arrival_mindset": matched["customer_mindset"],
        "core_web_vitals_target": {
            "lcp": matched["target_lcp"],
            "cls": matched["target_cls"]
        },
        "architecture_decision_score": {
            "score": f"{ads_score}/15",
            "formula": f"Catalog ({comps['catalog']}) + Search ({comps['search']}) + Deliberation ({comps['deliberation']}) - Immediacy ({comps['immediacy']}) = {ads_score}",
            "recommended_topology": topology,
            "topology_rationale": topology_reason,
            "detected_features_influencing_topology": features_detected
        },
        "canonical_route_architecture": canonical_routes,
        "universal_stack_standard": "Next.js 15 (App Router) + TypeScript + Tailwind CSS v4 + Motion + Lucide React + Radix UI",
        "inferred_experience_modality": matched["modality"],
        "design_thesis": {
            "recommended_specialist_skill": matched["specialist_skill"],
            "spatial_geometry": f"1:1 Structural DNA & Spatial Cadence of {input_data['reference_url']}" if input_data.get("reference_url") else matched["spatial_geometry"],
            "color_palette": matched["palette"],
            "typography_pairing": matched["typography"]
        },
        "needed_things": {
            "canonical_page_and_section_anatomy": matched["sections"],
            "interactive_conversion_modules": matched["interactive_modules"],
            "north_star_conversion_action": matched["north_star_cta"],
            "whatsapp_payload_template": matched["whatsapp_template"],
            "back_office_dispatch_hub": matched["back_office"]
        },
        "curated_live_benchmarks": matched["benchmarks"]
    }

    return result

def print_summary(result):
    """Outputs a rich, executive markdown summary to stdout."""
    print("=" * 80)
    print("  WEBSITE ARCHITECT: AUTONOMOUS BUSINESS CLASSIFICATION & REQUIREMENTS")
    print("=" * 80)
    print(f"\n🏢 BUSINESS NAME:      {result['business_name']}")
    print(f"🏷️ DETECTED CATEGORY:  {result['raw_category_detected']}")
    print(f"🎯 MATCHED ARCHETYPE:   {result['identified_archetype']}")
    print(f"✨ COMMERCIAL SUB-TYPE: {result['identified_sub_type']}")
    print(f"💰 REVENUE MODEL:       {result['primary_revenue_model']}")
    print(f"⏳ SCARCE RESOURCE:     {result['scarce_operational_resource']}")
    print(f"🧠 CUSTOMER MINDSET:    {result['customer_arrival_mindset']}")
    print(f"⚡ TARGET PERFORMANCE:  LCP {result['core_web_vitals_target']['lcp']}, CLS {result['core_web_vitals_target']['cls']}")
    
    ads = result['architecture_decision_score']
    print(f"\n📐 ARCHITECTURE TOPOLOGY (ADS SCORE: {ads['score']})")
    print(f"   Calculation: {ads['formula']}")
    print(f"   Result:      {ads['recommended_topology']}")
    print(f"   Rationale:   {ads['topology_rationale']}")
    if ads['detected_features_influencing_topology']:
        print(f"   Features Influencing Topology: {', '.join(ads['detected_features_influencing_topology'])}")
    print(f"   Tech Stack:  {result['universal_stack_standard']}")
    print(f"   Modality:    {result['inferred_experience_modality']}")
    
    print(f"\n🗺️ CANONICAL ROUTE ARCHITECTURE")
    for r in result['canonical_route_architecture']:
        print(f"   • {r['path']} ({r['name']}) -> {r['purpose']}")

    dt = result['design_thesis']
    print(f"\n🎨 DESIGN THESIS & AESTHETIC DNA")
    print(f"   Specialist Skill: {dt['recommended_specialist_skill']}")
    print(f"   Spatial Geometry: {dt['spatial_geometry']}")
    print(f"   Display Font:     {dt['typography_pairing']['display']}")
    print(f"   Body Font:        {dt['typography_pairing']['body']}")
    print(f"   Palette Tokens:   Background: {dt['color_palette']['background']}, Foreground: {dt['color_palette']['foreground']}, Accent: {dt['color_palette']['accent']}")
    
    nt = result['needed_things']
    print(f"\n📋 NEEDED THINGS: CANONICAL SECTION ANATOMY")
    for sec in nt['canonical_page_and_section_anatomy']:
        print(f"   [{sec['id']}] {sec['title']} ({sec['type']}): {sec['description']}")
        
    print(f"\n⚙️ NEEDED THINGS: INTERACTIVE CONVERSION MODULES (MUST-HAVES)")
    for mod in nt['interactive_conversion_modules']:
        print(f"   • {mod}")
        
    print(f"\n🎯 NORTH-STAR CONVERSION EVENT: {nt['north_star_conversion_action']}")
    print(f"   WhatsApp Payload Schema:\n   \"{nt['whatsapp_payload_template']}\"")
    print(f"   Back-Office Hub: {nt['back_office_dispatch_hub']}")
    
    print(f"\n🏆 CURATED LIVE BENCHMARK REFERENCES (Award-Winning Human Craft)")
    for b in result['curated_live_benchmarks']:
        print(f"   • {b['name']} ({b['url']})")
        print(f"     Visual DNA: {b['dna']}")
    print("=" * 80)

def main():
    parser = argparse.ArgumentParser(description="Autonomous Business Classification for Website Architect")
    parser.add_argument("--maps-data", help="Path to scraped maps_data.json file")
    parser.add_argument("--pitch", help="Raw business description or pitch string")
    parser.add_argument("--name", help="Business name override")
    parser.add_argument("--reference-url", help="URL of benchmark reference website to ground spatial geometry")
    parser.add_argument("--topology", choices=["spa", "mpa", "auto"], default="auto", help="Force Single-Page (spa) or Multi-Page (mpa)")
    parser.add_argument("--out", default="assets/business_profile.json", help="Path to write output profile JSON")
    args = parser.parse_args()

    input_data = {}
    if args.maps_data and os.path.exists(args.maps_data):
        with open(args.maps_data, "r", encoding="utf-8") as f:
            input_data = json.load(f)
        input_data["source"] = "google_maps_scrape"
    elif args.pitch:
        input_data = {
            "source": "business_pitch",
            "pitch": args.pitch,
            "title": args.name or (args.pitch.split()[0] if args.pitch else "Business")
        }
    else:
        print("[!] Error: Either --maps-data or --pitch must be provided.")
        sys.exit(1)

    if args.name:
        input_data["title"] = args.name
    if args.reference_url:
        input_data["reference_url"] = args.reference_url
    if args.topology and args.topology != "auto":
        input_data["topology"] = args.topology

    result = classify(input_data)
    
    # Save output
    out_dir = os.path.dirname(args.out)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print_summary(result)

if __name__ == "__main__":
    main()
