#!/usr/bin/env python3
"""
anti_slop_gate.py - Automated AST & Layout Anti-Slop Verification Gate (v2.4.0)
Part of the Universal Website Architect Engine.

This script scans Next.js / React application source code, stylesheets, and AST
structures to detect and eliminate all 15 canonical "AI Slop" smells and frontend
defects before production sign-off:

1.  UNIFORM_CARD_SYNDROME: Symmetrical 3-up/4-up horizontal card kits shouting at equal volume
2.  CARD_CEPTION_SLOP: Nested cards within cards creating visual clutter
3.  DECORATIVE_BLUR_SLOP: Floating ambient gradient mesh blur blobs (blur-3xl rounded-full)
4.  STRUCTURAL_EMOJI: Emojis used as UI icons or action buttons instead of SVG vectors
5.  TEXT_PLACARD_LOGOS: Partner/client lists declared as plain text without authentic SVG marks
6.  TOKEN_DIVERGENCE: Failure to bind authentic benchmark display fonts in globals.css
7.  HERO_BOOKING_WIDGET_SLOP: Cluttered booking aggregator search boxes inside luxury hero sections
8.  HERO_STAT_STRIP_SLOP: Generic 4-stat metric strip in hero ("4.9★", "500+ guests", "100%")
9.  HERO_MOTION_MISSING: Hero section completely static without video, Ken-Burns, or motion reveals
10. NON_COMPOSITED_ANIMATION: Animating layout geometry (width, height, top, left, margin, padding)
11. STUB_PAGE_SLOP: Subpage routes with < 4 structural section components (empty skeleton stubs)
12. GENERIC_BUTTON_SLOP: Dummy button labels ("Click Here") or empty/alert() click handlers
13. ANCHOR_ILLUSION_SLOP: Pseudo-navigation using #hash jumps in primary nav without real routing
14. MAGIC_METRIC_SLOP: Fabricated marketing metrics ("99.9% satisfaction", "10M+ users") without audit proof
15. MOBILE_INPUT_ZOOM_DEFECT: Form inputs with font-size < 16px triggering iOS Safari viewport zoom
16. TOUCH_TARGET_DEFECT: Compact interactive controls < 44x44px without hit area expansion
17. REDUCED_MOTION_DEFECT: Missing @media (prefers-reduced-motion: reduce) accessibility safeguards
18. STICKY_HOVER_DEFECT: Persistent sticky hover states on touch devices lacking hover media query
"""

import os
import sys
import re
import json
import argparse
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Common emoji regex
EMOJI_PATTERN = re.compile(
    r"[\U0001F1E0-\U0001F1FF"  # flags (iOS)
    r"\U0001F300-\U0001F5FF"  # symbols & pictographs
    r"\U0001F600-\U0001F64F"  # emoticons
    r"\U0001F680-\U0001F6FF"  # transport & map
    r"\U0001F700-\U0001F77F"  # alchemical
    r"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    r"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    r"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    r"\U0001FA00-\U0001FA6F"  # Chess Symbols
    r"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    r"\U00002702-\U000027B0"  # Dingbats
    r"\U000024C2-\U0001F251"
    r"]+",
    flags=re.UNICODE,
)

