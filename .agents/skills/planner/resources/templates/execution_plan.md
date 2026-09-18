---
description: "Reusable Execution Plan template. Generated during Phase 2 Planning."
type: template
---

# Execution Plan — [Project/Feature Name]

> **Date:** [YYYY-MM-DD]
> **Output:** `EXECUTION_PLAN.md` at the target project root
> **Target project root:** [exact path]
> **Scope:** Spike / One-Shot / Project
> **Intent Brief:** `INTENT_BRIEF.md` [approved revision] at the target project root
> **Domain glossary:** `CONTEXT.md` at the target project root
> **Plan ID and revision:** [stable ID and revision]
> **Status:** Draft / In Review / Approved / Blocked

## Authoring and Execution Rules

Write for an engineer with zero codebase context. Replace every execution placeholder with exact paths, complete proposed code or diffs, commands, and acceptance criteria before approval. Execution evidence remains `Not run` until actually observed. Use target-project-relative file paths; specify the shell and exact working directory for each command. Template source links resolve within the planner skill: [intent brief](./intent_brief.md), [domain glossary](./context_template.md), and [ADR](./adr_template.md). Never fill in the shipped original. Rewrite every copied local link, including the later Phase 4 fallback link, relative to the generated output file. Use exact target-project artifact names and the actual installed workflow-policy location. Verify each target and heading before approval; do not assume the skill is installed inside the target project.

The agent gathers facts from repository files and tools. Record sources below; do not ask the human to look them up. Match detail to scope and mark irrelevant architecture sections N/A with a reason. Apply DRY (Don't Repeat Yourself) by reusing existing behavior and contracts. Apply YAGNI (You Aren't Gonna Need It) by excluding speculative features and abstractions.

**Hard gate:** Both `INTENT_BRIEF.md` and this `EXECUTION_PLAN.md` need explicit human approval before any implementation, generated implementation code, scaffold, automated agent application, or throwaway Spike. Draft code blocks are review material only. Silence, mode selection, and ADR acceptance are not approval. Material scope or design changes require renewed approval. Separate install, deletion, schema, and deployment permissions still apply.

For a Spike, specify the hypothesis, timebox, experiment, pass/fail criteria, and disposal plan. Do not execute the experiment before dual approval. Final delivery DoD does not apply before discovery or planning can finish.

## Observed Context and Command Inventory

| Fact or Convention | Exact Source Path and Symbol | Observed Value or Evidence | Uncertainty |
|--------------------|------------------------------|----------------------------|-------------|
| [existing implementation, dependency, or contract] | [path and anchor] | [observed fact] | [none or blocker] |

| Check | Exact Command | Shell | Working Directory | Prerequisites and Source | Expected Result |
|-------|---------------|-------|-------------------|--------------------------|-----------------|
| Focused test | [actual project command] | [shell] | [exact directory] | [script/CI source and setup] | [test name and pass condition] |
| Regression tests | [actual command] | [shell] | [directory] | [source] | [suite and expected exit code] |
| Lint | [actual command or unavailable] | [shell] | [directory] | [source or blocker] | [expected exit code] |
| Typecheck | [actual command or unavailable] | [shell] | [directory] | [source or blocker] | [expected exit code] |
| Build | [actual command or N/A with reason] | [shell] | [directory] | [source] | [expected result] |

Discover commands from project scripts, configuration, or CI. Do not assume tools are installed or silently install them. An unavailable check is blocked, not passed; record the agreed alternative and approval before execution.

---

## Architecture

### System Narrative
[Plain-English description of how the system works end-to-end]

### Component Diagram
```
[ASCII diagram or mermaid code block]
```

### Tech Stack

| Layer | Technology | Version | Rationale |
|-------|-----------|---------|-----------|
| [e.g., Frontend] | [e.g., React] | [e.g., 19.x] | [Why this choice] |
| [e.g., Backend] | [e.g., FastAPI] | [e.g., 0.115] | [Why this choice] |
| [e.g., Database] | [e.g., PostgreSQL] | [e.g., 16] | [Why this choice] |
| [e.g., AI/LLM] | [observed or proposed provider/package] | [exact version] | [evidence and rationale] |

