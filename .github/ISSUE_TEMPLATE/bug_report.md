---
name: Bug Report
about: Create a report to help us improve AgentSec
title: "[Bug] "
labels: bug
assignees: ''
---

## Describe the Bug

A clear and concise description of what the bug is.

## To Reproduce

Steps to reproduce the behavior:

1. Run command: `agentsec scan ...`
2. See error: ...

## Expected Behavior

A clear description of what you expected to happen.

## Actual Behavior

What actually happened. Include error messages, stack traces, or unexpected output.

## Environment

- AgentSec version: <!-- pip show agentsec-cli | grep Version -->
- Python version: <!-- python3 --version -->
- Operating system: <!-- e.g., Ubuntu 24.04, macOS 15, Windows 11 -->
- Installation method: <!-- pip install, pipx, from source -->

## Sample Input

If applicable, provide a sanitized sample of the configuration you scanned.

```json
{
  "mcpServers": {
    "example": {
      "command": "node",
      "args": []
    }
  }
}
```

## Additional Context

Add any other context about the problem here.
