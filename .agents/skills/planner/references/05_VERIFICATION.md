---
description: "Phase 5: Fresh evidence-based verification, requirement traceability, security gates, and four-phase debugging."
phase: 5
checkpoint: true
---

# Phase 5: Verification & Quality Assurance

> **Goal:** Validate the whole implementation against the approved Intent Brief and Definition of Done. Task-level success is not proof that the integrated system works.

Use [the verification report](../resources/templates/verification_report.md). Preserve evidence in that report and the [task ledger](../resources/templates/task_execution_log.md). Report facts, not confidence or expected results. If the Phase 4 canonical fallback was used, record it in the verification report.

## Step 5.1 — Fresh Full-Suite Execution

1. Confirm Phase 4 approval, task acceptance, and completion of required documentation. Read the authoritative artifact paths from the plan. Record workspace, base/current revision, deliverable file set and exact content identity, and separate mutable evidence paths under the [Phase 4 candidate identity contract](./04_IMPLEMENTATION.md#candidate-identity-contract). Finalize any evidence snapshots that must ship before final checks. Record tool versions and relevant environment settings without secrets.
2. Discover the project's actual commands from its manifest, CI configuration, and documentation. Identify all required suites from the approved brief. Do not assume a framework, install tools without permission, or silently narrow the suite.
3. Run broad unit, integration, and end-to-end suites fresh on the delivery candidate, not only tests touched by the task. Run the build, lint, typecheck, and other required gates too. Cached summaries, old CI runs, watch-mode results from another revision, and an implementer's statement are not fresh verification.
4. Capture evidence per command: time, revision and diff identity, absolute cwd, exact command, exit code, actual output or durable redacted output reference, test names, executed/pass/fail/skipped counts, and measured coverage if produced.
5. After any fix, rerun the failed check and affected regression tests, repeat spec review then quality/test review, and run the broad required suites fresh again on the final state. Link new evidence to the superseded run.

| Status | Meaning |
|--------|---------|
| PASS | Required assertions actually executed and passed on the recorded candidate. |
| FAIL | A check ran and reported a failure. |
| BLOCKED | Required execution cannot proceed because of environment, access, tools, or services. |
| NOT RUN | No execution evidence exists; give the reason and next action. |
| N/A | Outside the approved scope, with evidence and explicit applicability rationale. Not a waiver. |

Required tests are never waived. Required skipped, blocked, or unrun tests prevent readiness. A successful process exit with zero required tests executed is not a pass. Do not weaken assertions, quarantine failures, or reduce coverage to clear a gate. A failure labelled “warning” is still a blocker when it belongs to a required test or check.

For documentation-only changes, validate frontmatter, headings, tables, fenced blocks, relative links, and acceptance criteria structurally. Record manual readback and its limitations. Do not fabricate Red/Green evidence or claim document checks prove runtime behavior. Existing runtime requirements remain required if the change affects them.

## Step 5.2 — Code Quality Scan

Run the configured linter, formatter in check mode, and type checker. Record commands, exit codes, output, errors, and warnings. Review complexity hotspots, large files, dead code, naming, and maintainability. Changes must follow existing conventions and remain within approved file scope. Do not add comments or extra documentation unless requested.

If a required tool is unavailable, mark the check BLOCKED and request the needed permission or command. Do not present a manual approximation as a passing tool run.

## Step 5.3 — Security Audit

Use the approved brief's security thresholds, not a looser default invented during delivery. If thresholds are missing or contradictory, ask the human before readiness. A brief requiring zero known vulnerabilities is stricter than a generic “no critical/high” rule and must remain so.

Record dependency audit and secret-scan tools, versions, commands, output, vulnerability identifiers, severity, affected packages/files, fixes, and evidence. Do not expose secrets in the report or send private code to an external service without authorization.

Review applicable controls:

- No hardcoded secrets; credentials stay outside tracked code.
- Input validation and parameterized database queries.
- Output encoding, cross-site scripting prevention, and CSRF protection where relevant.
- Authentication and authorization, including negative access tests.
- Sensitive data protection at rest and in transit.
- User-facing errors do not expose internal details.

Escalate security findings immediately. Only **nonblocking advisories** may remain documented, and only with explicit human acceptance within the approved brief's security thresholds. Record the finding, evidence, rationale, impact, owner, follow-up date, approver, and approval reference. Human acceptance of an advisory does not waive a required test, security gate, or threshold. If the brief forbids the finding, remediation is required.

## Step 5.4 — Performance Validation

For each applicable non-functional requirement, record the approved target, workload, environment, measurement command, actual result, and evidence. Do not treat example targets as requirements.

| Metric | Approved target / NFR | Actual | Evidence | Status |
|--------|-----------------------|--------|----------|--------|
| API latency p50 / p99 | [target] | [measurement] | [ID] | [status] |
| Page load / memory / bundle size | [target] | [measurement] | [ID] | [status] |
| Load scenario / throughput | [workload and target] | [measurement] | [ID] | [status] |

Use only authorized test environments and loads. Missing infrastructure for a required benchmark means BLOCKED, not N/A or PASS.

## Step 5.5 — Functional Requirement to Test Matrix

Map **every functional requirement** in the approved `INTENT_BRIEF.md`, not only Must Have items. Cite the exact test case or assertion and fresh run evidence, not just a test filename or coverage percentage.

| FR ID / approved requirement | Implementation path:line | Test case / assertion | Fresh run evidence | Result / gap |
|------------------------------|--------------------------|-----------------------|--------------------|--------------|
| FR-01 / [behavior] | [path:line] | [test ID and assertion] | [E-ID] | [PASS / gap] |
| FR-02 / [behavior] | [path:line or missing] | [test ID or missing] | [E-ID or absent] | [FAIL / BLOCKED / NOT RUN] |

Any in-scope requirement without passing proof blocks readiness. Explicitly out-of-scope items must cite the approved brief and remain visible as excluded, not satisfied. Changing a priority label or recording a safe ruling does not remove an acceptance obligation. Documentation requirements map to structural checks and readback evidence instead of invented runtime tests. Track non-functional requirements and DoD items with the same evidence discipline.

### Output and Trajectory Evaluation

For nondeterministic agent behavior, run the evaluation cases and rubric defined in the approved plan alongside deterministic tests. Output evaluation checks the final result against requirements. Trajectory evaluation checks observable actions: tool calls, permissions, required checks, source use, stopping conditions, and resource limits. Use recorded events and concise decision records, not private model reasoning. A plausible answer with unauthorized actions or skipped required checks fails the applicable process criterion.

Record case-set and rubric revisions, model/configuration, number of trials, pass thresholds, actual results, and redacted evidence. Include representative normal, boundary, and failure cases. Obtain permission for live calls or sensitive data transfer; blocked required evaluations prevent readiness. Group failures by cause, improve only approved prompts/tools/code, and rerun affected evaluations and regressions. For planning-only or documentation work, use an explicit artifact-review rubric and mark runtime evaluations N/A with a scope reason; never simulate human approval to satisfy it.

## Step 5.6 — Four-Phase Systematic Debugging

For any unexpected build, test, review, or environment failure, follow these phases in order. Persist evidence and hypotheses in the task's existing ledger.

1. **Root Cause Investigation:** Reproduce with the exact command and environment. Read the full error and stack trace. Inspect recent changes and trace data across affected boundaries. Record actual versus expected behavior. If reproduction is blocked, preserve that fact; do not guess a fix.
2. **Pattern Analysis:** Compare with working code and documented contracts. Identify differences, dependencies, and affected layers. Explain why the working case differs before copying a solution.
3. **Hypothesis Testing:** State one falsifiable cause, its evidence, and a predicted result. Change or inspect one variable in a safe isolated experiment. Run it and record the observation. Reject unsupported hypotheses rather than stacking speculative fixes.
4. **Fix Implementation:** Add or correct a regression test and observe its actual failing assertion before production code changes. Apply the smallest root-cause fix, run Green, refactor without behavior change, and rerun affected tests plus the fresh broad suites. For documentation, use structural regression checks instead. Repeat ordered reviews after the fix.

Remediation consumes the [Phase 4 shared budget](./04_IMPLEMENTATION.md): one initial attempt plus up to 5 total fix rounds per task across build, test, and both reviews. Resume the existing count even when a Phase 5 or whole-branch review reopens a task. Attribute new cross-task findings to an owning task; ask for a new approved task for genuinely new scope, never rename a failure to reset its budget.

Request a higher-tier model for rounds 4–5 if available. Record actual availability and selection. If unavailable, record it and use a fresh reviewer without pretending the model changed. If fresh review is unavailable, mark it BLOCKED. After 5 failed fix rounds, stop and escalate to the human with evidence and 2–3 options. Security, scope, destructive actions, and missing permissions require immediate escalation, not a delayed fifth-round decision. Never use automatic destructive rollback.

## Step 5.7 — Definition of Done and Verdict

- [ ] Every in-scope functional requirement has passing fresh evidence.
- [ ] All required unit, integration, end-to-end, and regression tests ran and passed.
- [ ] Build, lint, typecheck, and formatting meet the approved gates.
- [ ] Security and secret checks meet the approved brief's thresholds.
- [ ] Performance targets have measured evidence where required.
- [ ] Required documentation, change log, and interfaces are accurate and in scope.
- [ ] Spec review approved before quality/test review on the final state.
- [ ] All fixes were revalidated; stale evidence is clearly superseded.
- [ ] Only nonblocking advisories remain, with qualifying human acceptance.
- [ ] Ledger, FR matrix, approvals, and unresolved issues are current.

Summarize each category with status, evidence IDs, executed counts, and blockers. Use `READY FOR DELIVERY`, `NEEDS REMEDIATION`, or `BLOCKED`. Do not default a template to success. No required failure, missing evidence, or unaccepted review may be hidden in an advisory list.

Request Orchestrator approval of the summary before [Phase 6: Delivery](./06_DELIVERY.md). Readiness and transition approval do not authorize commit, push, merge, deployment, or worktree deletion.
