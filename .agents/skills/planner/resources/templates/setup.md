# Setup: [project name]

<!-- Write the completed file beside PLAN.md. Replace all placeholders, remove
irrelevant sections, and make the plan link work. Keep it usable without the chat
or these skills. Never claim installation or verification ran during planning. -->

## Before you start

- Project folder: [target path; explain how a recipient chooses their local equivalent]
- Plan: [relative path to authoritative plan; make a working link]
- Environment: [OS, shell, coding host, selected stack]
- Last source check: [date]
- Setup readiness: [ready to follow / blocked, with unresolved prerequisites]
- Current authorization: [planning only / actual setup authorization and limits]

Follow the numbered steps yourself, or give this file and the project files to an
AI that can run commands using the prompt below. Optional tools are not required.
[If there are no additions, say "No new installations are required" and retain
checks for required existing tools.]

## What you need

| Item and version | Type | Why the plan needs it | Status | Official source |
| --- | --- | --- | --- | --- |
| [Selected item] | [tool / skill / runtime / package / integration] | [Requirement] | [required addition / already available / optional / unresolved] | [Official URL and release or commit when relevant] |

[List direct dependencies or refer to exact manifest/lockfile paths and the
package-manager step that installs them. Include companion resources for skills.
Explain how to check required items reported available on the original machine.]

## Install in order

### 1. [Concrete setup step]

- Requires: [earlier steps, existing files, or none]
- First check: [detect whether the correct version/configuration is already present]
- Install location: [project-local or user/system scope, exact destination]
- Shell and working directory: [actual shell and project-relative cwd]
- Action: [exact documented command in a shell-labeled code block, or numbered UI steps]
- Verify: [command or UI check and expected outcome]
- Evidence: [official source/date; documented but not run, or actual run result]
- If it fails: [specific next check; stop dependent steps]

[Repeat for required steps only. Do not leave runnable-looking placeholder commands.
Keep unresolved procedures out of this sequence. Skills must include all required
bundle files and a discovery check in the chosen host.]

## Steps that need you

[Only actual sign-in, account, license, payment, admin, or UI requirements; otherwise
"None identified." For configuration use variable names and locations, not secrets.]

## Optional extras

[Name, benefit, cost/overlap, and link to official setup; skip unless selected.
Write "None" if there are no useful extras.]

## Unresolved items

[Item, what is unknown, how to verify it, and which steps it blocks; or "None."]

## Let an AI do the setup

Copy this prompt with the completed file. Replace paths before delivery:

```text
Use [actual SETUP.md path] to set up [target project folder]. I authorize the
required, verified setup steps described there. Read the project instructions,
confirm this machine's OS, shell, host, and existing files, then follow the steps
in dependency order. Reuse compatible installed tools; skip optional items.
Preserve existing configuration and project files. Do not change the selected
stack to work around a conflict. If the environment differs, a procedure is
unverified, or a prerequisite fails, stop affected steps and explain what is needed.
Ask me to complete any necessary sign-in or other human-only step; do not request
secret values in chat. Run the listed verification checks and report what actually
passed, what changed, and what remains blocked. Do not build or deploy the app yet.
```

## Setup completion

[List final checks. Initially mark each not run. The installer records actual
results here, including blockers. A download alone does not establish readiness.]