### Dependency Graph
[Module-to-module interaction map, including third-party dependencies]

### Code Interaction Map
[Which functions call which, which components render which, which services talk to which]

---

## Architecture Decisions

Use frontier rounds of 1 to 3 human decision questions. Give each question at most 2 to 3 viable options and a plain-text `Recommendation:` with a reason. Collect technical facts first; keep resolved vocabulary in `CONTEXT.md` and architecture choices here.

| Decision | Options and Trade-offs | Recommendation and Human Decision | Evidence |
|----------|------------------------|-----------------------------------|----------|
| [decision ID] | [viable alternatives] | [recommendation; actual answer or pending] | [source paths or decision reference] |

Create `docs/adr/000X-<slug>.md` only if all three gates are Yes with evidence. If any is No or unknown, retain lightweight rationale here and do not create an ADR. Reserve a unique exact ADR number/path.

| Decision | Hard to Reverse: Yes/No + Evidence | Surprising Without Context: Yes/No + Evidence | Real Trade-off: Yes/No + Rejected Alternatives | ADR Path or No-ADR Rationale |
|----------|------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------|
| [decision ID] | [concrete reversal cost] | [why a future developer would question it] | [viable alternatives and sacrificed benefits] | [exact path only if all three pass; otherwise reason] |

## File Change Plan

| Action | Exact File Path and Anchor | Owning Task | Readers and Writers | Description | Separate Permission Required |
|--------|----------------------------|-------------|---------------------|-------------|------------------------------|
| [CREATE / MODIFY / DELETE] | [target-project-relative path and symbol] | [task ID] | [task IDs and access mode] | [exact change] | [permission and evidence, or none] |

---

## Task Breakdown

Retain Foundation, Core Features, and Integration groups when useful, but split them into one-behavior tasks. Each action should normally take 2 to 5 minutes. An effort label does not replace executable detail. Repeat the task card below for every task.

| Task ID | Group | Requirement IDs | Behavior | Dependencies | Read Files | Write Files | Action Estimates |
|---------|-------|-----------------|----------|--------------|------------|-------------|------------------|
| T-01 | [Foundation / Core Features / Integration] | [FR/NFR IDs] | [one testable behavior] | [IDs or none] | [exact paths] | [exact paths] | [minutes per action] |

### Task T-01 — [One Testable Behavior]

- **Requirement and acceptance:** [ID; Given/When/Then criteria, including relevant edge case]
- **Dependencies:** [completed task IDs and evidence needed, or none]
- **Implementer and workspace:** [fresh implementer identity/role; exact branch/worktree or workspace path]
- **Read first:** [exact paths, symbols or line anchors, fixtures, conventions, and contracts]
- **Owned changes:** [exact test and production paths; create/modify/delete; replacement anchors]
- **Do not touch:** [explicit ownership boundaries]
- **Prerequisites:** [existing dependencies, configuration, permissions, and setup]
- **Shell and working directory:** [exact shell and directory]
- **Ledger:** [exact target-project-relative progress path; no unresolved plan ID]
- **Spec reviewer:** [identity/role; requirement, plan, and diff inputs]
- **Quality/test reviewer:** [different identity/role; code, tests, conventions, and evidence inputs]

#### 1. Red — Add the Test and Observe the Failure

**Test path and insertion/replacement anchor:** [exact path and symbol]

```text
[Replace with the complete proposed test code or exact diff, including imports, fixture setup, and assertions. Use the appropriate code fence language in the filled plan.]
```

**Run:**

```text
[Exact focused test command; shell and working directory stated above]
```

