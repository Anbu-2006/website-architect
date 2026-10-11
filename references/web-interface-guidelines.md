# Web Interface Guidelines & Authoritative AGENTS.md Rulebook

> **Authoritative UI/UX Implementation Standards for `/website-architect`**  
> Synthesized from Vercel Labs' *Web Interface Guidelines* and *AGENTS.md* specification.  
> Interfaces succeed because of hundreds of choices. All agents, builders, and frontend workflows MUST adhere to these framework-agnostic and React/Next.js decisions.

---

## 1. Quick Reference: MUST / SHOULD / NEVER Rule Matrix

```
┌────────────────────────────────────────────────────────────────────────┐
│                   WEB INTERFACE GUIDELINES MATRIX                      │
├─────────────────────┬──────────────────────────────────────────────────┤
│ MUST                │ • Full keyboard support per WAI-ARIA APG         │
│                     │ • Visible, unobscured focus rings (:focus-visible)│
│                     │ • Hit target ≥ 24px (mobile ≥ 44px)              │
│                     │ • Mobile <input> font-size ≥ 16px (no iOS zoom)  │
│                     │ • Hydration-safe inputs (no lost focus/value)    │
│                     │ • Links use <a> or <Link> for navigation         │
│                     │ • Animate compositor-friendly (transform, opacity│
│                     │ • Skeletons mirror final content (zero CLS)      │
│                     │ • color-scheme: dark on <html> for dark themes   │
│                     │ • Native <select> explicit bg & color (Windows)  │
├─────────────────────┼──────────────────────────────────────────────────┤
│ SHOULD              │ • Optimistic UI updates with rollback / Undo     │
│                     │ • URL reflects state (deep-link filters/tabs/nuqs│
│                     │ • Tabular numbers (font-variant-numeric: tabular-│
│                     │ • Layered shadows (ambient + direct)             │
│                     │ • Nested radii (child ≤ parent, concentric)      │
│                     │ • translate="no" on brand names & code tokens    │
│                     │ • <video autoplay muted loop> over animated GIF  │
├─────────────────────┼──────────────────────────────────────────────────┤
│ NEVER               │ • NEVER outline: none without focus replacement  │
│                     │ • NEVER disable browser zoom (user-scalable=no)  │
│                     │ • NEVER block paste in <input> or <textarea>     │
│                     │ • NEVER use <div onClick> for page navigation    │
│                     │ • NEVER transition: all (list properties)        │
│                     │ • NEVER animate layout props (top, left, width)  │
│                     │ • NEVER pre-disable submit button on forms       │
└─────────────────────┴──────────────────────────────────────────────────┘
```

---

## 2. Interactions & Keyboard Operability

### 2.1 Keyboard
* **MUST: Full keyboard support per [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/patterns/)**: Every interactive flow (dialogs, dropdowns, menus, tabs, accordions) is keyboard operable with Tab, Shift+Tab, Arrow keys, Enter, and Escape.
* **MUST: Clear, unobscured focus rings**: Use `:focus-visible` rather than `:focus` to avoid distracting pointer users. Group controls with `:focus-within`. Sticky headers, footers, banners, and modal overlays must **never** cover the focused element.
* **MUST: Manage focus**: When opening modals or drawers, trap focus within the dialog; return focus to the triggering element upon close.
* **NEVER: `outline: none`**: Never remove outlines without providing an accessible, high-contrast replacement focus indicator.

### 2.2 Targets & Touch
* **MUST: Match visual and hit targets**: Minimum hit target is **≥ 24px** on desktop and **≥ 44px** on mobile. If the visual element is smaller than 24px (e.g. an icon button), expand its interactive bounding box with padding or negative margin.
* **MUST: Mobile input size**: `<input>` font size must be **≥ 16px** on mobile viewports to prevent iOS Safari auto-zoom/pan on focus. Alternatively, set `<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />`.
* **NEVER: Disable browser zoom**: Never lock user scale (`user-scalable=no`, `maximum-scale=1` without 16px inputs).
* **MUST: `touch-action: manipulation`**: Prevent the 300ms double-tap zoom delay on interactive controls and buttons.
* **SHOULD: Tap highlight follows design**: Set `-webkit-tap-highlight-color` to match your brand palette or transparent if custom active states exist.

