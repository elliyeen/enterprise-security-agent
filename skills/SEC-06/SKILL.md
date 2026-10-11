---
name: elliyeen-sec-06
description: Software Supply Chain for risk-based Elliyeen secure software delivery.
---

# SEC-06 — Software Supply Chain

## Objective
Review dependency risks, SBOM, pinned actions, provenance and artifact integrity.

## Inputs
Lockfiles, build definitions, dependency inventory.

## Procedure
1. Confirm project scope, permission, environment and governing policy version.
2. Inspect provided evidence read-only and identify missing information.
3. Assess applicable threats and controls using current authoritative references.
4. Specify tests, expected outcomes and reproducible evidence requirements.
5. Record confirmed findings separately from suspected and untested risks.
6. Produce SUPPLY-CHAIN-REVIEW.md with commit, artifact and environment identity.
7. Escalate critical failures to independent review and human release authority.

## Acceptance criteria
Known critical risks triaged; release artifact provenance documented.

## Guardrails
No invented results, unauthorized active tests, production changes, self-approved risk exceptions, secrets in reports or claims of regulatory authorization.
