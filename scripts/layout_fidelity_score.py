#!/usr/bin/env python3
"""
scripts/layout_fidelity_score.py
Production-Grade Structural Layout Fidelity Scorer for /website-architect.
Compares reference wireframe IR against generated component AST to verify:
  1. Section primitive sequence match
  2. Column ratio alignment across responsive breakpoints
  3. Visual mask fidelity (arched clip-paths, organic curves)
  4. Animation signature presence (WAAPI, CSS @keyframes, GSAP triggers)
  5. Micro-interaction hover definitions for buttons and cards
  6. Responsive breakpoint column mappings (Desktop, Tablet, Mobile)
  7. Penalizes static desktop-only pixel values where fluid clamp()/rem was extracted
"""

import json
import sys
import re
import os
import argparse


def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def score_primitive_sequence(ref_sections, gen_sections):
    """Scores how well the generated section primitive types match the reference order."""
    if not ref_sections:
        return 1.0
    matches = 0
    for r, g in zip(ref_sections, gen_sections):
        if r.get("primitive_type") == g.get("primitive_type"):
            matches += 1
    return matches / max(len(ref_sections), 1)


def score_column_ratios(ref_sections, gen_sections):
    """Scores column ratio alignment across all responsive tiers."""
    if not ref_sections:
        return 1.0
    matches = 0
    total = 0
    for r, g in zip(ref_sections, gen_sections):
        r_geo = r.get("spatial_geometry", {})
        g_geo = g.get("spatial_geometry", {})

        r_cols = r_geo.get("columns", {})
        g_cols = g_geo.get("columns", {})

        # Support both dict-style {"mobile": 1, "tablet": 2, "desktop": 4}
        # and flat int-style (legacy)
        if isinstance(r_cols, dict) and isinstance(g_cols, dict):
            for tier in ["mobile", "tablet", "desktop"]:
                total += 1
                if r_cols.get(tier) == g_cols.get(tier):
                    matches += 1
        else:
            total += 1
            if r_cols == g_cols:
                matches += 1

    return matches / max(total, 1)


def score_mask_fidelity(ref_sections, gen_sections):
    """Scores arched / bespoke image mask preservation."""
    if not ref_sections:
        return 1.0
    matches = 0
    for r, g in zip(ref_sections, gen_sections):
        r_mask = r.get("spatial_geometry", {}).get("has_arched_mask", False)
        g_mask = g.get("spatial_geometry", {}).get("has_arched_mask", False)
        if r_mask == g_mask:
            matches += 1
    return matches / max(len(ref_sections), 1)


def score_section_count_penalty(ref_sections, gen_sections):
    """Penalizes for missing or extra sections vs reference."""
    if not ref_sections:
        return 1.0
    diff = abs(len(ref_sections) - len(gen_sections))
    return max(0.0, 1.0 - (diff / max(len(ref_sections), 1)))


def check_animation_signatures(ref_data, gen_data):
    """
    Checks that animation signatures exist in generated output
    when the reference site uses WAAPI/GSAP/CSS @keyframes.
    Returns (score, warnings).
    """
    warnings = []
    ref_anim = ref_data.get("animation_signatures", {})
    gen_anim = gen_data.get("animation_signatures", {})

    ref_has_anims = bool(
        ref_anim.get("active") or
        ref_anim.get("keyframesMap") or
        ref_anim.get("gsapData")
    )

    if not ref_has_anims:
        return 1.0, warnings

    gen_has_anims = bool(
        gen_anim.get("active") or
        gen_anim.get("keyframesMap") or
        gen_anim.get("gsapData")
    )

    if not gen_has_anims:
        warnings.append("[WARN] Reference has animation signatures but generated output has NONE. Motion parity missing.")
        return 0.0, warnings

    # Score based on coverage
    ref_keyframes = set(ref_anim.get("keyframesMap", {}).keys())
    gen_keyframes = set(gen_anim.get("keyframesMap", {}).keys())

    if ref_keyframes:
        kf_overlap = len(ref_keyframes & gen_keyframes) / len(ref_keyframes)
    else:
        kf_overlap = 1.0

    ref_gsap_count = len(ref_anim.get("gsapData") or [])
    gen_gsap_count = len(gen_anim.get("gsapData") or [])

    if ref_gsap_count > 0 and gen_gsap_count == 0:
        warnings.append(f"[WARN] Reference has {ref_gsap_count} GSAP ScrollTrigger instances but generated has 0.")
        gsap_score = 0.0
    else:
        gsap_score = 1.0

    return (0.6 * kf_overlap + 0.4 * gsap_score), warnings


def check_micro_interactions(ref_data, gen_data):
    """
    Checks that hover/active micro-interactions exist for buttons and cards
    when the reference defines them.
    Returns (score, warnings).
    """
    warnings = []
    ref_mi = ref_data.get("micro_interactions", {})
    gen_mi = gen_data.get("micro_interactions", {})

    if not ref_mi:
        return 1.0, warnings

    ref_keys = set(ref_mi.keys())
    gen_keys = set(gen_mi.keys())

    if not gen_keys:
        warnings.append("[WARN] Reference defines hover micro-interactions but generated output has NONE.")
        return 0.0, warnings

    overlap = len(ref_keys & gen_keys) / max(len(ref_keys), 1)

    missing = ref_keys - gen_keys
    if missing:
        warnings.append(f"[WARN] Missing hover definitions for: {', '.join(missing)}")

    return overlap, warnings


