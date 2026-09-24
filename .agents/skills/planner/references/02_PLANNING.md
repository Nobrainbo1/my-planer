# Planning: enough detail for the next implementer

Use the [plan template](../resources/templates/execution_plan.md) as an outline,
not a form that must be filled in every time. Remove irrelevant sections. Keep
one authoritative plan; retain existing brief or decision files when useful and
link to them instead of copying conflicting versions.

Keep install instructions in the companion `SETUP.md`, using the
[setup template](../resources/templates/setup.md). Link it from the plan; do not
maintain two copies of installation commands. Both files are default planner outputs,
even when setup only says the existing tools are sufficient.

## Choose the right level of detail

- Small change: expected behavior, affected area, and how to verify it.
- New project: user outcome, first-version boundary, data and component responsibilities, important constraints, and the first end-to-end slice.
- Feasibility experiment: question, method, limit, pass/fail evidence, and resulting decision. Defer the full build plan until the result is known.
- Handoff to a workflow with its own technical planner: provide the product brief, constraints, decisions, and acceptance criteria. Let that workflow own its detailed task format.

If the request is explicitly for a detailed technical plan, expand tasks using
repository evidence. Detail should remove ambiguity, not prescribe code that has
not been tested. Let the implementer adapt local mechanics while preserving the
agreed behavior and constraints.

## Explain consequential choices

For an important design choice, record the requirement it serves, viable simpler
alternative, trade-off, and what evidence would cause reconsideration. Prefer
the current architecture when it is adequate. Describe data ownership and failure
behavior when those affect acceptance; diagrams are optional.

Keep rationale in the plan by default. Use the project's existing architecture
decision record convention when a decision has lasting migration costs or needs
an independently maintained history. Do not create ceremonial records for routine
library choices or invent approval evidence.

## Make tasks verifiable

Each near-term task needs a concrete outcome, prerequisites, relevant existing
paths or proposed new locations, and an acceptance check. Use requirement IDs
only when they make traceability easier. Prefer behavior-sized tasks to arbitrary
minute estimates or one task per function.

Start with a thin end-to-end path that proves the main assumption. Include failure
cases that matter to users. For existing projects, derive validation commands from
manifests or documented workflows and state the working directory and shell when
relevant. For new projects, label setup and verification commands as proposed
until the selected starter establishes them. Expected results are not test evidence.

Order dependent tasks. Parallel work is optional; propose it only for separable
work with clear contracts and an integration check. Serialize shared configuration,
lockfile, and overlapping source edits. Do not require multiple agents or reviewers
for an ordinary change.

## Check the plan before delivery

- Every must-have has an observable check, including important failure behavior.
- The first task can begin with the listed inputs; missing inputs are explicit blockers.
- Task dependencies exist and have no cycles; proposed parallel work has no unresolved ownership conflict.
- Names, data contracts, scope, and tool recommendations agree across the document.
- Existing paths and sources are verified; new locations and uncertain commands are labeled.
- Review status, technical readiness, and authorization reflect the actual conversation.

If implementation later disproves an assumption, revise the affected part of the
plan and explain the impact. Ask for a decision only when the change exceeds the
user's delegated scope or needs a consequential choice. A plan is not a ban on learning.