### 2.3 Forms & Inputs
* **MUST: Hydration-safe inputs**: Inputs must not lose focus or typed value upon client-side hydration. Inputs with `value` require `onChange` (or use uncontrolled `defaultValue`).
* **NEVER: Block paste**: Never prevent users from pasting into `<input>` or `<textarea>` fields (especially passwords, OTPs, or credit card numbers).
* **MUST: Loading buttons**: Show an inline spinner and preserve the original label text. Do not replace the button label with just a spinner unless dimensions are strictly reserved.
* **MUST: Minimum loading-state duration**: When displaying a spinner or skeleton, add a show-delay (~150–300ms) and minimum visible duration (~300–500ms) to prevent visual jarring and flickering on rapid network responses (React `<Suspense>` handles this).
* **MUST: Enter submits**: When a single text input is focused, Enter submits. In a `<textarea>`, Enter inserts a newline, while `⌘/Ctrl + Enter` submits.
* **MUST: Submission rule & idempotency**: Keep the submit button enabled until the user clicks it. Disable it during the in-flight network request, show a spinner, and generate an idempotency key.
* **MUST: Don't block typing**: Even if a field only accepts numeric values (e.g., zip code or phone), allow keystrokes and validate asynchronously. Blocking keystrokes leaves users confused.
* **MUST: Don't pre-disable submit buttons**: Allow users to submit incomplete forms so inline field-level validation highlights errors. Pre-disabled buttons force users to hunt for what is missing.
* **MUST: Error placement & focus**: Place error messages directly adjacent to the offending input; upon failed submit, automatically focus the first invalid input.
* **MUST: Autocomplete & inputmode**: Always set appropriate `autocomplete` tokens (`name`, `email`, `tel`, `address-line1`, `one-time-code`) and `inputmode` (`numeric`, `decimal`, `email`, `tel`, `url`).
* **SHOULD: Selective spellcheck**: Set `spellcheck="false"` on usernames, email addresses, API keys, codes, and URLs.
* **MUST: Text expansion trim**: Strip accidental trailing whitespace added by mobile keyboards before validation.
* **MUST: No dead zones on checkboxes/radios**: The input control and its `<label>` share a single generous bounding box.
* **MUST: Warn on unsaved changes**: Prompt the user with a `beforeunload` dialog before navigating away from dirty forms.

### 2.4 Navigation & State
* **MUST: URL as state**: Persist filter criteria, active tab indexes, pagination offsets, and search queries in the URL (`nuqs` or search params) so refresh, bookmarking, and Back/Forward work seamlessly.
* **MUST: Scroll position restoration**: Back/Forward browser navigation must restore prior scroll coordinates.
* **MUST: Links are links**: Navigation elements MUST use semantic `<a>` or framework `<Link>` tags. Never use `<div onClick>` or `<button>` for routing, ensuring Cmd/Ctrl+Click and right-click "Open in new tab" function natively.
* **SHOULD: Optimistic UI**: Reflect updates immediately on optimistic interactions; reconcile on server response. On failure, rollback state and display an inline error toast with an Undo action.
* **MUST: Confirm destructive actions**: Destructive actions (deletions, purges) must require explicit modal confirmation or provide an immediate Undo toast window (5–10s).
* **MUST: Announce async updates**: Use polite `aria-live="polite"` for non-disruptive notifications, toast messages, and validation feedback.

### 2.5 Touch & Drag
* **MUST: Delay tooltip sequence**: Delay the initial tooltip in a group (300–500ms); subsequent sibling peers display instantly.
* **MUST: Overscroll containment**: Set `overscroll-behavior: contain` inside modal dialogs and slide-out drawers to prevent background page bounce.
* **MUST: Clean drag interactions**: Disable text selection (`user-select: none`) and set `inert` on dragged elements so hover and text selection do not clash.
* **MUST: Gesture alternatives**: Drag, swipe, and pinch gestures must have accessible click/tap button alternatives.

---

## 3. Animation & Motion Engineering

* **MUST: Honor `prefers-reduced-motion`**:
  ```css
  @media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
      animation-duration: 0.01ms !important;
      animation-iteration-count: 1 !important;
      transition-duration: 0.01ms !important;
      scroll-behavior: auto !important;
    }
  }
  ```
