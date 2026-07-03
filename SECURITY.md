# Security Policy

## Supported Versions

| Version | Supported          |
|---------|--------------------|
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

AgentSec takes security vulnerabilities seriously. We appreciate your efforts to responsibly disclose your findings.

### How to Report

Please **do not** file a public issue for security vulnerabilities. Instead, send a private report via one of the following methods:

1. **GitHub Private Vulnerability Reporting**: Use the "Report a vulnerability" feature under the repository's Security tab.
2. **Email**: Send details to the maintainer via locface@users.noreply.github.com.

### What to Include

- Type of issue (e.g., code execution, data exposure, etc.)
- Full paths of source file(s) related to the manifestation of the issue
- The location of the affected source code (tag/branch/commit or direct URL)
- Any special configuration required to reproduce the issue
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit it

### Response Expectations

- **Acknowledgement**: We will acknowledge receipt of your report within 48 hours.
- **Status Update**: We will provide a status update within 5 business days.
- **Fix Timeline**: We aim to release a fix within 14 days for critical issues, depending on complexity.
- **Disclosure**: We will coordinate disclosure timing with you.

## Disclosure Policy

- We request that you give us 90 days from the time you report the issue to release a fix before publishing details.
- We will publish a security advisory on GitHub once the fix is released.
- We will credit the reporter in the advisory unless they request anonymity.

## Scope

The following are in scope:

- The `agentsec` Python package (source code in this repository)
- Documentation generation and CI/CD integrations

The following are out of scope:

- Third-party MCP servers used as example data
- The landing page website (report separately via the landing page repository)
- Previously reported issues that have been fixed

## Safe Harbor

We consider security research conducted under this policy to be:

- Authorized conduct under the Computer Fraud and Abuse Act
- Exempt from any anti-circumvention provisions in our Terms of Service
- Lawful, and we will not pursue legal action against researchers acting in good faith

Please act in good faith — do not intentionally damage systems or access data beyond what is necessary to demonstrate the vulnerability.