def check_responsive_breakpoints(ref_data, gen_data):
    """
    Checks that responsive column mappings exist for mobile, tablet, and desktop
    when the reference defines them.
    Returns (score, warnings).
    """
    warnings = []
    ref_bp = ref_data.get("responsive_breakpoints", {})
    gen_bp = gen_data.get("responsive_breakpoints", {})

    if not ref_bp:
        return 1.0, warnings

    required_tiers = ["desktop", "tablet", "mobile"]
    present = 0
    for tier in required_tiers:
        if tier in gen_bp:
            present += 1
        else:
            warnings.append(f"[WARN] Missing responsive breakpoint tier: {tier}")

    return present / len(required_tiers), warnings


def check_fluid_math_compliance(ref_data, gen_data):
    """
    Penalizes generated output using static desktop-only pixel values (px)
    where the reference extracted clamp() or rem values.
    Returns (score, warnings).
    """
    warnings = []
    ref_declared = ref_data.get("declared_typography", {})
    gen_declared = gen_data.get("declared_typography", {})

    if not ref_declared:
        return 1.0, warnings

    fluid_patterns = re.compile(r'clamp\(|calc\(|min\(|max\(|rem|vw|vh')
    compliant = 0
    total = 0

    for key, ref_rules in ref_declared.items():
        ref_decl = ref_rules.get("declared_rules", {})
        gen_rules = gen_declared.get(key, {}).get("declared_rules", {})

        for prop, ref_val in ref_decl.items():
            if fluid_patterns.search(str(ref_val)):
                total += 1
                gen_val = gen_rules.get(prop, "")
                if fluid_patterns.search(str(gen_val)):
                    compliant += 1
                else:
                    warnings.append(f"[WARN] {key}.{prop}: Reference uses fluid '{ref_val}' but generated uses static '{gen_val}'")

    if total == 0:
        return 1.0, warnings
    return compliant / total, warnings


def score_layout_fidelity(reference_path: str, generated_path: str, strict: bool = True):
    """
    Comprehensive layout fidelity scoring with all 7 verification vectors.
    """
    ref = load_json(reference_path)
    gen = load_json(generated_path)

    ref_sections = ref.get("sections", [])
    gen_sections = gen.get("sections", [])

    # Core structural scores (original 4 vectors)
    s_prim = score_primitive_sequence(ref_sections, gen_sections)
    s_cols = score_column_ratios(ref_sections, gen_sections)
    s_mask = score_mask_fidelity(ref_sections, gen_sections)
    s_count = score_section_count_penalty(ref_sections, gen_sections)

    # Extended verification vectors (new 4 vectors)
    s_anim, w_anim = check_animation_signatures(ref, gen)
    s_micro, w_micro = check_micro_interactions(ref, gen)
    s_resp, w_resp = check_responsive_breakpoints(ref, gen)
    s_fluid, w_fluid = check_fluid_math_compliance(ref, gen)

    all_warnings = w_anim + w_micro + w_resp + w_fluid

    # Weighted composite score
    # Core structural: 60% | Extended vectors: 40%
    final_score = (
        0.20 * s_prim +
        0.15 * s_cols +
        0.10 * s_mask +
        0.05 * s_count +
        0.15 * s_anim +
        0.10 * s_micro +
        0.15 * s_resp +
        0.10 * s_fluid
    )

    # Report
    print("=" * 64)
    print("  LAYOUT FIDELITY VERIFICATION REPORT")
    print("=" * 64)
    print(f"\n  Reference:  {reference_path}")
    print(f"  Generated:  {generated_path}")
    print(f"\n  {'Vector':<40} {'Score':>8}")
    print(f"  {'-'*40} {'-'*8}")
    print(f"  {'1. Primitive Sequence Match':<40} {s_prim*100:>6.1f}%")
    print(f"  {'2. Column Ratio Alignment':<40} {s_cols*100:>6.1f}%")
    print(f"  {'3. Visual Mask Fidelity':<40} {s_mask*100:>6.1f}%")
    print(f"  {'4. Section Count Parity':<40} {s_count*100:>6.1f}%")
    print(f"  {'5. Animation Signature Presence':<40} {s_anim*100:>6.1f}%")
    print(f"  {'6. Micro-Interaction Hover Defs':<40} {s_micro*100:>6.1f}%")
    print(f"  {'7. Responsive Breakpoint Coverage':<40} {s_resp*100:>6.1f}%")
    print(f"  {'8. Fluid Math Compliance':<40} {s_fluid*100:>6.1f}%")
    print(f"\n  {'COMPOSITE FIDELITY SCORE':<40} {final_score*100:>6.1f}%")
    print()

    if all_warnings:
        print("  WARNINGS:")
        for w in all_warnings:
            print(f"    {w}")
        print()

    threshold = 0.85
    if final_score < threshold:
        print(f"  [FAIL] Layout fidelity score {final_score:.3f} is below {threshold}.")
        print(f"         Median AI slop or missing extraction vectors detected!")
        if strict:
            sys.exit(1)
    else:
        print(f"  [PASS] Layout fidelity verified at {final_score:.3f}!")
        print(f"         Bespoke reference geometry, motion, and responsiveness preserved.")

    print("=" * 64)
    return final_score


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Score layout fidelity between reference and generated wireframes.")
    parser.add_argument("ref", help="Path to reference wireframe IR JSON (ref_ir.json)")
    parser.add_argument("gen", help="Path to generated wireframe AST JSON (gen_ast.json)")
    parser.add_argument("--no-strict", action="store_true", help="Don't exit with code 1 on failure")

    args = parser.parse_args()
    score_layout_fidelity(args.ref, args.gen, strict=not args.no_strict)
