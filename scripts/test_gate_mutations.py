#!/usr/bin/env python3
"""
test_gate_mutations.py - Comprehensive Seeded-Defect Mutation Runner & Gate Integrity Matrix (v2.4.0)
Validates all adversarial edge cases identified during Lead Reviewer AI Audits:
- Continuous Slate Space & Modern CSS notations (OKLCH, HSL, bare triplets, Slate-800, Teal-slate, Purple-slate)
- Legitimate Brand Navy preservation (Stripe #0A2540, Classic #001F3F, Prussian #003049, Oxford #14213D, Steel #1D3557)
- False-positive resistance (valid anchors, camelCase IDs, JSX arrow handlers in images, text #add)
- Rule-scoped pragmas vs un-scoped evasions
- Fail-closed guarantees
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

PATCH_SCRIPT = Path(__file__).parent / "anti_slop_static_patch.py"


def run_gate(project_dir: Path) -> tuple[int, dict]:
    res = subprocess.run(
        [sys.executable, str(PATCH_SCRIPT), str(project_dir)],
        capture_output=True,
        text=True
    )
    try:
        data = json.loads(res.stdout)
    except Exception:
        data = {"errors": 1 if res.returncode != 0 else 0, "raw": res.stdout, "stderr": res.stderr}
    return res.returncode, data


def create_base_valid_project(root: Path):
    app = root / "src" / "app"
    app.mkdir(parents=True, exist_ok=True)
    (app / "globals.css").write_text(
        ":root {\n"
        "  --color-canvas: #121212;\n"
        "  --color-ink: #f5f5f5;\n"
        "  --color-stone: #1C1917;\n"
        "  --color-stripe-navy: #0A2540;\n"
        "  --color-classic-navy: #001F3F;\n"
        "  --color-prussian: #003049;\n"
        "  --color-oxford: #14213D;\n"
        "  --color-steel: #1D3557;\n"
        "}\n",
        encoding="utf-8"
    )
    (app / "page.tsx").write_text(
        'export const metadata = { title: "Valid Title" };\n'
        'export default function Page() {\n'
        '  return (\n'
        '    <main id="main-content">\n'
        '      <a href="#main-content" className="sr-only">Skip to content</a>\n'
        '      <p>Click here to jump to #add section: <a href="#add">Add Section</a></p>\n'
        '      <a href="#cafe">Cafe Section</a>\n'
        '      <a href="#fee">Fee Breakdown</a>\n'
        '      <a href="#addToCart">Add to Cart</a>\n'
        '      <Image onLoad={() => console.log("ready")} src="/hero.jpg" alt="Hero banner" />\n'
        '    </main>\n'
        '  );\n'
        '}\n',
        encoding="utf-8"
    )


def test_mutations():
    print("=" * 82)
    print("   ADVERSARIAL MUTATION RUNNER & STATIC GATE INTEGRITY MATRIX (v2.4.0)")
    print("=" * 82)

    test_cases = [
        # 1. Clean valid baseline with brand navies, charcoals, valid anchors (MUST PASS 100%)
        ("Clean valid project (Stripe/Oxford navies, charcoal, stone, valid #add)",
         lambda r: None, 0, "clean-baseline"),

        # 2. Tailwind v4 OKLCH slate-900 in globals.css (MUST FAIL)
        ("Tailwind v4 OKLCH slate-900 in globals.css",
         lambda r: (r / "src" / "app" / "globals.css").write_text(
             ":root { --bg: oklch(0.208 0.042 265.755); }\n", encoding="utf-8"
         ), 1, "banned-slate"),

        # 3. HSL slate-900 in globals.css (MUST FAIL)
        ("HSL slate-900 hsl(222.2 47.4% 11.2%) in globals.css",
         lambda r: (r / "src" / "app" / "globals.css").write_text(
             ":root { --bg: hsl(222.2 47.4% 11.2%); }\n", encoding="utf-8"
         ), 1, "banned-slate"),

        # 4. Bare HSL triplet token in globals.css (MUST FAIL)
        ("Bare HSL triplet token --background: 222.2 47.4% 11.2%;",
         lambda r: (r / "src" / "app" / "globals.css").write_text(
             ":root { --background: 222.2 47.4% 11.2%; }\n", encoding="utf-8"
         ), 1, "banned-slate"),

        # 5. Slate-800 (#1E293B) in globals.css via continuous slate-space (MUST FAIL)
        ("Slate-800 #1E293B in globals.css (continuous slate region)",
         lambda r: (r / "src" / "app" / "globals.css").write_text(
             ":root { --card: #1E293B; }\n", encoding="utf-8"
         ), 1, "banned-slate-region"),

        # 6. Gray-800 (#1F2937) in module.css (MUST FAIL)
        ("Tailwind gray-800 #1F2937 in card.module.css",
         lambda r: (r / "src" / "card.module.css").write_text(
             ".card { background: #1F2937; }\n", encoding="utf-8"
         ), 1, "banned-slate-region"),

        # 7. Teal-slate (#0F1B1E, hue 221°) in globals.css (MUST FAIL)
        ("Teal-slate #0F1B1E in globals.css (widened hue region)",
         lambda r: (r / "src" / "app" / "globals.css").write_text(
             ":root { --bg: #0F1B1E; }\n", encoding="utf-8"
         ), 1, "banned-slate-region"),

        # 8. Purple-slate (#17141F, hue 302°) in globals.css (MUST FAIL)
        ("Purple-slate #17141F in globals.css (widened hue region)",
         lambda r: (r / "src" / "app" / "globals.css").write_text(
             ":root { --bg: #17141F; }\n", encoding="utf-8"
         ), 1, "banned-slate-region"),

        # 9. Raw hex color bypass in TSX (MUST FAIL)
        ("Raw hex color in TSX component",
         lambda r: (r / "src" / "app" / "page.tsx").write_text(
             'export const metadata = { title: "T" };\nexport default function Page() { return <div color="#ff5500">Hello</div>; }',
             encoding="utf-8"
         ), 1, "raw-color-bypasses-tokens"),

        # 10. Literal rgb() color function in TSX (MUST FAIL)
        ("Literal rgb() color function in TSX",
         lambda r: (r / "src" / "app" / "page.tsx").write_text(
             'export const metadata = { title: "T" };\nexport default function Page() { return <div style={{ color: "rgb(255, 0, 0)" }}>Hi</div>; }',
             encoding="utf-8"
         ), 1, "raw-color-function"),

        # 11. Decorative purple blur blob in TSX (MUST FAIL)
        ("Decorative purple blur blob in TSX",
         lambda r: (r / "src" / "app" / "page.tsx").write_text(
             'export const metadata = { title: "T" };\nexport default function Page() { return <div className="blur-2xl bg-purple-600">Blob</div>; }',
             encoding="utf-8"
         ), 1, "purple-blur-blob"),

        # 12. Image missing alt attribute (MUST FAIL)
        ("Image missing alt attribute",
         lambda r: (r / "src" / "app" / "page.tsx").write_text(
             'export const metadata = { title: "T" };\nexport default function Page() { return <img src="/test.jpg" />; }',
             encoding="utf-8"
         ), 1, "img-missing-alt"),

        # 13. Form blocking paste event (MUST FAIL)
        ("Form blocking paste event",
         lambda r: (r / "src" / "app" / "page.tsx").write_text(
             'export const metadata = { title: "T" };\nexport default function Page() { return <input onPaste={e => e.preventDefault()} />; }',
             encoding="utf-8"
         ), 1, "paste-blocked"),

        # 14. Dangling hash anchor href="#" (MUST FAIL)
        ("Dangling hash link href='#'",
         lambda r: (r / "src" / "app" / "page.tsx").write_text(
             'export const metadata = { title: "T" };\nexport default function Page() { return <a href="#">Link</a>; }',
             encoding="utf-8"
         ), 1, "dangling-hash-link"),

        # 15. Client component page missing metadata (MUST FAIL)
        ("Client component page without server metadata",
         lambda r: (r / "src" / "app" / "page.tsx").write_text(
             '"use client";\nexport default function Page() { return <div>Client only</div>; }',
             encoding="utf-8"
         ), 1, "client-page-no-metadata"),

        # 16. Empty project - fail closed (MUST FAIL)
        ("Empty workspace directory (0 files)",
         lambda r: shutil.rmtree(r / "src"),
         1, "no-files-scanned"),

        # 17. Unscoped pragma evasion attempt (MUST FAIL)
        ("Unscoped pragma attempt '// anti-slop-allow' without rule/reason",
         lambda r: (r / "src" / "app" / "page.tsx").write_text(
             'export const metadata = { title: "T" };\n'
             '// anti-slop-allow\n'
             'export default function Page() { return <div color="#ff5500">Unscoped</div>; }',
             encoding="utf-8"
         ), 1, "raw-color-bypasses-tokens"),

        # 18. Modern lab() dark slate in globals.css (MUST FAIL)
        ("Modern lab() dark slate lab(10.5 1.5 -9.5) in globals.css",
         lambda r: (r / "src" / "app" / "globals.css").write_text(
             ":root { --bg: lab(10.5 1.5 -9.5); }\n", encoding="utf-8"
         ), 1, "banned-slate"),

        # 19. Modern lch() dark slate in globals.css (MUST FAIL)
        ("Modern lch() dark slate lch(10.5 9.6 280) in globals.css",
         lambda r: (r / "src" / "app" / "globals.css").write_text(
             ":root { --bg: lch(10.5 9.6 280); }\n", encoding="utf-8"
         ), 1, "banned-slate"),

        # 20. Modern oklab() dark slate in globals.css (MUST FAIL)
        ("Modern oklab() dark slate oklab(0.208 -0.005 -0.042) in globals.css",
         lambda r: (r / "src" / "app" / "globals.css").write_text(
             ":root { --bg: oklab(0.208 -0.005 -0.042); }\n", encoding="utf-8"
         ), 1, "banned-slate"),

        # 21. Modern color(display-p3) dark slate in globals.css (MUST FAIL)
        ("Modern color(display-p3) dark slate in globals.css",
         lambda r: (r / "src" / "app" / "globals.css").write_text(
             ":root { --bg: color(display-p3 0.06 0.09 0.16); }\n", encoding="utf-8"
         ), 1, "banned-slate"),

        # 22. Rogue allowlisting via design_tokens.json attempt (MUST FAIL)
        ("Rogue self-approval attempt: #0F172A injected into design_tokens.json",
         lambda r: (
             (r / "design_tokens.json").write_text('{"colors": {"brand": "#0F172A"}}', encoding="utf-8"),
             (r / "src" / "app" / "globals.css").write_text(':root { --card: #0F172A; }\n', encoding="utf-8")
         ), 1, "banned-slate"),
    ]

    total = len(test_cases)
    passed_cases = 0

    for idx, (name, mutate, expected_code, expected_rule) in enumerate(test_cases, 1):
        tmp_dir = Path(tempfile.mkdtemp(prefix=f"mutation_matrix_{idx}_"))
        try:
            create_base_valid_project(tmp_dir)
            mutate(tmp_dir)
            code, data = run_gate(tmp_dir)

            success = False
            if expected_code == 0:
                success = (code == 0 and data.get("errors", 0) == 0)
                detail = "PASSED (Clean build verified, zero false alarms)"
            else:
                findings = data.get("findings", [])
                matched = any(f.get("rule") == expected_rule for f in findings)
                success = (code != 0 and matched)
                detail = f"CAUGHT [Rule: {expected_rule}]" if matched else f"MISSED (Errors: {data.get('errors')}, Findings: {[f.get('rule') for f in findings]})"

            if success:
                passed_cases += 1
                print(f"  [{idx:02d}/{total:02d}] PASS: {name:<65} -> {detail}")
            else:
                print(f"  [{idx:02d}/{total:02d}] FAIL: {name:<65} -> {detail}")

        finally:
            shutil.rmtree(tmp_dir, ignore_errors=True)

    print("=" * 82)
    print(f"MUTATION SUMMARY: {passed_cases}/{total} cases passed ({passed_cases/total*100:.1f}% catch & fidelity rate)")
    print("=" * 82)
    return passed_cases == total


if __name__ == "__main__":
    ok = test_mutations()
    sys.exit(0 if ok else 1)
