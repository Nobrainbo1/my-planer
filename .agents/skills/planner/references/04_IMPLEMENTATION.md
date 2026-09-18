---
description: "Phase 4: Implementation through isolated subagents, test-first development, and evidence-backed task reviews."
phase: 4
checkpoint: true
---

# Phase 4: Implementation — Subagent-Driven Development

> **Goal:** Execute the approved Execution Plan with the tools from Phase 3. Each small change passes the Builder-Validator loop and two independent reviews before the next task starts.

The Builder implements one task. The Validator runs checks. A spec reviewer checks the contract first. A quality/test reviewer then checks correctness, maintainability, and test strength. Passing tools alone does not prove spec compliance.

## Step 4.0 — Pre-Implementation Gate

- [ ] Intent Brief and Execution Plan have explicit Orchestrator approval.
- [ ] Prerequisite tools and development environment for the next task are available. Approved custom-tool tasks may precede consumers; those consumers remain blocked until their tool dependency is accepted. Missing permissions block the affected action immediately.
- [ ] Inspect git status, current revision, base branch, and existing worktrees. Preserve unrelated edits and record their ownership.
- [ ] Use an isolated git worktree or dedicated task branch. Record its absolute path, branch, base revision, and owned files. Do not work directly on a shared integration branch.
- [ ] Check task dependencies, file collisions, and interface contracts before dispatch.
- [ ] Select a writable, persistent ledger: `.superpowers/sdd/<plan>/progress.md` or an explicitly chosen local ledger. Record the exact path. Logging is mandatory, not an optional deep-log mode.
- [ ] Confirm fresh implementer and reviewer dispatch is available. If unavailable, record the capability gap and apply the canonical fallback in Step 4.0.1. Do not describe self-review as independent review.
- [ ] Identify exact build, lint, typecheck, test, and documentation validation commands from the project. Do not install tools without approval.

Branch creation does not authorize commits or any destructive action. If the permitted file scope excludes the default ledger, choose an approved local ledger within scope or ask for permission before writing elsewhere.

Before dispatch into a worktree, read the plan's authoritative artifact map. Record the original target root and execution workspace separately. Verify the brief, glossary, approved plan, and single writable ledger at their recorded absolute paths; uncommitted files do not appear in a new worktree automatically. Pass these paths to all agents. Copy only within approved locations, verify approved revision/content identity, and keep copies non-authoritative. Record any authorized relocation and update entry points before resuming.

### Candidate Identity Contract

Define the candidate as the approved base revision plus the explicit deliverable file set and its exact content/diff identity, including additions and deletions. Record current HEAD separately. Include all intended code, configuration, tests, and documentation; never exclude a deliverable to evade review. List mutable ledger, report, and approval-record paths separately from the candidate. Evidence-only updates do not change deliverable identity, but remain traceable and must be inspected for accuracy, scope, and secrets. Changes to requirements, approved design, or deliverable content still invalidate affected approvals and checks.

If a plan, report, handoff, or other evidence artifact must itself ship, finalize and freeze its contents, include that snapshot in the deliverable set, and run applicable checks and ordered reviews on that candidate. Store subsequent verdicts and action records in a separately approved non-deliverable evidence location; do not insert them into the frozen snapshot. Any later edit to a frozen deliverable requires revalidation and ordered review. This separation does not waive required evidence or grant permission to create files.

### 4.0.1 — Canonical Fallback When Fresh Agents Are Unavailable

If fresh implementer or reviewer dispatch is unavailable, apply exactly this fallback; do not improvise alternatives.

- **Single-agent implementation:** Proceed as a single agent only with the Orchestrator's explicit approval, recorded in the ledger. The implementing agent can never approve its own work.
- **Human review replacement:** Unavailable subagent reviews may be replaced by two distinct, named human reviewers — neither may be the implementer. The spec compliance reviewer reviews first; the quality/test reviewer reviews only after spec approval.
- **Required evidence per review:** Each review records the exact candidate (revision and diff identity), reviewed scope, cited evidence, and an explicit verdict, plus the human authorization that approved the fallback.
- **Blocking rule:** Missing either review, or missing fallback authorization, blocks task acceptance. Never label self-review as independent review.

Reference this fallback in the task ledger, the Phase 5 verification report, and the Phase 6 whole-branch review whenever it is used.

