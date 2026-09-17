---
description: "Architecture Decision Record template. Create a record only when all three ADR gates pass."
type: template
---

# ADR [000X] — [Decision Title]

> **Output:** `docs/adr/000X-<slug>.md` relative to the target project root. Select an unused number and replace the slug before creation.
> **Date:** [YYYY-MM-DD]
> **Status:** Proposed / Accepted / Rejected / Superseded
> **Decision owner:** [name or role]
> **Intent and plan:** `INTENT_BRIEF.md` [revision], `EXECUTION_PLAN.md` [revision], both at the target project root
> **Related requirements:** [FR/NFR IDs]
> **Supersedes / Superseded by:** [exact ADR path or none]

## Creation Gate — All Three Required

Evaluate these gates in `EXECUTION_PLAN.md` before creating this ADR. Copy the supporting evidence here only if all three are Yes. If any is No or unknown, keep the rationale or open question in the plan and do not create an ADR.

| Gate | Yes/No | Concrete Evidence |
|------|--------|-------------------|
| Hard to reverse | [answer] | [migration, compatibility, data, or operational cost of changing later] |
| Surprising without context | [answer] | [why a future developer would question this choice without its rationale] |
| Real trade-off | [answer] | [viable alternatives rejected and benefits sacrificed] |

## Context

[Describe the problem, constraints, and decision drivers using canonical terms from the target project's `CONTEXT.md`. Separate observed repository facts from assumptions. Cite exact paths, symbols, measurements, or human decision references.]

## Options Considered

Include 2 to 3 viable options at most. Include the current or simpler approach when viable. Do not manufacture alternatives to pass the gate.

| Option | Benefits | Costs and Risks | Reason Chosen or Rejected |
|--------|----------|----------------|---------------------------|
| [option A] | [benefits] | [costs] | [reason] |
| [option B] | [benefits] | [costs] | [reason] |

Recommendation: [preferred option and evidence-based reason]

## Decision

[State the exact choice, scope, and affected contracts. Explain why its trade-offs fit the approved intent. Identify existing code or conventions reused under DRY (Don't Repeat Yourself), and speculative features excluded under YAGNI (You Aren't Gonna Need It).]

## Consequences

- **Benefits:** [expected improvements]
- **Accepted costs:** [capabilities or simplicity sacrificed]
- **Risks and mitigations:** [failure modes, owner, and safeguards]
- **Reversal or migration:** [what changing this decision later would require]
- **Revisit trigger:** [evidence or condition that should reopen the decision]

## Validation and Review

| Claim or Risk | Planned Validation | Actual Evidence | Reviewer and Verdict |
|---------------|--------------------|-----------------|----------------------|
| [claim] | [exact check or linked execution task ID, command, and working directory] | Not run | Pending |

Predicted results are not evidence. Record actual timestamp, exit code, relevant output, and evidence path when validation runs. Link implementation tasks to `EXECUTION_PLAN.md`; do not turn this ADR into a task ledger.

## Decision Approval

| Approver | Date | ADR Revision | Decision | Explicit Approval Evidence |
|----------|------|--------------|----------|----------------------------|
| [Orchestrator] | [date] | [revision] | Pending / Accepted / Rejected | [message or reference] |

An accepted ADR is not implementation approval. Both `INTENT_BRIEF.md` and `EXECUTION_PLAN.md` must have explicit human approval before any generated implementation, scaffold, or Spike code. Record material changes in a replacement or revised decision and obtain renewed plan approval before affected execution.
