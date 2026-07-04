"""Tests for baseline functionality."""
import json
import pytest
from pathlib import Path
from agentsec.baseline import compute_finding_id, load_baseline, save_baseline, compare_findings

def test_compute_finding_id():
    f = {"code": "AGENT001", "rule": "test", "file": "/a/b", "server": "s1"}
    id1 = compute_finding_id(f)
    assert isinstance(id1, str)
    assert len(id1) == 32
    f2 = dict(f)
    assert compute_finding_id(f2) == id1
    f3 = dict(f)
    f3["server"] = "s2"
    assert compute_finding_id(f3) != id1

def test_save_and_load(tmp_path):
    findings = [{"code": "AGENT001", "rule": "A", "file": "a.json", "severity": "high", "server": "s1"}]
    path = tmp_path / "baseline.json"
    save_baseline(str(path), findings)
    assert path.exists()
    data = json.loads(path.read_text())
    assert "findings" in data
    loaded = load_baseline(str(path))
    assert loaded == data["findings"]

def test_compare():
    f1 = {"code": "AGENT001", "rule": "A", "file": "a.json", "severity": "high", "server": "s1"}
    f2 = {"code": "AGENT002", "rule": "B", "file": "b.json", "severity": "low", "server": "s2"}
    f2_changed = {"code": "AGENT002", "rule": "B", "file": "b.json", "severity": "medium", "server": "s2"}
    f3 = {"code": "AGENT003", "rule": "C", "file": "c.json", "severity": "critical", "server": "s3"}
    id1 = compute_finding_id(f1)
    id2 = compute_finding_id(f2)
    baseline = {id1: "high", id2: "low"}
    current = [f1, f2_changed, f3]
    new, changed, removed = compare_findings(current, baseline)
    assert len(new) == 1 and new[0]["rule"] == "C"
    assert len(changed) == 1 and changed[0]["rule"] == "B"
    assert len(removed) == 0
