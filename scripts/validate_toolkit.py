#!/usr/bin/env python3
"""Fail-closed structural validation for Elliyeen security toolkit.
This is NOT an application vulnerability scanner."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
for i in range(1, 13):
    p = ROOT / f"skills/SEC-{i:02d}/SKILL.md"
    if not p.is_file():
        errors.append(f"Missing: {p.relative_to(ROOT)}")
        continue
    body = p.read_text(encoding="utf-8")
    for heading in ("## Objective", "## Inputs", "## Procedure", "## Acceptance criteria", "## Guardrails"):
        if heading not in body:
            errors.append(f"{p.relative_to(ROOT)}: missing {heading}")
    if not body.startswith("---\n") or not re.search(r"(?m)^name: elliyeen-sec-\d{2}$", body):
        errors.append(f"{p.relative_to(ROOT)}: invalid skill metadata")
for name in ("AGENTS.md", "docs/SECURITY-AGENT-STANDARD.md", "docs/IMPLEMENTATION.md",
             "templates/SECURITY-ASSESSMENT.md", "templates/SECURITY-FINDINGS.json",
             "templates/RELEASE-DECISION.json"):
    if not (ROOT / name).is_file():
        errors.append(f"Missing: {name}")
for name in ("SECURITY-FINDINGS.json", "RELEASE-DECISION.json"):
    p = ROOT / "templates" / name
    if p.is_file():
        try:
            json.loads(p.read_text(encoding="utf-8"))
        except (ValueError, UnicodeError) as exc:
            errors.append(f"{name}: {exc}")
workflow = ROOT / ".github/workflows/security-pr.yml"
if workflow.is_file():
    text = workflow.read_text(encoding="utf-8")
    if not re.search(r"actions/checkout@[a-f0-9]{40}", text):
        errors.append("Checkout must be pinned to a full commit SHA")
else:
    errors.append("Missing PR validation workflow")
if errors:
    print("\n".join(f"ERROR: {e}" for e in errors), file=sys.stderr)
    sys.exit(1)
print("PASS: 12 skill structures, required documents, JSON templates and pinned checkout.")
print("LIMITATION: This check does not assess deployed application security.")
