---
description: "Reusable Intent Brief template. Fill this out at the start of every project or feature."
type: template
---

# Intent Brief — [Project/Feature Name]

> **Date:** [YYYY-MM-DD]  
> **Orchestrator:** [Your Name]  
> **Status:** Draft / In Review / Approved
> **Output:** `INTENT_BRIEF.md` at the target project root
> **Target project root:** [exact absolute path]
> **Scope:** Spike / One-Shot / Project
> **Brief ID and revision:** [stable ID and exact revision]
> **Approved write locations:** [exact project paths; preserve existing artifacts]

Read this template as a source; never fill in the shipped original. Rewrite copied links relative to the generated artifact and verify exact filename case and heading targets. Mark irrelevant sections N/A with a reason. For a Spike, record hypothesis, timebox, experiment, success/failure criteria, and disposal plan; both intent and plan still require approval before execution.

---

## 1. Problem Statement

**What problem are we solving?**  
[Describe the pain point, inefficiency, or gap]

**Who experiences this problem?**  
[End users, developers, ops team, business stakeholders]

**What does "solved" look like?**  
[Describe the desired end state]

**What happens if we don't solve it?**  
[Impact of inaction]

---

## 2. Scope

### In-Scope
- [ ] [Feature/capability 1]
- [ ] [Feature/capability 2]

### Out-of-Scope
- [ ] [Explicitly excluded item 1]
- [ ] [Explicitly excluded item 2]

### Assumptions
- [Assumption 1]
- [Assumption 2]

---

## 3. Functional Requirements

| ID | Requirement | Priority | Acceptance Criteria |
|----|-------------|----------|---------------------|
| FR-01 | [The system must...] | Must Have | [Given X, When Y, Then Z] |
| FR-02 | [The system must...] | Should Have | [Given X, When Y, Then Z] |
| FR-03 | [The system should...] | Could Have | [Given X, When Y, Then Z] |

---

## 4. Non-Functional Requirements

### Performance
- Response time: [target]
- Throughput: [target]
- Resource budget: [target]

### Security
- Authentication: [method]
- Data sensitivity: [classification]
- Access control: [model]
- Required security checks and thresholds: [exact dependency/secret-scan rules and acceptance limits, or justified applicability decisions; resolve before approval]

### Reliability
- Uptime target: [%]
- Error handling: [strategy]

### Maintainability
- Code style: [standard]
- Test coverage: [minimum %]
- Documentation: [requirements]

### Compatibility
- Platforms: [list]
- Browsers: [list]
- Dependencies: [constraints]

---

## 5. Stakeholders

| Role | Name/Team | Interest | Approval Authority |
|------|-----------|----------|-------------------|
| Orchestrator | [You] | Overall quality | Final approval |
| End User | [Persona] | Usability | User testing |

---

## 6. User Personas

**Persona 1:** [Name]  
- Role: [role]  
- Tech literacy: [low / medium / high]  
- Primary goal: [what they want to accomplish]  
- Frustration: [current pain point]

---

## 7. Definition of Done

This checklist applies at delivery, not before discovery or planning can finish. Define applicable checks and security thresholds explicitly; do not treat template examples as approved requirements.

- [ ] Every in-scope functional requirement has fresh passing test or documentation-check evidence.
- [ ] All required runtime tests pass where applicable. Required skipped, blocked, or unrun checks prevent readiness.
- [ ] Applicable configured lint, typecheck, and build checks pass. Record unavailable required checks as blocked.
- [ ] Documentation-only work passes structural, link, fence, and acceptance readback checks; runtime checks are N/A with a scope reason, not fabricated passes.
- [ ] Security findings meet the explicitly approved thresholds; unresolved threshold conflicts block readiness.
- [ ] Required documentation and change log are updated.
- [ ] Every task has ordered spec and quality/test approvals on the verified candidate, with authorized human-review substitutions recorded where needed.
- [ ] Orchestrator approved delivery readiness; restricted delivery actions still need separate authorization.

---

## 8. Observed Evidence and Design Tree

| Evidence ID | Fact | Exact Source Path and Symbol or Tool Result | Observed Value | Uncertainty / Next Action |
|-------------|------|------------------------------------------------|----------------|---------------------------|
| E-01 | [repository or environment fact] | [source and observation date] | [actual result] | [none or unverified blocker] |

| Decision ID | Parent Decision | Question | Options / Recommendation and Reason | Status | Answer and Decision Evidence | Owner | Scope Impact |
|-------------|-----------------|----------|-------------------------------------|--------|------------------------------|-------|--------------|
| D-01 | [resolved parent ID or none] | [human goal or trade-off] | [2–3 options at most; recommendation] | Open / Resolved / Deferred | [actual answer, date, message/reference] | [owner] | [effect and deferral impact] |

Ask only 1 to 3 frontier questions per round. Resolve blockers before approval; deferred non-blockers need an owner and impact. Update resolved terms immediately in `CONTEXT.md`, not this decision backlog.

---

## 9. Approval

| Brief ID / Approved Revision | Approver | Date | Status | Explicit Approval Message or Reference |
|------------------------------|----------|------|--------|----------------------------------------|
| [exact ID and revision] | [Orchestrator] | [date] | Pending / Approved | [actual message or durable reference] |

A status or checked box alone is not approval. Record the exact reviewed revision; changed scope or design requires renewed approval before affected implementation. This approval does not authorize implementation until the execution plan is also explicitly approved.
