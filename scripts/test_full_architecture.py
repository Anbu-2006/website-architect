import sys
import os
import json
import subprocess
from pathlib import Path

def run_tests():
    report = {
        "timestamp": "2026-09-28T23:38:00Z",
        "mcp_servers": {},
        "scripts": {},
        "gateway_bridge": {},
        "design_systems": {},
        "img2threejs": {},
        "summary": {}
    }

    # 1. Test Gateway Bridge
    try:
        bridge_script = Path(r"c:\Users\anbua\.gemini\.agents\skills\website-architect\scripts\get_gateway_key.py")
        res = subprocess.run(["python", str(bridge_script)], capture_output=True, text=True, timeout=10)
        if res.returncode == 0:
            data = json.loads(res.stdout)
            report["gateway_bridge"] = {
                "status": "PASS",
                "api_key_detected": bool(data.get("api_key")),
                "base_url": data.get("base_url"),
                "gateway_path": data.get("gateway_path")
            }
        else:
            report["gateway_bridge"] = {"status": "FAIL", "error": res.stderr}
    except Exception as e:
        report["gateway_bridge"] = {"status": "FAIL", "error": str(e)}

    # 2. Test All Website Architect Scripts
    scripts_dir = Path(r"c:\Users\anbua\.gemini\.agents\skills\website-architect\scripts")
    for py_file in sorted(scripts_dir.glob("*.py")):
        if py_file.name == "test_full_architecture.py":
            continue
        try:
            res = subprocess.run(["python", str(py_file), "--help"], capture_output=True, text=True, timeout=8)
            report["scripts"][py_file.name] = {
                "status": "PASS" if res.returncode == 0 else "FAIL",
                "exit_code": res.returncode
            }
        except Exception as e:
            report["scripts"][py_file.name] = {"status": "FAIL", "error": str(e)}

    # 3. Test Design Systems Registry
    ds_dir = Path(r"c:\Users\anbua\.gemini\.agents\skills\website-architect\references\design-systems")
    brand_dirs = [d for d in ds_dir.iterdir() if d.is_dir()]
    valid_brands = 0
    for b in brand_dirs:
        spec = b / "DESIGN.md"
        if not spec.exists():
            spec = b / "README.md"
        if spec.exists():
            valid_brands += 1
    report["design_systems"] = {
        "status": "PASS" if valid_brands >= 70 else "WARN",
        "total_brands": len(brand_dirs),
        "valid_specs": valid_brands,
        "index_exists": (ds_dir / "INDEX.md").exists()
    }

    # 4. Test img2threejs
    img3d_dir = Path(r"c:\Users\anbua\.gemini\.agents\skills\img2threejs")
    img3d_skill = img3d_dir / "SKILL.md"
    img3d_script = img3d_dir / "scripts" / "capture_threejs_playwright.py"
    res3d = subprocess.run(["python", str(img3d_script), "--help"], capture_output=True, text=True, timeout=5)
    report["img2threejs"] = {
        "status": "PASS" if (img3d_skill.exists() and res3d.returncode == 0) else "FAIL",
        "skill_md": img3d_skill.exists(),
        "capture_script": res3d.returncode == 0
    }

    # Summary
    total_scripts = len(report["scripts"])
    passed_scripts = sum(1 for v in report["scripts"].values() if v.get("status") == "PASS")
    
    report["summary"] = {
        "total_scripts_tested": total_scripts,
        "scripts_passed": passed_scripts,
        "all_scripts_green": total_scripts == passed_scripts,
        "gateway_connected": report["gateway_bridge"].get("status") == "PASS",
        "design_systems_count": report["design_systems"].get("total_brands"),
        "img2threejs_ready": report["img2threejs"].get("status") == "PASS"
    }

    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    run_tests()
