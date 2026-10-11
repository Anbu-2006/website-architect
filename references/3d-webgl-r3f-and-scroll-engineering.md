# 3D WebGL, React Three Fiber (R3F) & Unified Scroll Engineering

> **Website Architect Reference Standard — Version 2.5.0**  
> *Authoritative WebGL Performance Budgets, Leak-Free R3F Canvas Architecture, and Unified Scroll Ticker Synchronization.*

---

## 1. 3D WebGL & R3F Performance Budgets for Commercial Web

Interactive 3D should be introduced into commercial platforms only when spatial interaction clarifies value—such as exploring architectural spaces, luxury automotive finishes, or mechanical assemblies.

When a 3D canvas is justified, it must operate within strict performance boundaries to guarantee 60fps on standard displays and 120fps on Apple ProMotion hardware:

| Performance Metric | Strict Budget Threshold | Enforcement Mechanism |
| :--- | :--- | :--- |
| **Frame Render Budget** | $\le 16.67\text{ms}$ (60fps) / $\le 8.33\text{ms}$ (120fps) | Profiling via Chrome DevTools Performance & PerformanceObserver |
| **Draw Calls Per Frame** | $\le 25\text{ calls}$ | Mesh merging via `THREE.BufferGeometryUtils` or InstancedMesh |
| **Triangle Count** | $\le 60,000\text{ triangles}$ | Decimation in Blender / gltf-pipeline |
| **Geometry File Footprint** | $\le 3.0\text{MB}$ total payload | Draco / Meshopt compression (`--draco.compressionLevel 7`) |
| **Device Pixel Ratio (DPR)** | Clamped to $\text{DPR} \in [1.0, 2.0]$ | R3F Canvas prop: `dpr={[1, 2]}` |
| **Mobile Fill Rate Guard** | Clamped viewport resolution | CSS aspect ratio clamping; mobile shader resolution decimation |

---

## 2. Leak-Free R3F Canvas Architecture (Zero Route Memory Leaks)

In Next.js 15 App Router applications, client-side route navigation can leave WebGL contexts allocated in GPU memory if unmanaged. The canvas component must cleanly dispose of scene resources on unmount and provide an accessible static fallback:

```tsx
"use client";
import React, { useRef, useEffect, useState } from "react";
import { Canvas, useFrame } from "@react-three/fiber";
import { useGLTF } from "@react-three/drei";
import * as THREE from "three";

interface ModelViewerProps {
  modelPath: string;
  fallbackImageUrl: string;
}

export function InteractiveSceneCanvas({ modelPath, fallbackImageUrl }: ModelViewerProps) {
  const [hasWebGLContext, setHasWebGLContext] = useState(true);
  const canvasRef = useRef<HTMLCanvasElement | null>(null);

  useEffect(() => {
    const testCanvas = document.createElement("canvas");
    const gl = testCanvas.getContext("webgl2") || testCanvas.getContext("webgl");
    if (!gl) {
      setHasWebGLContext(false);
      return;
    }

    return () => {
      // Clean up GPU context on unmount to prevent Next.js route memory leaks
      if (canvasRef.current) {
        const activeGl = canvasRef.current.getContext("webgl2") || canvasRef.current.getContext("webgl");
        if (activeGl && "getExtension" in activeGl) {
          const ext = activeGl.getExtension("WEBGL_lose_context");
          if (ext) {
            ext.loseContext();
          }
        }
      }
    };
  }, []);

  if (!hasWebGLContext) {
    return (
      <div className="relative w-full aspect-16/9 bg-neutral-950 flex items-center justify-center overflow-hidden">
        <picture>
          <img
            src={fallbackImageUrl}
            alt="Product visual architecture fallback"
            className="w-full h-full object-cover"
            loading="lazy"
          />
        </picture>
        <span className="sr-only">Interactive WebGL unavailable. Static asset fallback active.</span>
      </div>
    );
  }

  return (
    <div className="relative w-full aspect-16/9 bg-neutral-950 overflow-hidden">
      <Canvas
        ref={canvasRef}
        camera={{ position: [0, 0, 4.5], fov: 45 }}
        dpr={[1, 2]}
        gl={{
          antialias: true,
          powerPreference: "high-performance",
          alpha: true,
        }}
        onCreated={({ gl, scene }) => {
          return () => {
            // Recursive disposal of scene geometries and materials
            scene.traverse((node) => {
              if (node instanceof THREE.Mesh) {
                node.geometry?.dispose();
                if (Array.isArray(node.material)) {
                  node.material.forEach((m) => m.dispose());
                } else if (node.material) {
                  node.material.dispose();
                }
              }
            });
            gl.dispose();
          };
        }}
      >
        <ambientLight intensity={0.6} />
        <directionalLight position={[8, 8, 4]} intensity={1.4} />
      </Canvas>
    </div>
  );
}
```

---

## 3. Unified Scroll Engine: Lenis + GSAP ScrollTrigger Synchronization

Running separate animation loops for smooth scrolling (Lenis) and visual pinning (GSAP) causes visual micro-stutter and desynchronized pins. Unifying them under GSAP's central ticker ensures scroll calculations and visual pinning execute within the same render cycle:

```ts
import { useEffect } from "react";
import Lenis from "lenis";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

export function useUnifiedScrollEngine() {
  useEffect(() => {
    // Respect OS reduced motion preference
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      return;
    }

    gsap.registerPlugin(ScrollTrigger);

    const lenis = new Lenis({
      duration: 1.1,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      orientation: "vertical",
      gestureOrientation: "vertical",
      smoothWheel: true,
      wheelMultiplier: 1.0,
      touchMultiplier: 1.5,
    });

    lenis.on("scroll", ScrollTrigger.update);

    const handleTicker = (time: number) => {
      lenis.raf(time * 1000);
    };

    gsap.ticker.add(handleTicker);
    gsap.ticker.lagSmoothing(0);

    return () => {
      gsap.ticker.remove(handleTicker);
      lenis.destroy();
      ScrollTrigger.getAll().forEach((trigger) => trigger.kill());
    };
  }, []);
}
```

---

## 4. Damped Harmonic Oscillator Physics & CSS `linear()` Polyfill Curves

Rather than running expensive JavaScript spring engines on the main thread during simple hover/toggle states, solve the classical harmonic equation at build time and emit CSS `linear()` polyfill curves:

$$m \frac{d^2x}{dt^2} + c \frac{dx}{dt} + kx = 0$$

Where:
- $m$: Mass of the UI element
- $k$: Spring stiffness
- $c$: Damping coefficient
- $\zeta = \frac{c}{2\sqrt{mk}}$: Dimensionless damping ratio

Underdamped ($\zeta < 1$) equations are sampled at 60 points to generate CSS `linear()` strings:
```css
:root {
  --spring-snappy: linear(
    0, 0.006, 0.025 2.8%, 0.101 6.1%, 0.539 18.9%, 0.721 25.3%, 0.849 31.5%,
    0.937 38.1%, 0.968 41.8%, 0.991 45.7%, 1.006 50.1%, 1.015 55%, 1.017 60.7%,
    1.001 78.4%, 1
  );
}
```
All transitions run directly on the GPU compositor with zero JavaScript layout recalculation.
