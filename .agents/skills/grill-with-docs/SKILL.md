---
name: grill-with-docs
description: >-
  Interview the user about an uncertain idea or consequential design trade-off
  and record resolved decisions in a working brief. Use when asked to grill,
  stress-test an idea, work through unresolved goals, or as the planner's
  discovery step. Skip unnecessary questions when
  the requirements are clear or the user has delegated the remaining choices.
---

# Grill with docs

The planner reads and applies this skill automatically. It can also be used
independently. Focus on decisions that change the outcome; when the necessary
details are already known, complete a brief check without redundant questions.

## Working document

Locate the target project and its existing brief or plan. Update that document
instead of creating a competing source of truth. If none exists, use `PLAN.md`
in the project's normal documentation location or root. If the user wants only
a conversation or no target workspace is available, keep a concise decision
summary in the conversation.

Read repository evidence before asking about technical facts. Record observations,
assumptions, decisions, and blockers separately. Follow the target repository's
instructions. An interview request authorizes discovery and drafting; it does
not by itself authorize building, installing tools, or changing external services.

## Interview loop

1. Identify the open choice that most changes the first useful version. Resolve parent decisions before dependent details.
2. Ask one to three concise questions. Offer a few viable options when helpful, state the trade-offs, and recommend one with a reason.
3. Wait for required answers while continuing independent research. Do not treat your recommendation or silence as consent.
4. Record the answer and its scope impact. Add domain definitions only where different meanings would change the plan.
5. Drop branches that no longer matter. Defer reversible details with explicit assumptions, especially when the user asks you to use your judgment.

Test the idea against simpler alternatives, including doing nothing or using an
existing solution. Challenge contradictions and unsupported assumptions without
forcing the user to defend every preference.

## Completion

Stop when the outcome, scope, constraints, acceptance checks, and consequential
choices are sufficient for the next step. Return resolved decisions, remaining
blockers, and a recommendation. "Validate the need first" is a valid result.

When called by the planner, return the decisions to its planning step; do not
invoke the planner again or create a recursive skill loop. When used independently,
continue with the [planner](../planner/SKILL.md) if a full handoff was requested.
Do not repeat completed discovery or claim that
interview completion authorizes execution. Keep short rationale in the plan;
use an existing architecture decision record convention only when warranted.
