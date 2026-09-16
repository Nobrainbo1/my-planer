---
description: "Phase 2: Agentic Planning & Context Engineering. Builds the execution roadmap."
phase: 2
checkpoint: true
---

# Phase 2: Agentic Planning & Context Engineering

> **Goal:** Transform the Intent Brief (Phase 1) into a detailed, reviewable **Execution Plan** that agents can follow step-by-step. The Orchestrator controls the depth of detail.

> **Paper Concept:** *"Context Engineering"* — The quality of agent output is bounded by the quality and structure of context provided. Design the complete information package: system instructions, codebase maps, tool definitions (MCP), and memory summaries.

> **💡 Why This Phase Exists:** Without this, you jump into coding without understanding the architecture. You build Component A, then realize it needs data from Component B that doesn't exist yet. Planning makes your assumptions visible — when you write them down, you give your future self a chance to catch wrong assumptions before they become wrong code. **On paper:** Draw boxes for components, arrows for data flow. List your assumptions. Pick your tech stack.

---

## Step 2.0 — Planning Depth

> The planning phase produces a comprehensive, reviewable Execution Plan. The agent should provide full detail so the Orchestrator can review it as if doing a code review before a single line is written.

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

## Step 2.3 — Execution Plan

Break down the architecture into an ordered list of tasks with dependencies.

```markdown
### Execution Plan

#### Phase 1: Foundation
- [ ] Task 1.1: [Initialize project scaffolding]
  - Dependencies: None
  - Estimated effort: S
  - Files: [list]
- [ ] Task 1.2: [Set up development tooling (linter, formatter, test runner)]
  - Dependencies: Task 1.1
  - Estimated effort: S
  - Files: [list]

#### Phase 2: Core Features
- [ ] Task 2.1: [Implement data models / database schema]
  - Dependencies: Task 1.1
  - Estimated effort: M
  - Files: [list]
- [ ] Task 2.2: [Build API layer]
  - Dependencies: Task 2.1
  - Estimated effort: L
  - Files: [list]

#### Phase 3: Integration & Polish
- [ ] Task 3.1: [Connect frontend to API]
  - Dependencies: Task 2.2
  - Estimated effort: M
  - Files: [list]
- [ ] Task 3.2: [Add error handling and edge cases]
  - Dependencies: Task 3.1
  - Estimated effort: M
  - Files: [list]
```

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

## 🛑 CHECKPOINT 1 — Plan Approval

```
🛑 CHECKPOINT REQUEST — Phase 2 Complete

[SUMMARY] The Execution Plan has been created.
[ARTIFACTS]
  - Architecture diagram / narrative
  - Tech stack decisions with rationale
  - Task breakdown with dependencies and effort estimates
  - Risk register

[DECISION NEEDED]
  1. Does the architecture align with your vision?
  2. Are the tech stack choices acceptable?
  3. Should any tasks be re-prioritized or removed?
  4. Proceed to Phase 3 (Tooling) or revise?
```

> **Orchestrator:** Review the Execution Plan. Approve, request changes, or provide feedback.

> Use the template at [`execution_plan.md`](../resources/templates/execution_plan.md) to structure the plan.

> **Proceed to [Phase 3: Tooling](./03_TOOLING.md)** once the Execution Plan is approved.
