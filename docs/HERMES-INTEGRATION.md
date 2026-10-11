# Hermes security skill integration — adapter contract

**Status: not installed or verified.** This repository is not sufficient to activate Hermes automatically.

## Adapter requirements
1. Identify the Hermes version, executable, agent configuration, skill discovery paths and delegated tool permissions in the actual host environment.
2. Install a **pinned reviewed commit** of the public toolkit; do not execute remote mutable skill content.
3. Supply the project classification to a skill selector; load only applicable skills plus mandatory baseline controls.
4. Execute only explicitly authorized scanners and tests in isolated environments with minimal tokens.
5. Return structured findings, evidence identifiers and a release recommendation to Hermes.
6. Let protected GitHub workflows, not Hermes, enforce required checks; human approver retains release authority.
7. Validate with a non-sensitive sandbox project before testing any customer/government repository.

## Pilot acceptance tests
- Skill discovery resolves SEC-01 and SEC-12.
- Selection distinguishes an AI web app from a CAC/PIV integration.
- Malicious repository instructions do not override agent policies.
- Missing scan evidence results in NOT_TESTED, never PASS.
- Agent cannot merge, deploy or approve exceptions.
- Findings include source commit and reproducible evidence references.

## Current blocker
Hermes host configuration and installed skill interface have not been inspected. Do not claim live agent integration.
