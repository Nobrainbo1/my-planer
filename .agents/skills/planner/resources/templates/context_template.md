---
description: "Live domain glossary template. Maintained during discovery and throughout the target project."
type: template
---

# Context — [Project/Feature Name]

> **Output:** `CONTEXT.md` at the target project root, alongside `INTENT_BRIEF.md` and `EXECUTION_PLAN.md`.
> **Target project root:** [exact path]
> **Last updated:** [YYYY-MM-DD]

## Purpose and Maintenance

This is the project's glossary of **ubiquitous language**: the same terms used in requirements, plans, code, tests, and human discussion. It is not an implementation plan or scratchpad.

- Add or update each resolved term immediately during each frontier round, not at the end of the interview.
- The agent collects codebase and environment facts with tools. Ask the human to resolve goals, preferences, and ambiguous meanings, not to look up technical facts.
- Keep one precise canonical term for each concept. Record its boundaries and a short usage example. Do not merge concepts just because their names are similar.
- Mark rejected or misleading terms with `_Avoid_`, the preferred replacement, and a reason. Do not present them as accepted aliases.
- On a naming change, update the current definition, source of agreement, and affected glossary relationships. Track any required implementation changes in `EXECUTION_PLAN.md`, not here.
- Keep tasks, command output, debugging notes, unresolved decisions, and execution history out of this file. Open decisions belong in `INTENT_BRIEF.md`; architecture rationale belongs in `EXECUTION_PLAN.md` or a qualifying ADR; progress belongs in the execution ledger.
- Remove template prompts when filling this file. Keep only agreed domain language and its sources. Unknown meanings remain open questions in the brief.

## Canonical Terms

| Canonical Term | Definition and Boundary | Accepted Aliases | Usage Example | Agreement or Evidence Source | Updated |
|----------------|-------------------------|------------------|---------------|------------------------------|---------|
| [term] | [precise meaning; what it excludes] | [aliases or none] | [short domain sentence] | [human decision reference or exact source path and symbol] | [date] |

## Terms to Avoid

| Tag | Avoided Term | Use Instead | Reason | Agreement Source |
|-----|--------------|-------------|--------|------------------|
| _Avoid_ | [misleading or rejected term] | [canonical term] | [ambiguity or incorrect meaning] | [decision reference] |

## Domain Relationships and Invariants

An **invariant** is a domain rule that must remain true. Record domain meaning here, not implementation mechanics or database design.

| Terms | Relationship or Invariant | Boundary or Example | Source |
|-------|---------------------------|---------------------|--------|
| [canonical term A; canonical term B] | [domain relationship or rule] | [example or excluded case] | [agreement reference] |

## Glossary Review

Before handing context to another agent, verify that every term is resolved, every `_Avoid_` entry has a canonical replacement, and relationships use the same canonical names. Confirm that no plan, backlog, raw logs, or scratchpad content has entered this glossary.
