# Installation

## Via pip

```bash
pip install agentsec
```

## From source

```bash
git clone https://github.com/locface/AgentSec.git
cd AgentSec
pip install -e .
```

## Development install

```bash
pip install -e ".[dev]"
```

## Docker

```bash
docker build -t agentsec .
docker run --rm -v $(pwd):/scan agentsec scan /scan
```

## Verify

```bash
agentsec --help
```

You should see:

```
Usage: agentsec [OPTIONS] COMMAND [ARGS]...

  AgentSec — security scanner for AI agent configs.

Commands:
  scan  Scan a directory for security risks in AI agent configurations.
```
