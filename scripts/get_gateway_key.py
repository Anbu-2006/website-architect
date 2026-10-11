#!/usr/bin/env python3
"""
scripts/get_gateway_key.py
Automated API Key & Gateway Bridge for Antigravity_to_api.
Part of the Universal Website Architect Engine.

Connects to E:\\Antigravity_to_api to:
1. Extract the active OpenAI-compatible API key directly from the SQLite store.
2. Check health status of http://localhost:20128/api/health.
3. Automatically launch the gateway server if not running (when --start is specified).
"""

import os
import sys
import json
import argparse
import subprocess
import urllib.request
from pathlib import Path

GATEWAY_DIR = Path(r"E:\Antigravity_to_api")
GATEWAY_HEALTH_URL = "http://localhost:20128/api/health"
GATEWAY_BASE_URL = "http://localhost:20128/v1"

def check_gateway_running(timeout=2):
    try:
        req = urllib.request.Request(GATEWAY_HEALTH_URL, headers={"User-Agent": "Antigravity-Bridge"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            if resp.status == 200:
                data = json.loads(resp.read().decode("utf-8"))
                return True, data
    except Exception:
        pass
    return False, None

def get_key_from_db():
    if not GATEWAY_DIR.exists():
        return None, f"Gateway directory not found at {GATEWAY_DIR}"
    
    node_script = """
    import('./server/db.mjs').then(async m => {
      let keys = m.getKeys();
      let raw = null;
      if (keys && keys.length > 0) {
        raw = m.getKeyRaw(keys[0].id);
      } else {
        const created = m.createKey({ name: 'website-architect', model_access_mode: 'all' });
        raw = created.key;
      }
      console.log(JSON.stringify({ status: 'ok', key: raw }));
    }).catch(err => {
      console.log(JSON.stringify({ status: 'error', error: err.message }));
    });
    """
    
    try:
        res = subprocess.run(
            ["node", "-e", node_script],
            cwd=str(GATEWAY_DIR),
            capture_output=True,
            text=True,
            timeout=10
        )
        out = res.stdout.strip()
        if out:
            data = json.loads(out)
            if data.get("status") == "ok":
                return data.get("key"), None
            return None, data.get("error")
        return None, res.stderr.strip()
    except Exception as e:
        return None, str(e)

def start_gateway():
    is_running, _ = check_gateway_running()
    if is_running:
        return True, "Gateway is already running"
    
    try:
        subprocess.Popen(
            ["node", "server/index.mjs"],
            cwd=str(GATEWAY_DIR),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name == "nt" else 0
        )
        return True, "Gateway process launched"
    except Exception as e:
        return False, str(e)

def main():
    parser = argparse.ArgumentParser(description="Antigravity Gateway Bridge")
    parser.add_argument("--start", action="store_true", help="Start the gateway if not running")
    parser.add_argument("--json", action="store_true", default=True, help="Output JSON format")
    args = parser.parse_args()

    is_running, health_data = check_gateway_running()

    if not is_running and args.start:
        started, msg = start_gateway()
        import time
        time.sleep(1.5)
        is_running, health_data = check_gateway_running()

    key, err = get_key_from_db()

    payload = {
        "gateway_path": str(GATEWAY_DIR),
        "gateway_running": is_running,
        "base_url": GATEWAY_BASE_URL,
        "api_key": key,
        "error": err if not key else None,
        "health": health_data
    }

    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(f"API Key: {key}")
        print(f"Base URL: {GATEWAY_BASE_URL}")
        print(f"Gateway Running: {is_running}")

if __name__ == "__main__":
    main()