- **Expected failure:** [test name, assertion, expected/actual difference, and why behavior is missing]
- **Actual evidence:** Not run. [At execution: timestamp, command, working directory, exit code, failing assertion/output, and evidence path]
- **Red gate:** Run the test and observe the intended behavior failure before writing production code. Syntax errors, missing imports, broken setup, or unrelated failures do not count. If it passes unexpectedly, investigate whether behavior already exists or the test is wrong; do not invent a failure.

For documentation-only tasks, replace the runtime test with an exact structural/content acceptance check. Capture the real pre-change failure and post-change result. If automation is unavailable, agree on a review-based alternative before execution and label it honestly.

#### 2. Green — Make the Minimum Change

**Production path and insertion/replacement anchor:** [exact path and symbol]

```text
[Replace with the complete minimal production code or exact diff. Reuse existing utilities; exclude unrelated features and speculative abstractions.]
```

**Run:**

```text
[Exact same focused test command used for Red]
```

- **Expected result:** [focused tests pass; exact expected exit code]
- **Actual evidence:** Not run. [At execution: timestamp, command, directory, exit code, relevant passing output, and evidence path]
- **Green gate:** Stop and investigate if the focused test still fails. Do not hide failures or weaken assertions to force a pass.

#### 3. Refactor — Clean Up Without Changing Behavior

**Cleanup and affected paths:** [exact proposed cleanup diff/block, or explicitly no cleanup with a reason]

```text
[Exact focused test command]
[Exact relevant regression command]
[Exact lint command]
[Exact typecheck command]
```

State a shell and working directory for any command that differs from the task defaults. Resolve unavailable checks before approval; do not put guessed commands in the final plan.

- **Expected result:** [all applicable checks pass without behavior changes]
- **Actual evidence:** Not run. [At execution: timestamp, each command, exit code, output summary, and evidence path]
- **Refactor gate:** Verify even when no cleanup is needed. Return to investigation for any regression.

#### 4. Review, Fix, and Record

| Order | Reviewer | Acceptance | Verdict | Findings and Fix Round | Evidence |
|-------|----------|------------|---------|------------------------|----------|
| 1 | [spec compliance reviewer] | All requested behavior or documentation structural criteria; no scope additions; exact approved paths/contracts | Pending | [findings and resolution] | [review record and requirement/test or structural-check mapping] |
| 2 | [quality and test reviewer] | Maintainable minimal code; DRY/YAGNI; meaningful tests; actual Red/Green/Refactor evidence, or documentation structural equivalent with runtime N/A reason | Pending | [findings and resolution] | [review record and fresh verification or structural readback output] |

