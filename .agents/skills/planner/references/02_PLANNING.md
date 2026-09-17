---
description: "Phase 2: Agentic Planning & Context Engineering. Builds the execution roadmap."
phase: 2
checkpoint: true
---

# Phase 2: Agentic Planning & Context Engineering

> **Goal:** Transform the Intent Brief (Phase 1) into a detailed, reviewable **Execution Plan** that agents can follow step-by-step. The Orchestrator controls the depth of detail.

> **Paper Concept:** *"Context Engineering"* — The quality of agent output is bounded by the quality and structure of context provided. Design the complete information package: system instructions, codebase maps, tool definitions (MCP), and memory summaries.

> **Why This Phase Exists:** Without this, you jump into coding without understanding the architecture. You build Component A, then realize it needs data from Component B that doesn't exist yet. Planning makes your assumptions visible — when you write them down, you give your future self a chance to catch wrong assumptions before they become wrong code. **On paper:** Draw boxes for components, arrows for data flow. List your assumptions. Pick your tech stack.

---

## Step 2.0 — Planning Depth

> Write for a junior engineer with zero codebase context. Do not depend on chat history, implied conventions, or good design judgment. The plan must supply the exact paths, proposed code diffs or complete blocks, and verification commands needed to execute safely.

Read the approved `INTENT_BRIEF.md` and live `CONTEXT.md` at the target project root. Write `EXECUTION_PLAN.md` at that same root. These artifact paths are relative to the target project, not the planner skill. Template links below resolve within the skill.

Match detail to Spike, One-Shot, or Project scope without omitting execution essentials. Mark irrelevant sections N/A with a reason rather than inventing architecture. Use **DRY (Don't Repeat Yourself)**: reuse existing code and shared contracts instead of duplicating behavior. Use **YAGNI (You Aren't Gonna Need It)**: exclude speculative features, dependencies, and abstractions.

**Hard gate:** No implementation or generated implementation code, including a Spike, scaffold, or automated agent application, until the human explicitly approves both the intent and execution plan revisions. Proposed code in the plan is review material, not authorization to apply or run it. Plan approval does not waive separate install, deletion, schema, or deployment permissions.

The agent will produce:
- A **plain-English architectural narrative** explaining how the system works end-to-end.
- A **component diagram** showing the major parts and how they relate.
- **Detailed tech stack specification** including exact versions, package names, and configuration options.
- **File-by-file change plan** — which files will be created, modified, or deleted, and what each change does.
- **Data flow diagrams** showing how data moves through the system at the function/API level.
- **Interface contracts** — exact API signatures, database schemas, type definitions.
- **Dependency graph** — how every module interacts with every other module, including third-party dependencies.
- **Code interaction map** — which functions call which, which components render which, which services talk to which.
- **Edge case analysis** — what happens when things go wrong at each boundary.
- **Risk summary** with mitigation strategies.
- **Test plan** — specific test cases with inputs, expected outputs, and test types.

```markdown
### Planning Configuration

- **Focus Areas:** [e.g., "Focus on the API layer" or "Full stack"]
- **Constraints:** [e.g., "Must use existing database schema" or "Greenfield"]
```

---

## Step 2.1 — Context Gathering

Before planning, the agent must gather all relevant context. This is the foundation of *Context Engineering*.

### Four Dimensions of Context (from the paper)

#### 1. Instruction Context
*Rules, conventions, and organizational standards.*
- [ ] Read project `AGENTS.md` / `.cursorrules` / `CLAUDE.md` / `.clinerules`
- [ ] Read any existing coding standards documents
- [ ] Read the Intent Brief from Phase 1
- [ ] Identify any regulatory or compliance requirements

#### 2. Codebase Context
*Repository structure, architectural patterns, and cross-repo dependencies.*
- [ ] Map the existing file/folder structure (e.g., use `tree -L 3` or `fd` or `ls -R`)
- [ ] Identify architectural patterns in use (e.g., use `grep` or `rg` for common framework markers)
- [ ] List all existing dependencies and their versions (e.g., read `package.json`, `requirements.txt`, or `Cargo.toml`)
- [ ] Identify any existing tests and their coverage (e.g., search for `*.test.*` or `test/` folders)
- [ ] Note any legacy code or technical debt
- [ ] Search for existing similar implementations before writing new ones

#### 3. Tool/Skill Context
*What the agent can DO — via MCP servers, APIs, CLIs, and plugins.*
- [ ] List available MCP servers (see [Phase 3: Tooling](./03_TOOLING.md))
- [ ] List available CLI tools in the environment
- [ ] List available APIs and their authentication status
- [ ] Identify any existing automation scripts or CI/CD pipelines
- [ ] Note any AI tools available (code generation, image generation, search)

#### 4. Session Context
*Conversation memory, state, and decision history.*
- [ ] Review any prior conversations or decisions about this project
- [ ] Check for existing PRs, issues, or tickets related to this work
- [ ] Note any ongoing work by other team members or agents

