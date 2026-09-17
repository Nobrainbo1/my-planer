---
description: "Reusable evidence-based verification report with FR traceability, debugging, security thresholds, and branch completion gates."
type: template
---

# Verification Report — [Project/Feature Name]

## 1. Candidate and Required Checks

- **Date / Orchestrator / approved brief and plan:** [values and approval references]
- **Status:** [NOT RUN / NEEDS REMEDIATION / BLOCKED / READY FOR DELIVERY]
- **Workspace / branch / base / current revision:** [absolute cwd and revisions]
- **Uncommitted content identity:** [diff reference or changed-file hashes]
- **Ledger / owning tasks / consumed fix rounds:** [persistent path and counts]
- **Environment / tools / versions:** [redacted values]
- **Required suites and commands / source:** [manifest, CI, brief, or approved commands]
- **Applicability:** [scope-based N/A decisions; required tests cannot be waived]
- **Approved security thresholds:** [exact brief rule and reference; missing or conflicting thresholds block readiness]

## 2. Fresh Execution Evidence

Run broad required suites on the final candidate, not only focused task tests. Rerun after fixes or candidate/base changes; mark old evidence superseded. Use the actual project commands. Never install tools without approval.

| Evidence ID / time | Category | Revision + diff identity | Absolute cwd | Exact command | Exit code | Actual output or durable redacted reference | Executed / passed / failed / skipped | Status |
|--------------------|----------|--------------------------|--------------|---------------|-----------|--------------------------------------------|------------------------------------|--------|
| [E-01] | [unit / integration / E2E / build / lint / typecheck / format / security / performance / docs] | [identity] | [path] | [command] | [code] | [assertions, errors, counts] | [actual counts or N/A] | [PASS / FAIL / BLOCKED / NOT RUN / N/A] |

- **Coverage:** [measured line/branch coverage and evidence; not an estimate]
- **Failed test names / errors:** [IDs and output]
- **Blocked or unrun commands:** [reason, permission/tool/service needed, owner, next action]
- **Superseded evidence:** [old ID -> new ID and reason]
- **Documentation checks:** [frontmatter, heading/table structure, fence pairing, relative links, and acceptance readback; manual procedure and result]

PASS means required assertions executed and passed on this candidate. An exit-zero run with no required tests, missing services, skipped required cases, or a past result is not a pass. N/A requires approved scope justification; it cannot relabel a required check. Documentation-only checks are not production Red/Green or runtime proof.

## 3. Functional Requirement to Test Matrix

Include every FR from the approved brief. A file name alone is not a test result. Every in-scope FR needs passing fresh evidence before readiness.

| FR ID / approved requirement | Implementation path:line | Exact test case / assertion or document check | Fresh evidence ID | Status / gap |
|------------------------------|--------------------------|----------------------------------------------|-------------------|--------------|
| [FR-01 / behavior] | [path:line] | [test ID and assertion] | [E-ID] | [PASS / FAIL / BLOCKED / NOT RUN] |

- **Explicit scope exclusions:** [FR ID and approved brief reference; excluded is not satisfied]
- **NFR / performance matrix:** [requirement, approved target, environment/workload, actual measurement, evidence, result]
- **Missing mappings:** [blockers, owner, next action]

## 4. Quality, Security, and Advisories

- **Linter / formatter / type checker:** [actual errors and warnings, evidence, status]
- **Complexity / dead code / maintainability review:** [findings and reviewed state]
- **Dependency audit:** [tool/version, vulnerability ID, affected package, severity, evidence, action]
- **Secret scan:** [evidence and findings, redacted; never include discovered secrets]
- **Applicable controls:** [input validation, injection/XSS/CSRF defenses, authentication/authorization, data protection, safe errors; evidence or justified N/A]

Escalate security findings immediately. Do not substitute a generic “no critical/high” standard for a stricter approved brief. Only nonblocking advisories may remain with explicit human acceptance within the approved security thresholds.

| Advisory / evidence | Why nonblocking under the brief | Impact and risk | Owner / follow-up date | Human approver / approval reference |
|---------------------|---------------------------------|-----------------|------------------------|------------------------------------|
| [finding] | [threshold and rationale] | [impact] | [owner/date] | [explicit acceptance or pending] |

No required test or check may be waived, weakened, quarantined, or moved into this table to obtain readiness. A finding outside the brief's allowed threshold remains a blocker even if someone labels it an advisory.

## 5. Four-Phase Debugging and Revalidation

| Owning task / shared fix round | Root cause investigation | Pattern analysis | Hypothesis test / observed result | Minimal fix / regression evidence | Revalidation and ordered reviews |
|--------------------------------|--------------------------|------------------|-----------------------------------|-----------------------------------|----------------------------------|
| [task / 1–5] | [exact reproduction and traces] | [working comparison, layers] | [one cause, prediction, actual observation] | [actual assertion Red -> Green -> Refactor; structural checks for docs] | [focused + broad fresh IDs; spec then quality/test] |

