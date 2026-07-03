# Contributing to AgentSec

Thank you for considering contributing to AgentSec. This document outlines the process for contributing code, reporting issues, and improving documentation.

## Table of Contents

- [Development Setup](#development-setup)
- [Running Tests](#running-tests)
- [Code Style](#code-style)
- [Commit Style](#commit-style)
- [Branch Naming](#branch-naming)
- [Pull Request Workflow](#pull-request-workflow)
- [Reporting Issues](#reporting-issues)
- [Review Process](#review-process)

## Development Setup

### Prerequisites

- Python 3.10 or later
- git

### Setup

```bash
# Clone the repository
git clone https://github.com/locface/AgentSec.git
cd AgentSec

# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install in development mode
pip install -e .[dev]

# Verify installation
agentsec --help
```

## Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run a specific test file
pytest tests/test_baseline.py

# Run tests with coverage
pip install pytest-cov
pytest --cov=agentsec
```

Tests are located in the `tests/` directory. Each test file follows the `test_*.py` naming convention.

### Writing Tests

- Place test files in `tests/`
- Name test files `test_<module>.py`
- Use descriptive test function names
- Use fixtures for sample configs (see `tests/fixtures/`)
- Test each rule independently
- Prefer behavioral assertions over snapshot comparisons

## Code Style

- Follow [PEP 8](https://peps.python.org/pep-0008/) for Python code.
- Use type hints for all function signatures.
- Maximum line length: 100 characters.
- Use descriptive variable names — avoid single-letter names except in comprehensions.
- Prefer `pathlib.Path` over `os.path`.
- Use `pathlib.Path` for file operations.
- Keep functions focused and small.

## Commit Style

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>: <description>

[optional body]
```

Types:

- `feat:` — new feature
- `fix:` — bug fix
- `docs:` — documentation only
- `style:` — formatting, missing semicolons, etc.
- `refactor:` — code change that neither fixes a bug nor adds a feature
- `test:` — adding or modifying tests
- `chore:` — build process, dependencies, etc.
- `perf:` — performance improvement
- `ci:` — CI configuration
- `security:` — security fixes

Examples:

```
feat: add --fail-on flag for CI gating
fix: handle missing server field in json output
docs: add SARIF integration example
```

## Branch Naming

- `feat/<short-description>` — new features
- `fix/<short-description>` — bug fixes
- `docs/<short-description>` — documentation
- `chore/<short-description>` — maintenance

Use hyphens to separate words. Keep names short but descriptive.

## Pull Request Workflow

1. Fork the repository.
2. Create a branch from `main`.
3. Make your changes.
4. Run tests: `pytest`.
5. Ensure your code follows the style guide.
6. Commit using conventional commit format.
7. Push your branch and open a pull request.
8. In the PR description, explain what the change does and why.
9. Ensure CI passes.
10. Request review from a maintainer.

### Pull Request Checklist

- [ ] Tests pass (`pytest`)
- [ ] New tests added for new functionality
- [ ] Code follows project style
- [ ] Documentation updated (if applicable)
- [ ] CHANGELOG entry added (if applicable)
- [ ] Commits follow conventional commit format
- [ ] Branch is up-to-date with `main`

## Reporting Issues

### Bug Reports

When filing a bug report, include:

- AgentSec version (`agentsec --version` or `pip show agentsec-cli`)
- Python version
- Operating system
- Steps to reproduce
- Expected behavior
- Actual behavior
- Sample input (if possible, sanitize sensitive data)

### Feature Requests

When requesting a feature, describe:

- What you want to do
- Why existing functionality doesn't cover it
- How you envision the feature working (API, flags, etc.)

### Security Issues

For security vulnerabilities, **do not** file a public issue. Instead, follow the process in [SECURITY.md](./SECURITY.md).

## Review Process

1. A maintainer will review your PR within a few days.
2. Address any feedback with additional commits.
3. Once approved, a maintainer will merge your PR.
4. The change will be included in the next release.

## Questions?

If you have questions, open a [Discussion](https://github.com/locface/AgentSec/discussions) or reach out via the issue tracker.
