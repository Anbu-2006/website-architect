# Physics Motion & Spring Damping Mathematical Treatise

> **Website Architect Reference Standard — Version 2.4.0**  
> *Authoritative Physics Equations, CSS `linear()` Spring Polynomials, and 60fps Compositor Motion.*

---

## 1. Mathematical Foundations: The Damped Harmonic Oscillator

Organic, premium micro-interactions emulate Newtonian classical mechanics rather than synthetic Bézier curves (`ease-in-out` or `cubic-bezier`). The motion of an interactive UI element responding to user pointer displacement is governed by the second-order linear differential equation of a damped harmonic oscillator:

$$m \frac{d^2 x(t)}{dt^2} + c \frac{dx(t)}{dt} + k x(t) = 0$$

Where:
- $m$: Mass of the UI element (inertia, default $m = 1.0$)
- $k$: Spring stiffness constant (restoring force toward equilibrium)
- $c$: Damping coefficient (viscous friction preventing indefinite oscillation)

### Damping Ratio & Natural Frequency

$$\omega_n = \sqrt{\frac{k}{m}} \quad (\text{Undamped Natural Angular Frequency})$$

$$\zeta = \frac{c}{2 \sqrt{m k}} \quad (\text{Dimensionless Damping Ratio})$$

### Regimes of Motion

1. **Underdamped ($\zeta < 1$)**:
   The roots of the characteristic polynomial are complex conjugates:
   $$r_{1,2} = -\zeta \omega_n \pm i \omega_d \quad \text{where} \quad \omega_d = \omega_n \sqrt{1 - \zeta^2}$$
   Position over time:
   $$x(t) = 1 - e^{-\zeta \omega_n t} \left( \cos(\omega_d t) + \frac{\zeta}{\sqrt{1 - \zeta^2}} \sin(\omega_d t) \right)$$
   *Use case*: Snappy buttons, modal reveals, switch toggles requiring a micro-overshoot ($\sim 1\% - 3\%$) that feels tactile and alive.

2. **Critically Damped ($\zeta = 1$)**:
   $$x(t) = 1 - e^{-\omega_n t} (1 + \omega_n t)$$
   *Use case*: Drawer slide-overs, dropdown menus, context menus requiring the fastest convergence to equilibrium without any overshoot.

3. **Overdamped ($\zeta > 1$)**: Sluggish exponential decay; strictly avoided in high-performance digital interfaces.

---

## 2. Modern CSS `linear()` Physics Spring Presets

Rather than loading large JavaScript physics animation runtimes for basic interactions, modern browsers (Chrome 113+, Safari 17.2+, Firefox 112+) support the `linear()` easing function, which samples damped harmonic oscillator differential equations directly into native CSS:

### 2.1 Snappy Spring (`--spring-snappy`)
- Parameters: $m = 1$, $k = 180$, $c = 12 \implies \zeta \approx 0.447$
- Characteristics: Immediate acceleration, crisp settle, subtle $1.7\%$ tactile bounce.

```css
:root {
  --spring-snappy: linear(
    0, 0.006, 0.025 2.8%, 0.101 6.1%, 0.539 18.9%, 0.721 25.3%, 0.849 31.5%,
    0.937 38.1%, 0.968 41.8%, 0.991 45.7%, 1.006 50.1%, 1.015 55%, 1.017 60.7%,
    1.001 78.4%, 1
  );
}
```

### 2.2 Gentle Spring (`--spring-gentle`)
- Parameters: $m = 1$, $k = 100$, $c = 18 \implies \zeta \approx 0.90$
- Characteristics: Smooth luxury glide, zero perceptible bounce, near-critical damping.

```css
:root {
  --spring-gentle: linear(
    0, 0.004, 0.016 2.1%, 0.065 4.7%, 0.344 14.5%, 0.467 19.3%, 0.578 24.1%,
    0.678 29.1%, 0.764 34.3%, 0.837 39.8%, 0.896 45.7%, 0.941 52.1%, 0.972 59.2%,
    0.991 67.4%, 1
  );
}
```

### 2.3 Elastic Bounce (`--spring-bounce`)
- Parameters: $m = 1$, $k = 250$, $c = 10 \implies \zeta \approx 0.316$
- Characteristics: Playful interaction, energetic feedback for badge pulses and bookmark triggers.

