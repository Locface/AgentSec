"""Suppression system (.agentsecignore and inline comments) for AgentSec."""

import re
from pathlib import Path
from typing import Dict, List, Set, Optional
import pathspec


class SuppressionManager:
    """Manages finding suppressions from ignore files and inline comments."""

    def __init__(self, root: Path, ignore_file: Optional[Path] = None):
        self.root = root
        self.global_ignored_rules: Set[str] = set()
        self.path_ignored_rules: List[tuple[pathspec.PathSpec, Set[str]]] = []
        self._load_ignore_file(ignore_file or (root / ".agentsecignore"))

    def _load_ignore_file(self, ignore_path: Path) -> None:
        if not ignore_path.exists() or not ignore_path.is_file():
            return
        try:
            lines = ignore_path.read_text(encoding="utf-8", errors="ignore").splitlines()
        except OSError:
            return

        for raw_line in lines:
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue

            if ":" in line:
                # Format: glob_pattern: RULE1, RULE2
                pattern, rules_part = line.split(":", 1)
                pattern = pattern.strip()
                rules = {r.strip().upper() for r in rules_part.split(",") if r.strip()}
                spec = pathspec.PathSpec.from_lines("gitignore", [pattern])
                self.path_ignored_rules.append((spec, rules))
            elif re.match(r"^AGENT\d{3}$", line.upper()):
                # Global rule ignore: AGENT001
                self.global_ignored_rules.add(line.upper())
            else:
                # Path ignore: everything in this path is ignored
                spec = pathspec.PathSpec.from_lines("gitignore", [line])
                self.path_ignored_rules.append((spec, {"*"}))

    def is_ignored(self, finding: Dict[str, str], rel_path_str: str, file_content: Optional[str] = None) -> bool:
        code = finding.get("code", "").upper()
        rule_name = finding.get("rule", "")

        # 1. Check global rule ignore
        if code in self.global_ignored_rules or "*" in self.global_ignored_rules:
            return True

        # 2. Check path-based ignore
        normalized_path = rel_path_str.replace("\\", "/")
        for spec, rules in self.path_ignored_rules:
            if spec.match_file(normalized_path):
                if "*" in rules or code in rules:
                    return True

        # 3. Check inline comments in file content
        if file_content:
            # Pattern: agentsec:ignore AGENT001 or agentsec:ignore=AGENT001,AGENT002
            inline_pattern = re.compile(
                r"agentsec:ignore(?:=|\s+)([A-Za-z0-9_,\s*]+)",
                re.IGNORECASE
            )
            for match in inline_pattern.finditer(file_content):
                ignored_in_line = {item.strip().upper() for item in match.group(1).split(",")}
                if "*" in ignored_in_line or code in ignored_in_line:
                    return True

        return False
