#!/usr/bin/env python3
"""
creative_director_agent.py - Agent 2 (Creative Art Director) for Website Architect v2.5.0
Synthesizes business profiles and competitive benchmarks into an intentional, non-generic
visual thesis. Computes fluid typography clamping, calibrated OKLCH color palettes, and
damped harmonic oscillator physics parameters. Emits validated creative_thesis.json.
"""

import os
import sys
import json
import math
import argparse

# Canonical Archetype Creative Design Mappings
ARCHETYPE_DESIGN_SYSTEMS = {
    "luxury_boutique_hotel": {
        "display_family": "Canela, Ogg, 'Playfair Display', serif",
        "ui_family": "'Maison Neue', 'Plus Jakarta Sans', sans-serif",
        "headline_tracking": "-0.035em",
        "color_tokens": {
            "canvas": "oklch(0.97 0.01 75)",
            "surface": "oklch(0.94 0.015 75)",
            "border": "oklch(0.88 0.02 75)",
            "primary_text": "oklch(0.22 0.03 55)",
            "muted_text": "oklch(0.48 0.03 60)",
            "accent": "oklch(0.42 0.08 45)"
        },
        "spatial_pacing": {
            "section_density_alternation": True,
            "bento_asymmetry_ratio": "8:4"
        },
        "motion_physics": {
            "spring_stiffness": 160.0,
            "spring_damping": 22.0,
            "spring_mass": 1.0
        }
    },
    "high_frequency_fintech": {
        "display_family": "'Geist Sans', 'Suisse Int\\'l', sans-serif",
        "ui_family": "'Geist Mono', 'JetBrains Mono', monospace",
        "headline_tracking": "-0.04em",
        "color_tokens": {
            "canvas": "oklch(0.12 0.005 260)",
            "surface": "oklch(0.16 0.008 260)",
            "border": "oklch(0.24 0.012 260)",
            "primary_text": "oklch(0.96 0.002 260)",
            "muted_text": "oklch(0.65 0.008 260)",
            "accent": "oklch(0.68 0.18 155)"
        },
        "spatial_pacing": {
            "section_density_alternation": True,
            "bento_asymmetry_ratio": "8:4"
        },
        "motion_physics": {
            "spring_stiffness": 320.0,
            "spring_damping": 28.0,
            "spring_mass": 1.0
        }
    },
    "industrial_precision_machinery": {
        "display_family": "'Archivo SemiCondensed', 'PP Neue Montreal', sans-serif",
        "ui_family": "'JetBrains Mono', 'IBM Plex Mono', monospace",
        "headline_tracking": "-0.03em",
        "color_tokens": {
            "canvas": "oklch(0.16 0.01 240)",
            "surface": "oklch(0.20 0.012 240)",
            "border": "oklch(0.28 0.018 240)",
            "primary_text": "oklch(0.94 0.005 240)",
            "muted_text": "oklch(0.60 0.01 240)",
            "accent": "oklch(0.85 0.18 95)"
        },
        "spatial_pacing": {
            "section_density_alternation": False,
            "bento_asymmetry_ratio": "7:5"
        },
        "motion_physics": {
            "spring_stiffness": 220.0,
            "spring_damping": 20.0,
            "spring_mass": 1.0
        }
    },
    "modern_saas_platform": {
        "display_family": "'Inter', 'Plus Jakarta Sans', sans-serif",
        "ui_family": "'Inter', -apple-system, sans-serif",
        "headline_tracking": "-0.04em",
        "color_tokens": {
            "canvas": "oklch(0.99 0.002 260)",
            "surface": "oklch(0.96 0.004 260)",
            "border": "oklch(0.90 0.006 260)",
            "primary_text": "oklch(0.14 0.01 260)",
            "muted_text": "oklch(0.52 0.01 260)",
            "accent": "oklch(0.55 0.19 250)"
        },
        "spatial_pacing": {
            "section_density_alternation": True,
            "bento_asymmetry_ratio": "8:4"
        },
        "motion_physics": {
            "spring_stiffness": 260.0,
            "spring_damping": 24.0,
            "spring_mass": 1.0
        }
    }
}

