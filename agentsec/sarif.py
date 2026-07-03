"""SARIF (Static Analysis Results Interchange Format) report generator.

Conforms to SARIF v2.1.0 (https://docs.oasis-open.org/sarif/sarif/v2.1.0/).
"""

import json
import datetime
from typing import List, Dict, Any
from pathlib import Path


def generate_sarif(findings: List[Dict[str, Any]], repo_root: str = ".") -> Dict[str, Any]:
    """Convert AgentSec findings to SARIF format."""
    
    rules = {}
    results = []
    
    severity_mapping = {
        "critical": 3.0,
        "high": 2.0,
        "medium": 1.0,
        "low": 0.5,
    }
    
    for idx, finding in enumerate(findings):
        rule_id = finding['rule'].replace(" ", "_").lower()
        
        if rule_id not in rules:
            desc = finding['description']
            owasp = finding.get('owasp', '')
            full_desc = desc
            if owasp:
                full_desc = f"[{owasp}] {desc}"
            
            rules[rule_id] = {
                "id": rule_id,
                "shortDescription": {"text": finding['rule']},
                "fullDescription": {"text": full_desc},
                "defaultConfiguration": {"level": "warning"},
                "help": {
                    "text": finding['recommendation'],
                    "markdown": f"**Recommendation:** {finding['recommendation']}"
                },
                "properties": {
                    "precision": "very-high",
                    "security-severity": str(severity_mapping.get(finding['severity'].lower(), 1.0)),
                }
            }
            if owasp:
                rules[rule_id]["properties"]["owasp"] = owasp
        
        result = {
            "ruleId": rule_id,
            "level": "warning" if finding['severity'].lower() in ["medium", "low"] else "error",
            "message": {
                "text": f"{finding['description']} — {finding['recommendation']}"
            },
            "locations": [
                {
                    "physicalLocation": {
                        "artifactLocation": {
                            "uri": finding['file']
                        },
                        "region": {
                            "startLine": 1,
                            "endLine": 1
                        }
                    }
                }
            ],
            "properties": {
                "severity": finding['severity'].upper(),
            }
        }
        if finding.get('owasp'):
            result["properties"]["owasp"] = finding['owasp']
        if finding.get('server'):
            result["properties"]["server"] = finding['server']
        
        results.append(result)
    
    sarif_doc = {
        "$schema": "https://raw.githubusercontent.com/oasis-tcs/sarif-spec/master/Schemata/sarif-schema-2.1.0.json",
        "version": "2.1.0",
        "runs": [
            {
                "tool": {
                    "driver": {
                        "name": "AgentSec",
                        "organization": "AgentSec",
                        "informationUri": "https://github.com/locface/AgentSec",
                        "rules": list(rules.values()),
                        "version": "1.0.3"
                    }
                },
                "results": results,
                "properties": {
                    "startTimeUtc": datetime.datetime.now(datetime.UTC).isoformat().replace("+00:00", "Z")
                }
            }
        ]
    }
    
    return sarif_doc


def print_sarif(findings: List[Dict[str, Any]], repo_root: str = ".") -> None:
    """Print SARIF report to stdout."""
    sarif = generate_sarif(findings, repo_root)
    print(json.dumps(sarif, indent=2))
