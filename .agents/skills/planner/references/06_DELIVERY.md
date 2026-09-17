---
description: "Phase 6: Whole-branch review, approval-gated delivery, safe workspace retention, handoff, and retrospective."
phase: 6
checkpoint: true
---

# Phase 6: Delivery, Handoff & Retrospective

> **Goal:** Package verified work, obtain separate action approvals, and preserve evidence and lessons for the next session. Delivery can be an uncommitted handoff; it does not always mean deployment.

## Step 6.0 — Whole-Branch Completion Review

Before any merge, review the **entire branch against the approved base**, not only the last commit or individual task diffs.

1. Read the approved brief, plan, task ledger, and [verification report](../resources/templates/verification_report.md). Require fresh Phase 5 evidence and transition approval. Identify the base branch and merge base, current HEAD, and uncommitted content identity.
2. Inspect all included commits, the complete base-to-candidate diff, staged and unstaged changes, and untracked files. For an uncommitted handoff, include the intended working-tree diff in the candidate. Preserve unrelated work; do not include it in the changeset or silently claim it was reviewed.
3. Use a fresh reviewer for broad spec compliance, then a distinct fresh quality/test reviewer after spec approval. Review interactions between tasks, contracts, security, regressions, tests, documentation, dependencies, and deployment effects. Record reviewer identities, actual models if known, exact reviewed state, findings, and verdicts. If subagent reviews are unavailable, apply only the [Phase 4 canonical fallback](./04_IMPLEMENTATION.md#401--canonical-fallback-when-fresh-agents-are-unavailable): two distinct named human reviewers, neither the implementer, spec first then quality/test. Record human fallback authorization and each review's exact candidate, scope, evidence, and verdict. Missing either approval blocks completion; single-agent permission covers implementation only and self-review never satisfies independence. Whole-branch reviews are additional to each task's review pair.
4. Assign findings to their owning task and use its remaining shared fix budget. Follow [four-phase debugging](./05_VERIFICATION.md), revalidate every fix, repeat ordered reviews, and run fresh broad required suites on the final candidate. A changed base, conflict resolution, or candidate change invalidates affected prior approval and evidence. Do not merge until the new state is reviewed and verified.
5. Inspect git history and status for accidental files, secrets, unrelated commits, unresolved conflicts, or unintended staging. Record the result. Do not rewrite history or discard work merely to make it look clean.

A required failure or missing check blocks merge and delivery readiness. Required tests cannot be waived. Only nonblocking advisories with explicit human acceptance within the approved brief's security thresholds may remain. Escalate security, scope, destructive actions, and missing permissions immediately; do not wait for five failed fix rounds.

## Step 6.1 — PR / Changeset Packaging

Prepare a local summary within approved file scope. Creating a PR or publishing artifacts requires explicit approval. Include:

```markdown
### Change Package Summary
- Title and purpose: [relation to approved brief]
- Candidate: [branch, base/current revision, uncommitted diff identity]
- Statistics: [files and lines added/changed/deleted; tests; dependency changes]
- Components: [paths and behavior changes]
- Verification: [report and evidence IDs, actual statuses and counts]
- Whole-branch reviews: [reviewers, reviewed state, verdicts]
- Breaking changes and migration path: [details or none]
- Blocking issues: [details or none; never move required failures to advisories]
- Accepted nonblocking advisories: [impact, owner, approval reference]
- Recovery plan: [trigger, preserved state, exact proposed actions, data impact, approval boundary]
- Requested next action: [retain local handoff, commit, PR, or deployment decision]
```

Do not prefill successful test or security results. Copy only evidence from the verified candidate. A recovery plan is not permission to execute it. No automatic destructive rollback is allowed.

### Separate Action Approvals

| Action | Required approval and checks |
|--------|------------------------------|
| Commit | Explicit commit approval; inspect status, diffs, and recent history; stage only owned intended files; never secrets. |
| Push | Separate push approval naming remote and branch; inspect outgoing commits. |
| Create PR | Explicit PR approval; inspect complete branch diff, base, and tracking. |
| Merge | Separate merge approval for the reviewed candidate and target; complete whole-branch review and fresh checks first. |
| Deploy | Separate environment-specific deployment approval at Checkpoint 3, including candidate and recovery plan. |
| Delete worktree | Separate deletion approval for the exact path after preservation and cleanliness checks. |

Plan approval, task acceptance, or approval of one action does not grant the others. Preserve uncommitted work when commit approval is absent. No forced push, reset, clean, branch deletion, or history rewrite is implied by this protocol. Any destructive recovery needs its own explicit approval and impact review.

## Step 6.2 — Deployment Checklist

Before requesting deployment approval:

- [ ] Phase 5 checks and whole-branch reviews approve the exact delivery candidate.
- [ ] No required tests or checks are failed, blocked, skipped, or unrun.
- [ ] Target environment, credentials, permissions, and configuration are confirmed without logging secrets.
- [ ] Database migrations and data impact are reviewed; schema changes need separate permission.
- [ ] Feature flags, monitoring, alerts, and health checks are ready where applicable.
- [ ] Recovery steps, triggers, backups, data-loss risk, and responsible owner are documented and tested safely in an authorized environment.
- [ ] Exact deployment sequence and post-deployment smoke checks are recorded.

```text
CHECKPOINT 3 — Deployment Approval
[SUMMARY] Actual verification verdict and whole-branch review references.
[CANDIDATE] Revision, artifact identity, target environment.
[RISKS] Known nonblocking advisories and their human acceptance; any blockers prevent deployment.
[RECOVERY] Proposed steps, triggers, data impact, and required permissions.
[DECISION NEEDED] Approve deployment of this candidate to this environment?
```

After approval, execute only the approved steps. Record command/cwd/revision/exit/output evidence for each step. Verify health, core user flows, error rates, performance, and logs with fresh results. If checks fail, stop rollout, preserve evidence, and escalate immediately for security or destructive recovery. Do not automatically run a rollback or assume deployment approval authorizes destructive database restoration.

If deployment is not requested or approved, hand off artifacts and record `NOT DEPLOYED`; do not claim a live release.

## Step 6.3 — Documentation Update

Update only approved deliverables as applicable: README setup and usage, change log, API documentation, architecture records, and operations runbook. Do not create or change extra files without scope approval. Do not add comments unless requested.

```markdown
## [Version] — [Date]
### Added
- [New feature]
### Changed
- [Modified behavior]
### Fixed
- [Bug fix]
### Removed
- [Approved removal]
### Security
- [Security change]
```

## Step 6.3.5 — Session Handoff and Workspace Retention

Use [the handoff template](../resources/templates/handoff_artifact.md) when that artifact is authorized; otherwise record handoff in the chosen local ledger. Preserve:

- System state: what works, what is partial, and what is blocked.
- Workspace path, branch, base/current revision, owned diff identity, and unrelated changes.
- Exact ledger path, current task, consumed fix rounds, pending reviews, evidence references, and next command/action.
- Key decisions and safe rulings with rationale, affected requirements, impact, and reversal path.
- Unresolved issues, accepted advisories, approvals granted or still needed, and files to read first.

Create this record before compaction, session end, agent/model changes, or human handoff. On resume, compare the actual workspace with the saved state and revalidate stale evidence.

### Git Cleanliness and Worktree Cleanup

Inspect status, staged/unstaged diffs, untracked files, history, and the worktree list. Record clean or dirty truthfully for each relevant workspace. Dirty uncommitted delivery is allowed as a retained handoff, but is not a clean completed merge or deployment.

Before deleting a worktree, confirm separate human approval of its exact path, no active agent uses it, and all required changes and ledger/output evidence are durably preserved outside it in an approved location. Check for uncommitted and untracked work; unresolved content blocks deletion. Do not force removal or delete a branch implicitly. If permission or safe preservation is absent, retain the worktree and report cleanup pending. After authorized cleanup, recheck worktree list and status to prove the result.

## Step 6.4 — Retrospective

Use [the retrospective template](../resources/templates/retrospective.md) only within approved output scope. Capture what worked, what failed, surprises, tools and harness limitations, safe rulings, and decision rationale. Include task counts, shared fix rounds, escalations, unavailable models/reviewers, and verification gaps. Do not invent time-saved metrics or claim a model upgrade without evidence.

## Step 6.5 — Harness Evolution

Propose concrete improvements to rules, tools, templates, and workflow based on evidence. Record expected impact and owner. Apply them only under a separately approved scope; a retrospective does not authorize modifying the harness or installing tools automatically.

## Phase 6 Output

Report actual state for each item: changeset prepared, whole-branch review, verification, action approvals, commit/push/merge/deployment, git cleanliness, workspace retention or approved cleanup, handoff, retrospective, and proposed improvements. Use `COMPLETE`, `BLOCKED`, `PENDING APPROVAL`, or justified `N/A`; no default completion claims.

Return to [Phase 1: Discovery](./01_DISCOVERY.md) for the next approved iteration. Retained work and unresolved blockers remain visible in the ledger.
