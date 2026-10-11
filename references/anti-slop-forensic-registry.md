# Anti-Slop Forensic Registry & Engineering Standards

> **Website Architect Reference Standard — Version 2.4.0**  
> *Authoritative Forensic Matrix, Mathematical Guardrails, and AST Enforcement Contracts.*

---

## 1. Executive Summary & Forensic Rationale

Commercial websites engineered with generic AI defaults suffer from predictable visual and technical degradation: identical 3-card symmetrical feature rows, floating ungrounded purple/cyan blur blobs, cards nested inside cards without spatial logic, fake "10k+ Happy Customers" metric counters, layout thrashing from JavaScript accordion height measurements, and inaccessible touch/zoom behavior on mobile devices.

This registry codifies the **18 Anti-Slop Engineering Rules** enforced by the `anti_slop_gate.py` AST validator and establishes the canonical **ALWAYS vs NEVER** production standards for all websites built under `website-architect`.

---

## 2. The 18 Anti-Slop Forensic Rules & Enforcement Matrix

| Rule ID | Anti-Pattern | Forensic Failure Mode | Mandated Production Remediation |
| :--- | :--- | :--- | :--- |
| **`SLOP_PURPLE_GRADIENT`** | `bg-gradient-to-r from-purple-500 to-indigo-600` | Generic SaaS template cliché; destroys brand distinctiveness. | Single calibrated semantic brand accent (e.g., OKLCH `oklch(0.48 0.14 150)`) with monochromatic ink contrast. |
| **`SLOP_3CARD_KIT`** | `grid-cols-3` or `col-span-4` (3 identical cards) | Uniform visual rhythm, cognitive numbness, zero information hierarchy. | **Asymmetric Bento Grid 2.0**: 8-column primary showcase cell + 4-column secondary vertical telemetry stack. |
| **`SLOP_BLUR_BLOB`** | `blur-3xl`, `blur-[120px]` floating background blobs | Ungrounded cosmic vapor, GPU compositor memory pressure, unanchored lighting. | Grounded ambient lighting via pseudo-elements tied to physical card borders or structured CSS mesh grids. |
| **`SLOP_CARD_CEPTION`** | Card wrapper enclosing sub-cards with redundant borders | Nested container syndrome; cognitive clutter; broken padding rhythm. | Flat bento grid hierarchy; border applied once to outer parent; child elements structured via typography and whitespace. |
| **`SLOP_ANCHOR_ILLUSION`** | `<a href="#services">` or `<a href="#pricing">` | Anchor hash jumps creating illusion of content while generating zero indexable URLs. | Next.js App Router multi-page routing (`/services`, `/pricing`, `/about`, `/contact`) with rich multi-section pages. |
| **`SLOP_MAGIC_METRIC`** | Unsubstantiated "10k+ Clients", "99.9% Uptime", "500% ROI" | Fabricated credibility markers that trigger customer distrust. | Verified domain telemetry: authenticated Google Maps ratings, ISO certifications, exact historical founding dates. |
| **`SLOP_SKELETON_SUBPAGE`**| 1-section stub page (Hero + empty form/placeholder) | Incomplete subpage scaffolding abandoned mid-generation. | Subpages MUST contain $\ge$ 4 to 6 full structural sections (Hero, Features, Direct Concierge, GPS/Map, FAQ, Footer). |
| **`DEFECT_MOBILE_ZOOM`** | `input`, `select`, `textarea` with `font-size < 16px` | Triggers aggressive iOS Safari auto-zoom viewport distortion. | Explicit `text-base` or `@media (max-width: 768px) { font-size: 16px !important; }` in CSS baseline. |
| **`DEFECT_TOUCH_TARGET`** | Interactive elements with hit boxes `< 44px` | Violates WCAG 2.5.5 / 2.5.8 target size; high misclick rate on mobile. | Minimum hit box `min-h-[44px] min-w-[44px]` with `touch-action: manipulation`. |
| **`DEFECT_STICKY_HOVER`** | `:hover` styles persisting indefinitely after mobile tap | Sticky ghost hover states degrading mobile touch navigation. | Guard interactive hover states with `@media (hover: hover) and (pointer: fine)`. |
| **`DEFECT_REDUCED_MOTION`**| Continuous loops, parallax, and heavy transforms without media query | Causes vestibular disorientation and motion sickness for sensitive users. | Global `@media (prefers-reduced-motion: reduce)` reset enforcing zero animation duration and instant transforms. |
| **`DEFECT_FOCUS_RING`** | `outline: none` without replacement `:focus-visible` ring | Traps keyboard navigators; violates WCAG 2.4.7 Focus Visible. | Unobscured `:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }`. |
| **`SLOP_GENERIC_AVATAR`** | `unsplash.com/photo-1534528741775` stock headshots | Fake team members or generic placeholder testimonials. | Editorial client initials in typographic tokens, verified customer reviews, or authentic team photos. |
| **`SLOP_ACCORDION_THRASH`**| JS height animation (`element.offsetHeight` / `maxHeight: 1000px`) | Forces synchronous CPU layout recalculation on every animation frame. | **Zero-JS CSS Grid Layout**: `grid-template-rows: 0fr -> 1fr` on `overflow: hidden; min-height: 0;`. |
| **`SLOP_FLAT_SHADOW`** | `box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1)` single-layer shadow | Inverted lighting illusion; looks muddy and artificial on dark mode. | **Layered Umbra/Penumbra**: Subtle key shadow + diffuse ambient shadow using OKLCH neutral tokens. |
| **`SLOP_BORDER_CONTRAST`**| High-contrast solid borders (`border-gray-700`, `border-black`) | Sharp harsh outlines that fragment visual continuity. | Semi-transparent crisp border tokens (`border-white/10` or `oklch(var(--border) / 0.4)`). |
| **`SLOP_EMOJI_ICON`** | Emoji symbols (`🚀`, `💡`, `✨`, `🔥`) used as UI icons | Inconsistent cross-platform rendering; looks unpolished and amateur. | Unified SVG iconography (Lucide, Heroicons, or Material Symbols) styled with matching stroke widths. |
| **`DEFECT_PRE_DISABLED_BTN`**| Submit buttons rendered with `disabled` attribute prior to user input | Prevents users from discovering what validation fields are missing. | Keep buttons enabled; validate on click; scroll to and focus the first invalid field with inline error message. |

