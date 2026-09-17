---
name: subagent-driven-development
description: >-
  Execute an approved plan with fresh implementers, persistent progress, and
  ordered independent reviews. Use for /sdd or "execute plan with subagents".
---

# Subagent-Driven Development

SDD assigns each task to a fresh implementer and verifies its result before dependent work starts. Follow [root rules](../../AGENTS.md) and [Phase 4](../planner/references/04_IMPLEMENTATION.md). This skill describes a workflow; it cannot create missing agent or model-selection capabilities.

## Preflight

1. Read the explicitly approved target-project `INTENT_BRIEF.md`, `CONTEXT.md`, and `EXECUTION_PLAN.md`. Confirm approval covers the current revisions and requested execution. Unapproved plans block implementation, including spikes and scaffolding.
2. Inspect the workspace without changing unrelated work. Use an approved dedicated branch or isolated worktree and exact file ownership. If workspace operations are disallowed, disclose the constraint and obtain an approved alternative. Never work around denied permissions.
3. Scan file read/write collisions, producer/consumer contracts, and circular task dependencies. Resolve conflicts before dispatch. Parallel work needs independent ownership, satisfied dependencies, and an explicit integration task.
4. Confirm fresh implementer and reviewer tools are available. If unavailable, record the gap and ask for an approved alternative. Self-review is not independent review.
5. Choose an exact persistent ledger path, normally target-project `.superpowers/sdd/<plan-id>/progress.md`, or an approved local ledger. Use the [task log template](../planner/resources/templates/task_execution_log.md) as a source, never as a live session log. Discover actual validation commands from project configuration.

## Per-Task Protocol

1. Persist task ID, approved requirements, owned files, dependencies, workspace and content identity, status, remaining fix budget, and next action before dispatch.
2. Dispatch a **fresh implementer per task**, without prior task conversation. Provide full task text, exact paths/code/commands, relevant context, approval limits, ledger location, and dependencies. Resume a partially finished task with saved evidence and budget, not a new count.
3. Require [TDD](../test-driven-development/SKILL.md): observed Red before production changes, minimum Green, then behavior-preserving Refactor. Documentation uses structural acceptance checks instead of invented runtime tests.
4. Run focused and required broader checks. Record time, exact command, absolute cwd, candidate identity, exit code, actual output, and PASS/FAIL/BLOCKED/NOT RUN/N/A. Explain N/A. Missing checks are not passes.
5. Dispatch a fresh **spec compliance reviewer**, distinct from the implementer. Compare the actual files and tests with every approved acceptance criterion. Reject missing requirements and extra scope. Record findings, evidence, reviewed identity, and verdict.
6. Only after spec approval, dispatch a distinct fresh **quality/test reviewer**. Inspect correctness, clarity, security, edge cases, regression risk, and whether tests prove the claims. Do not rely solely on the implementer's report.
7. For findings, use the shared fix budget below. Rerun affected checks and repeat spec review before quality review on the changed candidate.
8. Read back every acceptance criterion against current evidence. Persist both approvals and ACCEPTED status before dependent tasks start. An implemented task with missing review is BLOCKED, not accepted.

## Shared Fix Budget

Allow one initial attempt plus up to **5 total fix rounds per task**. Build, test, spec review, and quality review share the count. Expected TDD Red is not a fix round. Persist a round when remediation begins; never reset it after context loss, a changed reviewer, or a later phase.

Use [systematic debugging](../systematic-debugging/SKILL.md) for every unexpected failure. Rounds 1–3 use the available implementer. For rounds 4 and 5, request a higher-tier model if available and record the actual model used. If unavailable, record that fact and use a fresh reviewer at the available tier. Never claim an unavailable model upgrade. Missing independent review blocks acceptance pending an approved alternative.

After 5 failed fix rounds, stop and escalate to the human with failure evidence, attempted hypotheses, and 2 to 3 options with a recommendation. No automatic sixth round. Security, scope, destructive actions, and missing permissions require immediate escalation; never wait for budget exhaustion.

## Rulings, Not Stalls

For a minor ambiguity, choose the smallest reversible action within approved scope. Record the question, alternatives, ruling, rationale, affected files/requirements, test/cost/risk impact, and reversal path in the ledger. Continue only if behavior and acceptance criteria are preserved. A ruling cannot authorize new scope, weaken tests, or bypass permissions.

## Resume and Completion

Persist the ledger after every check/review and before compaction or handoff. Include agent identities, actual models where known, task statuses, commands/output, current round, rulings, blockers, and next exact action. On resume, compare saved candidate identity with actual files and revalidate stale evidence.

Run [Phase 5](../planner/references/05_VERIFICATION.md) and [Phase 6](../planner/references/06_DELIVERY.md) for integrated verification and whole-branch review. Keep unrelated work intact. Commit, push, PR creation, merge, deployment, and worktree deletion each need explicit permission. Do not automatically reset, delete, or roll back work. Report changed files, actual verification status, and the next decision only.
