---
description: "Phase 1: Discovery & Specification. Transforms vague ideas into structured, executable intent."
phase: 1
checkpoint: true
---

# Phase 1: Discovery & Specification

> **Goal:** Transform a vague idea, user story, or problem statement into a structured **Intent Brief** — the single source of truth that all downstream phases reference.

> **Paper Concept:** *"Spec-Driven Development"* — AI agents perform significantly better when given formal, standardized requirement documents rather than conversational chat history.

> **Why This Phase Exists:** Without this, you build the wrong thing. The agent codes for 2 hours, then you realize the requirements were ambiguous and half the work is wasted. A 15-minute spec saves 2 hours of wrong code. Specs are cheaper than rewrites. **On paper:** Write what you want in plain sentences, then ask "what would convince me this is done?" — that's your Definition of Done.

---

## Step 1.0 — Classify Scope and Lock Implementation

Record the target project root and scope path in `INTENT_BRIEF.md`. All output paths in these phases are relative to that target project, not the workflow repository or skill directory.

Read shipped templates and references as sources; never fill them in or store project material in the skill's resources. Select approved output paths before writing. Rewrite every copied local link relative to its generated output file, preserving exact filename case and checking its target and heading. Links to workflow policy must resolve to the actual installed skill location, not an assumed project layout. Record authoritative artifact paths in the plan before changing execution workspaces.

| Path | Use When | Required Planning |
|------|----------|-------------------|
| Spike | Test feasibility with throwaway code | Timebox, hypothesis, experiment, success/failure criteria, disposal plan, and a small execution plan |
| One-Shot | Make a small, bounded change | Brief specification, acceptance criteria, and bite-sized execution tasks |
| Project | Build a multi-step feature or a new application | Full specification, architecture, dependencies, risks, and execution tasks |

Scope changes planning depth, never approval requirements. A Spike is not permission to code first.

**Hard gate:** Do not implement, generate implementation code, copy scaffolds, or create runnable agent applications until the human explicitly approves both `INTENT_BRIEF.md` and `EXECUTION_PLAN.md`. This applies to every scope path and both automated and manual modes, including throwaway experiments. Read-only investigation and draft planning documents are allowed. Proposed code blocks in a draft plan are review material only; do not apply or execute them before approval.

Record approver, date, approved artifact revision, and the explicit approval message or reference. Silence, scope classification, mode selection, and an existing unapproved document are not approval. A changed scope or design requires renewed approval before affected implementation. Dependency installation, deletion, schema changes, and deployment still require their separate permissions.

## Step 1.1 — Problem Statement

Before any solution, articulate the problem clearly.

### Instructions for the Agent and Orchestrator
Use the prompts below as an interview guide, not a bulk questionnaire. The agent gathers repository and environment facts with tools first. Ask the Orchestrator only for goals, preferences, or decisions that cannot be established from evidence.

```markdown
### Problem Statement
- **What problem are we solving?**
  [Describe the pain point, inefficiency, or gap]

- **Who experiences this problem?**
  [End users, developers, ops team, business stakeholders]

- **What does "solved" look like?**
  [Describe the desired end state — what changes when this is done?]

- **What happens if we don't solve it?**
  [Impact of inaction — helps prioritize]
```

---

## Step 1.1b — Grilling with Frontier Rounds

A **Design Tree** maps decisions and the choices that depend on them. A **frontier** is the set of unresolved decisions whose parent choices are already known.

1. Read the relevant files, existing tests, manifests, and configuration. Collect versions, current behavior, constraints, and conventions yourself. Record evidence as exact paths or tool results in `INTENT_BRIEF.md`; do not ask the human to look these up.
2. Build a compact Design Tree in the brief's open questions. Track each decision's parent, status, answer, and effect on scope. Mark unknown facts as unverified; do not invent them.
3. Ask only 1 to 3 frontier questions per round. Start with decisions that unblock the most dependent choices. Offer at most 2 to 3 viable options per question and state the essential trade-off.
4. Give every question a plain-text `Recommendation:` line and a reason. Wait for the human's answers before opening dependent branches. Do not treat your recommendation as consent.
5. Update the brief and the live glossary immediately after each answer. Remove branches that no longer apply. Repeat until blocking goals and preferences are resolved; record deferred non-blockers with their effect and owner.

```text
Round [number] — [frontier decision]
Question: [goal or preference that needs a human decision]
Options: [option A and trade-off]; [option B and trade-off]
Recommendation: [preferred option and evidence-based reason]
Depends on: [resolved parent decision or none]
```

If tools cannot establish a fact, record the blocker and request access or evidence. Do not convert an unknown technical fact into a preference question.

### Live Domain Model — CONTEXT.md

Create `CONTEXT.md` at the target project root using the skill template [`context_template.md`](../resources/templates/context_template.md) in the planner skill directory.

- Record each resolved term immediately during the interview, not in a batch at the end.
- Use one canonical term and a precise meaning shared by requirements, plans, code, and tests. This shared vocabulary is **ubiquitous language**.
- Record aliases and `_Avoid_` terms with the canonical replacement and reason. Ask for clarification before merging terms with different meanings.
- Keep definitions, domain relationships, short usage examples, and the source of agreement current. Revise entries when the human resolves a naming conflict.
- `CONTEXT.md` is a glossary, never an implementation plan, task list, decision backlog, session log, or scratchpad. Keep unresolved decisions in `INTENT_BRIEF.md`, architecture decisions in the plan or ADRs, and execution history in the ledger.