## Step 4.1 — Task Execution Protocol

Use [the task execution log](../resources/templates/task_execution_log.md) for each task. Persist state before dispatch, after every check or review, and before handoff or compaction.

```text
Approved task and isolated workspace
  -> Fresh implementer
  -> Red -> Green -> Refactor, or structural validation for documentation
  -> Build, lint, typecheck, and relevant tests
  -> Spec compliance reviewer
  -> Quality/test reviewer, only after spec approval
  -> Persist accepted evidence and read back acceptance criteria
  -> Next task
Any failure -> Four-phase debugging -> Shared fix budget -> Revalidate and review
```

### 4.1.1 — Fresh Implementer (Builder)

Dispatch a new isolated implementer for every task unless single-agent implementation is explicitly authorized under Step 4.0.1. Outside that implementation-only fallback, do not reuse the previous implementer's conversation. Give it the task text, approved requirements, exact file ownership, relevant code context, dependency status, commands, and ledger path. A resumed task also receives its existing evidence and remaining budget.

1. Follow the plan. Do not add features, alter architecture, or refactor unrelated files.
2. Complete and verify one task before starting the next dependent task.
3. Read existing owned files and follow project conventions. Do not add comments unless requested.
4. Report created, modified, and approved deleted files, tests, results, blockers, and safe rulings.
5. Keep changes uncommitted unless the human separately approves a commit.

### 4.1.2 — TDD Iron Law: Production Code Only

Do not write or change production behavior before observing a failing test for that behavior.

1. **Red:** Write a focused test. Run it and capture the actual failing assertion. Confirm it fails for the missing behavior, not a syntax error, missing dependency, import failure, or broken environment. A predicted failure or an unrun test is not Red.
2. **Green:** Write the minimum production code needed to pass. Run the same test and record its passing result.
3. **Refactor:** Clean up without changing behavior. Rerun the focused tests and relevant regression suite. Record a no-change decision if no refactor is needed.

Apply this law to production-code features, fixes, and behavior changes. Documentation-only tasks use structural checks, link and fence checks, and acceptance readback instead. Do not invent a failing production test for prose or claim structural checks prove runtime behavior. Configuration that changes runtime behavior still needs appropriate behavioral verification.

### 4.1.3 — Validator

Run project-defined syntax, typecheck, lint, unit tests, integration tests, and build commands as applicable. Discover commands rather than copying framework examples blindly. Record each result with:

- Evidence ID and time; task and attempt or fix round.
- Base and current revision plus uncommitted diff identity, such as content hashes of changed files.
- Absolute working directory, exact command, environment/tool version where relevant, and exit code.
- Actual output or a durable redacted output reference; test names, assertions, counts, and failures.
- Status: `PASS`, `FAIL`, `BLOCKED`, `NOT RUN`, or `N/A` with scope justification.

A missing tool, skipped required suite, permission failure, or unavailable service is not a pass. An exit code of zero with no required tests executed is not proof of success. Do not weaken assertions, remove required tests, or relabel them optional to clear a gate.

### 4.1.4 — Ordered Independent Reviews

Use fresh subagent reviewers by default. If unavailable, only the authorized human review replacement in Step 4.0.1 satisfies these same ordered gates and evidence requirements.

**Tier 1: Spec compliance reviewer.** Dispatch a fresh reviewer distinct from the implementer. Compare the actual diff with the approved task, Intent Brief, and plan. Check every functional requirement, non-functional constraint, owned-file boundary, missing behavior, and unplanned side effect. Cite implementation and test evidence. Return `APPROVED`, `CHANGES REQUIRED`, or `BLOCKED`.

**Tier 2: Quality/test reviewer.** Only dispatch after spec approval. Use a fresh reviewer distinct from the implementer and spec reviewer. Review design, readability, security, edge cases, regression risk, and whether tests prove the claims. Inspect actual code and outputs, not just the implementer's summary.

Record reviewer identity, actual model if known, reviewed revision/diff identity, findings, and verdict for each tier. After a fix, rerun affected checks and repeat spec review before quality/test review on the new state. A review of an older diff does not approve a newer one. Before accepting a task, read back all acceptance criteria against the saved evidence.

### 4.1.5 — Shared Fix Budget and Debugging

