# Screenshots

This document describes the screenshots that should be created for the AgentSec README and documentation.

## Screenshot List

### 1. `terminal-basic.png`

**Command:** `agentsec scan .`

**Expected output:**

```
 Scanning /home/user/project...

[CRITICAL] MCP shell execution
  File: mcp-servers/package.json
  Description: MCP server can execute shell commands
  Recommendation: Require explicit approval or remove shell access.

[CRITICAL] MCP filesystem write access
  File: mcp-servers/package.json
  Description: MCP server has filesystem write access
  Recommendation: Restrict filesystem access to read-only or specific directories.

Total findings: 124
```

**Purpose:** Show the default terminal output format with findings, severity levels, and recommendations.

---

### 2. `terminal-sarif.png`

**Command:** `agentsec scan . --format sarif`

**Expected output:** Valid SARIF v2.1.0 JSON with `runs[0].tool.driver.name: "agentsec"`, findings with rule indices, locations, and OWASP tags.

**Purpose:** Show SARIF output format for GitHub CodeQL integration.

---

### 3. `terminal-json.png`

**Command:** `agentsec scan . --format json`

**Expected output:** Valid JSON array of finding objects with fields: `rule`, `severity`, `description`, `recommendation`, `file`, `server`, `owasp`.

**Purpose:** Show JSON output format for programmatic consumption.

---

### 4. `terminal-markdown.png`

**Command:** `agentsec scan . --format markdown`

**Expected output:** Markdown report with severity headings, file paths, descriptions, and recommendations.

**Purpose:** Show Markdown output format for generated reports.

---

### 5. `terminal-owasp.png`

**Command:** `agentsec scan . --show-owasp`

**Expected output:** Terminal output with `LLM06, AG02` style OWASP IDs appended to each finding line.

**Purpose:** Show OWASP mapping feature.

---

### 6. `terminal-fail-on.png`

**Command:** `agentsec scan . --fail-on high; echo "Exit: $?"`

**Expected output:** Terminal output followed by `Exit: 1`.

**Purpose:** Demonstrate CI/CD gating — the tool exits with code 1 when findings match the severity threshold.

---

### 7. `help-screen.png`

**Command:** `agentsec --help`

**Expected output:**

```
Usage: agentsec [OPTIONS] COMMAND [ARGS]...

  AgentSec — security scanner for AI agent configs.

Options:
  --help  Show this message and exit.

Commands:
  scan  Scan a directory for security risks in AI agent configurations.
```

**Purpose:** Show the CLI help screen.

---

### 8. `scan-help.png`

**Command:** `agentsec scan --help`

**Expected output:** Full `scan` subcommand help with all options: `--format`, `--severity`, `--fail-on`, `--include-hidden`, `--baseline`, `--update-baseline`, `--show-owasp`.

**Purpose:** Show all available scan options.

---

### 9. `github-code-scanning.png`

**Command:** N/A — this is a GitHub UI screenshot showing SARIF results in the Security > Code scanning tab.

**Purpose:** Show how AgentSec integrates with GitHub CodeQL.

---

### 10. `landing-page.png`

**Command:** N/A — screenshot of https://locface.github.io/AgentSec/ landing page.

**Purpose:** Show the project landing page.

---

## How to Generate

### Local screenshots

```bash
cd /path/to/your/project

# Basic scan
agentsec scan . | tee screenshots/terminal-basic.txt

# SARIF
agentsec scan . --format sarif > screenshots/terminal-sarif.txt
python3 -m json.tool screenshots/terminal-sarif.txt | head -50

# JSON
agentsec scan . --format json > screenshots/terminal-json.txt

# Markdown
agentsec scan . --format markdown > screenshots/terminal-markdown.txt

# OWASP
agentsec scan . --show-owasp | tee screenshots/terminal-owasp.txt

# Fail-on
agentsec scan . --fail-on high; echo "Exit: $?"

# Help screens
agentsec --help
agentsec scan --help
```

### Converting to images

Use a terminal recording tool like `asciinema` or `agg` for GIFs, or `terminalshot` for static screenshots.

```bash
# Install terminalshot
pip install terminalshot

# Capture scan command
agentsec scan . | terminalshot capture --out screenshots/terminal-basic.png
```
