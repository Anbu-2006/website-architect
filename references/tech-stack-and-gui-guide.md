# Universal Omnipotent Frontend Architecture & Runtime Guide

## 1. The Autonomous Architectural Standard

To eliminate configuration friction and ensure industrial-grade scalability across 100% of commercial archetypes, the **`/website-architect`** engine enforces **one universal, omnipotent tech stack**:

$$\mathbf{Universal\ Stack} = \mathbf{Next.js\ 15\ (App\ Router)} + \mathbf{TypeScript} + \mathbf{Tailwind\ CSS\ v4} + \mathbf{Motion\ (Framer\ Motion)} + \mathbf{Lucide\ React} + \mathbf{Radix\ UI}$$

The agent **never prompts the user with tech stack questions**. It locks this universal foundation into every build because Next.js 15 App Router uniquely satisfies all extremes of the web spectrum:
- **Instant Speed (<0.8s FCP)**: Static route pre-rendering (`output: 'export'` or Edge CDN cache), sub-second initial paint, zero runtime bloat.
- **Rich Client Interactivity**: Seamless `"use client"` hydration boundaries for dynamic booking sliders, stay rate calculators, persistent cart drawers, and filter bars.
- **Fluid 60fps Motion**: Native GPU-accelerated compositor animations via `motion/react`, scroll timeline triggers, and spring physics.
- **Enterprise Full-Stack Capabilities**: Edge API routes, Server Actions, typed JSON-LD structured schemas, and webhook integrations (Stripe, n8n, WhatsApp).
- **Flagship 3D & Canvas**: Drop-in client boundary canvas for `@designcodeio/threeui`, Three.js scene graphs, or HTML5 60fps canvas scrollytelling.

---

## 2. Universal Stack Capabilities Matrix Across Commercial Mindsets

| Customer Arrival Mindset | Business Archetype Example | How the Universal Next.js 15 Stack Fulfills It Autonomously | Target CWV (LCP / CLS) |
| :--- | :--- | :--- | :--- |
| **Urgent / Convenience** | Highway Dining, Takeaway Counter, Emergency Trades | Static Pre-rendering (`next build`), Edge deployment, 1-tap phone dialer, WhatsApp redirect, zero runtime JS hydration block on initial paint. | **LCP < 0.6s**<br>CLS < 0.01 |
| **High-Ticket Experiential** | Luxury Farmstays, Boutique Resorts, Wedding Grounds | `"use client"` interactive booking engine, guest slider, real-time rate calculator, 60fps canvas scrollytelling, slide-out cart drawer. | **LCP < 1.2s**<br>CLS < 0.02 |
| **High-Volume Transactional** | Multi-SKU E-Commerce, Apparel, Electronics | Dynamic product catalog with React Server Components (RSC), Edge API search, Server Actions for checkout, persistent cart context. | **LCP < 1.4s**<br>CLS < 0.05 |
| **B2B Software & SaaS** | Developer Platforms, Cloud Observability, API Hubs | Interactive ROI calculators, tiered billing switchers, animated terminal demos (`magicuidesign-mcp`), SOC 2 trust strips. | **LCP < 1.2s**<br>CLS < 0.02 |
| **Brand Statement / Flagship** | Luxury Automotive, Consumer Electronics Launch | Dynamic Three.js WebGL canvas or 60fps image sequence scrubbing with LCP poster safety image and `prefers-reduced-motion` bypass. | **LCP < 1.8s**<br>CLS < 0.05 |

---

## 3. Autonomous Experience Modality Inference & Stack Configuration

The engine automatically infers the **Experience Modality** from the business archetype and configures the Next.js 15 architecture accordingly:

### Modality 1: High-Utility & Velocity Engine
- **Archetypes**: Local Dining, Emergency Services, Healthcare Clinics, Professional Law Practices, Quick-Service Counters.
- **Architectural Recipe**:
  - Pre-rendered Server Components (`page.tsx`) for maximum TTFB and sub-0.8s LCP.
  - Sticky Top/Bottom Action Bar (`Quick Call`, `Directions`, `Book Now`) with CSS `:focus-visible` styling.
  - Inline zero-layout-shift micro-interactions (`motion.button` tap scaling `0.98`).
  - Next.js dynamic OpenGraph and JSON-LD schema tags automatically injected into `layout.tsx`.

