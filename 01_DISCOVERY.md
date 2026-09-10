---
description: "Phase 1: Discovery & Specification. Transforms vague ideas into structured, executable intent."
phase: 1
checkpoint: false
---

# Phase 1: Discovery & Specification

> **Goal:** Transform a vague idea, user story, or problem statement into a structured **Intent Brief** — the single source of truth that all downstream phases reference.

> **Paper Concept:** *"Spec-Driven Development"* — AI agents perform significantly better when given formal, standardized requirement documents rather than conversational chat history.

---

## Step 1.1 — Problem Statement

Before any solution, articulate the problem clearly.

### Instructions for the Orchestrator
Answer these questions. Be as specific as possible. The agent will use these answers to build the Intent Brief.

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
| FR-03 | [The system should...] | Nice to Have | [Given X, When Y, Then Z] |
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

The universal checklist that MUST be satisfied before any phase is considered complete.

```markdown
### Definition of Done

- [ ] All functional requirements have corresponding tests.
- [ ] All tests pass (unit, integration, e2e as applicable).
- [ ] Code passes linting and type-checking with zero errors.
- [ ] No known security vulnerabilities (dependency audit clean).
- [ ] Documentation updated (README, API docs, inline comments).
- [ ] Self-review checklist completed by Agent (Phase 5).
- [ ] Orchestrator has reviewed and approved (Checkpoint).
- [ ] Change log updated with summary of modifications.
```

---

## Phase 1 Output — The Intent Brief

When this phase is complete, the Orchestrator should have a filled-out **Intent Brief** (use the template at [`templates/intent_brief.md`](./templates/intent_brief.md)). This document becomes the contract that all agents reference throughout the project.

> **Proceed to [Phase 2: Planning](./02_PLANNING.md)** once the Intent Brief is finalized.
