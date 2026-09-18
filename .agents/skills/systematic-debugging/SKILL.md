---
name: systematic-debugging
description: >-
  Investigate failures with evidence before fixing their cause. Use for /debug,
  "systematic debugging", or "fix test failure".
---

# Systematic Debugging

This is an original local adaptation of the four-phase workflow defined in [root rules](../../AGENTS.md), [Phase 4](../planner/references/04_IMPLEMENTATION.md), and [Phase 5](../planner/references/05_VERIFICATION.md); it is not an installed upstream package.

## Inputs and Boundaries

- Confirm explicitly approved intent and execution plan before implementation, code generation, or scaffolding. A debugging request does not waive either gate. Read the owning task, acceptance criteria, relevant code, and existing evidence.
- Confirm the permitted workspace, exact owned files, and existing task ledger. If workspace operations or ledger writes are outside permission, request an approved alternative; do not create files elsewhere.
- Discover actual validation commands and available tools from project configuration. Never assume a framework or install a missing tool automatically.
- Preserve unrelated work. Escalate security issues, scope changes, destructive actions, and missing permissions immediately. Do not wait for the retry limit.

## Four Phases

### 1. Reproduce and Collect Evidence

Run the smallest reliable reproduction in the permitted environment. Record the exact command, inputs, expected result, actual result, and full relevant error or stack trace. Redact secrets. Inspect relevant changes and trace data across affected boundaries.

If reproduction is intermittent, record its frequency and conditions. If blocked, state the missing evidence and next diagnostic action. Do not guess a production fix from an unconfirmed symptom.

### 2. Compare Patterns

Find a working case and the applicable documented contract. Compare inputs, dependencies, configuration, and affected layers. List meaningful differences and explain why each could matter. Understand the working pattern before copying it; resemblance alone is not evidence of a cause.

### 3. Test One Falsifiable Hypothesis

State one proposed cause, supporting evidence, and a predicted observation that could prove it wrong. Inspect or vary one factor in a safe isolated experiment. Observe the result and record whether it supports or rejects the prediction.

Retain rejected hypotheses and results. Return to investigation when evidence is insufficient. Do not stack speculative patches. Experiments must respect ownership and approval limits; production behavior still requires observed test Red first.

### 4. Apply the Minimal Fix and Verify

For production behavior, add or correct a focused regression test and run it before changing production code. Capture the actual intended failing assertion. A missing tool, import error, syntax error, unrun test, or predicted failure is not Red.

Apply the smallest correction to the supported root cause. Run the same test to observe Green. Refactor only without changing behavior, then rerun focused and affected regression tests. Run all required broad suites, build, lint, and typecheck fresh on the final candidate. Never weaken assertions or remove required tests to pass.

For documentation-only changes, use structural regression checks, relative-link and fence checks, and acceptance readback. Do not invent runtime tests or claim these checks prove runtime behavior. Configuration that changes runtime behavior still needs behavioral verification.

Repeat spec compliance review before quality/test review under [subagent-driven development](../subagent-driven-development/SKILL.md). Reviews must cover the changed candidate, not an older state.

## Shared Fix Budget

One initial attempt is followed by at most **5 total fix rounds per task**, shared across build, test, spec review, and quality/test review. Expected TDD Red is not a fix round; remediation of an unintended failure is. Persist the count when remediation starts, including its revalidation and reviews. Resume that count across sessions, phases, and skill changes; never reset it by renaming a failure.

For rounds 4 and 5, request a higher-tier model if available. Record the request, availability, and actual selection. If unavailable, record the limitation and use a fresh reviewer at the available tier. Never claim an unavailable model switch or independent review. If fresh review is unavailable, apply only [Phase 4 §4.0.1](../planner/references/04_IMPLEMENTATION.md#401--canonical-fallback-when-fresh-agents-are-unavailable): two distinct named human reviewers, neither the implementer, spec first then quality/test only after spec approval. Record fallback authorization and each review's exact candidate, scope, evidence, and verdict. Acceptance remains BLOCKED until reviewers are available and both approvals and fallback authorization are recorded. Single-agent implementation approval does not authorize self-approval.

After 5 failed fix rounds, stop remediation and escalate with evidence, attempted hypotheses, remaining risks, and 2 to 3 options with a recommendation. No automatic sixth round. Immediate security, scope, destructive-action, and permission escalation takes precedence over this budget.

## Evidence and Completion

Persist each hypothesis, experiment, fix round, and check in the approved existing ledger. Record time, task, candidate content identity, absolute working directory, exact command, exit code, actual redacted output, and executed/pass/fail/skipped counts where applicable. Use PASS, FAIL, BLOCKED, NOT RUN, or justified N/A. Missing checks and zero required tests executed are not passes.

Read back every acceptance criterion against fresh evidence. Distinguish a verified fix from a task awaiting independent review or human approval. Report changed files, actual verification status, and the next decision. Preserve phase checkpoints. Commit, push, PR creation, merge, deployment, installation, and file or worktree deletion each require explicit permission. Never automatically reset, delete, or roll back work.
