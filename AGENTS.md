# IntentFlow project guidance

This repository maintains portable planning skills. The reusable entry point is
[planner](.agents/skills/planner/SKILL.md); [grill-with-docs](.agents/skills/grill-with-docs/SKILL.md)
is its built-in discovery step and can also be used independently.

## Working on this repository

- Improve the skills, references, and validation tools within the user's requested scope. Maintaining this repository is not a planning-only session.
- Keep instructions short and decision-focused. Do not add a dependency, named methodology, mandatory approval round, or generated document without a concrete need.
- Keep project-specific plans and session logs outside the shipped skills. Do not retain worker dispatches, copied skills, or audit transcripts as product files.
- After editing, check local Markdown links and skill frontmatter. Use the planner's [evaluation cases](.agents/skills/planner/references/EVALUATION.md) for substantial behavior changes. Report what was actually checked.

## Using the skills in another project

- Planning-only applies when the user requests planning. It does not prohibit later implementation that the user authorizes.
- Follow the target repository's instructions and the user's existing authorization. These skills do not replace project governance or require changes to it.
- Read templates from their installed location; write completed artifacts in the target project's established documentation location.
- Do not assume a particular instruction file or command syntax loads automatically in every coding tool. Use the host's documented skill invocation or explicitly point the agent to `SKILL.md`.
