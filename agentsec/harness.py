"""Harness Engineering generator for AgentSec.

Initializes production-grade security controls, policy files, suppression baselines,
and agent prompt safeguards across the workspace.
"""

from pathlib import Path
from typing import Dict, List, Any


AGENTSEC_IGNORE_TEMPLATE = """# AgentSec Suppression Configuration (.agentsecignore)
# Global suppression:
# AGENT022

# Scoped suppression for test fixtures:
tests/**: AGENT001, AGENT002, AGENT046, AGENT047
fixtures/**: *
"""

AGENTSEC_POLICY_TEMPLATE = """# AgentSec Security Policy (.agentsec.yaml)
version: 1.0

# General agent permission boundaries
policy:
  allow_shell: false
  require_human_confirmation: true
  network_egress:
    block_link_local: true
    block_private_ranges: true
    allowed_domains:
      - "api.github.com"
      - "registry.npmjs.org"
      - "pypi.org"

  filesystem:
    read_only_root: true
    allowed_write_paths:
      - "./workspace"
      - "./output"
      - "./dist"

  audit:
    min_security_score: 80
    fail_on_severity: "high"
"""

PRE_COMMIT_CONFIG_TEMPLATE = """# Pre-commit configuration with AgentSec
repos:
  - repo: https://github.com/locface/AgentSec
    rev: v1.2.0
    hooks:
      - id: agentsec
"""

AGENT_SECURITY_GUIDELINES = """
## Security & Tool Execution Guidelines
- **Autonomous Shell:** Direct shell execution without user confirmation is strictly prohibited.
- **Data Protection:** Never output or expose API keys, tokens, or private credentials in chat or commits.
- **Filesystem Integrity:** Restrict write operations to the active project workspace. Do not modify system root or external home paths.
- **Destructive Operations:** Always prompt for human approval before executing destructive actions (e.g. drop table, rm -rf, force push).
"""



HARNESS_FILES = [
    ".agentsecignore",
    ".agentsec.yaml",
    ".pre-commit-config.yaml",
    "AGENTS.md",
]

def init_security_harness(root: Path, force: bool = False) -> Dict[str, Any]:
    """Initialize security harness files in the given directory."""
    created = []
    skipped = []

    # 1. .agentsecignore
    ignore_file = root / ".agentsecignore"
    if not ignore_file.exists() or force:
        ignore_file.write_text(AGENTSEC_IGNORE_TEMPLATE, encoding="utf-8")
        created.append(str(ignore_file.name))
    else:
        skipped.append(str(ignore_file.name))

    # 2. .agentsec.yaml policy
    policy_file = root / ".agentsec.yaml"
    if not policy_file.exists() or force:
        policy_file.write_text(AGENTSEC_POLICY_TEMPLATE, encoding="utf-8")
        created.append(str(policy_file.name))
    else:
        skipped.append(str(policy_file.name))

    # 3. .pre-commit-config.yaml
    pre_commit_file = root / ".pre-commit-config.yaml"
    if not pre_commit_file.exists() or force:
        pre_commit_file.write_text(PRE_COMMIT_CONFIG_TEMPLATE, encoding="utf-8")
        created.append(str(pre_commit_file.name))
    else:
        skipped.append(str(pre_commit_file.name))

    # 4. Recommend AGENTS.md update if exists, or create basic AGENTS.md
    agents_md = root / "AGENTS.md"
    if not agents_md.exists() or force:
        agents_md.write_text(f"# Agent Guidelines\n{AGENT_SECURITY_GUIDELINES}", encoding="utf-8")
        created.append(str(agents_md.name))
    else:
        existing_content = agents_md.read_text(encoding="utf-8")
        if "Security & Tool Execution Guidelines" not in existing_content:
            agents_md.write_text(f"{existing_content.rstrip()}\n\n{AGENT_SECURITY_GUIDELINES}", encoding="utf-8")
            created.append(f"{agents_md.name} (appended security guidelines)")
        else:
            skipped.append(str(agents_md.name))

    return {
        "created": created,
        "skipped": skipped,
        "root": str(root),
    }
