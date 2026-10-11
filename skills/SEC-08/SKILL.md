---
name: elliyeen-sec-08
description: DevSecOps and CI/CD for risk-based Elliyeen secure software delivery.
---

# SEC-08 — DevSecOps and CI/CD

## Objective
Review branch rules, token permissions, workflows, checks, build promotion and rollback.

## Inputs
CI workflows, repo policies, deployment architecture.

## Procedure
1. Confirm project scope, permission, environment and governing policy version.
2. Inspect provided evidence read-only and identify missing information.
3. Assess applicable threats and controls using current authoritative references.
4. Specify tests, expected outcomes and reproducible evidence requirements.
5. Record confirmed findings separately from suspected and untested risks.
6. Produce CI-CD-SECURITY-REVIEW.md with commit, artifact and environment identity.
7. Escalate critical failures to independent review and human release authority.

## Acceptance criteria
Mandatory checks independently enforced and no agent self-bypass.

## Guardrails
No invented results, unauthorized active tests, production changes, self-approved risk exceptions, secrets in reports or claims of regulatory authorization.
