---
name: elliyeen-sec-03
description: Application and API Security for risk-based Elliyeen secure software delivery.
---

# SEC-03 — Application and API Security

## Objective
Assess authorization, authentication, injection, SSRF, tenancy, sessions and business logic.

## Inputs
Routes, API schemas, authentication flows, authorization tests.

## Procedure
1. Confirm project scope, permission, environment and governing policy version.
2. Inspect provided evidence read-only and identify missing information.
3. Assess applicable threats and controls using current authoritative references.
4. Specify tests, expected outcomes and reproducible evidence requirements.
5. Record confirmed findings separately from suspected and untested risks.
6. Produce SECURITY-TEST-PLAN.md with commit, artifact and environment identity.
7. Escalate critical failures to independent review and human release authority.

## Acceptance criteria
Every sensitive API has negative authorization tests.

## Guardrails
No invented results, unauthorized active tests, production changes, self-approved risk exceptions, secrets in reports or claims of regulatory authorization.
