---
name: elliyeen-sec-12
description: Independent Verification for risk-based Elliyeen secure software delivery.
---

# SEC-12 — Independent Verification

## Objective
Reproduce findings, validate evidence and assess release gate independently.

## Inputs
Security findings, test evidence, build identity, exceptions.

## Procedure
1. Confirm project scope, permission, environment and governing policy version.
2. Inspect provided evidence read-only and identify missing information.
3. Assess applicable threats and controls using current authoritative references.
4. Specify tests, expected outcomes and reproducible evidence requirements.
5. Record confirmed findings separately from suspected and untested risks.
6. Produce PRODUCTION-READINESS.md with commit, artifact and environment identity.
7. Escalate critical failures to independent review and human release authority.

## Acceptance criteria
No untested control treated as passed; human approval remains required.

## Guardrails
No invented results, unauthorized active tests, production changes, self-approved risk exceptions, secrets in reports or claims of regulatory authorization.
