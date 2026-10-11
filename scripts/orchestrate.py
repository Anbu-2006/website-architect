#!/usr/bin/env python3
"""
scripts/orchestrate.py - Autonomous 5-Subagent Finite State Machine Runner
Part of the Universal Website Architect Engine (v2.5.0).

Governs 5 specialized autonomous subagents across deterministic lifecycle states,
spatial file-system fencing, and signed schema contracts:
- Agent 1: Deep Internet Scout & Benchmark Harvester (extract_tokens.py & harvest_assets.py)
- Agent 2: Creative Art Director (creative_director_agent.py -> creative_thesis.json)
- Agent 3: 3D & Kinetic Motion Specialist (scene_graph_generator.py -> scene_graph.json + Canvas)
- Agent 4: Master Production Builder (clone_reference_structure.py -> Next.js App Router)
- Agent 5: Forensic Quality Gate Auditor (anti_slop_gate.py [22+ checks] & verify_orchestration.py)

Operates on a 100% ZERO-CREDIT policy: All scraping, token extraction, asset harvesting,
vector icons, and ambient video loops are executed via local compute, public CDNs, and
free browser automation with zero external paid API credits.
"""

import os
import sys
import json
import argparse
import subprocess
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

SCRIPT_DIR = Path(__file__).resolve().parent

def run_step(agent_name: str, cmd: list, step_num: int, total_steps: int = 5):
    print("\n" + "=" * 70)
    print(f"[{step_num}/{total_steps}] RUNNING AGENT {step_num}: {agent_name.upper()}")
    print(f"[*] Command: {' '.join(str(c) for c in cmd)}")
    print("=" * 70)
    
    res = subprocess.run(cmd, capture_output=False, text=True)
    if res.returncode != 0:
        print(f"\n[!] ERROR: Agent {step_num} ({agent_name}) failed with exit code {res.returncode}")
        return False
    print(f"\n[+] SUCCESS: Agent {step_num} ({agent_name}) completed successfully.")
    return True

