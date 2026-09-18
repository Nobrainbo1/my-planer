---
name: test-driven-development
description: >-
  Verify intended behavior with a failing test before production changes. Use for
  /tdd, "write tests first", or "red green refactor".
---

# Test-Driven Development

This is an original local adaptation of the test-first workflow defined in [root rules](../../AGENTS.md), [Phase 4](../planner/references/04_IMPLEMENTATION.md), and [Phase 5](../planner/references/05_VERIFICATION.md); it is not an installed upstream package.

## Inputs and Boundaries

- Confirm explicitly approved intent and execution plan before implementation, code generation, or scaffolding. Invoking this skill does not approve either gate. Read the owning task and map its acceptance criteria to observable behavior.
- Confirm the permitted workspace, exact owned files, and existing task ledger. Request an approved alternative when workspace operations or ledger writes are outside permission. Preserve unrelated work.
- Read nearby tests and project configuration. Use existing test conventions and discover exact focused, regression, build, lint, and typecheck commands. Do not assume a framework or install missing tools automatically.
- Apply this protocol to production features, bug fixes, and behavior changes. Keep each cycle small enough to prove one intended behavior.

## Red: Observe the Intended Failure

1. Write a focused test that asserts the approved behavior through the relevant interface. Use controlled inputs and meaningful expected results. For a bug, reproduce the reported failure in a regression test.
2. Run the test before writing or changing production behavior. Capture the actual assertion and output. Confirm the failure demonstrates the missing or incorrect behavior, not a syntax error, missing tool or dependency, import failure, or broken environment.
3. If the test already passes, investigate whether the behavior exists or the test misses the requirement. Correct the test within approved scope and rerun it. Never invent a failure or break production code merely to manufacture Red.
4. If execution is blocked, record BLOCKED and resolve the prerequisite within permission before continuing. Predicted output, an unrun test, and a missing-tool failure do not satisfy Red.

Do not write production behavior until the intended assertion actually fails. If production changes were made first, disclose the sequence violation. Preserve work and agree on a safe recovery within scope; never delete or reset code automatically or claim retroactive TDD evidence.

## Green: Make the Smallest Passing Change

1. Change only the production code needed to satisfy the failing behavior. Do not add speculative features or unrelated cleanup.
2. Run the same focused test and observe its intended assertions passing. Record the actual result, not an expected result.
3. Run affected regression tests. An unexpected failure enters [systematic debugging](../systematic-debugging/SKILL.md), using the same task and remaining fix budget.

Never weaken assertions, remove required tests, replace meaningful checks with tautologies, or silently skip a required suite to obtain Green. A successful exit with zero required tests executed is not proof of success.

## Refactor: Preserve Behavior and Reverify

Improve structure only where needed without changing the approved behavior. If no cleanup is justified, record that decision. After any refactor, rerun focused and affected regression tests. New behavior requires a new Red cycle.

Run all required broader suites, build, lint, and typecheck fresh on the final candidate. Use [subagent-driven development](../subagent-driven-development/SKILL.md) for spec compliance review first, then a distinct quality/test reviewer. After fixes, rerun affected checks and repeat ordered reviews on the changed candidate. Passing a focused test does not replace integrated verification or human checkpoints.

## Documentation and Runtime Configuration

Documentation-only work uses frontmatter, heading, table, relative-link, and fence checks plus acceptance readback. Verify each document after writing before starting the next dependent item. Record manual checks as manual checks; do not invent Red/Green runtime evidence or claim document structure proves runtime behavior.

Configuration that changes runtime behavior still needs appropriate behavioral verification. A missing required environment or tool means BLOCKED, not a documentation exemption or a pass.

## Shared Fix Budget and Escalation

Allow one initial attempt plus at most **5 total fix rounds per task**, shared across build, test, spec review, and quality/test review. Expected TDD Red is not a fix round; correcting an unintended failure is. Persist the count when remediation begins, including revalidation and reviews. Carry it across cycles, skills, sessions, and phases; never reset it for a new failure category.

For rounds 4 and 5, request a higher-tier model if available. Record the request, availability, and actual selection. If unavailable, record that limitation and use a fresh reviewer at the available tier. Never claim an unavailable model switch or independent review. If fresh review is unavailable, apply only [Phase 4 §4.0.1](../planner/references/04_IMPLEMENTATION.md#401--canonical-fallback-when-fresh-agents-are-unavailable): two distinct named human reviewers, neither the implementer, spec first then quality/test only after spec approval. Record fallback authorization and each review's exact candidate, scope, evidence, and verdict. Acceptance remains BLOCKED until reviewers are available and both approvals and fallback authorization are recorded. Single-agent implementation approval does not authorize self-approval.

After 5 failed fix rounds, stop remediation and escalate with evidence, attempted hypotheses, risks, and 2 to 3 options with a recommendation. No automatic sixth round. Escalate security issues, scope changes, destructive actions, and missing permissions immediately, regardless of the remaining budget.

## Evidence and Completion

Use the approved existing ledger to record task, requirement, time, candidate content identity, absolute working directory, exact command, exit code, actual redacted output, test assertions, and executed/pass/fail/skipped counts. Preserve Red, Green, final regression evidence, fix rounds, review identities and verdicts, blockers, and the next exact action. Use PASS, FAIL, BLOCKED, NOT RUN, or justified N/A; missing checks are not passes.

Read back all acceptance criteria against fresh evidence. Report changed files, actual verification status, and the next decision. Distinguish implementation complete from review accepted. Preserve intent, plan, and phase approval gates. Commit, push, PR creation, merge, deployment, installation, and file or worktree deletion each require explicit permission. Never automatically reset, delete, or roll back work.