def calculate_fluid_clamp(min_size_px=40, max_size_px=80, min_vp_px=390, max_vp_px=1440):
    """
    Computes CSS clamp() using linear interpolation:
    clamp(V_min, intercept + slope * 100vw, V_max)
    """
    slope = (max_size_px - min_size_px) / (max_vp_px - min_vp_px)
    intercept_px = min_size_px - (slope * min_vp_px)
    min_rem = min_size_px / 16.0
    max_rem = max_size_px / 16.0
    intercept_rem = intercept_px / 16.0
    vw_factor = slope * 100.0
    return f"clamp({min_rem:.3f}rem, {intercept_rem:.3f}rem + {vw_factor:.2f}vw, {max_rem:.3f}rem)"

def compile_spring_to_linear_easing(stiffness=200.0, damping=14.0, mass=1.0, samples=60):
    """
    Solves damped harmonic oscillator differential equation:
    m*(d^2x/dt^2) + c*(dx/dt) + k*x = 0
    Emits CSS linear() polyfill curve for 60fps compositor transitions.
    """
    omega = math.sqrt(stiffness / mass)
    zeta = damping / (2.0 * math.sqrt(stiffness * mass))
    if zeta >= 1.0:
        zeta = 0.999 # Clamp to near critical damping
    omega_d = omega * math.sqrt(1.0 - (zeta ** 2))
    zeta_fac = zeta / math.sqrt(1.0 - (zeta ** 2))

    # Calculate settle duration
    settle_duration = 1.0
    t = 0.05
    while t < 6.0:
        x = 1.0 - math.exp(-zeta * omega * t) * (math.cos(omega_d * t) + zeta_fac * math.sin(omega_d * t))
        if abs(x - 1.0) < 0.001:
            settle_duration = t
            break
        t += 0.01

    stops = []
    for i in range(samples + 1):
        curr_t = (i / float(samples)) * settle_duration
        x = 1.0 - math.exp(-zeta * omega * curr_t) * (math.cos(omega_d * curr_t) + zeta_fac * math.sin(omega_d * curr_t))
        stops.append(f"{x:.4f}")

    return f"linear({', '.join(stops)})"

def formulate_creative_thesis(business_profile_path=None, archetype_override=None, out_path="creative_thesis.json"):
    archetype = "luxury_boutique_hotel"
    if archetype_override:
        archetype = archetype_override
    elif business_profile_path and os.path.exists(business_profile_path):
        with open(business_profile_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            raw_arch = data.get("matched_archetype") or data.get("archetype") or ""
            if "fintech" in raw_arch.lower():
                archetype = "high_frequency_fintech"
            elif "industrial" in raw_arch.lower() or "machinery" in raw_arch.lower():
                archetype = "industrial_precision_machinery"
            elif "saas" in raw_arch.lower() or "software" in raw_arch.lower():
                archetype = "modern_saas_platform"
            else:
                archetype = "luxury_boutique_hotel"

    design_system = ARCHETYPE_DESIGN_SYSTEMS.get(archetype, ARCHETYPE_DESIGN_SYSTEMS["luxury_boutique_hotel"])
    fluid_clamp = calculate_fluid_clamp(min_size_px=40, max_size_px=80)

    thesis = {
        "archetype": archetype,
        "color_tokens": design_system["color_tokens"],
        "typography": {
            "display_family": design_system["display_family"],
            "ui_family": design_system["ui_family"],
            "headline_tracking": design_system["headline_tracking"],
            "fluid_clamp_root": fluid_clamp
        },
        "spatial_pacing": design_system["spatial_pacing"],
        "motion_physics": design_system["motion_physics"]
    }

    if out_path:
        os.makedirs(os.path.dirname(os.path.abspath(out_path)) if os.path.dirname(out_path) else ".", exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(thesis, f, indent=2)
        print(f"[+] Creative Art Director formulated & emitted thesis: {out_path} (Archetype: {archetype})")

    return thesis

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Agent 2: Creative Art Director")
    parser.add_argument("--profile", default="assets/business_profile.json", help="Path to business_profile.json")
    parser.add_argument("--archetype", default=None, help="Explicit archetype override")
    parser.add_argument("--out", default="creative_thesis.json", help="Output path for creative_thesis.json")
    args = parser.parse_args()

    formulate_creative_thesis(args.profile, args.archetype, args.out)