### Modality 2: Hybrid Scrollytelling & Visual Commerce Engine
- **Archetypes**: Luxury Farmstays, Boutique Hotels, High-End Venues, Artisan Products, Design Agencies.
- **Architectural Recipe**:
  - Sticky hero with layered ambient 60fps video loop (`<video autoPlay loop muted playsInline>`).
  - Interactive Client Island (`"use client"`): Room/Service picker with dynamic rate calculator ($Rate = Base \times Guests \times Days$) and direct WhatsApp payload formulation.
  - Asymmetric 60/40 editorial grid with scroll-triggered fade-up cards via `motion.div` (`whileInView={{ opacity: 1, y: 0 }}`).
  - Accessible image carousel with hardware-accelerated swipe and keyboard arrow navigation.

### Modality 3: Full Canvas & Immersive WebGL Engine
- **Archetypes**: Flagship Tech Products, Luxury Fashion Lines, Interactive 3D Showcases.
- **Architectural Recipe**:
  - Client Boundary Canvas (`<CanvasErrorBoundary><ImmersiveCanvas /></CanvasErrorBoundary>`).
  - ThreeUI / Three.js scene loaded via `next/dynamic` with `ssr: false` to ensure zero hydration mismatch.
  - **LCP Safety Poster**: Static WebP/AVIF hero image rendered in the HTML DOM; WebGL canvas mounts behind/over it after initial paint.
  - Strict `prefers-reduced-motion` listener: gracefully disables WebGL camera orbits and falls back to a clean, high-contrast visual photo grid.

---

## 4. Production Foundation & Dependency Standard

Every `/website-architect` production build initializes with this verified standard:

```json
{
  "name": "production-website",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "next": "^15.1.0",
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "motion": "^12.0.0",
    "lucide-react": "^0.470.0",
    "@radix-ui/react-dialog": "^1.1.4",
    "@radix-ui/react-dropdown-menu": "^2.1.4",
    "@radix-ui/react-accordion": "^1.2.2",
    "@radix-ui/react-slot": "^1.1.1",
    "clsx": "^2.1.1",
    "tailwind-merge": "^2.6.0"
  },
  "devDependencies": {
    "typescript": "^5.7.0",
    "@types/node": "^22.0.0",
    "@types/react": "^19.0.0",
    "@types/react-dom": "^19.0.0",
    "tailwindcss": "^4.0.0",
    "@tailwindcss/postcss": "^4.0.0",
    "postcss": "^8.5.0"
  }
}
```

### Tailwind CSS v4 Theme Standard (`src/app/globals.css`)
```css
@import "tailwindcss";

@theme {
  --font-display: var(--font-heading, "Outfit", sans-serif);
  --font-body: var(--font-body, "Inter", sans-serif);
  
  --color-brand-primary: var(--primary);
  --color-brand-accent: var(--accent);
  --color-brand-surface: var(--surface);
  --color-brand-text: var(--text-main);
  --color-brand-muted: var(--text-muted);
  
  --spacing-section: clamp(4rem, 8vw, 8rem);
  --radius-subtle: 8px;
  --radius-card: 16px;
  --radius-pill: 9999px;
}
```

---

## 5. Architectural Quality Guardrails

1. **Zero Raw Hex in JSX**: All colors must reference CSS custom properties or Tailwind tokens defined in `globals.css` / `DESIGN.md`.
2. **Strict Semantic Structure**: Every canonical route must contain exactly one `<h1>`, structured `<header>`, `<main>`, `<section>`, and `<footer>`.
3. **No Hash Anchor Illusion**: Section routing must NEVER use fake anchor hashes (`#contact`, `#menu`) when representing primary canonical pages. Multi-page architecture uses clean Next.js App Router paths (`/menu`, `/suites`, `/contact`).
4. **Interactive Form Resilience**: Forms must never pre-disable submit buttons, never block paste, must submit on `Enter`, and must validate inline with clear, high-contrast error states.
5. **Compositor-Only Animations**: Animations must only touch `transform` and `opacity`. Never animate `top`, `left`, `width`, or `height`.