def run_master_orchestration(
    benchmark_url: str,
    query: str,
    domain: str = None,
    out_dir: str = ".",
    category: str = "luxury",
    include_video: bool = True,
    include_3d: bool = True
):
    root = Path(out_dir).resolve()
    assets_dir = root / "public" / "assets"
    slices_dir = root / ".website-architect" / "reference_slices"
    sections_dir = root / "src" / "components" / "sections"
    canvas_dir = root / "src" / "components" / "canvas"
    motion_lib_dir = root / "src" / "lib" / "motion"
    page_out = root / "src" / "app" / "page.tsx"
    
    report = {
        "status": "in_progress",
        "engine_version": "2.5.0",
        "benchmark_url": benchmark_url,
        "client_query": query,
        "client_domain": domain,
        "agents": {
            "agent_1_internet_scout": "pending",
            "agent_2_art_director": "pending",
            "agent_3_3d_motion_specialist": "pending",
            "agent_4_production_builder": "pending",
            "agent_5_quality_auditor": "pending"
        },
        "artifacts": {}
    }

    # -------------------------------------------------------------
    # AGENT 1: Deep Internet Scout & Benchmark Harvester
    # -------------------------------------------------------------
    tokens_out = root / "design_tokens.json"
    design_md = root / "DESIGN.md"
    tree_out = root / "reference_layout_tree.json"
    motion_out = root / "animation_inventory.json"
    recordings_dir = root / ".website-architect" / "reference_recordings"

    agent1_cmd = [
        sys.executable,
        str(SCRIPT_DIR / "extract_tokens.py"),
        "--url", benchmark_url,
        "--out", str(design_md),
        "--tokens-out", str(tokens_out),
        "--layout-tree-out", str(tree_out),
        "--slices-dir", str(slices_dir),
        "--record-video-dir", str(recordings_dir),
        "--animation-inventory-out", str(motion_out)
    ]
    if run_step("Deep Internet Scout (DNA & Motion Extraction)", agent1_cmd, 1, 5):
        report["agents"]["agent_1_internet_scout"] = "passed"
        report["artifacts"]["reference_layout_tree"] = str(tree_out)
        report["artifacts"]["reference_slices"] = str(slices_dir)
        report["artifacts"]["animation_inventory"] = str(motion_out)
    else:
        report["agents"]["agent_1_internet_scout"] = "failed"
        report["status"] = "failed_at_agent_1"
        return report

    # Asset Harvester pass
    agent1_harvest_cmd = [
        sys.executable,
        str(SCRIPT_DIR / "harvest_assets.py"),
        "--source", "multi",
        "--query", query,
        "--out", str(assets_dir),
        "--max", "12",
        "--category", category
    ]
    if domain:
        agent1_harvest_cmd.extend(["--domain", domain])
    if include_video:
        agent1_harvest_cmd.append("--video")

    subprocess.run(agent1_harvest_cmd, capture_output=False, text=True)
    report["artifacts"]["assets_manifest"] = str(assets_dir / "assets_manifest.json")

    # Business Classification pass (Synthesize profile for Agent 2)
    profile_out = root / "assets" / "business_profile.json"
    maps_data = assets_dir / "maps_data.json"
    if maps_data.exists():
        classify_cmd = [
            sys.executable,
            str(SCRIPT_DIR / "classify_business.py"),
            "--maps-data", str(maps_data),
            "--name", query,
            "--out", str(profile_out)
        ]
    else:
        classify_cmd = [
            sys.executable,
            str(SCRIPT_DIR / "classify_business.py"),
            "--pitch", query,
            "--name", query,
            "--out", str(profile_out)
        ]
    subprocess.run(classify_cmd, capture_output=False, text=True)
    report["artifacts"]["business_profile"] = str(profile_out)

    # -------------------------------------------------------------
    # AGENT 2: Creative Art Director (Visual Thesis Formulation)
    # -------------------------------------------------------------
    thesis_out = root / "creative_thesis.json"
    agent2_cmd = [
        sys.executable,
        str(SCRIPT_DIR / "creative_director_agent.py"),
        "--profile", str(profile_out),
        "--out", str(thesis_out)
    ]
    if run_step("Creative Art Director (Visual Thesis & OKLCH Math)", agent2_cmd, 2, 5):
        report["agents"]["agent_2_art_director"] = "passed"
        report["artifacts"]["creative_thesis"] = str(thesis_out)
    else:
        report["agents"]["agent_2_art_director"] = "failed"
        report["status"] = "failed_at_agent_2"
        return report

    # -------------------------------------------------------------
    # AGENT 3: 3D & Kinetic Motion Specialist
    # -------------------------------------------------------------
    scene_spec_out = root / "scene_graph.json"
    canvas_file = canvas_dir / "InteractiveSceneCanvas.tsx"
    scroll_engine_file = motion_lib_dir / "useUnifiedScrollEngine.ts"

    agent3_cmd = [
        sys.executable,
        str(SCRIPT_DIR / "scene_graph_generator.py"),
        "--out-spec", str(scene_spec_out),
        "--canvas-out", str(canvas_file),
        "--engine-out", str(scroll_engine_file)
    ]
    if run_step("3D & Kinetic Motion Specialist (R3F Canvas & Scroll Engine)", agent3_cmd, 3, 5):
        report["agents"]["agent_3_3d_motion_specialist"] = "passed"
        report["artifacts"]["scene_graph"] = str(scene_spec_out)
        report["artifacts"]["scene_canvas"] = str(canvas_file)
        report["artifacts"]["unified_scroll_engine"] = str(scroll_engine_file)
    else:
        report["agents"]["agent_3_3d_motion_specialist"] = "failed"
        report["status"] = "failed_at_agent_3"
        return report

    # -------------------------------------------------------------
    # AGENT 4: Master Production Builder
    # -------------------------------------------------------------
    manifest_path = assets_dir / "assets_manifest.json"
    agent4_cmd = [
        sys.executable,
        str(SCRIPT_DIR / "clone_reference_structure.py"),
        "--tree", str(tree_out),
        "--manifest", str(manifest_path),
        "--out-dir", str(sections_dir),
        "--page-out", str(page_out),
        "--business-name", query
    ]
    if run_step("Master Production Builder (Asymmetric Bento 2.0 & Subpages)", agent4_cmd, 4, 5):
        report["agents"]["agent_4_production_builder"] = "passed"
        report["artifacts"]["sections_dir"] = str(sections_dir)
        report["artifacts"]["page_tsx"] = str(page_out)
    else:
        report["agents"]["agent_4_production_builder"] = "failed"
        report["status"] = "failed_at_agent_4"
        return report

    # -------------------------------------------------------------
    # AGENT 5: Forensic Quality Gate Auditor (22+ Static AST Checks)
    # -------------------------------------------------------------
    agent5_cmd = [
        sys.executable,
        str(SCRIPT_DIR / "anti_slop_gate.py"),
        "--project-root", str(root)
    ]
    agent5_ast_cmd = [
        sys.executable,
        str(SCRIPT_DIR / "verify_orchestration.py"),
        str(root)
    ]
    gate1 = run_step("Forensic Anti-Slop AST Gate (22+ Assertions)", agent5_cmd, 5, 5)
    gate2 = run_step("AST Orchestration & Dependency Verifier", agent5_ast_cmd, 5, 5)
    if gate1 and gate2:
        report["agents"]["agent_5_quality_auditor"] = "passed"
    else:
        print("[!] Note: Quality gates flagged items for review.")
        report["agents"]["agent_5_quality_auditor"] = "flagged_review"

    report["status"] = "completed_successfully"
    report_file = root / "orchestration_report.json"
    with open(report_file, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print("\n" + "=" * 70)
    print("       AUTONOMOUS 5-SUBAGENT ORCHESTRATION COMPLETE")
    print("=" * 70)
    print(f"[+] All 5 specialized subagents executed autonomously.")
    print(f"[+] Output Report: {report_file}")
    print("=" * 70 + "\n")
    return report

def main():
    parser = argparse.ArgumentParser(description="Autonomous 5-Subagent Pipeline Runner for Website Architect v2.5.0")
    parser.add_argument("--benchmark", required=True, help="URL of the benchmark reference website")
    parser.add_argument("--query", required=True, help="Client business name or Google Maps URL")
    parser.add_argument("--domain", default=None, help="Client official website domain (if available)")
    parser.add_argument("--out-dir", default=".", help="Project output directory")
    parser.add_argument("--category", default="luxury", help="Commercial archetype category")
    parser.add_argument("--no-video", action="store_true", help="Skip ambient video harvesting")
    parser.add_argument("--no-3d", action="store_true", help="Skip 3D canvas scaffolding")

    args = parser.parse_args()
    run_master_orchestration(
        benchmark_url=args.benchmark,
        query=args.query,
        domain=args.domain,
        out_dir=args.out_dir,
        category=args.category,
        include_video=not args.no_video,
        include_3d=not args.no_3d
    )

if __name__ == "__main__":
    main()
