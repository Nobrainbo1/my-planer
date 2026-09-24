# Tool selection: solve a gap, then stop

Review what the plan needs on every run. Research additions only when a requirement is not covered, a consequential choice
needs evidence, or the user explicitly requests options. Start with what is
already available. Do not turn every planning request into a marketplace survey.

## Keep the categories separate

| Category | What it contributes | Decision to make |
| --- | --- | --- |
| Coding agent or harness | Edits, command execution, permissions, and working context | Can the user's current environment do the work? |
| Development workflow or skill | Interview, planning, implementation, or review instructions | Is the missing behavior already covered? |
| Application framework or library | Runtime capabilities inside the delivered application | Does a product requirement need it? |
| Starter or scaffolder | Initial application files and project structure | Does it fit the chosen stack and deployment constraints? |
| CLI, connector, or MCP server | Access to an external capability or service | Is that access actually required and available? |

Using AI to build a product does not imply the product needs an agent runtime.
A workflow that writes plans is not necessarily an application starter. Determine
which category the user means by "scaffolder" before comparing candidates.
When a new project needs a starting point, scan the [scaffold and framework
discovery map](SCAFFOLDS.md) for relevant leads. It is a prompt for research,
not a default stack or a substitute for current documentation.

## Evaluate the smallest useful set

Compare the existing setup or no addition with one recommendation and, if useful,
one serious alternative. More candidates are warranted only when the decision
remains unresolved. Do not impose an arbitrary count on the tools available to
the coding agent.

For each proposed addition record:

- The requirement or capability gap it addresses and why the existing setup is insufficient.
- An official documentation or repository URL, the date checked, and version or commit when relevant to compatibility.
- Relevant OS, shell, runtime, and host integration requirements; distinguish a generic CLI from a host-specific plugin or hook.
- Setup and maintenance effort, cost when relevant, license constraints, external access, and meaningful overlap with existing tools.
- Recommendation status: reuse, recommend, investigate, or reject; state the remaining uncertainty and verification step.

Verify current features, compatibility, install instructions, and material cost
claims against primary sources. If browsing is unavailable, label candidates
unverified and provide a concrete check for the next agent; do not imply readiness.
Missing documentation is an unknown, not proof of incompatibility. A tool need
not name every AI editor to work as a normal CLI on a supported OS.

For external access, compare any relevant AXI, official CLI/API, MCP server, or existing connector against the actual operation and current environment. AXI is an option, not a mandatory first stop.

Prefer the simplest adequate integration. There is no universal CLI-versus-MCP
winner, mandatory log optimizer, persona library, or default multi-agent fleet.
Recommend a custom skill only for a recurring instruction gap; a one-off need
usually belongs in the task brief.

## Avoid duplicate planning

Inspect the chosen workflow's current input expectations. If it provides its own
discovery and planning, supply the agreed outcome, constraints, decisions, and
acceptance criteria as its input. Do not promise automatic import of `PLAN.md`.
Use a documented adapter only if it exists; otherwise provide a reading prompt.

Tool selection ends with a justified choice or an explicitly unresolved question.
Installation and configuration belong to authorized implementation. Record
prerequisites without changing agent rules, installing packages, or authenticating
services as a side effect of research.

## Write SETUP.md for a person or an AI

Use the [setup template](../resources/templates/setup.md). Keep this file beside
the plan as the authoritative install checklist. It must be understandable without
this skill or earlier chat history. Link the plan, but include the target project,
OS, shell, coding host, selected stack, and setup scope in the setup file itself.
If the destination environment is unknown, mark that as a prerequisite to resolve
before platform-specific commands can run; do not present a guessed command as ready.

Inventory the chosen tools and skills, runtimes, package manager, direct application
dependencies, and required external integrations. Existing manifests and lockfiles
own package versions; reference their exact paths and install commands. In a new
project, specify the intended versions or supported range from official sources,
and make starter initialization an explicit prerequisite if it creates the manifest.
Never recommend running a package install against a nonexistent project manifest.

For each required addition, provide the reason, official source and date checked,
version or commit, installation scope and destination, prerequisites, exact commands
with shell and working directory (or numbered UI steps), and a verification command
with its expected result. For a skill, include the source repository/subdirectory,
required companion skills and resources, host-specific destination, and how to
confirm the host discovers it. Downloading a SKILL.md alone may omit its dependencies.

Separate documentation verification from execution: "checked against official docs;
not run here" is useful and honest. If a source or procedure cannot be verified,
mark the item unresolved, specify the missing check, and keep it out of the runnable
install sequence. Do not use placeholder shell commands as if they were executable.

Order steps by dependency: environment prerequisites, chosen starter if needed,
project packages, skills/integrations, then checks. Before each change, inspect
what is present and reuse compatible installations. Do not blindly reinstall,
overwrite existing configuration, or upgrade incompatible versions. Explain
conflicts and the required decision. Keep optional tools in a separate section
and skip them unless selected; no new installs is a valid setup checklist.

List environment variable names and where to configure them, never secret values.
Identify sign-in, payment, license acceptance, administrator access, or host UI
actions where actually needed. An AI without shell/browser access can guide a
person but cannot perform those actions itself. Follow existing authorization;
creating this file does not authorize installation.

Include a copyable AI prompt that explicitly authorizes setup when the user sends
it, limits work to required verified items, checks the receiving environment, skips
compatible installed items, preserves existing files, and reports actual checks.
On an incompatible environment or failed prerequisite, stop dependent steps and
explain the blocker rather than improvising a different stack. Request user action
only when needed. Building the application is a separate next step.
