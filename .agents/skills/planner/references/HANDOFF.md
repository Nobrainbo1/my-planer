# Handoff without changing the project's rules

The recipient can be the same agent, a new conversation, another developer, or
a workflow with its own planner. The goal is to transfer decisions and evidence,
not assume a particular tool imports a particular filename.

## Readiness and authority

Record two separate fields in the plan:

- **Readiness:** draft, blocked (with named blockers), or ready for the stated next step. Name that step: technical planning, feasibility experiment, or implementation.
- **Authorization:** planning only, or implementation authorized with a reference to the user's instruction and its limits. List outstanding permissions only when relevant.

A draft can be delivered for review without approval. A detailed plan is not
proof of approval. Existing authorization remains valid within its scope; this
skill does not require two new approval rounds or authorize external actions.

## Transfer enough context

Include the authoritative plan and `SETUP.md` paths and supporting files, target project and
repository state if available, the first task, unresolved assumptions, and how to
verify the intended behavior. Record uncommitted files that the next workspace
needs. A new worktree or a different computer may not contain them.

Keep working repository paths relative to its root where possible. Before claiming
the handoff is usable, check local links and confirm needed files exist in the
recipient's workspace, or explicitly list what must be transferred. Do not change
workspaces or copy files to external services just to deliver the plan.

Use this prompt as a starting point, replacing placeholders with actual values:

```text
Read [actual plan path], [actual setup-guide path], and the target repository instructions in [project root].
The requested next step is [technical planning / experiment / implementation].
Preserve the agreed first-version scope, constraints, and acceptance criteria.
Treat observations, proposed assumptions, and unresolved questions separately.
Existing authorization: [the user's instruction and limits, or planning only].
Start with [first task]. Before affected work, resolve [actual blockers, or none].
Verify results using [checks in the plan]. If repository evidence contradicts the
plan, explain the impact and update it within the authorized scope.
```

When the recipient uses another workflow, let it map the brief into its documented
format and satisfy its own requirements. Do not mark its gates complete based
on IntentFlow's readiness field. Do not require repeating decisions already made.

Leave installed skills and project governance in place. No automatic archiving,
`AGENTS.md` replacement, tool installation, or "execution mode" rewrite is needed.

Before delivery, reconcile both outputs: every required tool or skill in the plan
appears in the setup inventory, and each required install supports the chosen plan.
Update both when a decision changes. `SETUP.md` includes its own setup-only prompt
for an AI with the necessary access, as well as the same steps for manual use.
List unresolved or human-only steps instead of promising fully unattended setup.
