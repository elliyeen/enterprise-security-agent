---
name: elliyeen-sec-02
description: Threat Modeling for risk-based Elliyeen secure software delivery.
---

# SEC-02 — Threat Modeling

## Objective
Identify assets, trust boundaries, STRIDE threats, abuse cases, mitigations and testable controls.

## Inputs
Architecture diagrams, identities, data flows, dependencies.

## Procedure
1. Confirm project scope, permission, environment and governing policy version.
2. Inspect provided evidence read-only and identify missing information.
3. Assess applicable threats and controls using current authoritative references.
4. Specify tests, expected outcomes and reproducible evidence requirements.
5. Record confirmed findings separately from suspected and untested risks.
6. Produce THREAT-MODEL.md with commit, artifact and environment identity.
7. Escalate critical failures to independent review and human release authority.

## Acceptance criteria
All critical trust boundaries assessed and threats mapped to tests.

## Guardrails
No invented results, unauthorized active tests, production changes, self-approved risk exceptions, secrets in reports or claims of regulatory authorization.
