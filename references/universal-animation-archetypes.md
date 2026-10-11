# Universal Animation Archetypes & Sourcing Reference Guide

## 1. Overview
Modern Awwwards, Godly, and Siteinspire websites achieve emotional impact through intentional motion choreography. This guide indexes the **30 Universal Web Animation Archetypes**, mapping each directly to battle-tested, 100% free open-source component implementations (Magic UI, Aceternity UI, 21st.dev, Framer Motion, and GSAP).

---

## 2. The 30 Universal Web Animation Archetypes Matrix

| # | Archetype | Visual Description | Implementation Source | Sourcing / Install Command |
|---|---|---|---|---|
| **1** | **Infinite Marquee** | Seamless horizontal rolling stream of brand logos, customer quotes, or awards | Magic UI Marquee | `npx shadcn@latest add @magicui/marquee` |
| **2** | **Sticky Stacking Bento** | Pinned cards that scale down and stack with subtle elevation shadows as user scrolls | Aceternity BentoGrid | `npx shadcn@latest add @aceternity/bento-grid` |
| **3** | **Cursor Spotlight** | Radial gradient flashlight tracking mouse cursor across dark surfaces | Aceternity Spotlight | `npx shadcn@latest add @aceternity/spotlight` |
| **4** | **Text Split Scramble** | Matrix-style character scrambling resolving into editorial headlines | ReactBits ScrambleText | `npx shadcn@latest add @reactbits/scramble` |
| **5** | **Curtain Clip-Path Reveal** | Section unveiling via animating `clip-path: inset(0 0 0 0)` or polygon curtains | NudaUI ClipReveal / Framer Motion | Direct CSS / Framer Motion variant |
| **6** | **Card Tilt Parallax** | 3D perspective tilt reacting to mouse position with specular highlight | Fancy Components TiltCard | `npx 21st-dev add tilt-card` |
| **7** | **Ken-Burns Zoom** | Slow 15s cinematic pan and scale (1.0 -> 1.15) over photography | Tailwind `@keyframes` | Built-in `animate-ken-burns` |
| **8** | **Navbar Blur Shrink** | Transparent header transitioning to compact glassmorphic blur pill on scroll | Magic UI Navbar | `npx shadcn@latest add @magicui/navbar` |
| **9** | **Horizontal Scroll Strip** | Vertical page scroll converting into smooth horizontal gallery translation | GSAP ScrollTrigger | `npm i gsap` with `ScrollTrigger.create({ scrub: true })` |
| **10** | **Accordion Spring Reveal** | Physics-based spring layout transition on expanding/collapsing FAQ items | Framer Motion AnimatePresence | `npx shadcn@latest add accordion` |
| **11** | **Text Gradient Sweep** | Shimmering multi-stop gradient sweeping horizontally across display typography | Tailwind text-transparent bg-clip-text | Built-in `animate-gradient` |
| **12** | **Magnetic Button** | CTA button pulling toward the cursor on hover with spring elasticity | NudaUI Magnetic / Framer Motion | Framer Motion `useMotionValue` + `useSpring` |
| **13** | **Aurora Background** | Ethereal shifting Northern Lights colored waves behind hero copy | Magic UI AuroraBackground | `npx shadcn@latest add @magicui/aurora` |
| **14** | **Particle Globe** | Interactive 3D WebGL rotating particle sphere for global reach | Aceternity Globe | `npx shadcn@latest add @aceternity/globe` |
| **15** | **Animated Border Trace** | Glowing laser beam tracing the perimeter of card containers | NudaUI BorderTrace / Magic UI BorderBeam | `npx shadcn@latest add @magicui/border-beam` |
| **16** | **Scroll-Driven Progress** | CSS `animation-timeline: scroll()` progress line locked to viewport travel | Native CSS scroll-timeline | CSS `@keyframes` with `animation-timeline` |
| **17** | **Typewriter Effect** | Terminal-style smooth character typing with blinking cursor | ReactBits Typewriter | `npx shadcn@latest add @reactbits/typewriter` |
| **18** | **Stagger Children Reveal** | Staggered entrance cascade of list items or feature pills | Framer Motion variants | `variants={{ visible: { transition: { staggerChildren: 0.1 } } }}` |
| **19** | **Parallax Image Layers** | Multi-plane depth separation shifting background at 0.4x and foreground at 1.0x | Locomotive / Framer Motion `useScroll` | `const y = useTransform(scrollYProgress, [0, 1], [-50, 50])` |
| **20** | **Morphing SVG Paths** | Organic fluid blob shape-shifting between SVG path coordinates | GSAP MorphSVG / Framer Motion | `gsap.to("#path", { morphSVG: "#target" })` |
| **21** | **Counter Animation** | Smooth numeric ease-up from 0 to statistic value upon viewport entry | ReactBits CountUp | `npx shadcn@latest add @reactbits/count-up` |
| **22** | **Ripple Button Click** | Material-inspired fluid wave expanding from exact click coordinate | NudaUI Ripple | `npm i framer-motion` |
| **23** | **Glassmorphism Card** | Frosted glass backdrop with crisp semi-transparent border and direct shadow | Magic UI GlassCard | Tailwind `backdrop-blur-md bg-white/10 border border-white/20` |
| **24** | **Infinite Logo Cloud** | Two-row alternating marquee of client/partner badges | Magic UI LogoCloud | `npx shadcn@latest add @magicui/marquee` |
| **25** | **Scroll Progress Bar** | Ultra-thin progress indicator pinned to top of screen showing reading depth | Framer Motion `useScroll` | `<motion.div style={{ scaleX: scrollYProgress }} />` |
| **26** | **Reveal on Scroll** | Smooth fade-up (`opacity: 0, y: 32` -> `opacity: 1, y: 0`) with cubic-bezier easing | Framer Motion `whileInView` | `<motion.section whileInView={{ opacity: 1, y: 0 }} />` |
| **27** | **Image Trail Cursor** | Trailing sequence of photo thumbnails spawning on mouse movement | Aceternity ImageTrail | `npx shadcn@latest add @aceternity/image-trail` |
| **28** | **Lottie Micro-Interaction** | Vector animation icon triggering playful state loop on hover | Lottie React | `npm i lottie-react` |
| **29** | **3D Card Flip** | Two-sided card flipping 180 degrees on Y-axis to reveal back specifications | NudaUI CardFlip | CSS `perspective: 1000px`, `transform-style: preserve-3d` |
| **30** | **Noise Texture Overlay** | Subtle film grain layer eliminating digital flat banding | SVG feTurbulence filter | CSS `url("data:image/svg+xml,...")` fixed overlay |