There is **one initial attempt plus up to 5 total fix rounds per task**. Build, test, spec review, and quality/test review share this count. They do not each receive five rounds. Expected Red is not a fix round; correcting an unintended failure is. A round starts when remediation begins and includes its revalidation and ordered reviews. Persist the counter before starting the round. Never reset it after a restart, phase change, reviewer change, or new failure category.

| Stage | Required action |
|-------|-----------------|
| Initial attempt | Implement, validate, and run ordered reviews; record round 0. |
| Fix rounds 1–3 | Investigate and apply a minimal evidence-backed correction. |
| Fix rounds 4–5 | Request an available higher-tier model and record the request and actual selection. If unavailable, record that fact and use a fresh reviewer at the available tier. Never pretend the model changed. If fresh review is also unavailable, report a blocker. |
| After 5 failed fix rounds | Stop task remediation and escalate to the human with evidence and options. No automatic sixth round. |

Use [Phase 5's four-phase debugging protocol](./05_VERIFICATION.md): root cause investigation, pattern analysis, hypothesis testing, then minimal fix implementation with regression verification. Retain prior failed hypotheses and outcomes.

Escalate security issues, scope changes, destructive actions, and missing permissions immediately. Do not wait for budget exhaustion. Budget exhaustion options include human diagnosis or a revised approved plan; never silently skip required work. Preserve the current diff and evidence. Do not automatically reset, clean, restore, stash, delete, or roll back the workspace.

This shared five-round policy reconciles legacy three-retry examples for this workflow. If a loaded governing policy still mandates three retries, surface the conflict and obtain explicit human resolution before exceeding it. Do not silently override a higher-priority rule.

### 4.1.6 — Rulings, Not Stalls

For a minor ambiguity, make a safe operational ruling only when it is reversible, within owned scope, and preserves the approved behavior and acceptance criteria. Record the question, evidence, alternatives, decision, rationale, affected files/requirements, impact on tests, cost and risk, and reversal path in the ledger. Continue with the smallest safe choice.

Security decisions, scope expansion, destructive operations, missing permissions, and changes to the approved brief are not safe rulings. Stop the affected action and ask the human. Rulings cannot waive required tests or approve deployment.

## Step 4.2 — Persistent Progress and Resume

The ledger must contain plan identity and approval, workspace/base/current revision, owned files, task dependencies and status, fresh agent identities, current fix round, evidence, ordered review verdicts, rulings with impact, blockers, and next exact action. Record each task as `PENDING`, `IN PROGRESS`, `BLOCKED`, or `ACCEPTED`; distinguish implementation complete from review accepted.

Before resuming, read the ledger and approved task, inspect git status and content identity, and compare the workspace with the last verified state. Revalidate changed or stale evidence. Resume the saved round and pending review, not a new budget. Do not infer completion from a checkbox without evidence.

## Step 4.3 — Commits and Branch Hygiene

Prepare an atomic changeset per completed task. **Commit, push, merge, deploy, and worktree deletion each require separate explicit human approval.** Approval of a plan or one action does not authorize the others. Creating a PR also requires explicit approval.

When a commit is approved, inspect status, staged/unstaged diffs, and recent history; stage only intended files and never secrets. Match the repository's message style. A conventional form, where used, is `<type>(<scope>): <description>` with `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, or `style`. Do not rewrite history or discard unrelated work for cleanliness. Record uncommitted delivery honestly.

## Step 4.4 — Context Health and Compaction

Monitor context capacity and reserve room for handoff. Near 70%, persist progress, outputs, pending reviews, rulings, and the remaining budget. Ask for explicit compaction approval when the harness supports that choice. After compaction or a new session, follow the resume checks above; do not rely on conversation memory.

## CHECKPOINT 2 — Implementation Review

```text
[SUMMARY] Accepted tasks X/Y; implemented but blocked tasks; files and tests changed.
[EVIDENCE] Ledger path, revision/diff identity, commands and outputs, ordered review verdicts.
[RISKS] Required failures, unavailable checks/reviewers, rulings and their impact.
[DECISION NEEDED] Approve Phase 5 verification, or identify tasks to revisit?
```

A milestone may be reviewed while other tasks remain blocked, but it is not whole-plan completion. Proceed to [Phase 5: Verification](./05_VERIFICATION.md) after Orchestrator approval. Required tests and review gates remain mandatory.
