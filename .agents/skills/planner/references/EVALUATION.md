# Behavioral evaluation cases

Use these when changing the planner. They test decisions, not exact wording.
In a fresh conversation, supply the skill, the scenario, and any fixture repository.
Keep outputs in a temporary workspace. Do not install tools or contact live services
as part of these cases. For interactive cases, provide the stated user responses.

| Case | Request and context | Observable pass condition |
| --- | --- | --- |
| Clear small change | "Plan changing the existing CSV export to include a total. Keep the stack." Supply a small repository with an export function and documented test command. | Direct route; applies grill-with-docs as a completeness check without redundant questions. Brief plan using real paths and SETUP.md that reuses the stack. No mandatory installs. |
| Vague product | "I want a booking app." No repository. | Asks about the user and booking workflow before architecture. Does not assume payments, multiple businesses, or an agent framework. After answers, limits the first version. |
| Delegated decisions | "Plan a personal offline recipe organizer. No accounts or sync. Pick sensible defaults; don't interview me." | Produces a useful plan with labeled defaults and offline acceptance criteria. No gratuitous question round or invented user approval. |
| Technical uncertainty | "Plan importing my old proprietary archive. I don't know if its format is readable." No sample or format docs. | Feasibility route with sample acquisition, bounded experiment, pass/fail criterion, and fallback. Does not claim parsing works or invent the full importer design. |
| Existing planner | "I already use a workflow that does discovery and detailed task planning. Prepare input for it." Supply its documented input format and an agreed product brief. | Reuses the brief and supplies missing inputs; does not generate a competing technical plan or claim automatic import. |
| Tool research unavailable | "Recommend a Windows-compatible workflow for this plan." Disable browsing; supply only the installed-tool inventory. | Distinguishes known local capabilities from unverified candidates, provides verification steps, and does not fabricate compatibility or installation commands. |
| Planning only | "Plan a small tracker. Do not build or install anything." | Delivers a plan and handoff marked planning only. No edits outside the planning artifacts, installs, or governance changes. |
| Existing authorization | "Plan then implement this bounded change; use your judgment." Supply a fixture repository and acceptance criteria. | No new intent/plan approval ceremony. Moves to implementation within scope and follows the repository's checks. |
| No worthwhile build | "I copy three values once a month. A custom platform would take days; I don't expect it to grow. Assess whether I should build it." | Weighs benefit against effort and recommends a manual/existing approach or a small experiment if justified. Does not force a platform plan. |
| Stale handoff | Supply a plan referencing a removed module and an unavailable command. | Identifies the mismatch, revises within scope or names the blocker, and does not call the handoff ready for implementation. |
| Single entry point | "/planner I want a booking app for my shop." Answer discovery questions with one shop, no payments, and one administrator. | Explicitly loads grill-with-docs, asks only missing consequential details, then continues without another command to PLAN.md and SETUP.md. Does not call the planner recursively from the interview skill. |
| Portable setup | Request a plan requiring a project package and a skill with supporting resources. Supply authoritative install documentation and a fixture manifest. | SETUP.md includes both, real sources/versions, skill bundle destination, dependency order, checks, and an AI setup prompt. A human can follow the same steps without the chat. No installs run during planning. |
| Existing and optional tools | Supply a compatible installed runtime and one optional integration. | Checks and reuses the runtime; keeps the integration outside the required install queue. Every required plan item is accounted for in SETUP.md. |
| Changed destination | Give the completed Windows SETUP.md to an installer on a different OS. | Identifies the mismatch before executing platform-specific steps and explains what needs revision. Does not blindly run the commands or replace the stack. |
| Incomplete setup evidence | No source access or confirmed host support for a proposed skill. | Marks the item unresolved, excludes guessed commands from runnable steps, and identifies the verification needed. Does not call setup fully ready. |

For each run record the inputs, route chosen, actual artifacts/actions, unnecessary
questions, incorrect assumptions, and whether a fresh implementer can take the
next step. A static read-through is not an executed behavioral test.

To evaluate whether this skill deserves its overhead, compare similar ideas using
the existing coding workflow alone and with IntentFlow. Track repeated questions,
time to a first accepted slice, missed requirements, and rework caused by assumptions.
These are evaluation criteria, not measured benefits. Keep the skill only where
it improves the result enough to justify the extra interaction.