---

## 3. High-Craft Architectural Patterns & Code Blueprints

### 3.1 Fluid Type Clamping Formula
Never rely on stepped media queries (`text-3xl sm:text-5xl md:text-7xl`) which cause sudden jarring line wrapping during window resizing. Apply linear interpolation clamped across standard viewport extremes ($375\text{px} \to 1440\text{px}$):

$$\text{font-size} = \text{clamp}(V_{\min}, \text{intercept} + \text{slope} \cdot \text{vw}, V_{\max})$$

For an $H_1$ scaling from $40\text{px}$ ($2.5\text{rem}$) at $375\text{px}$ viewport to $80\text{px}$ ($5.0\text{rem}$) at $1440\text{px}$ viewport:
- Slope: $\frac{80 - 40}{1440 - 375} = \frac{40}{1065} \approx 0.03756$ ($3.76\text{vw}$)
- Intercept: $40 - (375 \times 0.03756) = 25.92\text{px} \approx 1.62\text{rem}$

```css
/* Production Fluid Hero Typography */
h1.hero-title {
  font-size: clamp(2.5rem, 1.62rem + 3.76vw, 5rem);
  letter-spacing: -0.04em;
  line-height: 1.05;
}
```

---

### 3.2 Asymmetric Bento Grid 2.0 (Structural Blueprint)
Replaces the uniform 3-card kit with hierarchical spatial storytelling:

