# Demo Script

A 30–60 second terminal demo suitable for a GIF in the README.

## Recording Recommendations

- **Tool**: [agg](https://github.com/asciinema/agg) (convert asciicast to GIF) or [vhs](https://github.com/charmbracelet/vhs)
- **Terminal**: 80×24 character size (standard terminal)
- **Theme**: Dark background (Solarized Dark, Dracula, or similar)
- **Font**: 14px monospace (JetBrains Mono, Fira Code, or similar)
- **Framerate**: 30 fps for agg, or 60 fps for vhs
- **Total duration**: 30–45 seconds

## Script

### Scene 1: Welcome (5 seconds)

```
$ agentsec --version
agentsec-cli 1.0.0
```

**Overlay text:** "AgentSec — Static security scanner for AI agent configs"

### Scene 2: Scan a project (15 seconds)

```
$ agentsec scan ~/dev/ai-project

 Scanning /home/user/dev/ai-project...

[CRITICAL] MCP shell execution
  File: claude_desktop_config.json
  Server: shell-server
  Description: MCP server can execute shell commands
  Recommendation: Require explicit approval or remove shell access.

[HIGH] Broad path access
  File: mcp.json
  Server: filesystem
  Description: MCP server has broad filesystem path access (root or home)
  Recommendation: Restrict path to specific directories.

Total findings: 4 · Critical: 2 · High: 1 · Medium: 0 · Low: 1
```

**Overlay text:** "Detects dangerous permissions in MCP, Cursor, Claude, Codex, Cline configs"

### Scene 3: JSON output (5 seconds)

```
$ agentsec scan ~/dev/ai-project --format json | python3 -m json.tool
[
    {
        "rule": "MCP shell execution",
        "severity": "critical",
        "file": "claude_desktop_config.json",
        "server": "shell-server",
        "description": "MCP server can execute shell commands",
        "recommendation": "Require explicit approval or remove shell access.",
        "owasp": "LLM06, AG02"
    }
]
```

### Scene 4: CI/CD gating (5 seconds)

```
$ agentsec scan . --fail-on critical
...findings...
Failing due to critical finding: MCP shell execution
$ echo $?
1
```

**Overlay text:** "CI/CD gating with --fail-on — exit code 1 on critical/high findings"

### Scene 5: SARIF output (5 seconds)

```
$ agentsec scan . --format sarif > results.sarif
$ cat results.sarif | python3 -m json.tool | head -3
{
    "$schema": "https://raw.githubusercontent.com/oasis-tcs/...
    "version": "2.1.0",
```

**Overlay text:** "SARIF output for GitHub CodeQL and enterprise CI"

### Scene 6: Baseline comparison (5 seconds)

```
$ agentsec scan . --update-baseline baseline.json
 Baseline saved to baseline.json

$ agentsec scan . --baseline baseline.json
 Scanning /home/user/project...
 Baseline comparison:
   New findings: 1
   Changed severity: 0
   Removed findings: 0
```

**Overlay text:** "Track regressions with baseline comparison"

## vhs Script Format

If using [vhs](https://github.com/charmbracelet/vhs):

```bash
# Save as demo.tape
Output demo.gif
Set FontSize 14
Set Width 800
Set Height 450
Set Theme "Dracula"
Type "agentsec --version" Enter
Sleep 1s
Type "agentsec scan ~/dev/ai-project" Enter
Sleep 3s
Type "agentsec scan ~/dev/ai-project --format json | python3 -m json.tool" Enter
Sleep 2s
Type "agentsec scan . --fail-on critical" Enter
Sleep 2s
Type "echo Exit: $?" Enter
Sleep 1s
```

Run with:

```bash
vhs demo.tape
```

## agg Workflow

```bash
# Record with asciinema
asciinema rec agentsec-demo.cast

# ... perform the scenes above ...

# Convert to GIF
agg --font-family "JetBrains Mono" --font-size 14 --theme dracula agentsec-demo.cast agentsec-demo.gif
```