Run spec review before quality review. Fix findings and rerun affected checks and reviews before completion. If subagent reviews are unavailable, use only the [Phase 4 canonical fallback](../../references/04_IMPLEMENTATION.md#401--canonical-fallback-when-fresh-agents-are-unavailable). Record human authorization and two distinct named human reviewers, neither the implementer, with exact candidate, scope, evidence, and verdict for each ordered review. Missing either approval blocks acceptance; self-review is never independent review. Follow the active workflow retry limits and record every fix round and escalation.

**Task acceptance:** [ ] Observed Red failure, Green pass, and Refactor/regression verification, OR documentation-only structural equivalent with observed pre-change defect, post-change check/readback evidence, and runtime checks marked `N/A` with a scope reason; [ ] Spec accepted; [ ] Quality/tests or documentation quality accepted; [ ] Ledger updated. Both ordered review approvals remain mandatory for either path. Predictions and unchecked evidence fields do not count as completion.

## Execution Ledger and Resume Contract

- **Original target root / execution workspace:** [separate absolute paths; branch/worktree identity]
- **Authoritative artifact map:** [brief, glossary, plan, ledger, verification report; each absolute path, owner, and approved write permissions]
- **Copy or relocation handling:** [verify permitted copies against approved revision/content identity; keep copies non-authoritative; record authorized relocation and update all entry points]
- **Deliverable file set / candidate identity:** [approved base, exact paths including additions/deletions, and content/diff identity; current HEAD recorded separately]
- **Mutable evidence locations:** [explicit approved ledger/report/approval paths excluded from deliverable identity, not from accuracy/security inspection]
- **Delivery snapshot finalization:** [artifacts that must ship, owner, freeze point before final checks/reviews, and separate approved location for later verdicts; or none]
- **Ledger path:** [exact target-project-relative path and its authoritative absolute resolution, for example `.superpowers/sdd/feature-name/progress.md`]
- **Approved intent/plan revisions and evidence:** [revisions; approver; date; approval reference]
- **Workspace isolation:** [branch/worktree/path and integration owner; any single-agent fallback requires explicit human approval and covers implementation only, never approval of the implementer's own work; use the Phase 4 canonical fallback above]

Update the authoritative ledger after every action and review, not only at task completion. Pass absolute artifact paths to every fresh agent. A new worktree does not inherit uncommitted planning files; verify access to authoritative artifacts before dispatch. Copies remain non-authoritative unless an authorized relocation is recorded. Verify recorded state against the working tree and rerun stale checks; never infer completion from chat history.

Use the Phase 4 candidate identity contract: routine updates to separately listed mutable evidence do not change deliverable identity, but remain traceable and subject to accuracy, scope, and secret checks. Never exclude intended deliverables. If an artifact must ship, freeze its contents into the candidate before final verification and ordered reviews, and store later verdicts in the separate approved evidence location. Any edit to a frozen deliverable requires revalidation and ordered review. Requirement or design changes still require renewed approval.

Include required documentation and change log work as owned Phase 4 tasks, completed before final Phase 5 verification.

| Task | State | Implementer and Workspace | Last Action | Red/Green/Refactor Evidence | Spec Verdict | Quality Verdict | Blocker | Next Action |
|------|-------|---------------------------|-------------|----------------------------|--------------|-----------------|---------|-------------|
| T-01 | Not started | [identity/path] | None | Not run | Pending | Pending | [none or blocker] | [exact next step] |

| Date | Task | Operational Ruling or Plan Defect | Evidence and Impact | Authority or Approval | Follow-up |
|------|------|----------------------------------|---------------------|-----------------------|-----------|
| [date] | [ID] | [minor ambiguity and safe ruling] | [scope, files, contracts, risks] | [existing authority or renewed approval] | [next action] |

Minor rulings cannot change scope, bypass a gate, or authorize restricted actions. Stop affected work and request approval for material changes. Keep this ledger out of `CONTEXT.md`.

---

## Data Flow

### Primary User Flow
1. [Step 1 — user action → function in file]
2. [Step 2 — function calls API endpoint]
3. [Step 3 — handler validates and processes]
4. [Step 4 — service layer business logic]
5. [Step 5 — data persisted to database]
6. [Step 6 — response returned to user]

### Interface Contracts
```
[API signatures, type definitions, database schemas]
```

---

## Edge Case Analysis

| Boundary/Component | Edge Case | Expected System Behavior |
|-------------------|-----------|--------------------------|
| [e.g., API Input] | [e.g., Malformed JSON payload] | [e.g., Return 400 Bad Request with precise schema errors] |
| [e.g., Database]  | [e.g., Connection timeout]     | [e.g., Retry 3x with backoff, then 503] |

---

## Risk Register

| ID | Risk | Likelihood | Impact | Mitigation |
|----|------|-----------|--------|------------|
| R-01 | [risk] | [L/M/H] | [L/M/H] | [mitigation] |

---

## Test Strategy

| Category | Tool | Scope | Target Coverage |
|----------|------|-------|-----------------|
| Unit | [tool] | [what] | [X%] |
| Integration | [tool] | [what] | [X%] |
| E2E | [tool] | [what] | [key flows] |
| Security | [tool] | [what] | [all endpoints] |

### Agent Evaluation Plan, When Applicable

For nondeterministic behavior, define output and trajectory evaluation before execution. For ordinary deterministic work or planning-only artifacts, record the applicable tests or manual rubric instead; no agent runtime is required.

- **Case set and revision:** [representative normal, boundary, and failure cases; expected outcomes]
- **Output rubric and pass threshold:** [correctness, grounding, completeness, or other approved criteria]
- **Observable trajectory criteria:** [permitted tools/data, required checks, approval and stopping behavior; no private reasoning required]
- **Trial count / model and configuration / time and cost limits:** [approved values; do not infer reliability from one demo]
- **Method and permissions:** [actual command or exact manual procedure, dependencies, live-call/data permissions, and evidence destination]
- **Failure and regression handling:** [owning task, cause grouping, approved repair scope, and rerun criteria]
- **Planning-only status:** [runtime checks NOT RUN or N/A with reason; actual human approvals remain pending until received]

---

## Deployment & Migration

### Migration Plan
[Data migration steps, state transfers, API version deprecation strategy]

### Rollback Strategy
[How to revert these changes safely in production if something fails]

---

## Preflight Conflict Scan

Run before plan approval, immediately before execution, and after task, ownership, or contract changes. Inspect current work by other agents as well as this plan. Unresolved findings block approval and dispatch.

- **Plan revision, scan date, and reviewer:** [revision; timestamp; identity]
- **Topological task order:** [exact ordered task IDs; no missing, self-referencing, or cyclic prerequisites]
- **Parallel groups:** [only collision-free tasks with satisfied dependencies; otherwise sequential]

| Check | Evidence Inspected | Finding | Owner and Resolution | Rescan Evidence | Status |
|-------|--------------------|---------|----------------------|-----------------|--------|
| File access collisions | [read/write sets, shared configuration, generated files, lockfiles, active agent ownership] | [overlapping writes or read/write hazards] | [serialize, assign one owner, or isolate with integration task] | [actual rescan result] | Not run |
| Contract discrepancies | [producer/consumer signatures, types, schemas, errors, versions, fixtures, glossary terms] | [mismatch or none] | [agreed exact contract and all affected tasks updated] | [actual rescan result] | Not run |
| Circular dependencies | [task prerequisites and module graph] | [cycle, missing dependency, self-reference, or none] | [break cycle and validate topological order] | [actual rescan result] | Not run |

Listing conflicts is not a pass. Resolve and rescan each one. Workspace isolation does not fix incompatible contracts.

## Evidence and Delivery Acceptance

| Requirement ID | Acceptance Criterion | Task and Test/Check | Actual Result | Evidence Path and Timestamp | Reviewer |
|----------------|----------------------|---------------------|---------------|-----------------------------|----------|
| [FR/NFR ID] | [observable condition] | [task ID; exact test/check] | Not run | [record only after execution] | [identity] |

Record fresh focused, regression, lint, typecheck, build, and applicable security results with exact commands, directories, timestamps, exit codes, and relevant output. Redact secrets. Report unavailable checks and failures; never equate expected output with observed evidence. The final DoD from `INTENT_BRIEF.md` is a delivery-only gate, not a prerequisite for completing discovery or planning.

## Approval

- [ ] Intent scope is explicitly approved; blocking questions are resolved and non-blocking deferrals have owners and impact.
- [ ] Every task has exact paths, proposed code/diffs, commands, prerequisites, reviewers, and a ledger path; no unresolved execution placeholders remain.
- [ ] All-three ADR gates are recorded; only qualifying decisions have ADRs.
- [ ] Preflight has actual evidence and no unresolved collisions, contract discrepancies, or cycles.
- [ ] Orchestrator explicitly approved this exact plan revision.

| Artifact | Approved Revision | Approver | Date | Status | Explicit Approval Message or Reference |
|----------|-------------------|----------|------|--------|----------------------------------------|
| INTENT_BRIEF.md | [revision] | [human] | [date] | Pending | [evidence] |
| EXECUTION_PLAN.md | [revision] | [human] | [date] | Pending | [evidence] |

Approval checks concern planning readiness, not completed implementation. Runtime evidence stays `Not run` until execution. Recheck both approvals and preflight before generating or applying any implementation, including Spike code. A checked box alone is not approval evidence.
