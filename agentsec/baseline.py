"""Baseline (lockfile) management for AgentSec."""

import json
import hashlib
from pathlib import Path
from typing import Dict, List, Tuple


def compute_finding_id(finding: dict) -> str:
    """Compute a stable unique ID for a finding based on code, file, and server."""
    key = f"{finding['code']}|{finding['file']}|{finding.get('server', '')}"
    return hashlib.md5(key.encode()).hexdigest()


def load_baseline(path: str) -> Dict[str, str]:
    """Load baseline from JSON file. Returns dict of id -> severity."""
    p = Path(path)
    if not p.exists():
        return {}
    with open(p, 'r') as f:
        data = json.load(f)
    return data.get('findings', {})


def save_baseline(path: str, findings: List[dict]) -> None:
    """Save current findings as baseline."""
    baseline = {}
    for f in findings:
        fid = compute_finding_id(f)
        baseline[fid] = f['severity']
    with open(path, 'w') as f:
        json.dump({"findings": baseline}, f, indent=2)


def compare_findings(findings: List[dict], baseline: Dict[str, str]) -> Tuple[List[dict], List[dict], List[dict]]:
    """
    Compare current findings against baseline.
    Returns: (new, changed, removed)
      - new: findings not in baseline
      - changed: findings whose severity changed
      - removed: baseline entries not in current findings (as list of dict with 'id' and 'severity')
    """
    current_ids = set()
    new = []
    changed = []

    for f in findings:
        fid = compute_finding_id(f)
        current_ids.add(fid)
        if fid not in baseline:
            new.append(f)
        elif baseline[fid] != f['severity']:
            changed.append(f)

    removed = []
    for fid, sev in baseline.items():
        if fid not in current_ids:
            removed.append({'id': fid, 'severity': sev})

    return new, changed, removed
