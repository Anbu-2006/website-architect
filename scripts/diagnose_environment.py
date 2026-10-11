import sys
import os
import subprocess
import shutil
import json
from pathlib import Path

def run():
    results = {
        "os": os.name,
        "platform": sys.platform,
        "python_version": sys.version,
        "binaries": {},
        "python_modules": {},
        "scripts_audit": {},
        "mcp_servers_audit": {}
    }

    # 1. Test CLI Binaries
    binaries_to_check = ["node", "npm", "npx", "git", "python", "tsc"]
    for b in binaries_to_check:
        found_path = shutil.which(b)
        ver = None
        if found_path:
            try:
                res = subprocess.run([b, "--version"], capture_output=True, text=True, timeout=5)
                ver = res.stdout.strip() or res.stderr.strip()
            except Exception as e:
                ver = f"Error: {e}"
        results["binaries"][b] = {"installed": found_path is not None, "path": found_path, "version": ver}

    # 2. Test Python Modules
    modules_to_check = ["playwright", "bs4", "requests", "PIL", "ast", "urllib3", "json", "asyncio"]
    for m in modules_to_check:
        try:
            mod = __import__(m)
            ver = getattr(mod, "__version__", "builtin/available")
            results["python_modules"][m] = {"available": True, "version": ver}
        except ImportError as e:
            results["python_modules"][m] = {"available": False, "error": str(e)}

    # 3. Test website-architect Scripts Audit
    base_script_dir = Path(r"C:\Users\anbua\.gemini\config\skills\website-architect\scripts")
    expected_scripts = [
        "anti_slop_gate.py",
        "check_no_anchor_illusion.py",
        "classify_business.py",
        "clone_reference_structure.py",
        "crawl_sitemap.py",
        "creative_director_agent.py",
        "curate_user_assets.py",
        "extract_tokens.py",
        "harvest_assets.py",
        "layout_fidelity_score.py",
        "orchestrate.py",
        "resilient_sourcing.py",
        "scene_graph_generator.py",
        "section_option_previewer.py",
        "verify_orchestration.py",
        "video_to_wireframe.py"
    ]

    total_bytes = 0
    for s in expected_scripts:
        p = base_script_dir / s
        if p.exists():
            sz = p.stat().st_size
            total_bytes += sz
            results["scripts_audit"][s] = {"exists": True, "size_bytes": sz}
        else:
            results["scripts_audit"][s] = {"exists": False, "size_bytes": 0}
    results["scripts_total_bytes"] = total_bytes
    results["scripts_count"] = len(expected_scripts)

    # 4. Check MCP servers directory
    mcp_dir = Path(r"C:\Users\anbua\.gemini\antigravity-ide\mcp")
    if mcp_dir.exists():
        for server in mcp_dir.iterdir():
            if server.is_dir():
                tool_files = list(server.glob("*.json"))
                results["mcp_servers_audit"][server.name] = {
                    "tools_count": len(tool_files),
                    "tools": [t.stem for t in tool_files]
                }

    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    run()
