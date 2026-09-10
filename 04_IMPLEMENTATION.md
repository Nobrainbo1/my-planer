---
description: "Phase 4: Implementation. The Builder-Validator loop where agents write, test, and self-correct code against the approved Execution Plan."
phase: 4
checkpoint: true
---

# Phase 4: Implementation — Builder-Validator Loop

> **Goal:** Execute the approved Execution Plan from Phase 2 using the tools assembled in Phase 3. Code is written iteratively using the **Builder-Validator** pattern with **Actor-Critic** self-correction.

> **Paper Concept:** *"The Builder-Validator Chain"* — A deterministic structure where an agent's output is immediately verified by a secondary specialized test or automated test suite. The agent writes code, attempts to build, runs tests, and self-corrects up to a retry limit before escalating.

---

## Step 4.0 — Pre-Implementation Checklist

Before writing any code, verify:

```markdown
### Pre-Implementation Gate

- [ ] Intent Brief (Phase 1) is finalized and approved.
- [ ] Execution Plan (Phase 2) is approved by Orchestrator.
- [ ] Harness is configured with all required tools (Phase 3).
- [ ] Development environment is set up and functional.
- [ ] Version control is initialized (git init, .gitignore configured).
- [ ] Branch strategy is clear (e.g., feature branches off main).
```

---

## Step 4.1 — Task Execution Protocol

For each task in the Execution Plan, follow this protocol:

```
┌──────────────────────────────────────────────────────┐
│                    TASK T-XX                          │
├──────────────────────────────────────────────────────┤
│                                                      │
│  ┌──────────┐                                        │
│  │  BUILDER  │  ← Write code per plan                │
│  └────┬─────┘                                        │
│       │                                              │
│       ▼                                              │
│  ┌──────────┐                                        │
│  │ COMPILE  │  ← Does it build?                      │
│  └────┬─────┘                                        │
│       │ No → Self-correct (up to 3 retries)          │
│       │ Yes ↓                                        │
│       ▼                                              │
│  ┌──────────┐                                        │
│  │   TEST   │  ← Do tests pass?                      │
│  └────┬─────┘                                        │
│       │ No → Self-correct (up to 3 retries)          │
│       │ Yes ↓                                        │
│       ▼                                              │
│  ┌──────────┐                                        │
│  │  CRITIC  │  ← Does it meet the spec?              │
│  └────┬─────┘                                        │
│       │ No → Refine and re-enter Builder              │
│       │ Yes ↓                                        │
│       ▼                                              │
│  ┌──────────┐                                        │
│  │   DONE   │  ← Mark task complete, log changes     │
│  └──────────┘                                        │
│                                                      │
│  After 3 failed retries at any stage:                │
│  ⚠️ ESCALATE to Orchestrator                         │
└──────────────────────────────────────────────────────┘
```

### 4.1.1 — Builder (Actor)

The Builder's job is to **write code** that implements one task from the Execution Plan.

**Rules for the Builder:**
1. **Follow the plan.** Do not add features, refactor unrelated code, or change architecture without Orchestrator approval.
2. **One task at a time.** Complete and validate Task T-XX before starting T-XX+1.
3. **Commit atomically.** Each completed task should be a single, clean commit with a descriptive message.
4. **Write tests alongside code.** Do not defer testing to later.
5. **Document as you go.** Add inline comments for non-obvious logic. Update README if public interfaces change.

**Builder Output:**
```markdown
[BUILDER] Task T-XX: [Task Name]
[FILES CREATED]
  - path/to/new/file.ts — [purpose]
[FILES MODIFIED]
  - path/to/existing/file.ts — [what changed and why]
[FILES DELETED]
  - path/to/old/file.ts — [why removed]
[TESTS WRITTEN]
  - path/to/test/file.test.ts — [what is being tested]
[READY FOR VALIDATION]
```

### 4.1.2 — Validator (Compile + Test)

Immediately after the Builder produces code, run validation:

**Validation Steps:**
1. **Syntax Check:** Does the code parse without errors?
2. **Type Check:** Does the type checker pass? (e.g., `tsc --noEmit`, `mypy`, `cargo check`)
3. **Lint Check:** Does the linter pass? (e.g., `eslint .`, `ruff check`, `clippy`)
4. **Unit Tests:** Do all unit tests pass? (e.g., `vitest run`, `pytest`, `cargo test`)
5. **Integration Tests:** Do integration tests pass (if applicable)?
6. **Build:** Does the full build succeed? (e.g., `npm run build`, `cargo build --release`)