* **SHOULD: Implementation hierarchy**: Prefer CSS transitions/animations > Web Animations API > JavaScript animation engines (`motion` or GSAP).
* **MUST: Compositor-friendly properties only**: Animate only GPU-accelerated properties (`transform`, `opacity`).
* **NEVER: Animate layout properties**: Never animate `top`, `left`, `right`, `bottom`, `width`, `height`, `margin`, or `padding` as they force expensive CPU reflows and layout repaints.
* **NEVER: `transition: all`**: Explicitly declare animated properties (e.g. `transition: transform 0.2s cubic-bezier(0.2, 0, 0, 1), opacity 0.2s ease`). `transition: all` introduces accidental jank.
* **SHOULD: Easing fits the subject**: Use natural easing curves matching physical mass. Entry reveals: deceleration curves (`cubic-bezier(0, 0, 0.2, 1)` or `ease-out`); Exit transitions: acceleration curves (`ease-in`).
* **MUST: Interruptible & input-driven**: Animations must be cancellable by user clicks or keypresses.
* **MUST: Autoplay controls**: Autoplaying background motion lasting longer than 5 seconds must provide visible pause, stop, or hide controls.
* **MUST: Correct transform origin**: Explicitly anchor `transform-origin` to where the motion physically initiates (e.g. `transform-origin: top right` for dropdown menus).
* **MUST: Cross-browser SVG transforms**: Apply CSS transforms to `<g>` wrappers and specify:
  ```css
  transform-box: fill-box;
  transform-origin: center;
  ```

---

## 4. Layout & Responsive Geometry

* **SHOULD: Optical alignment**: Manually nudge elements ±1px when human perception beats mathematical geometry (e.g. play icons in round buttons).
* **MUST: Deliberate alignment**: Every UI element must align to a defined grid line, typographic baseline, edge, or optical center. Eliminate accidental positioning.
* **SHOULD: Balance contrast in lockups**: When an icon sits beside text, adjust stroke-width, size, or color to match visual weight (e.g. 1.75px stroke for medium text).
* **MUST: Responsive coverage**: Verify layouts across mobile (390px), laptop (1440px), and ultra-wide screens (simulate ultra-wide by zooming out to 50%).
* **MUST: Respect safe areas**: Support notched displays, home indicators, and mobile cutouts:
  ```css
  padding-top: env(safe-area-inset-top);
  padding-bottom: env(safe-area-inset-bottom);
  padding-left: env(safe-area-inset-left);
  padding-right: env(safe-area-inset-right);
  ```
* **MUST: Eliminate unwanted scrollbars**: Prevent horizontal layout overflow (`overflow-x: clip` or `hidden` on root). Test with macOS "Show scroll bars: Always" enabled.
* **SHOULD: Browser-native layout**: Leverage CSS Flexbox, Grid, and `min-width: 0` on flex children instead of computing element dimensions in JavaScript.

---

## 5. Content, Typography & Accessibility

* **SHOULD: Inline help first**: Provide concise inline explanations; use hover tooltips only as a last resort for secondary metadata.
* **MUST: Stable skeletons**: Skeleton loading states must match the exact dimensions, aspect ratio, and typography scale of final content to eliminate Cumulative Layout Shift (CLS).
* **MUST: Accurate page titles**: Update document `<title>` to reflect current page context, active record, or unsaved status.
* **MUST: No dead ends**: Every empty state, search zero-result, and error view must offer a recovery action (e.g., "Clear filters", "Create first item", "Back to dashboard").
* **MUST: All states designed**: Every component must account for 4 distinct states:
  1. *Empty state* (first-time user, 0 items)
  2. *Sparse state* (1–2 items)
  3. *Dense state* (100+ items, long strings, overflow)
  4. *Error state* (network failure, permission denied)
* **SHOULD: Typographic quotes & punctuation**: Use curly quotes (“ ”) over straight quotes (" "), and the real ellipsis character (`…` `\u2026`) instead of three consecutive periods (`...`).
* **SHOULD: Avoid widows and orphans**: Apply `text-wrap: balance` on headlines and `text-wrap: pretty` on body copy.
* **MUST: Tabular numbers**: Set `font-variant-numeric: tabular-nums` or a monospace font whenever numbers are compared in tables, pricing cards, counters, or timers.
* **MUST: Redundant status cues**: Never convey state through color alone. Combine color indicators with clear text labels or distinct vector icons.
* **MUST: Icons have labels**: Icon-only buttons must include an explicit, descriptive `aria-label`. Decorative icons must be hidden with `aria-hidden="true"`.
* **MUST: Anchored headings**: Ensure internal anchor links clear sticky headers:
  ```css
  h1, h2, h3, h4, section[id] {
    scroll-margin-top: calc(var(--header-height, 72px) + 24px);
  }
  ```