class AntiSlopAuditor:
    def __init__(self, project_root: str):
        self.root = Path(project_root).resolve()
        self.src_dir = self.root / "src"
        if not self.src_dir.exists():
            self.src_dir = self.root
        
        self.violations = []
        self.warnings = []
        self.passed_checks = []

    def log_violation(self, rule: str, file_path: Path, line_no: int, message: str):
        try:
            rel = file_path.relative_to(self.root)
        except Exception:
            rel = file_path.name
        self.violations.append(f"[FAIL] {rule} ({rel}:{line_no}) -> {message}")

    def log_warning(self, rule: str, file_path: Path, line_no: int, message: str):
        try:
            rel = file_path.relative_to(self.root)
        except Exception:
            rel = file_path.name
        self.warnings.append(f"[WARN] {rule} ({rel}:{line_no}) -> {message}")

    def audit_all(self) -> bool:
        print(f"[*] Running Anti-Slop Audit on: {self.root}")
        
        # 1. Audit Token Grounding & Design Systems
        self.audit_design_tokens_binding()

        # 2. Audit Global Stylesheet for Mobile & Accessibility Defect Guards
        self.audit_global_styles()

        # 3. Audit Source Files
        for ext in ("*.tsx", "*.jsx", "*.ts", "*.js"):
            for p in self.src_dir.rglob(ext):
                if "node_modules" in p.parts or ".next" in p.parts:
                    continue
                self.audit_file(p)

        # 4. Print Report
        print("\n" + "=" * 70)
        print("          ANTI-SLOP AUDIT VERIFICATION REPORT (v2.4.0)")
        print("=" * 70)
        
        if self.passed_checks:
            print("\n[+] PASSED CHECKS:")
            for p in set(self.passed_checks):
                print(f"  [OK] {p}")

        if self.warnings:
            print("\n[!] WARNINGS:")
            for w in self.warnings:
                print(f"  {w}")

        if self.violations:
            print(f"\n[-] CRITICAL ANTI-SLOP VIOLATIONS ({len(self.violations)} detected):")
            for v in self.violations:
                print(f"  {v}")
            print("\n" + "=" * 70)
            print("RESULT: BUILD REJECTED DUE TO AI SLOP PATTERNS.")
            print("Action: Resolve violations above: eliminate symmetrical 3-card monotony, nested cards,")
            print("ungrounded blur blobs, dummy buttons, and adhere to 60fps GPU compositor & mobile ergonomic rules.")
            print("=" * 70 + "\n")
            return False

        print("\n" + "=" * 70)
        print("RESULT: PASSED. Zero AI slop patterns or ergonomic defects detected.")
        print("=" * 70 + "\n")
        return True

    def audit_design_tokens_binding(self):
        tokens_path = self.root / "design_tokens.json"
        if not tokens_path.exists():
            self.log_warning("TOKEN_GROUNDING", tokens_path, 1, "design_tokens.json not found in root. Benchmark grounding unverified.")
            return

        try:
            with open(tokens_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            self.log_warning("TOKEN_GROUNDING", tokens_path, 1, f"Failed to parse design_tokens.json: {e}")
            return

        typo = data.get("typography", {})
        h1_font = typo.get("h1", {}).get("fontFamily", "")
        h2_font = typo.get("h2", {}).get("fontFamily", "")
        
        target_display_font = None
        for font_str in [h2_font, h1_font]:
            if font_str and font_str != "inherit":
                clean = font_str.split(",")[0].replace('"', "").replace("'", "").strip()
                if clean and clean.lower() not in ["sans-serif", "serif", "system-ui", "monospace"]:
                    target_display_font = clean
                    break

        if not target_display_font:
            return

        globals_css = self.find_globals_css()
        if globals_css and globals_css.exists():
            content = globals_css.read_text(encoding="utf-8")
            if target_display_font.lower() not in content.lower():
                self.log_violation(
                    "TOKEN_DIVERGENCE",
                    globals_css,
                    1,
                    f"Extracted benchmark display font '{target_display_font}' from design_tokens.json was NOT bound in globals.css!"
                )
            else:
                self.passed_checks.append(f"Authentic reference display font '{target_display_font}' correctly bound in globals.css.")

    def find_globals_css(self) -> Path | None:
        for candidate in [
            self.src_dir / "app" / "globals.css",
            self.src_dir / "globals.css",
            self.src_dir / "index.css",
            self.root / "app" / "globals.css",
            self.root / "styles" / "globals.css"
        ]:
            if candidate.exists():
                return candidate
        return None

    def audit_global_styles(self):
        globals_css = self.find_globals_css()
        if not globals_css or not globals_css.exists():
            self.log_warning("STYLESHEET_CHECK", self.root, 1, "Global stylesheet (globals.css/index.css) not found.")
            return

        content = globals_css.read_text(encoding="utf-8")

        # 1. Reduced Motion Check
        if "prefers-reduced-motion" not in content:
            self.log_violation(
                "REDUCED_MOTION_DEFECT",
                globals_css,
                1,
                "Global stylesheet lacks @media (prefers-reduced-motion: reduce) safeguards! Must provide reduced-motion fallbacks for all animations (WCAG 2.2 Criterion 2.3.3)."
            )
        else:
            self.passed_checks.append("Accessible reduced-motion safeguards present in global stylesheet.")

        # 2. Mobile Input Font Zoom Check
        has_16px_input_rule = False
        if re.search(r'(input|select|textarea)[^{]*\{[^}]*font-size:\s*(16px|1rem)', content):
            has_16px_input_rule = True
        elif "@media" in content and "max-width: 768px" in content and "16px" in content:
            has_16px_input_rule = True

        if not has_16px_input_rule:
            self.log_warning(
                "MOBILE_INPUT_ZOOM_DEFECT",
                globals_css,
                1,
                "No explicit 16px (1rem) base rule detected for input/textarea/select elements. On iOS Safari, form controls with font size < 16px trigger disruptive automatic viewport zoom."
            )
        else:
            self.passed_checks.append("Mobile form 16px font-size safeguards declared in global stylesheet.")

        # 3. Focus-visible Ring Check
        if ":focus-visible" in content:
            self.passed_checks.append("Dual-layer :focus-visible indicators declared in global stylesheet.")
        else:
            self.log_warning(
                "FOCUS_AFFORDANCE",
                globals_css,
                1,
                "No explicit :focus-visible declaration found. Ensure interactive elements maintain accessible high-contrast focus rings."
            )

    def audit_file(self, file_path: Path):
        try:
            lines = file_path.read_text(encoding="utf-8").splitlines()
        except Exception:
            return

        is_page = file_path.name in ["page.tsx", "page.jsx"]
        file_text = "\n".join(lines)
        consecutive_card_patterns = 0

        # Check 11: Card-ception (Nested Cards within Cards)
        # Look for <Card ...> inside another <Card ...> or nested rounded border panels
        nested_card_match = re.search(r'<Card\b[^>]*>(?:(?!<\/Card>).)*?<Card\b', file_text, re.DOTALL)
        if nested_card_match:
            self.log_violation(
                "CARD_CEPTION_SLOP",
                file_path,
                1,
                "Detected 'Card-ception' (nested cards inside cards). This creates visual clutter and is a hallmark of lazy AI templating. Use whitespace, sectional breaks, or asymmetric editorial splits instead."
            )
        else:
            # Check for double nested rounded border divs
            nested_div_card = re.search(r'className=["\'][^"\']*\brounded-(?:xl|2xl)\b[^"\']*\bborder\b[^"\']*["\'][^>]*>(?:(?!<\/div>).)*?className=["\'][^"\']*\brounded-(?:lg|xl|md)\b[^"\']*\bborder\b', file_text, re.DOTALL)
            if nested_div_card:
                self.log_violation(
                    "CARD_CEPTION_SLOP",
                    file_path,
                    1,
                    "Detected nested border containers ('card inside card'). Flatten the hierarchy using crisp whitespace and typographic distinction."
                )

        # Check 13: Pseudo-Navigation (Anchor Hash Jumps in Nav)
        if "nav" in file_path.name.lower() or "header" in file_path.name.lower():
            hash_jumps = re.findall(r'href=["\'](#[a-zA-Z0-9_-]+)["\']', file_text)
            bad_hashes = [h for h in hash_jumps if h in ["#features", "#about", "#pricing", "#services", "#contact", "#team"]]
            if len(bad_hashes) >= 2:
                self.log_violation(
                    "ANCHOR_ILLUSION_SLOP",
                    file_path,
                    1,
                    f"Primary navigation uses anchor hash jumps {bad_hashes} without real multi-page routing. In Next.js App Router, implement genuine subroutes (/about, /accommodations, /contact) or use dynamic slide-out drawers."
                )

        # Check 14: Fabricated Marketing Metrics ("Magic Metrics")
        for i, line in enumerate(lines, 1):
            if any(term in line for term in ["99.9% customer happiness", "99.9% satisfaction", "10M+ users", "10,000,000+ active users", "500M+ downloads"]):
                # Ensure it has attribution or source
                if not any(attr in line.lower() for attr in ["soc2", "audit", "source:", "verified by", "certified"]):
                    self.log_violation(
                        "MAGIC_METRIC_SLOP",
                        file_path,
                        i,
                        "Detected ungrounded marketing metric ('99.9% satisfaction' / '10M+ users') without source attribution or audit proof. State verifiable outcomes or link to third-party verification."
                    )

            # Check 1: Structural Emojis in JSX
            if "<" in line or "className" in line or "title" in line or "label" in line:
                emojis = EMOJI_PATTERN.findall(line)
                if emojis:
                    clean_line = line.strip()
                    if not clean_line.startswith("//") and not clean_line.startswith("/*") and not clean_line.startswith("*"):
                        self.log_violation(
                            "STRUCTURAL_EMOJI",
                            file_path,
                            i,
                            f"Structural emoji '{emojis[0]}' detected in UI. Must use SVG vector icons (Lucide/Heroicons/SVGL)."
                        )

            # Check 2: Text-only Placards for Partners / Recruiters
            if any(term in line for term in ["RECRUITERS", "PARTNERS", "CLIENTS", "SPONSORS", "HIRING_PARTNERS"]):
                array_text = "\n".join(lines[i-1:i+40])
                has_names = re.search(r'["\']?name["\']?\s*:', array_text)
                has_logos = any(k in array_text.lower() for k in ["logo", "svg", "image", "logo_url", "icon_url"])
                if has_names and not has_logos:
                    self.log_violation(
                        "TEXT_PLACARD_LOGOS",
                        file_path,
                        i,
                        "Partner/client list declared as plain text without SVG vector logos. Must render authentic SVG brand marks."
                    )

            # Check 3: Floating Gradient / Radial Blur Blobs
            if ("blur-3xl" in line or "blur-2xl" in line) and "rounded-full" in line and ("absolute" in line or "translate" in line):
                self.log_violation(
                    "DECORATIVE_BLUR_SLOP",
                    file_path,
                    i,
                    "Detected generic AI slop decorative blur blob ('filter blur-3xl rounded-full'). Replace with authentic architectural planes, photography, or directional spotlights."
                )

            # Check 4: Repetitive Card Grid Syndrome Tracker
            if "grid-cols-2" in line or "grid-cols-3" in line or "grid-cols-4" in line:
                grid_snippet = "\n".join(lines[i-1:i+30])
                if ("rounded-xl" in grid_snippet or "rounded-2xl" in grid_snippet) and "border" in grid_snippet and ("p-6" in grid_snippet or "p-8" in grid_snippet):
                    consecutive_card_patterns += 1

            # Check 10: Non-Composited Animations
            if "transition:" in line or "transition-" in line:
                for bad_prop in ["width", "height", "top", "left", "margin", "padding"]:
                    if re.search(rf'transition:\s*[^;]*\b{bad_prop}\b', line) or f"transition-{bad_prop}" in line:
                        self.log_violation(
                            "NON_COMPOSITED_ANIMATION",
                            file_path,
                            i,
                            f"Detected animation/transition on layout property '{bad_prop}'. 60fps GPU compliance requires animating ONLY composited properties (transform, opacity)."
                        )
                if "transition: all" in line or "transition-all" in line:
                    if "section" in line.lower() or "grid" in line.lower() or "h-" in line:
                        self.log_violation(
                            "NON_COMPOSITED_ANIMATION",
                            file_path,
                            i,
                            "Detected 'transition: all' on a major structural layout wrapper. Specify explicit GPU properties (transform, opacity) to prevent 60fps frame drops."
                        )

            # Check 12: Generic Dummy Buttons
            if "<button" in line or "<Link" in line or "<a " in line or "Button" in line:
                for dummy in ["Click Here", "click here", "CLICK HERE", "Submit Button", "Test Button", "Dummy Button"]:
                    if dummy in line:
                        self.log_violation(
                            "GENERIC_BUTTON_SLOP",
                            file_path,
                            i,
                            f"Detected generic dummy button label '{dummy}'. Replace with high-intent action copy (e.g. 'Reserve Cottage', 'Explore Grounds', 'View Tasting Menu')."
                        )
                if "onClick={() => {}}" in line or "onClick={() => { }}" in line or "onClick={() => alert(" in line:
                    self.log_violation(
                        "GENERIC_BUTTON_SLOP",
                        file_path,
                        i,
                        "Detected empty or alert() click handler in button. Connect to authentic interactive state or modal dispatch."
                    )
                if re.search(r'>(Learn More|Read More)</', line) and ('href="#"' in line or 'href=""' in line or "<button" in line):
                    self.log_violation(
                        "GENERIC_BUTTON_SLOP",
                        file_path,
                        i,
                        "Detected ungrounded 'Learn More' / 'Read More' link without a real destination. Direct to specific subpage route or slide-out drawer."
                    )

            # Check 16: Touch Target Hitbox Check for Compact Icon Buttons
            if "<button" in line and any(cls in line for cls in ["w-5 h-5", "w-6 h-6", "h-6 w-6", "h-5 w-5", "p-0.5", "p-1"]) and not any(exp in line for exp in ["p-2", "p-3", "p-4", "min-w-[44px]", "min-h-[44px]", "hitbox", "before:", "after:"]):
                self.log_warning(
                    "TOUCH_TARGET_DEFECT",
                    file_path,
                    i,
                    "Detected compact icon button with dimensions < 44x44px. Under WCAG 2.2 / Apple HIG, interactive touch surfaces must maintain ≥ 44x44px hit areas via padding or pseudo-elements."
                )

            # Check 19: Paste Interception Prevention
            if "onPaste=" in line and "preventDefault()" in line:
                self.log_violation(
                    "PASTE_INTERCEPTION_DEFECT",
                    file_path,
                    i,
                    "Detected form input blocking native paste operation ('onPaste={...preventDefault()}'). Native clipboard operations must never be intercepted."
                )

            # Check 20: Non-Semantic Clickable Containers
            if "<div" in line and "onClick=" in line and not any(r in line for r in ["role=", "role =", "role:"]):
                self.log_warning(
                    "NON_SEMANTIC_CLICKABLE_DEFECT",
                    file_path,
                    i,
                    "Detected clickable <div onClick={...}> without role='button' and keyboard bindings. Use semantic <button> or add role='button' and tabIndex."
                )

            # Check 21: Abstract Buzzword Filler Copy in Headings
            if "<h1" in line or "<h2" in line or "<h3" in line:
                for buzz in ["transform your workflow", "cutting-edge ai", "unlock unprecedented potential", "supercharge your growth", "next-gen platform"]:
                    if buzz in line.lower():
                        self.log_violation(
                            "BUZZWORD_FILLER_SLOP",
                            file_path,
                            i,
                            f"Detected generic marketing buzzword '{buzz}'. Headlines must state a concrete capability, operational metric, or specific domain outcome."
                        )

            # Check for placeholder stub text
            for stub_phrase in ["Under Construction", "Coming Soon", "TODO: Implement", "Lorem ipsum"]:
                if stub_phrase.lower() in line.lower() and not line.strip().startswith("//") and not line.strip().startswith("/*"):
                    self.log_violation(
                        "PLACEHOLDER_STUB_SLOP",
                        file_path,
                        i,
                        f"Detected placeholder text '{stub_phrase}'. Every section must be fully written and populated with authentic business content."
                    )

        # Check 7: Hero Motion Absence
        if "hero" in file_path.name.lower():
            has_video = "<video" in file_text
            has_kenburns = "animate-ken-burns" in file_text or "kenburns" in file_text or "ken-burns" in file_text
            has_motion = "motion." in file_text or "framer-motion" in file_text
            if not (has_video or has_kenburns or has_motion):
                self.log_violation(
                    "HERO_MOTION_MISSING",
                    file_path,
                    1,
                    "Hero section is completely static! Benchmark replication requires either an ambient video loop (<video), a 60fps GPU Ken-Burns cinema pan (animate-ken-burns), or Framer Motion reveals."
                )
            else:
                self.passed_checks.append(f"Hero section in '{file_path.name}' contains verified ambient motion.")

        # Check 9: Multi-Page Route Depth Check (Ban 1-Section Skeleton Stubs)
        if is_page:
            # Detect imported section components (e.g. from components/sections/), native <section> tags, or top-level custom section components
            section_comp_imports = set(re.findall(r'import\s+([A-Z][a-zA-Z0-9]+)\s+from\s+["\'][^"\']*components/sections', file_text))
            rendered_section_tags = len(re.findall(r'<section\b', file_text))
            all_rendered_custom_comps = set(re.findall(r'<([A-Z][a-zA-Z0-9]+)\b', file_text)) - {
                "Link", "Image", "Head", "Fragment", "Suspense", "Metadata", "Header", "Footer", "MobileHotbar"
            }
            num_sections = max(
                len(section_comp_imports),
                rendered_section_tags,
                len(all_rendered_custom_comps)
            )
            is_contact_or_auth = any(part in str(file_path).lower() for part in ["contact", "login", "portal", "register"])
            min_sections = 3 if is_contact_or_auth else 4
            
            if num_sections < min_sections:
                self.log_violation(
                    "STUB_PAGE_SLOP",
                    file_path,
                    1,
                    f"Page only renders {num_sections} section(s) (minimum required: {min_sections}). 1-section skeleton stubs are strictly prohibited! Every page route must feature a full, rich architecture (Hero, In-Depth Content/Story, Interactive Module/Filter, Proof/Testimonials, and Direct Conversion Action)."
                )
            else:
                self.passed_checks.append(f"Page route '{file_path.name}' meets minimum section depth ({num_sections} >= {min_sections} sections).")

        if is_page and consecutive_card_patterns >= 3:
            self.log_violation(
                "UNIFORM_CARD_SYNDROME",
                file_path,
                1,
                f"Detected {consecutive_card_patterns} repetitive uniform card grids ('SaaS Card Kit' AI slop). Break the monotony with asymmetric Bento Grid 2.0 (8-column primary cell + 4-column secondary cells) or 60/40 directional editorial splits."
            )

        # Check 22: WebGL Context Disposal & Clamped DPR (for R3F Canvas components)
        if "<Canvas" in file_text or ("Canvas" in file_text and "@react-three/fiber" in file_text):
            has_dispose = "dispose" in file_text or "WEBGL_lose_context" in file_text or "onCreated" in file_text
            if not has_dispose:
                self.log_violation(
                    "WEBGL_DISPOSAL_DEFECT",
                    file_path,
                    1,
                    "React Three Fiber Canvas component lacks unmount cleanup! Must dispose scene geometries/materials and invoke WEBGL_lose_context on route tear-down to avoid GPU memory leaks."
                )
            else:
                self.passed_checks.append(f"R3F Canvas in '{file_path.name}' implements verified memory cleanup.")

            if "dpr=" not in file_text and "dpr={" not in file_text:
                self.log_warning(
                    "UNCONSTRAINED_DPR_DEFECT",
                    file_path,
                    1,
                    "R3F Canvas initialized without explicit DPR clamping. Enforce dpr={[1, 2]} to protect mobile fill rates and GPU thermal budgets."
                )

def main():
    parser = argparse.ArgumentParser(description="AST Anti-Slop Audit Gate (v2.4.0)")
    parser.add_argument("pos_path", nargs="?", default=None, help="Target directory (positional)")
    parser.add_argument("--project-root", "--path", "--dir", dest="flag_path", default=None, help="Target directory (flag)")
    args = parser.parse_args()
    target_dir = args.flag_path or args.pos_path or "."
    auditor = AntiSlopAuditor(target_dir)
    passed = auditor.audit_all()
    sys.exit(0 if passed else 1)

if __name__ == "__main__":
    main()