**Validation Output:**
```markdown
[VALIDATOR] Task T-XX Results
[SYNTAX]       ✅ Pass / ❌ Fail — [details]
[TYPE CHECK]   ✅ Pass / ❌ Fail — [details]
[LINT]         ✅ Pass / ❌ Fail — [details]
[UNIT TESTS]   ✅ Pass (X/Y) / ❌ Fail (X/Y) — [failing test names]
[INTEGRATION]  ✅ Pass / ❌ Fail / ⏭ Skipped — [details]
[BUILD]        ✅ Pass / ❌ Fail — [details]
```

### 4.1.3 — Self-Correction Loop

If validation fails:

```markdown
[SELF-CORRECT] Attempt X/3 for Task T-XX
[ERROR] [exact error message or failing test output]
[ANALYSIS] [what the agent thinks caused the failure]
[FIX] [description of the change being applied]
[RETRYING VALIDATION...]
```

**After 3 failed attempts:**
```markdown
⚠️ ESCALATION — Build/Test Failure for Task T-XX
[CONTEXT] Failed to resolve after 3 self-correction attempts.
[ERROR] [persistent error details]
[ATTEMPTED]
  1. [Fix attempt 1 description]
  2. [Fix attempt 2 description]
  3. [Fix attempt 3 description]
[OPTIONS]
  A. [Proposed alternative approach]
  B. [Simplify the requirement]
  C. [Skip this task and proceed]
  D. [Orchestrator provides manual fix direction]
```

### 4.1.4 — Critic (Self-Review Against Spec)

After validation passes, the Critic asks:

```markdown
[CRITIC] Task T-XX Spec Compliance

Does the implementation satisfy the Intent Brief?
- [ ] Functional Requirement FR-XX is met: [evidence]
- [ ] Non-Functional Requirements respected:
  - [ ] Performance: [measurement or assertion]
  - [ ] Security: [no exposed secrets, input validated]
  - [ ] Code quality: [linting passes, naming conventions followed]
- [ ] No unplanned side effects introduced.
- [ ] Test coverage adequate for this task.

[VERDICT] ✅ Spec-compliant / ❌ Needs revision — [details]
```

---

## Step 4.2 — Progress Tracking

As tasks are completed, update the execution tracking:

```markdown
### Implementation Progress

| Task ID | Task Name | Status | Commit | Notes |
|---------|-----------|--------|--------|-------|
| T-1.1 | Project scaffolding | ✅ Done | `abc123` | Clean init |
| T-1.2 | Dev tooling setup | ✅ Done | `def456` | ESLint + Prettier |
| T-2.1 | Data models | 🔄 In Progress | — | Working on user schema |
| T-2.2 | API layer | ⏳ Pending | — | Blocked on T-2.1 |
| T-3.1 | Frontend integration | ⏳ Pending | — | |
```

---

## Step 4.3 — Incremental Commits & Branch Hygiene

```markdown
### Commit Convention

Format: `<type>(<scope>): <description>`

Types:
- `feat` — New feature
- `fix` — Bug fix
- `refactor` — Code restructuring without behavior change
- `test` — Adding or updating tests
- `docs` — Documentation changes
- `chore` — Build process, dependency updates
- `style` — Code formatting (no logic change)

Example: `feat(api): add user registration endpoint`
```

---

## 🛑 CHECKPOINT 2 — Implementation Review

Once all tasks in the Execution Plan are complete (or a meaningful milestone is reached):

```
🛑 CHECKPOINT REQUEST — Phase 4 Implementation Complete

[SUMMARY]
  Tasks completed: X / Y
  Files created: [count]
  Files modified: [count]
  Tests written: [count]
  Test pass rate: [X/Y passing]

[ARTIFACTS]
  - [List of significant files and their purpose]

[RISKS]
  - [Any known issues, tech debt, or deferred items]

[DECISION NEEDED]
  1. Proceed to Phase 5 (Verification)?
  2. Any tasks to revisit?
```

> **Proceed to [Phase 5: Verification](./05_VERIFICATION.md)** once the Orchestrator approves.
