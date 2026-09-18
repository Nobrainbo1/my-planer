---
name: grill-with-docs
description: >-
  Interview the user about goals and design trade-offs while maintaining domain
  language and decision records. Use for /grill-with-docs, /grill-me, or
  "stress-test this idea".
---

# Grill with Docs

Use this skill independently or during planner discovery and architecture review. This is a local adaptation of the interview methodology defined in [Phase 1](../planner/references/01_DISCOVERY.md) and [Phase 2](../planner/references/02_PLANNING.md), not an installed upstream package. Follow [root rules](../../AGENTS.md).

## Inputs and Boundaries

Confirm the target project root, existing intent, scope, and approved write locations. Read repository facts with tools before asking questions. Classify the work as Spike, One-Shot, or Project using [discovery](../planner/references/01_DISCOVERY.md).

No implementation, code generation, or scaffold copying occurs until the human explicitly approves both intent and execution plan. Draft planning documents are allowed; recommendations are not consent. Do not install tools or change external services during an interview.

## Frontier Round Protocol

1. Read relevant code, tests, manifests, and existing decisions. Record evidence and unknown facts in `INTENT_BRIEF.md` at the target root. Ask for access if facts cannot be established; do not ask the human to guess repository facts.
2. Build a **Design Tree**, a map of decisions and their dependencies, in the brief. Mark nodes resolved, open, or deferred. The **frontier** contains open nodes whose parent decisions are resolved.
3. Ask 1 to 3 frontier questions per round about human goals, preferences, or trade-offs. Start with the decision that unblocks the most work. Offer at most 2 to 3 viable options per question.
4. State essential facts and a `Recommendation:` with a reason for every question. Wait for the answers. Do not open dependent branches until their parent choices are resolved.
5. Immediately record each answer, its scope impact, and newly resolved terminology. Remove irrelevant branches. Repeat until blockers are resolved. Record owners and impact for deferred nonblocking questions.

```text
Question: [goal or preference]
Options: [A and trade-off]; [B and trade-off]
Recommendation: [choice and reason]
Depends on: [resolved decision]
```

## Live Domain Language

Create or update target-root `CONTEXT.md` from the [context template](../planner/resources/templates/context_template.md); never edit the shipped template. Write each resolved term during the round, not at the end.

Use canonical terms, precise meanings, domain relationships, short examples, and sources of agreement. Mark forbidden or confusing alternatives with `_Avoid_`, their canonical replacement, and reason. This shared vocabulary is **ubiquitous language**. Clarify conflicting meanings rather than merging them silently.

`CONTEXT.md` is a glossary only. Put tasks, unanswered questions, implementation plans, and session history elsewhere.

## Architecture Decisions

Use [planning](../planner/references/02_PLANNING.md) to test alternatives against requirements, failure modes, costs, and reversibility. An Architecture Decision Record (ADR) is warranted only when all three gates pass:

- **Hard to reverse:** Changing later has concrete migration or compatibility costs.
- **Surprising without context:** A future developer needs the rationale to understand the choice.
- **Real trade-off:** Viable alternatives were considered and rejected, with benefits sacrificed.

Record each gate's evidence in `EXECUTION_PLAN.md`. A No or unknown result means no ADR; keep a lightweight rationale or open question in the plan. When all pass, use the [ADR template](../planner/resources/templates/adr_template.md), inspect existing numbers, and choose a unique target-project `docs/adr/000X-<slug>.md`. Record decision owner, status, consequences, and explicit approval. An ADR does not authorize implementation.

## Completion Check

Read back each answer before the next round. Verify terms were saved immediately, `_Avoid_` replacements are clear, the glossary contains no tasks, and unresolved blockers remain visible. Check document structure and links after writes. Report resolved decisions, remaining blockers, and the next approval needed. Obtain explicit intent and plan approvals before handing implementation to SDD.
