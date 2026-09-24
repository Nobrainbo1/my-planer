# Plan: [project or feature]

<!-- Adapt this outline. Remove unused sections and these instructions. For a tiny
task, keep both output files short. Use inline output only when requested or files
cannot be written. Reuse existing project docs rather than duplicating them.
Keep later milestones coarse until the first slice validates the main assumptions. -->

- Target project: [path and relevant repository state, or no repository yet]
- Updated: [date]
- Route: [direct / discovery / feasibility, with reason]
- Readiness: [draft / blocked / ready for a named next step]
- Authorization: [planning only / user's implementation instruction and limits]
- Setup guide: [relative path to companion SETUP.md; make a working link]

## Outcome and scope

- User and current problem:
- Why build or change this, rather than keep the current approach:
- First useful version:
- Non-goals:
- Constraints that affect the solution:

## Acceptance

| Required behavior | Observable success check |
| --- | --- |
| [User outcome] | [Scenario and expected result, including a relevant failure case] |

## Evidence and decisions

| Item | Observed / assumed / unresolved | Source or rationale | Impact / next check |
| --- | --- | --- | --- |
| [Consequential fact or choice] | [Status] | [Repository path, source, or user decision] | [What changes if wrong] |

Domain terms, when ambiguity matters: [term, meaning, relationship].

## Approach

[Reuse or proposed stack, component responsibilities, important data contracts,
and the simplest alternative considered. Mark new paths as proposed.]

Tooling: [brief rationale for selected tools and skills; link to SETUP.md for the
complete inventory, sources, versions, installation steps, and checks].

## First end-to-end slice

- Outcome:
- Prerequisites and dependencies:
- Relevant existing paths / proposed new locations:
- Concrete work:
- Verification: [command and cwd if known; otherwise proposed check and what must be confirmed]
- Expected result: [prediction, not evidence that checks ran]

## Later milestones

| Milestone | Outcome | Depends on | Acceptance check |
| --- | --- | --- | --- |
| [Next useful increment] | [Behavior] | [Earlier outcome] | [Observable check] |

## Risks and open questions

[Only material risks and decisions. State whether each blocks the next step,
who or what can resolve it, and the fallback or stopping condition.]

## Handoff

- Authoritative files and any files to transfer:
- Next step and first task:
- Unperformed setup or verification:
- Copyable prompt for the next implementer, including authorization and blockers:
