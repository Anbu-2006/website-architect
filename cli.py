#!/usr/bin/env python3
"""
Website Architect & Master Builder — Unified Command Line Interface
Author: Anbuselvan T. (@Anbu-2006)
"""

import sys
import os
import argparse
import subprocess
from pathlib import Path

# Fix Windows console UTF-8 encoding
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = BASE_DIR / "scripts"

def run_script(script_name: str, args: list):
    script_path = SCRIPTS_DIR / script_name
    if not script_path.exists():
        print(f"Error: Script {script_name} not found at {script_path}", file=sys.stderr)
        sys.exit(1)
    cmd = [sys.executable, str(script_path)] + args
    return subprocess.run(cmd)

def main():
    parser = argparse.ArgumentParser(
        prog="website-architect",
        description="🏛️ Universal Website Architect & Master Builder Engine CLI"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # classify
    classify_parser = subparsers.add_parser("classify", help="Analyze business prompt or URL to determine design archetype")
    classify_parser.add_argument("--pitch", required=True, help="Business pitch or prompt string")
    classify_parser.add_argument("--reference-url", help="Benchmark reference website URL")

    # preview
    preview_parser = subparsers.add_parser("preview", help="Generate zero-credit 16:9 SVG wireframe section options")
    preview_parser.add_argument("--section", default="hero", help="Page section name (hero, bento, pricing, etc.)")
    preview_parser.add_argument("--archetype", default="dark-tech", help="Visual archetype name")
    preview_parser.add_argument("--output", help="Output path for preview HTML")

    # audit
    audit_parser = subparsers.add_parser("audit", help="Run 22+ AST forensic anti-slop checks on codebase")
    audit_parser.add_argument("path", default=".", nargs="?", help="Target project directory to audit")

    # extract
    extract_parser = subparsers.add_parser("extract", help="Extract live design tokens from a benchmark URL")
    extract_parser.add_argument("--url", required=True, help="Website URL to extract tokens from")
    extract_parser.add_argument("--output", help="Path to save tokens JSON")

    # verify
    verify_parser = subparsers.add_parser("verify", help="Verify component installation receipts and AST integrity")
    verify_parser.add_argument("path", default=".", nargs="?", help="Target project directory to verify")

    args, unknown = parser.parse_known_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    if args.command == "classify":
        sub_args = ["--pitch", args.pitch]
        if args.reference_url:
            sub_args += ["--reference-url", args.reference_url]
        res = run_script("classify_business.py", sub_args)
        sys.exit(res.returncode)

    elif args.command == "preview":
        sub_args = ["--section", args.section, "--archetype", args.archetype]
        if args.output:
            sub_args += ["--output", args.output]
        res = run_script("section_option_previewer.py", sub_args)
        sys.exit(res.returncode)

    elif args.command == "audit":
        res = run_script("anti_slop_gate.py", [args.path])
        sys.exit(res.returncode)

    elif args.command == "extract":
        sub_args = ["--url", args.url]
        if args.output:
            sub_args += ["--output", args.output]
        res = run_script("extract_tokens.py", sub_args)
        sys.exit(res.returncode)

    elif args.command == "verify":
        res = run_script("verify_orchestration.py", [args.path])
        sys.exit(res.returncode)

if __name__ == "__main__":
    main()
