"""Tests for OWASP mapping."""
import pytest
from agentsec.owasp import get_owasp, get_owasp_ids, format_owasp, RULE_OWASP_MAP
from agentsec.rules import load_rules


class TestOwaspMapping:
    """Test that all rules have OWASP mappings and the helper functions work."""

    def test_all_rules_have_owasp_mapping(self):
        """Every defined rule must have at least one OWASP mapping."""
        rules = load_rules()
        rule_names = {r.name for r in rules}
        mapped_names = set(RULE_OWASP_MAP.keys())
        unmapped = rule_names - mapped_names
        assert not unmapped, f"Rules without OWASP mapping: {unmapped}"
        
    def test_no_stale_mappings(self):
        """OWASP mappings should not reference rules that don't exist."""
        rules = load_rules()
        rule_names = {r.name for r in rules}
        mapped_names = set(RULE_OWASP_MAP.keys())
        stale = mapped_names - rule_names
        assert not stale, f"OWASP mappings for non-existent rules: {stale}"

    def test_get_owasp_returns_list(self):
        result = get_owasp("MCP shell execution")
        assert isinstance(result, list)
        assert len(result) >= 1
        owasp_id, category = result[0]
        assert isinstance(owasp_id, str)
        assert owasp_id.startswith("LLM") or owasp_id.startswith("AG")
        assert isinstance(category, str)

    def test_get_owasp_unknown_rule(self):
        assert get_owasp("nonexistent rule") == []

    def test_get_owasp_ids(self):
        ids = get_owasp_ids("MCP shell execution")
        assert "LLM06" in ids
        assert "AG02" in ids

    def test_get_owasp_ids_unknown(self):
        assert get_owasp_ids("nonexistent") == ""

    def test_format_owasp(self):
        formatted = format_owasp("MCP filesystem write access")
        assert "LLM08" in formatted
        assert formatted.startswith("[")

    def test_format_owasp_unknown(self):
        assert format_owasp("nonexistent") == ""

    def test_every_mapping_has_valid_owasp_id(self):
        """All OWASP IDs in the mapping must be valid (LLM01-10 or AG01-10)."""
        valid_llm = {f"LLM{i:02d}" for i in range(1, 11)}
        valid_ag = {f"AG{i:02d}" for i in range(1, 11)}
        valid = valid_llm | valid_ag
        for rule_name, mappings in RULE_OWASP_MAP.items():
            for owasp_id, _ in mappings:
                assert owasp_id in valid, f"Invalid OWASP ID '{owasp_id}' in rule '{rule_name}'"

    def test_finding_has_owasp_field(self, tmp_path):
        """Actual scan findings should include OWASP field."""
        from agentsec.scanner import Scanner
        from pathlib import Path
        
        # Create a temp MCP config
        config = tmp_path / "mcp.json"
        config.write_text('{"mcpServers": {"test": {"command": "bash", "args": []}}}')
        
        scanner = Scanner(tmp_path, include_hidden=True)
        findings = scanner.scan()
        
        # At least some findings should exist and have owasp field
        assert len(findings) > 0
        for f in findings:
            assert "owasp" in f, f"Finding missing 'owasp' field: {f['rule']}"
            assert f["owasp"] != "", f"Finding has empty 'owasp' field: {f['rule']}"
