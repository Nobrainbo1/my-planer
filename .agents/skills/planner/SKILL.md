---
name: planner
description: >-
  Turn an uncertain software idea into a scoped, evidence-based plan and portable
  handoff with grill-with-docs discovery and a separate setup guide. Use for
  /planner, $planner, planning a project, assessing an idea, or preparing a
  brief for a coding agent. Avoid adding a
  separate planning process to straightforward implementation requests or an
  existing adequate plan.
---

# IntentFlow planner

Help the user decide what is worth building, what the first useful version is,
and what the next implementer needs to know. One invocation runs discovery,
planning, tool selection, and setup-guide preparation. The user does not need to
call the supporting skills or phases separately. Default deliverables are
`PLAN.md` and `SETUP.md`; scale their detail to the project.

## 1. Decide how much planning helps

Read the user's request, relevant repository instructions, existing plans, and
the smallest set of files needed to understand current behavior. Locate the
target project from context; ask only if ambiguous. Do not use the skill's own
directory as the target just because the skill is installed there.

Choose and briefly explain one route:

| Route | Use when | Result |
| --- | --- | --- |
| Direct | Goal, scope, and validation are already clear | Brief plan and setup checklist; discovery confirms the known answers without repeating questions. |
| Discovery | User, problem, scope, or a consequential choice is unclear | Resolve the decision that most affects the first version, then produce a plan. |
| Feasibility | A technical unknown determines whether the idea can work | Timeboxed experiment plan with pass/fail criteria and a decision after the result. |

If the chosen execution workflow already covers discovery and planning well,
reuse its artifacts and offer a short input brief instead of repeating its process.
Do not choose a new workflow just to justify this skill.

## 2. Resolve the uncertainty that matters

Read and apply the [grill-with-docs skill](../grill-with-docs/SKILL.md) on every
planner invocation. Invoke it through the host's skill mechanism when available;
otherwise read the linked file and follow its interview loop in this conversation.
Tell the user it is being used. This is a skill step, not a request to spawn an agent.
Use [discovery guidance](references/01_DISCOVERY.md) for additional context.

Ask about missing details that affect the user, workflow, scope, constraints, or
success criteria. Use one to three questions per round and record the answers in
the working plan. Continue the planner automatically when discovery is sufficient;
do not require a second command. If answers are already known or the user delegates
the choices, apply the skill as a brief completeness check and record assumptions.

Ask only questions whose answers materially change scope, acceptance, or a costly
choice. Research repository facts yourself. For reversible details, state a
reasonable assumption and continue. If the user delegates decisions, choose
defaults within that scope; do not conduct an interview by habit.

Test the idea against doing nothing, a manual process, or an existing solution
when plausible. Recommend reducing scope, running an experiment, or not building
if the expected benefit does not justify the work. Explain the evidence and limits.

## 3. Produce the smallest useful plan

Read [planning guidance](references/02_PLANNING.md) and adapt the
[plan template](resources/templates/execution_plan.md). Write
`PLAN.md` in the target project's documentation location, or its root if no
convention exists. Reuse an existing authoritative plan instead of creating a
competing one. Write `SETUP.md` alongside it, linking both outputs. Honor an explicit
request for inline-only output; if no writable target is available, provide both
documents as copyable Markdown instead of claiming they were saved.

Include the problem and user, first-version scope and non-goals, observable
acceptance criteria, key decisions and assumptions, an implementation approach,
ordered work with verification, and the next action. Identify facts as observed,
assumptions as proposed, and important unknowns as unresolved. Add domain terms,
architecture, and tool recommendations only where they affect the work.

Detail the first useful end-to-end slice. Keep later work at milestone level until
its assumptions are tested. Do not invent file paths, commands, dependencies,
estimates, or passing test results. Mark proposed new paths and unverified commands.
Do not prewrite the entire implementation inside the plan.

## 4. Recommend tools only for demonstrated gaps

Always review required tooling using [tool selection](references/03_TOOLING.md).
Research additions when a capability is missing; do not invent a tool gap.
Prefer the existing stack and available skills.
Distinguish the coding workflow from the application framework and starter code.
Tie each recommendation to a requirement, explain its costs, and verify current
claims against official sources. No added tooling is a valid recommendation.

Create `SETUP.md` from the [setup template](resources/templates/setup.md). Inventory
all selected development tools, skills, runtimes, direct project dependencies,
and integrations needed for the plan. Separate required, already available,
optional, and unresolved items. Cover transitive packages through the package
manager and lockfile rather than listing each one manually. Give ordered manual
steps and a self-contained AI setup prompt; include sources, versions, install
locations, checks, and any login or other human-only steps. If nothing is needed,
say so explicitly. Rejected alternatives do not belong in the install queue.

Planning does not install tools, copy scaffolds, retrieve persona libraries,
rewrite agent configuration, or grant execution permissions. Put necessary setup
in the handoff with its actual authorization status.

## 5. Review and hand off

Apply the [handoff checks](references/HANDOFF.md). Make sure the first task is
actionable and every must-have has an acceptance check. Record blockers honestly.
Readiness and authorization are separate: a technically usable plan can still
have implementation outside the user's request.

For planning-only work, deliver both files, explain how to use `SETUP.md` manually
or with an AI, and provide a copyable prompt for the next agent.
No separate approval is needed to deliver a draft. Do not claim approval without
evidence. If the user already authorized planning and implementation, continue
within that authorization; do not impose new intent and plan approval ceremonies.
Ask about a material unresolved scope decision when necessary. Never change
repository rules or move the installed skills as a handoff step.

Maintenance: use [evaluation cases](references/EVALUATION.md) when changing this skill.