Use the same task ledger and budget across phases: one initial attempt plus up to 5 total fix rounds shared by build, test, and both reviews. Never reset on resume or reopen. Request a higher-tier model for rounds 4–5 if available; record actual availability and selection. If unavailable, record it and use a fresh reviewer without claiming a model change. Missing fresh review is BLOCKED. Stop after 5 failed fix rounds and escalate to the human. Escalate security, scope, destructive actions, and missing permissions immediately. Preserve failed evidence; no automatic destructive rollback.

## 6. Manual Verification and Whole-Branch Review

| Flow / procedure | Tested by | Candidate identity | Actual observation / evidence | Status |
|------------------|-----------|--------------------|-------------------------------|--------|
| [core flow or document readback] | [identity] | [revision + diff] | [result; exit code N/A for manual] | [status] |

Repeat this ordered review pair for **every task**, using its stable Task ID. Each task needs spec approval before quality/test review on the same exact candidate; one generic pair cannot approve multiple tasks.

| Task ID | Review gate | Reviewer identity / actual model | Exact candidate and reviewed scope | Evidence and findings | Verdict | Human fallback authorization |
|---------|-------------|----------------------------------|------------------------------------|-----------------------|---------|------------------------------|
| [T-ID] | Task spec compliance | [fresh reviewer or named human; not implementer] | [revision + diff identity; task paths/requirements] | [reference] | [APPROVED / CHANGES REQUIRED / BLOCKED] | [approver/date/reference or not used] |
| [same T-ID] | Task quality/test, after spec approval | [distinct reviewer or named human; not implementer or spec reviewer] | [same candidate; quality/test or documentation scope] | [reference and preceding spec approval] | [verdict] | [authorization reference or not used] |

Whole-branch reviews are **additional**, not substitutes for the per-task pairs.

| Review gate | Reviewer identity / actual model | Exact candidate and base-to-candidate scope | Evidence and findings | Verdict | Human fallback authorization |
|-------------|----------------------------------|--------------------------------------------|-----------------------|---------|------------------------------|
| Whole-branch spec compliance before merge | [fresh reviewer or named human; not implementer] | [base/current revision + diff identity; all included commits and intended uncommitted changes] | [reference] | [APPROVED / CHANGES REQUIRED / BLOCKED] | [approver/date/reference or not used] |
| Whole-branch quality/test, after spec approval | [distinct reviewer or named human; not implementer or spec reviewer] | [same whole-branch candidate and scope] | [reference and preceding spec approval] | [verdict] | [authorization reference or not used] |

If fresh agents are unavailable, use only the [Phase 4 canonical fallback](../../references/04_IMPLEMENTATION.md#401--canonical-fallback-when-fresh-agents-are-unavailable). Explicit human approval of single-agent implementation covers implementation only; the implementer cannot approve its own work. Unavailable subagent reviews may be replaced by two distinct named human reviewers, neither the implementer, spec first then quality/test. Record the exact candidate, scope, evidence, verdict, and human authorization for each review above; record model `N/A` for humans. Missing either approval or fallback authorization blocks acceptance. Never label self-review independent review. Revalidate fixes and repeat ordered reviews on the final state. Whole-branch review may be pending at Phase 5 transition, but must pass before merge or deployment.

## 7. Definition of Done and Approval State

- [ ] All in-scope FRs and NFRs have passing fresh evidence.
- [ ] All required suites, build, lint, typecheck, and other checks actually ran and passed.
- [ ] Security thresholds and required performance targets are met.
- [ ] Required documentation and change log are accurate and within scope.
- [ ] Task spec approval precedes quality/test approval on the final candidate.
- [ ] Fixes have fresh broad regression evidence; old evidence is superseded.
- [ ] Only qualifying nonblocking advisories remain with human acceptance.
- [ ] Required CI and manual gates passed where applicable.

- **Git cleanliness / history / worktree list evidence:** [commands, results, unrelated edits retained]
- **Whole-branch review readiness:** [passed or pending/blocking for merge]
- **Commit approval:** [reference or NOT AUTHORIZED]
- **Push approval:** [separate reference or NOT AUTHORIZED]
- **Merge approval:** [separate reference for exact candidate/target or NOT AUTHORIZED]
- **Deploy approval:** [separate environment/candidate reference or NOT AUTHORIZED]
- **Worktree deletion approval:** [separate path-specific reference or NOT AUTHORIZED]
- **Retention / cleanup:** [preserved ledger and outputs, dirty-work protection, actual status; no automatic deletion]

## 8. Final Verdict

| Category | Actual status | Evidence IDs / blockers |
|----------|---------------|-------------------------|
| Broad suites / coverage | [status] | [results] |
| Build / quality | [status] | [results] |
| Security / secrets | [status] | [results] |
| Performance | [status] | [results] |
| FR matrix / DoD | [status] | [results] |
| Task reviews / whole-branch review | [separate statuses] | [results] |

**Decision:** [READY FOR DELIVERY / NEEDS REMEDIATION / BLOCKED]

**Human transition approval:** [reference or pending; not commit/push/merge/deploy/delete approval]

**Unresolved issues and next exact action:** [owner, saved state, remaining budget, command or approval request]