```css
:root {
  --spring-bounce: linear(
    0, 0.008, 0.034 2.3%, 0.134 5.2%, 0.697 16.4%, 0.912 21.8%, 1.026 27.1%,
    1.069 32.5%, 1.054 38.2%, 1.018 44.5%, 0.994 51.5%, 0.989 59.8%, 1.001 75%, 1
  );
}
```

---

## 3. Interactive Magnetic Attraction Physics (TypeScript Component)

Magnetic buttons attract toward the cursor when the pointer enters an active threshold radius ($R_{\text{trigger}} = 80\text{px}$). The pull strength attenuates exponentially with distance:

$$F_{\text{pull}}(d) = (\mathbf{p}_{\text{cursor}} - \mathbf{p}_{\text{center}}) \cdot e^{-\frac{d^2}{2 \sigma^2}}$$

### Production Implementation

```tsx
"use client";
import React, { useRef, useEffect } from "react";

interface MagneticProps {
  children: React.ReactNode;
  strength?: number; // Default 0.35
  radius?: number;   // Default 80px
  className?: string;
}

export function MagneticContainer({
  children,
  strength = 0.35,
  radius = 80,
  className = ""
}: MagneticProps) {
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const el = ref.current;
    if (!el) return;

    let targetX = 0;
    let targetY = 0;
    let currentX = 0;
    let currentY = 0;
    let rafId: number;

    // Linear Interpolation (LERP) Loop for 60fps Smooth Compositor Updates
    const tick = () => {
      currentX += (targetX - currentX) * 0.12;
      currentY += (targetY - currentY) * 0.12;

      el.style.transform = `translate3d(${currentX.toFixed(2)}px, ${currentY.toFixed(2)}px, 0)`;

      if (Math.abs(targetX - currentX) > 0.01 || Math.abs(targetY - currentY) > 0.01) {
        rafId = requestAnimationFrame(tick);
      }
    };

    const onMouseMove = (e: MouseEvent) => {
      const rect = el.getBoundingClientRect();
      const centerX = rect.left + rect.width / 2;
      const centerY = rect.top + rect.height / 2;
      const dx = e.clientX - centerX;
      const dy = e.clientY - centerY;
      const dist = Math.hypot(dx, dy);

      if (dist < radius) {
        // Gaussian attenuation decay
        const factor = Math.exp(-(dist * dist) / (2 * radius * radius));
        targetX = dx * strength * factor;
        targetY = dy * strength * factor;
        cancelAnimationFrame(rafId);
        rafId = requestAnimationFrame(tick);
      } else {
        targetX = 0;
        targetY = 0;
        cancelAnimationFrame(rafId);
        rafId = requestAnimationFrame(tick);
      }
    };

    const onMouseLeave = () => {
      targetX = 0;
      targetY = 0;
      cancelAnimationFrame(rafId);
      rafId = requestAnimationFrame(tick);
    };

    window.addEventListener("mousemove", onMouseMove, { passive: true });
    el.addEventListener("mouseleave", onMouseLeave);

    return () => {
      window.removeEventListener("mousemove", onMouseMove);
      el.removeEventListener("mouseleave", onMouseLeave);
      cancelAnimationFrame(rafId);
    };
  }, [strength, radius]);

  return (
    <div ref={ref} className={`inline-block will-change-transform ${className}`}>
      {children}
    </div>
  );
}
```

---

## 4. Compositor Thread Execution Mandate

To guarantee a stable 60fps/120fps refresh rate on ProMotion and mobile displays, UI transitions must execute strictly on the GPU compositor thread:

1. **Permitted Animated Properties**:
   - `transform` (`translate3d`, `scale`, `rotate`)
   - `opacity`
   - `clip-path` (hardware accelerated paths only)

2. **Strictly Forbidden Animated Properties** (Trigger layout/paint thrash):
   - `top`, `left`, `right`, `bottom`
   - `width`, `height` (use `scale` or CSS Grid `0fr -> 1fr`)
   - `margin`, `padding`
   - `box-shadow` (animate opacity of a layered pseudo-element instead)
   - `transition: all` (indiscriminately thrashes layout on unmeasured properties)

---

## 5. Reduced-Motion Accessibility Protocol

Under WCAG 2.3.3 and 2.2.2, all motion effects must honor the user's operating system preferences without exception:

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```
In Framer Motion:
```tsx
import { useReducedMotion } from "framer-motion";

const shouldReduceMotion = useReducedMotion();
const transition = shouldReduceMotion ? { duration: 0 } : { duration: 0.8, ease: [0.16, 1, 0.3, 1] };
```
