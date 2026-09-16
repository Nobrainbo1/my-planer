---
description: "Reusable Execution Plan template. Generated during Phase 2 Planning."
type: template
---

# Execution Plan — [Project/Feature Name]

> **Date:** [YYYY-MM-DD]  
> **Intent Brief:** [Intent Brief](./intent_brief.md)  
> **Status:** Draft / Approved

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
| [e.g., AI/LLM] | [e.g., Claude via MCP] | [latest] | [Why this choice] |

### Dependency Graph
[Module-to-module interaction map, including third-party dependencies]

### Code Interaction Map
[Which functions call which, which components render which, which services talk to which]

---

## File Change Plan

| Action | File Path | Description |
|--------|-----------|-------------|
| [CREATE / MODIFY / DELETE] | [path] | [what this change does] |

---

## Task Breakdown

### Phase A: [Foundation / Setup]

| Task ID | Task | Dependencies | Effort | Files | Description |
|---------|------|-------------|--------|-------|-------------|
| T-A.1 | [task] | None | S | [files] | [details] |
| T-A.2 | [task] | T-A.1 | S | [files] | [details] |

### Phase B: [Core Features]

| Task ID | Task | Dependencies | Effort | Files | Description |
|---------|------|-------------|--------|-------|-------------|
| T-B.1 | [task] | T-A.2 | M | [files] | [details] |
| T-B.2 | [task] | T-B.1 | L | [files] | [details] |

### Phase C: [Integration & Polish]

| Task ID | Task | Dependencies | Effort | Files | Description |
|---------|------|-------------|--------|-------|-------------|
| T-C.1 | [task] | T-B.2 | M | [files] | [details] |
| T-C.2 | [task] | T-C.1 | M | [files] | [details] |

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

---

## Deployment & Migration

### Migration Plan
[Data migration steps, state transfers, API version deprecation strategy]

### Rollback Strategy
[How to revert these changes safely in production if something fails]

---

## Approval

- [ ] Orchestrator reviewed and approved this Execution Plan.
- [ ] All open questions from Intent Brief are resolved or deferred.