* **MUST: Resilient to user-generated content**: Text containers must handle extremely long strings with `overflow-wrap: break-word` and flex children must specify `min-width: 0`.
* **MUST: Locale-aware formats**: Format currencies, dates, times, and delimiters with browser-native `Intl.NumberFormat` and `Intl.DateTimeFormat`.
* **SHOULD: Shield technical content from auto-translation**: Wrap brand names, code snippets, tokens, and technical identifiers with `translate="no"` to prevent browser translation engines from breaking syntax.
* **MUST: Non-breaking spaces for units & shortcuts**: Use `&nbsp;` to prevent awkward line breaks:
  - Units: `10&nbsp;MB`, `24&nbsp;px`, `$280&nbsp;/ night`
  - Keyboard shortcuts: `⌘&nbsp;+&nbsp;K`, `Ctrl&nbsp;+&nbsp;Enter`
  - Proper brand names: `Vercel&nbsp;SDK`, `Krishi&nbsp;Farms`

---

## 6. Performance & Asset Delivery

* **MUST: Zero image-caused CLS**: All `<img>` and `<video>` tags must specify explicit `width` and `height` attributes or CSS `aspect-ratio`.
* **MUST: Preload above-the-fold media**: Set `fetchpriority="high"` and `loading="eager"` on the signature hero image; set `loading="lazy"` on all images below the fold.
* **MUST: Preconnect to critical CDNs**: Add `<link rel="preconnect" href="https://fonts.googleapis.com">` (with `crossorigin`) to eliminate DNS/TLS latency.
* **SHOULD: Preload critical fonts**: Add `<link rel="preload" as="font" type="font/woff2" crossorigin>` with `font-display: swap` for display headers.
* **MUST: Virtualize large lists**: Any data table or catalog rendering >50 items must use list virtualization (e.g. `virtua` or `@tanstack/react-virtual`) or `content-visibility: auto`.
* **SHOULD: Video over animated GIF**: Loop animations using `<video autoplay muted loop playsinline>` rather than GIF (shrinking file size by 80–90%). Always provide a still poster fallback.
* **MUST: Network latency budget**: User actions via `POST`/`PATCH`/`DELETE` must target perceived completion within `< 500ms`.

---

## 7. Theming, Dark Mode & Visual Polish

* **MUST: `color-scheme: dark`**: When dark mode is active, style the root `<html>` element with `color-scheme: dark` so scrollbars and native device UI render with correct contrast.
* **SHOULD: Browser UI matches canvas**: Align browser chrome color by injecting `<meta name="theme-color" content="#FAF8F5">` (or `#0F172A` in dark mode).
* **MUST: Windows `<select>` background fix**: Native `<select>` elements must explicitly declare `background-color` and `color` to prevent dark-mode illegibility on Windows:
  ```css
  select, option {
    background-color: var(--color-surface);
    color: var(--color-ink);
  }
  ```
* **SHOULD: Layered shadows**: Combine ambient and direct light into multi-layer shadows:
  ```css
  box-shadow: 
    0 1px 2px rgba(0, 0, 0, 0.04), 
    0 8px 24px -4px rgba(0, 0, 0, 0.08);
  ```
* **SHOULD: Crisp borders**: Combine hairline semi-transparent borders with subtle depth shadows for high edge clarity.
* **SHOULD: Nested radii (Concentric curves)**: Child corner radius must be less than or equal to parent radius:
  $$r_{\text{child}} = r_{\text{parent}} - \text{padding}$$
* **SHOULD: Hue consistency**: On non-neutral surfaces, tint borders, shadows, and secondary ink toward the primary background hue.
* **MUST: Contrast compliance**: All normal text must achieve ≥ 4.5:1 (WCAG AA); large text (≥ 18pt / 24px) ≥ 3:1. Prefer APCA for perceptual accuracy.
* **MUST: Interaction contrast escalation**: Active, hover, and focused states must exhibit higher contrast than rest states.

---

## 8. High-Craft Copywriting Rules

* **Active voice**: Use direct imperative phrasing ("Install the CLI", "Confirm booking", "Save API Key").
* **Title Case Chicago**: Apply Title Case for headlines and primary CTA buttons ("Explore Curated Suites", "Reserve Weekend Table").
* **Action-oriented**: Replace generic buttons like "Continue" or "Submit" with specific outcome declarations ("Confirm Reservation", "Place Order", "Download Whitepaper").
* **Numerals for counts**: Write "8 deployments" and "4 guests" instead of "eight deployments" or "four guests".
* **Error messages guide the exit**: Never just state what failed. Explain how to fix it:
  - *Bad:* "Invalid date range."
  - *Good:* "Check-out date must be after check-in. Select a departure date between Oct 12 and Oct 15."
* **Default to constructive language**: Frame errors as helpful next steps rather than system accusations.