Collect facts with tools, not interview questions. Record exact source paths, symbols, versions, and relevant observed command results in the plan. Discover the actual test, lint, typecheck, and build commands from project scripts or CI; never assume a framework or invent a command. State the shell, working directory, prerequisites, and expected exit code. Mark unavailable checks as blocked, not passed. Keep `CONTEXT.md` limited to resolved domain language; put working notes and execution state in the plan or ledger.

---

## Step 2.2 — Architecture Proposal

Based on gathered context, propose the system architecture.

### Architecture Template
```markdown
### Architecture Overview

#### System Narrative
[Plain-English description of how the system works end-to-end.
"A user opens the app, which loads... The frontend talks to... The backend processes... Data is stored in..."]

#### Component Diagram
[Describe or generate a diagram showing major components and their relationships]

#### Tech Stack Recommendation
| Layer | Technology | Why | Alternatives Considered |
|-------|-----------|-----|------------------------|
| Frontend | [e.g., React 19] | [Reason] | [e.g., Vue 3, Svelte 5] |
| Backend | [e.g., Node.js + Express] | [Reason] | [e.g., Python + FastAPI] |
| Database | [e.g., PostgreSQL 16] | [Reason] | [e.g., SQLite, MongoDB] |
| AI/LLM | [e.g., Claude 4 via API] | [Reason] | [e.g., GPT-4.5, Gemini 2.5] |
| Hosting | [e.g., Vercel + Supabase] | [Reason] | [e.g., AWS, Railway] |

#### Data Flow
[Step-by-step flow of a primary user action through the system]
1. User clicks [button] → triggers [function] in [file]
2. [function] calls [API endpoint] at [URL]
3. [API handler] in [file] validates input using [schema]
4. [Service layer] in [file] processes business logic
5. [Repository layer] in [file] writes to [table] in [database]
6. Response flows back: [database] → [service] → [handler] → [frontend]

#### Interface Contracts
[Exact API signatures, types, schemas]

#### Dependency Graph
[Module-to-module interaction map]

#### File Plan
| Action | File Path | Description |
|--------|-----------|-------------|
| CREATE | `src/components/Dashboard.tsx` | Main dashboard component |
| CREATE | `src/api/routes/users.ts` | User CRUD API routes |
| MODIFY | `package.json` | Add new dependencies |
| DELETE | `src/legacy/old-handler.ts` | Remove deprecated handler |
```

---

## Step 2.2b — Architectural Grilling and ADR Gates

Stress-test architecture choices before task breakdown. Reuse the [frontier round protocol](./01_DISCOVERY.md): ask 1 to 3 decision questions per round, offer 2 to 3 viable options at most, and give each a plain-text `Recommendation:` with a reason. The agent gathers technical facts; the human chooses goals, preferences, and trade-offs. Test failure modes, operating costs, migration costs, and simpler alternatives against the intent. Update resolved domain terms in `CONTEXT.md` immediately.

An **Architecture Decision Record (ADR)** explains a consequential choice. Create `docs/adr/000X-<slug>.md` under the target project only when **all three** gates pass with evidence:

| Gate | Required Evidence |
|------|-------------------|
| Hard to reverse | Concrete migration, compatibility, data, or operational cost of changing later |
| Surprising without context | Why a future developer would question this choice without its rationale |
| Real trade-off | Viable alternatives considered and rejected, including benefits sacrificed |

Record Yes/No and rationale for each gate in `EXECUTION_PLAN.md`. If any gate is No or unknown, do not create an ADR; retain the lightweight rationale or open decision in the plan. Do not manufacture trade-offs to justify an ADR. For qualifying decisions, use the skill template [`adr_template.md`](../resources/templates/adr_template.md) relative to the planner skill directory. Check existing ADR numbers and reserve a unique exact path before creation. Record status, decision owner, consequences, and approval evidence. An accepted ADR alone does not authorize implementation.

---

## Step 2.3 — Zero-Context Execution Tasks

Write `EXECUTION_PLAN.md` using [`execution_plan.md`](../resources/templates/execution_plan.md). Break the architecture into ordered, bite-sized tasks. Each task covers one testable behavior; each action should normally take 2 to 5 minutes. Split broad items such as "build the API" instead of labeling them small.

Each task must contain:

