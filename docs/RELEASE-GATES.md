# GitHub release gates — deployment checklist

**Current state:** PR toolkit validation only. No production deployment workflow is installed.

Before declaring this project ready for production:
- Configure branch protection/rulesets on `main`: require passing toolkit validation, review approval, no force pushes, no bypass by agent accounts.
- Review workflow permissions and pin external actions to immutable full SHAs.
- Enable repository secret scanning, push protection, and dependency alerts where available.
- Add application-specific SAST, SCA, IaC, API auth, and adversarial AI checks in each application repository.
- Enforce a separate protected production environment with designated reviewers.
- Use short-lived deployment credentials (OIDC where supported), immutable artifacts and verified provenance.
- Maintain risk exceptions outside agent authority.
- Confirm logs and evidence retention policies.

Never interpret a passing toolkit structural check as an application security certification.
