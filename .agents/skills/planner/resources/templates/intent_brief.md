---
description: "Reusable Intent Brief template. Fill this out at the start of every project or feature."
type: template
---

# Intent Brief — [Project/Feature Name]

> **Date:** [YYYY-MM-DD]  
> **Orchestrator:** [Your Name]  
> **Status:** Draft / In Review / Approved

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

## 8. Open Questions

| # | Question | Impact | Status | Answer |
|---|----------|--------|--------|--------|
| 1 | [question] | [High/Med/Low] | Open / Resolved | [answer when resolved] |

---

## 9. Approval

| Approver | Date | Status |
|----------|------|--------|
| [Orchestrator] | [date] | Pending / Approved |