---

## Step 1.2 — Scope Definition

Explicitly define boundaries. Unbounded scope is the #1 killer of agentic workflows.

```markdown
### Scope

#### In-Scope
- [ ] [Feature/capability 1]
- [ ] [Feature/capability 2]
- [ ] [Feature/capability 3]

#### Out-of-Scope (Explicitly)
- [ ] [Thing that might seem related but is NOT included]
- [ ] [Future enhancement that is deferred]

#### Assumptions
- [Assumption 1: e.g., "Users have Node.js 20+ installed"]
- [Assumption 2: e.g., "We are building for web, not mobile"]
```

---

## Step 1.3 — Functional Requirements

Define what the system must *do*. Use concrete, testable language.

```markdown
### Functional Requirements

| ID | Requirement | Priority | Acceptance Criteria |
|----|-------------|----------|---------------------|
| FR-01 | [The system must...] | Must Have | [Given X, When Y, Then Z] |
| FR-02 | [The system must...] | Should Have | [Given X, When Y, Then Z] |
| FR-03 | [The system should...] | Could Have | [Given X, When Y, Then Z] |
```

**Priority Scale (MoSCoW):**
- **Must Have** — System does not work without this.
- **Should Have** — Important but system is usable without it.
- **Could Have** — Desired if time and resources permit.
- **Won't Have** — Explicitly deferred to a future iteration.

---

## Step 1.4 — Non-Functional Requirements & Constraints

Define how the system must *behave*. These become the guardrails for agent-generated code.

```markdown
### Non-Functional Requirements

#### Performance
- Response time: [e.g., < 200ms for API calls]
- Throughput: [e.g., Must handle 10k concurrent users]
- Resource budget: [e.g., Must run on 512MB RAM]

#### Security
- Authentication: [e.g., OAuth 2.0 / API keys / none for internal tools]
- Data sensitivity: [e.g., PII handling, encryption requirements]
- Access control: [e.g., Role-based, tenant isolation]

#### Reliability
- Uptime target: [e.g., 99.9%]
- Error handling: [e.g., Graceful degradation, retry with backoff]
- Data durability: [e.g., Must not lose user data on crash]

#### Maintainability
- Code style: [e.g., Must pass ESLint with Airbnb config]
- Documentation: [e.g., All public APIs must have JSDoc/docstrings]
- Test coverage: [e.g., Minimum 80% line coverage]

#### Compatibility
- Platforms: [e.g., Windows, macOS, Linux]
- Browsers: [e.g., Chrome 120+, Firefox 115+, Safari 17+]
- Dependencies: [e.g., No dependencies with known CVEs]
```

---

## Step 1.5 — Stakeholder & User Context

```markdown
### Stakeholders

| Role | Name/Team | Interest | Approval Authority |
|------|-----------|----------|-------------------|
| Orchestrator | [You] | Overall quality & direction | Final approval |
| End User | [Persona/Group] | Usability & functionality | User testing |
| Ops/Infra | [Team] | Deployability & monitoring | Deployment approval |

### User Personas (if applicable)
- **Persona 1:** [Name], [Role], [Tech literacy level], [Primary goal]
- **Persona 2:** [Name], [Role], [Tech literacy level], [Primary goal]
```

---

## Step 1.6 — Definition of Done (DoD)

Define this final acceptance checklist during discovery. It applies at delivery only, not before every phase. Discovery completes when its specification and glossary are reviewable; planning completes at plan approval. Neither phase requires implementation or passing implementation tests.

```markdown
### Definition of Done

- [ ] All in-scope functional requirements have corresponding tests where runtime behavior applies.
- [ ] All required tests pass (unit, integration, e2e as applicable).
- [ ] Code passes linting and type-checking with zero errors where those checks apply.
- [ ] Documentation-only deliverables pass structural checks (links, fences, structure, acceptance readback); these are not runtime evidence.
- [ ] No known security vulnerabilities (dependency audit clean).
- [ ] Required documentation updated (README and API docs as applicable).
- [ ] Self-review checklist completed by Agent (Phase 5).
- [ ] Orchestrator has reviewed and approved (Checkpoint).
- [ ] Change log updated with summary of modifications.
```

---

## Phase 1 Outputs and Acceptance

- `INTENT_BRIEF.md` at the target project root: use [`intent_brief.md`](../resources/templates/intent_brief.md). Include scope classification, target root, problem, boundaries, requirements, constraints, stakeholders, delivery-only DoD, evidence, and Design Tree decisions.
- `CONTEXT.md` at the same root: the live glossary of resolved terms, relationships, and `_Avoid_` replacements.
- Resolve blocking questions. Record any deferred non-blockers, their owner, and their impact.
- Obtain explicit human approval of the intent. Record approver, date, approved revision, and approval evidence in `INTENT_BRIEF.md`.

> **Proceed to [Phase 2: Planning](./02_PLANNING.md)** after intent approval. No implementation is authorized until `EXECUTION_PLAN.md` is also explicitly approved.
