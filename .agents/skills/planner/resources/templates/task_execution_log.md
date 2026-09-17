---
description: "Reusable persistent SDD task ledger with shared fix budget, ordered reviews, and resumable evidence."
type: template
---

# Task Execution Log — [Task ID]

## 1. Identity and Resume State

- **Date / plan / task / approved requirements:** [values and approval reference]
- **Status:** [PENDING / IN PROGRESS / BLOCKED / ACCEPTED]
- **Ledger path:** [.superpowers/sdd/<plan>/progress.md or chosen local ledger; mandatory]
- **Workspace / branch / base / current revision:** [absolute cwd, branch, revisions]
- **Uncommitted content identity:** [diff reference or changed-file hashes]
- **Owned files / preserved unrelated edits:** [paths and ownership]
- **Dependencies / acceptance criteria:** [task IDs and exact criteria]
- **Implementer identity / actual model:** [fresh per task; unavailable is not independent execution]
- **Current round / remaining fixes:** [initial 0 or fix 1–5 / 5 minus consumed rounds]
- **Next exact action / pending review / blockers:** [resumable instructions]

Persist this state before dispatch, after checks and reviews, and before compaction or handoff. On resume, compare git status and file identity with saved evidence. Revalidate changed state. Never reset the task's budget.

## 2. Builder Output and TDD

- **Files created / modified / approved deleted:** [paths and reasons]
- **Tests written / requirements covered:** [test IDs and FR IDs]
- **Red:** [evidence ID for an actual observed assertion failure for missing behavior]
- **Green:** [minimal production change and passing evidence ID]
- **Refactor:** [behavior-preserving change or no-change rationale and rerun evidence]
- **Documentation-only alternative:** [structural, link, fence, and acceptance checks; not runtime proof]

Production-code changes require Red before Green. Parse errors, missing tools, and imagined failures do not satisfy Red. Documentation-only work does not require a fabricated failing production test.

## 3. Validator Evidence

| Evidence ID / time | Task / round | Revision + diff identity | Absolute cwd | Exact command or manual procedure | Exit code | Actual output or durable redacted reference | Status |
|--------------------|--------------|--------------------------|--------------|-----------------------------------|-----------|--------------------------------------------|--------|
| [E-01] | [T-ID / 0] | [HEAD + hashes] | [path] | [command] | [code; N/A for manual] | [assertions, counts, errors] | [PASS / FAIL / BLOCKED / NOT RUN / N/A] |

Include syntax, build, lint, typecheck, focused tests, integration/regression suites, and relevant document checks. Record tool/environment versions where relevant. Justify `N/A` by approved scope. Required blocked, skipped, or unrun checks cannot be reported as passing or waived.

## 4. Shared Fix Rounds and Four-Phase Debugging

One initial attempt plus up to 5 total fix rounds per task. Build, test, and both reviews share the count. Expected Red is not remediation. Persist a round when remediation starts; carry it across phases and sessions.

| Round | Failure evidence | Root cause investigation | Pattern analysis | Hypothesis and isolated test | Minimal fix and regression evidence | Actual model / reviewer | Outcome |
|-------|------------------|--------------------------|------------------|------------------------------|-----------------------------------|-------------------------|---------|
| [1–5] | [ID] | [reproduction and traces] | [working comparison and affected layers] | [prediction and observed result] | [change and IDs] | [identity] | [resolved / failed / blocked] |

For rounds 4–5, request a higher-tier model if available. Record the request, availability, and actual selection. If unavailable, record it and use a fresh reviewer at the available tier; never claim a model switch that did not occur. Missing fresh review is a blocker, not a fabricated approval. After 5 failed fix rounds, stop and escalate to the human. Escalate security, scope, destructive actions, and missing permissions immediately regardless of round.

## 5. Ordered Reviews and Acceptance Readback

| Tier | Reviewer identity / actual model | Reviewed revision + diff identity | Findings and evidence | Verdict |
|------|----------------------------------|-----------------------------------|-----------------------|---------|
| 1: Spec compliance | [fresh, not implementer] | [identity] | [requirements, scope, missing/extra behavior] | [APPROVED / CHANGES REQUIRED / BLOCKED] |
| 2: Quality/test | [fresh, distinct from tier 1 and implementer] | [identity] | [quality, security, edge cases, test strength] | [APPROVED / CHANGES REQUIRED / BLOCKED] |

Tier 2 starts only after tier 1 approval. After fixes, rerun affected checks and repeat reviews in order on the new state. If fresh agents are unavailable, apply only the [Phase 4 canonical fallback](../../references/04_IMPLEMENTATION.md#401--canonical-fallback-when-fresh-agents-are-unavailable). Explicit human permission for single-agent implementation does not authorize approval of the implementer's own work. Unavailable subagent reviews require two distinct named human reviewers, neither the implementer, spec first then quality/test. Record each review's exact candidate, scope, evidence, and verdict plus human fallback authorization. Missing either approval or authorization blocks acceptance. Record self-review separately; never label it independent review.

- **Fallback authorization:** [human approver, date, explicit approval reference, authorized implementation/review scope, or not used]
- **Human review scope and evidence:** [each tier's named reviewer, exact candidate and scope, evidence, verdict, and authorization reference; model N/A for humans]

- **Acceptance readback:** [criterion -> evidence -> result, before the next dependent task]
- **Task accepted by / time:** [identity or BLOCKED; implementation complete is not accepted]

## 6. Safe Rulings and Impact

| Question / evidence | Alternatives | Ruling and rationale | Affected files / FRs | Test, cost, risk impact | Reversal path | Human approval needed? |
|---------------------|--------------|----------------------|---------------------|------------------------|---------------|------------------------|
| [minor ambiguity] | [choices] | [smallest reversible in-scope choice] | [paths / IDs] | [impact] | [safe recovery] | [reference or no, with reason] |

Rulings cannot expand scope, weaken security thresholds, waive required tests, or authorize destructive operations. Preserve all work on failure; no automatic rollback. Record nonblocking advisories only with explicit human acceptance under the approved brief's security thresholds.

## 7. Handoff and Action Approvals

- **Decision / change / issue log:** [what, why, evidence, unresolved issues]
- **Saved state and entry points:** [ledger, plan, files, evidence]
- **Next action / remaining budget:** [exact continuation]
- **Commit / push / merge / deploy / worktree deletion:** [separate explicit approval for each, or NOT AUTHORIZED]
- **Whole-branch review / clean status:** [Phase 6 evidence or pending; never discard edits to make status clean]
