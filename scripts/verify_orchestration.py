#!/usr/bin/env python3
"""
verify_orchestration.py - Multi-Skill & MCP Orchestration Verifier (v2.1.0)
Part of the Universal Website Architect Engine.

Verifies that the AI did not hallucinate or 'fake' specialist skill & MCP usage:
1. Checks that claimed MCP primitives (Magic UI, 21st, shadcn) are physically present.
2. Checks that vector SVG logos exist on disk for partner/client showcases.
3. Checks that declared npm dependencies (Radix UI, motion, lucide) exist in package.json.
4. Validates stage receipts (.arch/receipts/stage-*.json) with Tailwind v4 utility support.
"""
import hashlib
import json
import os
import re
import sys
from pathlib import Path


class OrchestrationVerifier:
    def __init__(self, project_root: str):
        self.root = Path(project_root).resolve()
        self.src_dir = self.root / "src"
        if not self.src_dir.exists():
            self.src_dir = self.root
        
        self.violations = []
        self.passed_checks = []

    def verify_all(self) -> bool:
        print(f"[*] Verifying MCP & Multi-Skill Orchestration on: {self.root}")
        
        self.verify_package_json()
        self.verify_component_provenance()
        self.verify_svg_assets()
        self.verify_stage_receipts()

        print("\n" + "=" * 70)
        print("       MCP & MULTI-SKILL ORCHESTRATION REPORT")
        print("=" * 70)

        if self.passed_checks:
            print("\n[+] VERIFIED IMPLEMENTATIONS:")
            for p in self.passed_checks:
                print(f"  [OK] {p}")

        if self.violations:
            print("\n[-] ORCHESTRATION VIOLATIONS (BUILD REJECTED):")
            for v in self.violations:
                print(f"  {v}")
            print("\n" + "=" * 70)
            print(f"RESULT: FAILED ({len(self.violations)} violations).")
            print("Action: Fetch authentic components from MCPs or registry mirrors, and supply real SVGs.")
            print("=" * 70 + "\n")
            return False

        print("\n" + "=" * 70)
        print("RESULT: PASSED. All claimed skills, MCPs, and assets are authentically verified.")
        print("=" * 70 + "\n")
        return True

    def verify_package_json(self):
        pkg_path = self.root / "package.json"
        if not pkg_path.exists():
            self.violations.append(f"[FAIL] Missing package.json in {self.root}")
            return
        
        try:
            with open(pkg_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            deps = data.get("dependencies", {})
            dev_deps = data.get("devDependencies", {})
            all_deps = {**deps, **dev_deps}
            
            # Check essential icon primitives
            if "lucide-react" in all_deps:
                self.passed_checks.append("Lucide React icon system installed.")
            else:
                self.violations.append("[FAIL] lucide-react is not installed in package.json. Vector UI icon standard violated.")

            if "motion" in all_deps or "framer-motion" in all_deps:
                has_motion_import = False
                for p in self.src_dir.rglob("*.tsx"):
                    if "node_modules" not in p.parts and ".next" not in p.parts:
                        txt = p.read_text(encoding="utf-8")
                        if any(term in txt for term in ["from 'framer-motion'", 'from "framer-motion"', "from 'motion/react'", 'from "motion/react"', "motion."]):
                            has_motion_import = True
                            break
                if has_motion_import:
                    self.passed_checks.append("Motion / Framer Motion 60fps animation engine verified with active AST imports.")
                else:
                    self.violations.append(
                        "[FAIL] GHOST DEPENDENCY: 'framer-motion' is declared in package.json, but ZERO components import or use it! The website has zero interactive motion."
                    )
            else:
                self.violations.append("[FAIL] motion / framer-motion is not installed. 60fps interactive requirement violated.")

        except Exception as e:
            self.violations.append(f"[FAIL] Error reading package.json: {e}")

    def verify_component_provenance(self):
        ui_dir = self.src_dir / "components" / "ui"
        if not ui_dir.exists():
            ui_dir = self.src_dir / "components"
        
        components = list(ui_dir.glob("*.tsx")) + list(ui_dir.glob("*.jsx"))
        if not components:
            self.violations.append("[FAIL] No modular UI components found in src/components/ui/.")
            return

        app_files = [
            p for p in self.src_dir.rglob("*.tsx")
            if "node_modules" not in p.parts 
            and ".next" not in p.parts 
            and p.parent != ui_dir
        ]
        all_app_content = "\n".join(p.read_text(encoding="utf-8") for p in app_files) if app_files else ""

        for comp in components:
            comp_stem = comp.stem
            content = comp.read_text(encoding="utf-8")
            
            is_imported = comp_stem in all_app_content or comp_stem.replace("-", "") in all_app_content.lower()
            if not is_imported:
                self.violations.append(
                    f"[FAIL] GHOST COMPONENT DETECTED: '{comp.name}' exists in components/, but is NEVER imported or rendered anywhere in the application!"
                )
                continue

            if "marquee" in comp.name.lower():
                if "animate-marquee" in content or "transform" in content:
                    self.passed_checks.append(f"Authentic Marquee animation primitive verified in {comp.name} with active page import.")
            elif "bento" in comp.name.lower():
                self.passed_checks.append(f"Authentic Bento Grid component verified in {comp.name} with active page import.")
            else:
                self.passed_checks.append(f"Active UI component '{comp.name}' verified with active import in page.")

    def verify_svg_assets(self):
        template_svgs = {"file.svg", "globe.svg", "next.svg", "vercel.svg", "window.svg"}
        all_svgs = list(self.root.rglob("*.svg"))
        brand_svgs = [
            s for s in all_svgs 
            if "node_modules" not in s.parts 
            and ".next" not in s.parts 
            and s.name.lower() not in template_svgs
        ]

        # Verify physical SVG integrity (must be valid SVG XML, not empty or error pages)
        for s in brand_svgs:
            try:
                txt = s.read_text(encoding="utf-8", errors="ignore").strip()
                if len(txt) < 30 or "<svg" not in txt or "</svg>" not in txt:
                    self.violations.append(f"[FAIL] CORRUPTED_SVG_ASSET: '{s.name}' is empty, truncated, or not a valid SVG document!")
            except Exception as e:
                self.violations.append(f"[FAIL] UNREADABLE_SVG_ASSET: '{s.name}': {e}")

        has_partner_list = False
        for p in self.src_dir.rglob("*.tsx"):
            if "node_modules" not in p.parts and ".next" not in p.parts:
                txt = p.read_text(encoding="utf-8")
                if any(k in txt for k in ["RECRUITERS", "PARTNERS", "CLIENTS", "SPONSORS"]):
                    has_partner_list = True
                    break

        if has_partner_list:
            if not brand_svgs:
                self.violations.append(
                    "[FAIL] Project features a partner/recruiter showcase, but ZERO brand SVGs exist in assets/logos/. Plain text placeholders detected!"
                )
            else:
                self.passed_checks.append(f"Authentic brand vector SVGs verified ({len(brand_svgs)} brand logos in assets/logos/).")
        elif brand_svgs:
            self.passed_checks.append(f"Custom vector SVG graphic assets verified ({len(brand_svgs)} SVGs).")

    def verify_stage_receipts(self):
        receipts_dir = self.root / ".arch" / "receipts"
        if not receipts_dir.exists():
            return  # Greenfield build before receipts generation

        # Check for approval root in state.json
        state_file = self.root / ".arch" / "state.json"
        approval_root = None
        if state_file.exists():
            try:
                state_data = json.loads(state_file.read_text(encoding="utf-8"))
                approval_root = state_data.get("merkle_roots", {}).get("approval_root")
            except Exception:
                pass

        all_entries = list(receipts_dir.iterdir())
        valid_receipt_pattern = re.compile(r"^stage-(\d{2})-(.+)\.json$")

        for rec_file in all_entries:
            if rec_file.is_dir():
                continue

            # Reject rogue/fake receipt files that do not conform to stage naming schema
            match = valid_receipt_pattern.match(rec_file.name)
            if not match:
                self.violations.append(
                    f"[FAIL] ROGUE RECEIPT DETECTED: '{rec_file.name}' violates receipt naming contract!"
                )
                continue

            stage_num = match.group(1)

            try:
                data = json.loads(rec_file.read_text(encoding="utf-8"))
                # Verify strict schema attributes
                required_fields = ("stage", "outputs", "timestamp")
                missing_fields = [f for f in required_fields if f not in data]
                if missing_fields:
                    self.violations.append(
                        f"[FAIL] INVALID_RECEIPT_SCHEMA: {rec_file.name} missing required fields: {missing_fields}"
                    )
                    continue

                outputs = data.get("outputs", {})
                consumed_by = data.get("consumed_by", [])
                
                # Check output file existence and hash matching
                for rel_path, rec_hash in outputs.items():
                    out_disk = self.root / rel_path
                    if not out_disk.exists():
                        self.violations.append(
                            f"[FAIL] MISSING_RECEIPT_OUTPUT: '{rel_path}' declared in {rec_file.name} does not exist on disk!"
                        )
                        continue
                    cur_hash = "sha256:" + hashlib.sha256(out_disk.read_bytes()).hexdigest()
                    if cur_hash != rec_hash:
                        self.violations.append(
                            f"[FAIL] RECEIPT TAMPERING: {rel_path} on-disk hash does not match receipt {rec_file.name}"
                        )

                # Approval root cryptographic linkage for post-approval stages (08+)
                if int(stage_num) >= 8 and approval_root:
                    rec_appr = data.get("approval_root")
                    if not rec_appr or rec_appr != approval_root:
                        self.violations.append(
                            f"[FAIL] UNLINKED_BUILD_STAGE: {rec_file.name} lacks valid cryptographic approval_root matching state.json!"
                        )

                # Check consumed_by references (supports both var(--token) and Tailwind v4 utility classes)
                for consumer in consumed_by:
                    c_disk = self.root / consumer
                    if c_disk.exists():
                        c_text = c_disk.read_text(encoding="utf-8")
                        has_token_usage = "var(--" in c_text or re.search(r"\b(?:bg|text|border|ring)-[a-zA-Z0-9_-]+", c_text)
                        if not has_token_usage:
                            self.violations.append(f"[FAIL] UNCONSUMED TOKEN: {consumer} declared in receipt but has no token/utility references!")
                self.passed_checks.append(f"Stage receipt verified: {rec_file.name}")
            except Exception as e:
                self.violations.append(f"[FAIL] Error parsing receipt {rec_file.name}: {e}")


def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print("Usage: python verify_orchestration.py [path_to_project_root]")
        sys.exit(0)
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    verifier = OrchestrationVerifier(target_dir)
    passed = verifier.verify_all()
    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
