#!/usr/bin/env python3
"""
Scan public GitHub repositories for MCP configs and run AgentSec on them.
Usage: python scripts/scan_github.py --token TOKEN --limit 50
"""

import os
import sys
import json
import time
import base64
import argparse
import tempfile
from pathlib import Path
from typing import List, Dict, Any, Optional
from collections import Counter
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Add parent directory to sys.path to import agentsec
sys.path.insert(0, str(Path(__file__).parent.parent))

from agentsec.rules import load_rules


class GitHubScanner:
    def __init__(self, token: str, limit: int = 50, output_file: str = "github_scan_results.json"):
        self.token = token
        self.limit = limit
        self.output_file = output_file
        self.session = self._create_session()
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
        self.base_url = "https://api.github.com"
        self.results = []
        self.stats = {
            "total_repos": 0,
            "total_configs": 0,
            "findings_by_rule": Counter(),
            "findings_by_severity": Counter(),
            "repos_with_findings": set(),
            "errors": []
        }

    def _create_session(self):
        session = requests.Session()
        retries = Retry(total=3, backoff_factor=1, status_forcelist=[403, 429, 500, 502, 503, 504])
        session.mount('https://', HTTPAdapter(max_retries=retries))
        return session

    def search_mcp_configs(self) -> List[Dict]:
        """Search for files named mcp.json, mcp.yaml, mcp.yml, or containing 'mcp' in filename."""
        queries = [
            "filename:mcp.json",
            "filename:mcp.yaml",
            "filename:mcp.yml",
        ]
        all_items = []
        for query in queries:
            url = f"{self.base_url}/search/code"
            params = {
                "q": query,
                "per_page": 100
            }
            page = 1
            while len(all_items) < self.limit:
                params["page"] = page
                resp = self.session.get(url, headers=self.headers, params=params)
                if resp.status_code != 200:
                    print(f"Error searching for {query}: {resp.status_code} - {resp.text[:200]}")
                    break
                data = resp.json()
                items = data.get("items", [])
                if not items:
                    break
                all_items.extend(items)
                if len(all_items) >= self.limit:
                    break
                page += 1
                time.sleep(0.2)
        return all_items[:self.limit]

    def get_file_content(self, item: Dict) -> Optional[str]:
        """Get file content from GitHub API."""
        url = item["url"]
        resp = self.session.get(url, headers=self.headers)
        if resp.status_code != 200:
            return None
        data = resp.json()
        content = data.get("content", "")
        if content:
            try:
                decoded = base64.b64decode(content).decode("utf-8")
                return decoded
            except Exception:
                return None
        return None

    def scan_file_content(self, content: str, file_path: str, repo_name: str) -> List[Dict]:
        """Run AgentSec rules on file content."""
        findings = []
        rules = load_rules()
        for rule in rules:
            # Rule.detect expects (content: str, file_path: Path)
            if rule.detect(content, Path(file_path)):
                findings.append({
                    "file": file_path,
                    "rule": rule.name,
                    "severity": rule.severity,
                    "description": rule.description,
                    "recommendation": rule.recommendation,
                    "repo": repo_name
                })
        return findings

    def run(self):
        print(f"Searching for MCP configs (limit {self.limit})...")
        items = self.search_mcp_configs()
        print(f"Found {len(items)} config files.")
        self.stats["total_configs"] = len(items)
        unique_repos = set(item["repository"]["full_name"] for item in items)
        self.stats["total_repos"] = len(unique_repos)

        for idx, item in enumerate(items):
            repo_name = item["repository"]["full_name"]
            file_path = item["path"]
            print(f"[{idx+1}/{len(items)}] Scanning {repo_name}:{file_path}")
            content = self.get_file_content(item)
            if not content:
                self.stats["errors"].append(f"Failed to fetch content for {repo_name}:{file_path}")
                continue
            findings = self.scan_file_content(content, file_path, repo_name)
            if findings:
                self.stats["repos_with_findings"].add(repo_name)
                for f in findings:
                    self.stats["findings_by_rule"][f["rule"]] += 1
                    self.stats["findings_by_severity"][f["severity"]] += 1
                self.results.extend(findings)
            time.sleep(0.2)

        # Save results
        output = {
            "stats": {
                "total_repos": self.stats["total_repos"],
                "total_configs": self.stats["total_configs"],
                "repos_with_findings": len(self.stats["repos_with_findings"]),
                "findings_by_rule": dict(self.stats["findings_by_rule"]),
                "findings_by_severity": dict(self.stats["findings_by_severity"]),
                "errors": self.stats["errors"]
            },
            "findings": self.results
        }
        with open(self.output_file, 'w') as f:
            json.dump(output, f, indent=2)
        print(f"Results saved to {self.output_file}")
        print(f"Total findings: {len(self.results)}")
        print(f"Repos with findings: {len(self.stats['repos_with_findings'])}")


def main():
    parser = argparse.ArgumentParser(description="Scan GitHub for MCP configs with AgentSec.")
    parser.add_argument("--token", help="GitHub personal access token")
    parser.add_argument("--limit", type=int, default=50, help="Maximum number of config files to scan")
    parser.add_argument("--output", default="github_scan_results.json", help="Output file")
    args = parser.parse_args()
    token = args.token or os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Error: GitHub token required. Set GITHUB_TOKEN env var or pass --token.")
        sys.exit(1)
    scanner = GitHubScanner(token, limit=args.limit, output_file=args.output)
    scanner.run()

if __name__ == "__main__":
    main()