```tsx
<div className="grid grid-cols-1 lg:grid-cols-12 gap-6 min-h-0">
  {/* 1. Primary Showcase Cell (8 Columns / 2 Rows) */}
  <div className="lg:col-span-8 lg:row-span-2 group relative overflow-hidden rounded-sm bg-surface border border-border/40 p-8 flex flex-col justify-between">
    <div className="relative aspect-[16/10] w-full overflow-hidden rounded-sm mb-6">
      <Image
        src="/assets/showcase.jpg"
        alt="Flagship Offering"
        fill
        sizes="(max-width: 1024px) 100vw, 66vw"
        className="object-cover transition-transform duration-700 group-hover:scale-105"
      />
    </div>
    <div className="space-y-4">
      <span className="text-[11px] uppercase tracking-widest font-mono text-ink-muted">Flagship Suite</span>
      <h3 className="font-display text-3xl font-light text-ink">Forest Pavilion & Private Sanctuary</h3>
      <p className="text-sm text-ink-muted leading-relaxed font-body">1,800 sq ft standalone pavilion...</p>
    </div>
  </div>

  {/* 2. Secondary Supporting Cell (4 Columns) */}
  <div className="lg:col-span-4 rounded-sm bg-surface border border-border/40 p-6 flex flex-col justify-between">
    <div className="relative aspect-[4/3] w-full overflow-hidden rounded-sm mb-4">
      <Image src="/assets/dining.jpg" alt="Artisanal Dining" fill sizes="(max-width: 1024px) 100vw, 33vw" className="object-cover" />
    </div>
    <h4 className="font-display text-xl font-normal text-ink">Estate Gastronomy</h4>
  </div>

  {/* 3. Verified Proof & Telemetry Cell (4 Columns) */}
  <div className="lg:col-span-4 rounded-sm bg-surface border border-border/40 p-6 flex flex-col justify-between">
    <div className="space-y-2">
      <span className="text-[10px] uppercase tracking-widest font-mono text-ink-muted">Authentication</span>
      <h4 className="font-display text-2xl font-light text-ink">4.9 / 5.0 Rating</h4>
      <p className="text-xs text-ink-muted leading-relaxed font-body">1,400+ verified guest assessments.</p>
    </div>
  </div>
</div>
```

---

### 3.3 Zero-JS CSS Grid Accordion (Auto-Height Animation)
Eliminates JavaScript `scrollHeight` measurements that trigger forced synchronous reflows:

```tsx
<div
  style={{
    display: "grid",
    gridTemplateRows: isOpen ? "1fr" : "0fr",
    transition: "grid-template-rows 300ms cubic-bezier(0.16, 1, 0.3, 1)"
  }}
>
  <div style={{ overflow: "hidden", minHeight: 0 }}>
    <div className="px-6 pb-6 text-sm text-ink-muted leading-relaxed font-body font-light">
      {faq.answer}
    </div>
  </div>
</div>
```

---

### 3.4 Enterprise Footer with Live Office Telemetry & JSON-LD
Commercial websites must convey operational legitimacy through live global office statuses and search engine crawlable Schema metadata:

```tsx
<footer className="relative bg-stone-950 text-white pt-24 pb-12 px-6 border-t border-white/10" role="contentinfo">
  {/* JSON-LD Structured Data */}
  <script
    type="application/ld+json"
    dangerouslySetInnerHTML={{
      __html: JSON.stringify({
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": "The Odyssey Retreat",
        "telephone": "+91 98450 12345",
        "aggregateRating": {
          "@type": "AggregateRating",
          "ratingValue": "4.8",
          "reviewCount": "1200"
        }
      })
    }}
  />

  {/* Live Telemetry Clocks */}
  <div className="grid grid-cols-1 md:grid-cols-3 gap-6 py-8 border-y border-white/10 mb-16">
    {telemetry.map((off) => (
      <div key={off.city} className="flex items-center justify-between font-mono text-xs text-stone-400">
        <span>{off.city}</span>
        <div className="flex items-center gap-2">
          <span className={`inline-block w-2 h-2 rounded-full ${off.isOpen ? "bg-emerald-500 animate-pulse" : "bg-stone-600"}`} />
          <span>{off.localTime} &bull; {off.isOpen ? "Desk Open" : "Inquiries Active"}</span>
        </div>
      </div>
    ))}
  </div>
</footer>
```

---

## 4. AST Gate Verification CLI
To audit any project codebase against this entire forensic matrix prior to delivery:
```bash
python scripts/anti_slop_gate.py --project-root .
```
Every pull request and build must achieve **Zero Fatal Violations** and **Zero High-Severity Anti-Slop Flags**.