---

## 3. Video-to-Motion Code Synthesis Guidelines (MotiScope Style)

When decomposing a video walkthrough (`reference_walkthrough_60fps.webm`) into Next.js code:

1. **Extract Time Intervals & Keyframe Anchors**:
   - Dwell time: Duration an element remains static before user interaction.
   - Transition duration: Measured from initial state change to rest. Standard ranges:
     - Micro-interactions (hover, click): `200ms – 350ms`.
     - Layout reveals (modals, drawers, tabs): `400ms – 600ms`.
     - Section entrances & Ken-Burns: `800ms – 15000ms`.
2. **Translate Energy Curves into Cubic-Bezier**:
   - Explosive start + gentle settle: `cubic-bezier(0.16, 1, 0.3, 1)` (Quart ease-out).
   - Calm, stately luxury: `cubic-bezier(0.25, 1, 0.5, 1)` (Custom WAAPI curve from luxury benchmarks).
   - Mechanical / snappy: `cubic-bezier(0.4, 0, 0.2, 1)` (Material standard).

---

## 4. 60fps GPU Compositor Rules (Strictly Non-Negotiable)

To guarantee that code runs at a stable 60fps without layout thrashing:
- **ALLOWED**: Animate ONLY `transform` (`translate3d`, `scale`, `rotate`) and `opacity`.
- **STRICTLY BANNED**: Animating `width`, `height`, `top`, `left`, `right`, `bottom`, `margin`, or `padding` in transitions.
- **BANNED**: `transition: all` on major section containers.
- **REQUIRED**: `will-change: transform, opacity` applied only to active animated elements.
