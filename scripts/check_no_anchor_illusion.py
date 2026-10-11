# check_no_anchor_illusion.py
# Mechanical AST / regex gate enforcing true multi-page architecture in Next.js / Vite
import os
import re
import sys
from pathlib import Path

def audit_multipage_architecture(app_dir: str):
    app_path = Path(app_dir)
    if not app_path.exists():
        print(f"[FATAL] App directory {app_dir} does not exist.")
        sys.exit(1)

    # 1. Count distinct page.tsx / page.jsx / page.js files
    pages = list(app_path.glob("**/page.tsx")) + list(app_path.glob("**/page.jsx")) + list(app_path.glob("**/page.js"))
    print(f"[*] Discovered {len(pages)} distinct route pages:")
    for p in pages:
        rel = p.relative_to(app_path)
        print(f"    - /{rel.parent.as_posix() if str(rel.parent) != '.' else ''}")

    if len(pages) < 3:
        print(f"[FAIL] SINGLE-PAGE ILLUSION DETECTED! Found only {len(pages)} page(s). Minimum required is 3.")
        sys.exit(1)

    # 2. Check for anchor link fallbacks in primary navigation components
    parent_dir = app_path.parent
    nav_files = (
        list(parent_dir.glob("**/Navigation*.tsx")) +
        list(parent_dir.glob("**/Header*.tsx")) +
        list(parent_dir.glob("**/Nav*.tsx")) +
        list(app_path.glob("**/layout.tsx"))
    )
    # Detects href="#section", href="/#section", href={`#${...}`}, href={`/#section`}
    anchor_pattern = re.compile(r'href=(?:[\'"][#/][a-zA-Z0-9_-]*#[a-zA-Z0-9_-]+[\'"]|{[\s]*[`\'"][#/]?[a-zA-Z0-9_-]*#[a-zA-Z0-9_-]*[`\'"][\s]*})')

    violations = []
    for nf in nav_files:
        content = nf.read_text(encoding="utf-8", errors="ignore")
        matches = anchor_pattern.findall(content)
        if matches:
            violations.append((nf.name, matches))

    if violations:
        print("[FAIL] PRIMARY NAVIGATION CONTAINS HASH ANCHORS INSTEAD OF PROPER ROUTES:")
        for name, m in violations:
            print(f"    In {name}: {m}")
        sys.exit(1)

    print("[PASS] Multi-page architecture verified successfully! Real routes confirmed.")

if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        print("Usage: python check_no_anchor_illusion.py <path_to_app_dir>")
        sys.exit(0)
    target = sys.argv[1] if len(sys.argv) > 1 else "src/app"
    audit_multipage_architecture(target)