- A stable task ID, requirement IDs from `INTENT_BRIEF.md`, acceptance criteria, dependencies, and exact read/write file ownership.
- Required context with exact target-project-relative paths and symbols or line anchors, setup prerequisites, shell, and working directory. Include test fixtures, imports, and contracts so a fresh implementer needs no prior conversation.
- Exact proposed test and production code blocks or diffs, including insertion/replacement anchors. No "implement validation" instructions, ellipses, or unresolved execution placeholders in an approved plan.
- **Red:** Write the failing test first. Supply the exact focused test command and expected assertion failure. During execution, actually run it and record timestamp, exit code, failing test, and observed output before production code changes. A syntax, import, setup, or unrelated failure is not evidence of missing behavior; fix the test setup and rerun.
- **Green:** Apply only the minimum approved production change to pass the observed Red test. Rerun the exact focused command and record actual passing output.
- **Refactor:** Remove duplication and improve clarity without changing behavior. Rerun focused and relevant regression tests, lint, and typecheck; record actual results. If no cleanup is needed, record the reason and still verify.
- For documentation-only work, specify an exact reproducible structural or content acceptance check in place of a runtime test. Record the observed pre-change failure and post-change result; do not fabricate TDD output. Flag unavailable checks explicitly and agree on a review-based alternative before execution.
- Two review assignments: spec compliance first, then code quality and tests. For documentation-only tasks, reviewers verify the structural acceptance equivalent and record runtime checks as `N/A` with a reason. Name the reviewer or role, review inputs, acceptance criteria, findings, fix rounds, and evidence required for each verdict. If separate reviewers are unavailable, disclose that and obtain agreement on the fallback; do not claim independent review.
- An exact execution ledger path, such as `.superpowers/sdd/<plan-id>/progress.md`, resolved to a real path in the approved plan. Record task state, approved revision, implementer/workspace, evidence references, review outcomes, blockers, operational rulings with impact, and next action after every step. Resume from the ledger after context loss.

Expected outputs in the draft plan are predictions, not observed evidence. Leave execution evidence as `Not run` until execution occurs. Task completion requires recorded Red/Green/Refactor results, or for documentation-only tasks the approved structural equivalent with runtime checks recorded `N/A` and a reason. Both ordered review approvals are required in either case; checked boxes alone do not count. Unavailable subagent reviews must follow the [Phase 4 canonical fallback](./04_IMPLEMENTATION.md#401--canonical-fallback-when-fresh-agents-are-unavailable). Rulings may resolve minor operational details but must not bypass approval or expand scope.

---

## Step 2.4 — Risk Assessment

```markdown
### Risk Register

| ID | Risk | Likelihood | Impact | Mitigation |
|----|------|-----------|--------|------------|
| R-01 | [e.g., Third-party API rate limits] | Medium | High | [e.g., Implement caching layer] |
| R-02 | [e.g., LLM output inconsistency] | High | Medium | [e.g., Add validation layer + retries] |
| R-03 | [e.g., Scope creep from vague requirements] | Medium | High | [e.g., Strict adherence to Intent Brief] |
```

---

## Step 2.5 — Preflight Conflict Scan

Run this scan before plan approval and repeat it immediately before execution or after any task, contract, or ownership change. Record the plan revision, reviewer, date, findings, resolution, and rescan evidence in `EXECUTION_PLAN.md`.

| Check | Inspect | Resolve Before Execution |
|-------|---------|--------------------------|
| File access collisions | All task read/write sets, shared configuration, generated files, lockfiles, and other agents' current ownership | Serialize overlapping writes and read/write hazards, assign a single owner, or isolate workspaces with an explicit integration task |
| Contract discrepancies | Producer and consumer signatures, types, schemas, error behavior, versions, fixtures, and domain terms | Agree on one exact contract and update every dependent task and test |
| Circular dependencies | Task prerequisites and module dependency graph | Produce a valid topological task order; break cycles and resolve missing or self-referencing dependencies |

A list of possible conflicts is not a passed scan. Record each conflict's owner and actual resolution, then rescan. Unresolved findings block approval and dispatch. Only collision-free tasks with satisfied dependencies may run in parallel. Workspace isolation alone does not resolve incompatible contracts.

---

## CHECKPOINT 1 — Plan Approval

```text
CHECKPOINT REQUEST — Phase 2 Complete
[SUMMARY] EXECUTION_PLAN.md is ready for review, not yet authorized for execution.
[ARTIFACTS]
  - INTENT_BRIEF.md: approved revision and approval evidence
  - CONTEXT.md: current shared domain language
  - EXECUTION_PLAN.md: architecture, exact task code/commands, reviewers, ledger, risks, and preflight evidence
  - docs/adr/: exact qualifying ADR paths, or none with gate rationale
[RISKS] [remaining non-blocking risks and agreed deferrals]
[DECISION NEEDED] Approve this exact plan revision, or request changes?
Recommendation: [approve or revise, with evidence-based reason]
```

Before requesting approval, verify that all required sections are complete, every task is executable without chat history, and preflight has no unresolved findings. Record the Orchestrator, date, approved intent and plan revisions, and explicit approval message or reference. A drafted plan, accepted ADR, selected mode, or silence is not approval. Material changes require renewed approval before affected implementation.

Phase 2 acceptance requires a reviewable plan, resolved blocking decisions, passed preflight, and explicit approval. It does not require implemented features or completed execution evidence. The final Definition of Done in `INTENT_BRIEF.md` applies at delivery only.

> **Proceed to [Phase 3: Tooling](./03_TOOLING.md)** only after both `INTENT_BRIEF.md` and `EXECUTION_PLAN.md` are explicitly approved. Recheck approval and preflight before any generated implementation, including Spike and automated-mode code.
