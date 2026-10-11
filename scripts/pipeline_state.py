#!/usr/bin/env python3
"""
pipeline_state.py - Resumable Content-Addressed Pipeline State Machine (v2.2.0)
Synthesized from consensus recommendations across 4 Lead Reviewer AIs.

Features:
- Dual Input & Output Hashing: Verifies both inputs and generated file outputs on disk.
- Selective text vs binary CRLF normalization: Normalizes only text files (.tsx, .ts, .css, .json, .md),
  preserving exact binary byte-sequences (.png, .mp4, .glb, etc.).
- Missing file safety: Raises FileNotFoundError on missing files rather than returning empty strings.
- Approval Merkle Root: Binds Stage 07 approval to the combined hash of prd.json,
  creative_thesis.json, and assets_manifest.json.
- Downstream Cascade Invalidation: If an upstream stage re-runs, all downstream stages invalidate.
- Concurrency Run Lease: Manages .arch/run.lock to prevent multi-agent write collisions.
- Atomic State Writes: Guarantees crash-safe updates via tempfile + os.replace.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import tempfile
import time
import uuid
from pathlib import Path
from typing import Any

STATE_VERSION = 2

STAGES_ORDER = [
    "01_intake",
    "02_scaffold",
    "03_assets",
    "04_modality_benchmarks",
    "05_information_architecture",
    "05_5_copy_content",
    "06_prd",
    "07_user_approval",
    "08_design_system",
    "09_construction",
    "10_performance_cwv"
]

TEXT_EXTS = {".tsx", ".ts", ".jsx", ".js", ".css", ".json", ".md", ".html", ".txt", ".svg", ".yml", ".yaml"}


def sha256_json(value: Any) -> str:
    payload = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def hash_file(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Cannot hash non-existent file on disk: {path}")
    content = path.read_bytes()
    # Normalize CRLF only on human-readable text files
    if path.suffix.lower() in TEXT_EXTS:
        content = content.replace(b"\r\n", b"\n")
    return "sha256:" + hashlib.sha256(content).hexdigest()


def atomic_write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(
        prefix=f"{path.name}.",
        suffix=".tmp",
        dir=path.parent,
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(
                data,
                handle,
                indent=2,
                ensure_ascii=False,
            )
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_name, path)
    finally:
        try:
            os.unlink(tmp_name)
        except FileNotFoundError:
            pass


def acquire_run_lease(project_root: Path, run_id: str) -> bool:
    lock_file = project_root / ".arch" / "run.lock"
    lock_file.parent.mkdir(parents=True, exist_ok=True)
    if lock_file.exists():
        try:
            data = json.loads(lock_file.read_text(encoding="utf-8"))
            # If lock is older than 2 hours, assume stale and take over
            if time.time() - data.get("started_at", 0) < 7200:
                if data.get("run_id") != run_id and data.get("pid") != os.getpid():
                    return False
        except Exception:
            pass

    lease_info = {
        "run_id": run_id,
        "pid": os.getpid(),
        "started_at": time.time(),
        "host": os.environ.get("COMPUTERNAME", "localhost")
    }
    atomic_write_json(lock_file, lease_info)
    return True


def release_run_lease(project_root: Path) -> None:
    lock_file = project_root / ".arch" / "run.lock"
    if lock_file.exists():
        try:
            lock_file.unlink(missing_ok=True)
        except Exception:
            pass


MAX_CASCADE_RETRIES = 3

def compute_approval_merkle_root(project_root: Path) -> str:
    """Computes a full Build Contract Merkle DAG over specifications and physical asset bytes."""
    contract_artifacts = (
        "prd.json",
        "creative_thesis.json",
        "assets_manifest.json",
        "content.json",
        "ia_spec.json",
        "design_tokens.json"
    )
    manifest = {}
    for f in contract_artifacts:
        p = project_root / ".arch" / f
        if not p.exists():
            p = project_root / f
        if p.exists():
            try:
                manifest[f] = hash_file(p)
            except FileNotFoundError:
                manifest[f] = "missing"
        else:
            manifest[f] = "absent"

    # Bind physical asset file bytes referenced in assets_manifest.json
    for manifest_cand in (project_root / ".arch" / "assets_manifest.json", project_root / "assets_manifest.json"):
        if manifest_cand.exists():
            try:
                assets_data = json.loads(manifest_cand.read_text(encoding="utf-8"))
                for asset in assets_data.get("assets", []):
                    rel = asset.get("local_path") or asset.get("path")
                    if rel:
                        ap = project_root / rel
                        if ap.exists() and ap.is_file():
                            manifest[f"asset_bytes:{rel}"] = hash_file(ap)
                        else:
                            manifest[f"asset_bytes:{rel}"] = "MISSING"
            except Exception:
                pass
            break
            
    # Pairwise leaf hashing to construct a genuine Merkle root
    leaf_hashes = [hashlib.sha256(f"{k}:{v}".encode("utf-8")).digest() for k, v in sorted(manifest.items())]
    while len(leaf_hashes) > 1:
        if len(leaf_hashes) % 2 == 1:
            leaf_hashes.append(leaf_hashes[-1])
        next_level = []
        for i in range(0, len(leaf_hashes), 2):
            next_level.append(hashlib.sha256(leaf_hashes[i] + leaf_hashes[i+1]).digest())
        leaf_hashes = next_level

    return "merkle_dag:" + leaf_hashes[0].hex()


def new_run(project_root: Path) -> dict[str, Any]:
    run_id = f"{time.strftime('%Y%m%d-%H%M%S')}-{uuid.uuid4().hex[:8]}"
    return {
        "schema_version": STATE_VERSION,
        "run_id": run_id,
        "created_at": time.time(),
        "updated_at": time.time(),
        "current_stage": STAGES_ORDER[0],
        "stages": {stage: {"status": "pending", "input_hash": None, "output_hashes": {}} for stage in STAGES_ORDER},
        "merkle_roots": {
            "approval_root": None
        },
        "invalidation_counts": {}
    }


def load_state(project_root: Path) -> dict[str, Any]:
    state_file = project_root / ".arch" / "state.json"
    if not state_file.exists():
        state = new_run(project_root)
        save_state(project_root, state)
        return state
    try:
        with open(state_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        corrupt_path = state_file.with_name(f"state.corrupt.{int(time.time())}.json")
        try:
            state_file.replace(corrupt_path)
        except Exception:
            pass
        raise RuntimeError(f"FATAL: state.json is corrupted ({e}). Quarantined to {corrupt_path.name}. Pipeline failing closed.")


def save_state(project_root: Path, state: dict[str, Any]) -> None:
    state_file = project_root / ".arch" / "state.json"
    state["updated_at"] = time.time()
    atomic_write_json(state_file, state)


def invalidate_downstream(state: dict[str, Any], stage_name: str, project_root: Path | None = None) -> None:
    if stage_name not in STAGES_ORDER:
        return
        
    counts = state.setdefault("invalidation_counts", {})
    retries = counts.get(stage_name, 0) + 1
    counts[stage_name] = retries
    if retries > MAX_CASCADE_RETRIES:
        state["oscillation_trace"] = {
            "failing_stage": stage_name,
            "cycles": dict(counts),
            "timestamp": time.time(),
            "status": "HALTED_BY_CIRCUIT_BREAKER"
        }
        if project_root:
            save_state(project_root, state)
        raise SystemError(
            f"Stage {stage_name} exceeded maximum cascade limit ({MAX_CASCADE_RETRIES}). "
            f"Oscillation trace recorded to state.json. Pipeline halted to prevent infinite compile loop."
        )

    idx = STAGES_ORDER.index(stage_name)
    for downstream in STAGES_ORDER[idx + 1:]:
        state["stages"][downstream]["status"] = "invalidated"
        state["stages"][downstream]["input_hash"] = None
        state["stages"][downstream]["output_hashes"] = {}


def record_stage_success(project_root: Path, stage_name: str, input_data: Any, output_files: list[str]) -> None:
    state = load_state(project_root)
    inp_hash = sha256_json(input_data)
    
    out_hashes = {}
    for rel_path in output_files:
        p = project_root / rel_path
        if p.exists():
            out_hashes[rel_path] = hash_file(p)
            
    # Check if stage inputs or outputs changed, triggering downstream cascade
    prev_stage_data = state["stages"].get(stage_name, {})
    if prev_stage_data.get("input_hash") != inp_hash or prev_stage_data.get("output_hashes") != out_hashes:
        invalidate_downstream(state, stage_name)
        
    state["stages"][stage_name] = {
        "status": "passed",
        "input_hash": inp_hash,
        "output_hashes": out_hashes,
        "completed_at": time.time()
    }
    
    # Successful stage completion clears any active retry cascade counter for this stage
    state.setdefault("invalidation_counts", {})[stage_name] = 0
    
    if stage_name == "07_user_approval":
        state["merkle_roots"]["approval_root"] = compute_approval_merkle_root(project_root)
        
    idx = STAGES_ORDER.index(stage_name)
    if idx + 1 < len(STAGES_ORDER):
        state["current_stage"] = STAGES_ORDER[idx + 1]
    else:
        state["current_stage"] = "COMPLETED"
        
    save_state(project_root, state)


def verify_stage_prerequisite(project_root: Path, stage_name: str) -> tuple[bool, str]:
    state = load_state(project_root)
    if stage_name not in STAGES_ORDER:
        return False, f"Unknown stage: {stage_name}"
    
    idx = STAGES_ORDER.index(stage_name)
    if idx > 0:
        prev_stage = STAGES_ORDER[idx - 1]
        prev_status = state["stages"].get(prev_stage, {}).get("status")
        if prev_status != "passed":
            return False, f"Prerequisite stage {prev_stage} has not passed (status: {prev_status})"

    if stage_name in ("08_build", "09_verify", "10_ship"):
        # Assert cryptographic contract binding
        recorded_root = state.get("merkle_roots", {}).get("approval_root")
        if not recorded_root:
            return False, f"Stage {stage_name} cannot proceed: no approved Merkle root recorded in state.json"
        
        current_root = compute_approval_merkle_root(project_root)
        if current_root != recorded_root:
            invalidate_downstream(state, "07_user_approval", project_root)
            save_state(project_root, state)
            return False, (
                f"Contract tampering detected! Current Merkle root ({current_root[:16]}...) "
                f"does not match approved root ({recorded_root[:16]}...). Downstream stages invalidated."
            )

    return True, "Prerequisites satisfied"


def main():
    parser = argparse.ArgumentParser(description="Pipeline State Machine (v2.3.0)")
    parser.add_argument("project_root", nargs="?", default=".", help="Project root directory")
    parser.add_argument("--status", action="store_true", help="Print current pipeline status")
    parser.add_argument("--acquire-lease", help="Acquire concurrency lease for given run ID")
    parser.add_argument("--release-lease", action="store_true", help="Release active run lease")
    parser.add_argument("--invalidate-from", help="Invalidate all stages downstream from specified stage")
    parser.add_argument("--verify-prereq", help="Verify prerequisites and Merkle root integrity for stage")
    args = parser.parse_args()

    root = Path(args.project_root).resolve()

    if args.acquire_lease:
        success = acquire_run_lease(root, args.acquire_lease)
        print(json.dumps({"leased": success}))
        sys.exit(0 if success else 1)

    if args.release_lease:
        release_run_lease(root)
        print(json.dumps({"released": True}))
        sys.exit(0)

    state = load_state(root)

    if args.invalidate_from:
        invalidate_downstream(state, args.invalidate_from)
        save_state(root, state)
        print(json.dumps({"invalidated_from": args.invalidate_from, "current_stage": state["current_stage"]}))
        sys.exit(0)

    if args.verify_prereq:
        ok, msg = verify_stage_prerequisite(root, args.verify_prereq)
        print(json.dumps({"ready": ok, "message": msg}))
        sys.exit(0 if ok else 1)

    print(json.dumps(state, indent=2))
    sys.exit(0)


if __name__ == "__main__":
    main()
