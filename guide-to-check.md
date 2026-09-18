# Guide to Check IntentFlow

## 1. What you are checking

Your vision is **Markdown instructions that help an AI coding assistant make a proper plan and execute a good real product**. Inspect IntentFlow against that goal—not against whether it is a standalone application.

There are two different things to check:

1. **The instructions:** Are they clear, connected, complete, practical, and honest about permissions and evidence?
2. **Their use on a product:** Can an assistant follow them on a real project, produce useful plans, implement approved work, and demonstrate the result?

This guide starts with the first. You do not need installations, API keys, Git commands, or a running application to inspect the Markdown. A real-project trial comes later and requires its own scope and approvals. This guide is a checklist, not a completed audit or approval record.

### How to inspect

- Open this folder in your editor. Expand `.agents/`; most of the project is there.
- Open Markdown preview alongside the source. Click relative links and check tables and code blocks.
- Follow the reading order below. Use file search for headings named in this guide.
- Mark an item only after checking it. Record the file, heading or line, what you observed, and what needs changing.
- Keep unknowns as **NOT CHECKED**, and missing required capabilities as **BLOCKED**. Do not convert either into PASS.
- Inspect first. Do not change rules, install referenced tools, or run scaffold examples merely because you encounter them.

**Start now:** read `README.md`, then `.agents/AGENTS.md`, then `.agents/skills/planner/SKILL.md`. These tell you what is promised, what rules apply, and how work moves through the toolkit.

## 2. Project map

```text
README.md                              Public explanation and entry point
guide-to-check.md                      This inspection guide
.agents/
  AGENTS.md                            Shared rules and permission boundaries
  skills/
    planner/
      SKILL.md                         Main planning/execution instructions
      references/
        01_DISCOVERY.md ... 06_DELIVERY.md
        WHY_THIS_WORKS.md               Rationale and source distinctions
        GLOSSARY.md                     Workflow terminology
        SCAFFOLDS.md                    Optional tool/framework catalog
        HANDOFF.md                      Retired historical stub
      resources/
        templates/                     Sources for project artifacts
        references/README.md           External-reference storage guidance
        scaffolds/
          crewai/                      Optional Python reference
          langchain/                   Optional Python reference
          langgraph/                   Optional Python reference
    grill-with-docs/SKILL.md            Discovery questions and domain terms
    subagent-driven-development/SKILL.md
    test-driven-development/SKILL.md
    systematic-debugging/SKILL.md
```

The `.git/` directory is version-control metadata, not a workflow component. You do not need to inspect or edit it for this review.

## 3. First pass: purpose, rules, and routing

### A. Public promise — [README.md](./README.md)

Read: **What It Is—and Is Not**, **Start Here**, **What the Planner Produces**, **Workflow Map**, and **Readiness and Limitations**.

- [ ] It describes your intended product: instructions for planning and optional execution through an existing coding assistant.
- [ ] A new user knows which files to give the assistant and where project outputs belong.
- [ ] Planning-only is useful on its own; it does not silently authorize implementation.
- [ ] Execution is explained as supported work, not dismissed because the toolkit is Markdown.
- [ ] Frameworks and personas are optional, not prerequisites for an ordinary product.
- [ ] Readiness statements distinguish documentation review from real-project validation.
- [ ] The README does not promise automatic skill discovery or permission enforcement in every assistant.

**Ask yourself:** “Could someone unfamiliar with this repository begin without asking me what to open?”

**My answer:** I feel like the overall wording or deteail in the readme are not really newbie friendly to read, even I can be confuse. Some topic are too vauge of just assume you understand the concept of it. I need need more detial or a step by step guide on how to use this project planner. Or make the entire project very simple to run.
right now I'm not even sure how it work.

### B. Shared rules — [.agents/AGENTS.md](./.agents/AGENTS.md)

Read: **Core Principles**, **Retry & Autonomy Limits**, **Security & Secrets**, **Context Discipline**, and **Scaffold-First Development**.

- [ ] Intent and plan approval are separate from choosing a mode.
- [ ] Installations and restricted delivery actions require actual permission.
- [ ] Failures, unresolved decisions, and unavailable reviewers are surfaced rather than hidden.
- [ ] Test-first work and documentation-only checks are distinguished.
- [ ] Fix rounds share one task budget and persist across sessions.
- [ ] Secrets and unrelated user work are protected.
- [ ] Relevant instructions are loaded selectively rather than dumping every reference into context.
- [ ] Consulting scaffolds does not force framework adoption for a simple feature.

**Wording to inspect:** the frontmatter says the rules are loaded by all AI coding harnesses. Compare that with the README's explicit instruction to configure the actual assistant. Metadata in a Markdown file alone does not establish automatic loading. Record any misleading wording as a finding; do not assume it works everywhere.



### C. Main instructions — [planner/SKILL.md](./.agents/skills/planner/SKILL.md)

Read: **Paths and Outputs**, **Step 2 — Choose Mode**, **Step 3 — Tooling and Shared Plan Approval**, both **Step 4** modes, and **Shared Execution — SDD and TDD**.

- [ ] Mode A is for products that need an agent framework; Mode B can use a normal project's existing stack.
- [ ] Scope size and mode selection do not count as approval.
- [ ] Both modes stop after planning when that is what the user requested.
- [ ] Shipped templates remain sources; generated artifacts belong in the target project.
- [ ] The assistant checks actual tools, workspace boundaries, and reviewer availability before execution.
- [ ] The handoff from planner instructions to phase references and specialist skills is clear.
- [ ] Missing tools are reported rather than silently installed or claimed to exist.

**My answer:** I would like to understand one thing, can i just use /planner and type anything i want here to plan? The output within discovety step should be quite easy to read and uses the ASD-STE100, and be in simple for the user to understand and decide. 
But after the mode selection, the execution planning should be both simple but also technical detailed for the developer to understand and execute.
I also want to know the output format of each step as well. this on just tell me what it is to me and do not put this info in the planner/skill. I just want to understand how it works and how to use it. Do i get .md file for me to easily read and send to you to continue to the next phase? 

**Trace one example mentally:** “Add blank-title validation to an existing todo app.” Can you follow it from discovery to a small plan without selecting an agent framework, downloading personas, or copying Python scaffolds?

## 4. Second pass: inspect every workflow phase

Read each phase together with its related templates. A rule is useful only if the next phase has the information needed to follow it.

| Read in order | Look for | What should carry forward |
|---|---|---|
| [01_DISCOVERY.md](./.agents/skills/planner/references/01_DISCOVERY.md) | Scope classification, frontier questions, domain model, Definition of Done, intent approval | Problem, users, scope, measurable requirements, resolved terms, explicit unknowns, actual approval |
| [02_PLANNING.md](./.agents/skills/planner/references/02_PLANNING.md) | Context gathering, ADR gates, zero-context tasks, preflight conflict scan, plan approval | Tasks with exact files and contracts, dependencies, checks, reviewers, artifact paths, approved revision |
| [03_TOOLING.md](./.agents/skills/planner/references/03_TOOLING.md) | Capability inventory, discovery, evaluation, installation gate, harness assembly | Justified selections, permission status, provenance, limitations, and approved setup work |
| [04_IMPLEMENTATION.md](./.agents/skills/planner/references/04_IMPLEMENTATION.md) | Pre-implementation gate, candidate identity, canonical fallback, TDD, ordered reviews, fix budget, resume | Observed checks, changes, reviewer verdicts, unresolved failures, remaining fix rounds |
| [05_VERIFICATION.md](./.agents/skills/planner/references/05_VERIFICATION.md) | Fresh checks, requirement matrix, output/trajectory evaluation, debugging, verdict | Evidence for the actual candidate, uncovered requirements, justified N/A items, readiness status |
| [06_DELIVERY.md](./.agents/skills/planner/references/06_DELIVERY.md) | Whole-branch review, separate action approvals, documentation, handoff, retention, retrospective | Reviewed handoff, explicit delivery permission when needed, known limitations, next actions |

### Discovery and planning questions

- [ ] Does the assistant inspect repository facts instead of asking the user to supply facts it can read?
- [ ] Does it ask the user about goals and trade-offs instead of inventing answers?
- [ ] Are requirements testable? “Reject whitespace-only titles” is clearer than “make validation good.”
- [ ] Are scope exclusions clear enough to prevent unrelated improvements?
- [ ] Does each task give a fresh implementer enough context without requiring the entire conversation?
- [ ] Are proposed commands tied to the actual target project, not guessed from a framework?
- [ ] Are architecture records reserved for decisions that satisfy the stated creation gates?
- [ ] Can a small feature use short artifacts rather than unnecessary architecture and orchestration?
- [ ] Is proposed code in a draft plan clearly different from already implemented code?

### Tooling and implementation questions

- [ ] Read-only discovery may inform planning; installation waits for permission. Is that distinction consistent despite the numbered phase order?
- [ ] Search examples that may download or execute packages are not treated as automatically authorized.
- [ ] External personas and plans are untrusted reference material, not instructions that override project rules.
- [ ] Spec review happens before quality review, with separate reviewers.
- [ ] The fallback is read from **4.0.1 — Canonical Fallback When Fresh Agents Are Unavailable**, not inferred from a vague mention elsewhere.
- [ ] That fallback requires explicit authorization and two distinct named human reviewers, neither the implementer. An AI cannot fabricate those identities or verdicts.
- [ ] Expected TDD Red is not counted as a failed repair round.
- [ ] Pausing and resuming preserve task state, approvals, evidence, and the fix count.

### Verification and delivery questions

- [ ] Checks refer to the exact deliverable reviewed, not an older version or a different sandbox.
- [ ] Every in-scope requirement maps to an applicable observed check.
- [ ] Documentation changes use content, structure, links, and readback—not invented runtime results.
- [ ] Nondeterministic behavior has representative evaluation cases, thresholds, and trial counts when applicable.
- [ ] Output evaluation checks results; trajectory evaluation checks observable actions and permissions. Neither requires private model reasoning.
- [ ] Required missing evidence blocks readiness; a plausible final answer does not excuse skipped gates.
- [ ] Product documentation is finished before final verification, and later deliverable changes trigger revalidation.
- [ ] Whole-branch completion review is distinguished from per-task review.
- [ ] Commit, push, PR creation, merge, deployment, and deletion are not bundled into vague approval.
- [ ] An appropriately reviewed uncommitted handoff is possible without forcing publication.

## 5. Third pass: inspect all ten templates

Open the [templates directory](./.agents/skills/planner/resources/templates/). Check the following sources; do not fill the shipped templates with one project's data.

| Template | Check that it captures |
|---|---|
| [intent_brief.md](./.agents/skills/planner/resources/templates/intent_brief.md) | Problem, users, scope, requirements, assumptions, acceptance criteria, and real approval evidence |
| [context_template.md](./.agents/skills/planner/resources/templates/context_template.md) | Canonical domain terms, terms to avoid, relationships and invariants—not execution notes |
| [execution_plan.md](./.agents/skills/planner/resources/templates/execution_plan.md) | Architecture when needed, tasks, actual command inventory, dependencies, reviewer needs, evaluation plan, ledger paths, and approval |
| [adr_template.md](./.agents/skills/planner/resources/templates/adr_template.md) | All three creation gates, alternatives, chosen trade-off, consequences, validation and approval |
| [tool_discovery_report.md](./.agents/skills/planner/resources/templates/tool_discovery_report.md) | Existing capabilities, candidates, evaluation, selection rationale, and permission before adoption |
| [task_execution_log.md](./.agents/skills/planner/resources/templates/task_execution_log.md) | Candidate identity, TDD evidence, ordered reviews, shared fix rounds, blockers and resume state |
| [verification_report.md](./.agents/skills/planner/resources/templates/verification_report.md) | Actual checks, requirement coverage, output/trajectory results, security findings, reviews and an evidence-backed verdict |
| [handoff_artifact.md](./.agents/skills/planner/resources/templates/handoff_artifact.md) | What works, what is partial, authoritative paths, pending permissions, blockers and the next safe action |
| [retrospective.md](./.agents/skills/planner/resources/templates/retrospective.md) | Observed lessons, limitations and proposed improvements—not automatic permission to change the harness |
| [skill_creation_guide.md](./.agents/skills/planner/resources/templates/skill_creation_guide.md) | Skill metadata, body patterns, quality checks, and installation guidance verified against the actual assistant |

### Cross-template checklist

- [ ] A requirement identifier can be followed from brief to task to verification evidence.
- [ ] Brief and plan revision references identify what was actually approved.
- [ ] Approval and review fields are pending until a real decision is received.
- [ ] Expected output is clearly labeled as expected, not recorded as an observed result.
- [ ] An unrun command cannot look like a passing check.
- [ ] A manual check records its method and observation; its exit code is N/A.
- [ ] Execution state has an authoritative home rather than conflicting copies.
- [ ] Copied links are rewritten for the target artifact's location, including worktrees.
- [ ] The evaluation report can record every evaluation required by the plan.
- [ ] A reader can distinguish a source template, an illustrative example, and a completed project artifact.

**Paper exercise:** on a scratchpad, trace `FR-01: Reject blank titles` through a brief, one plan task, its acceptance check, and a verification row. Leave approvals pending and execution results NOT RUN. This tests information flow without pretending to execute the product.

## 6. Fourth pass: inspect the specialist skills

| File | Main question |
|---|---|
| [grill-with-docs/SKILL.md](./.agents/skills/grill-with-docs/SKILL.md) | Does it ask focused decision questions and keep domain terms separate from task history? |
| [subagent-driven-development/SKILL.md](./.agents/skills/subagent-driven-development/SKILL.md) | Does it preserve isolation, fresh implementers, ordered independent reviews, untrusted-input boundaries and evidence? |
| [test-driven-development/SKILL.md](./.agents/skills/test-driven-development/SKILL.md) | Does it require observing the intended failure before production changes, then Green and rechecking after refactoring? |
| [systematic-debugging/SKILL.md](./.agents/skills/systematic-debugging/SKILL.md) | Does it investigate causes before fixes, respect the shared task budget, and revalidate the fix? |

- [ ] Specialist skills agree with Phase 4 on reviewer independence and fallback.
- [ ] They do not introduce a second retry budget or reset the existing one.
- [ ] They do not override the brief, plan, or user permissions.
- [ ] Their live references lead to active phase documents, not the retired handoff stub.
- [ ] They remain relevant components of the Markdown toolkit, not mandatory separate applications.

## 7. Fifth pass: rationale, terminology, and optional references

### Rationale — [WHY_THIS_WORKS.md](./.agents/skills/planner/references/WHY_THIS_WORKS.md)

- [ ] Source-backed principles are separated from IntentFlow's own policy choices.
- [ ] Six source context types are distinguished from the local four-group planning checklist.
- [ ] Savings, repair times, and reliability are not presented as measured facts without evidence.
- [ ] The six phases allow iteration and re-approval, rather than implying a single rigid pass.
- [ ] “Change These Freely” style guidance is not mistaken for permission to change active project rules without authorization.
- [ ] The companion article is distinguished from a full review of the unavailable whitepaper text.

### Other reference files

- [ ] [GLOSSARY.md](./.agents/skills/planner/references/GLOSSARY.md): terms agree with how the skills and phases use them. This is workflow vocabulary; a generated project's `CONTEXT.md` is its domain vocabulary.
- [ ] [SCAFFOLDS.md](./.agents/skills/planner/references/SCAFFOLDS.md): catalog entries are discovery leads, not required installations or guarantees of compatibility.
- [ ] [resources/references/README.md](./.agents/skills/planner/resources/references/README.md): external project documents have an approved target-project location; shipped resources remain unchanged.
- [ ] [HANDOFF.md](./.agents/skills/planner/references/HANDOFF.md): clearly retired. Its historical status is not proof of current readiness.

**Important distinction:** retired `references/HANDOFF.md` is not the same thing as the active `resources/templates/handoff_artifact.md` template.

### Optional Agency Agents personas

Inspect the planner's **Step 4A** and the corresponding catalog/tooling guidance.

- [ ] Roles map to exact paths and a pinned commit before retrieval.
- [ ] Unneeded roles remain unmapped; the whole library is not pulled into context.
- [ ] Retrieval occurs only within authorized execution, not a planning-only request.
- [ ] Provenance and retrieved content are checked before adaptation.
- [ ] Selective retrieval is not described as a guaranteed automatic per-task loader.
- [ ] Illustrative Git commands are not claimed to be verified end-to-end for every environment.

Do not run the retrieval commands as part of this manual inspection.

## 8. Optional code-reference pass: all three scaffolds

These files exist in the toolkit, so an overall inspection should account for them. They are **optional adaptation references**, not requirements for using the Markdown workflow. Read their READMEs first. Do not install dependencies or run examples during this pass.

| Reference directory | Reading route | Main documented concerns to inspect |
|---|---|---|
| [crewai/](./.agents/skills/planner/resources/scaffolds/crewai/) | `README.md` → `src/your_project/main.py` → `crew.py` → `config/agents.yaml`, `config/tasks.yaml` → `tools/custom_tool.py` | Packaging and CLI arguments, tool compatibility, mock research, provider assumptions, telemetry and output collisions |
| [langchain/](./.agents/skills/planner/resources/scaffolds/langchain/) | `README.md` → `main.py` → `src/chain.py` → `config.py`, `prompts.py`, `output_parsers.py`, `tools.py` | Import-time client setup, incomplete integrations, mock search, tool binding versus execution, unsafe optional calculator |
| [langgraph/](./.agents/skills/planner/resources/scaffolds/langgraph/) | `README.md` → `main.py` and `langgraph.json` → `src/agent/graph.py` → `state.py`, `nodes.py`, `edges.py`, `prompts.py`, `tools.py` | Package/environment setup, research-to-writer data flow, unrestricted file access, persistence, approval boundaries and resource limits |

For each directory also inspect `requirements.txt`, `.env.example`, and its `__init__.py` files.

- [ ] README limitations match the code being shipped. Treat the table above as reading pointers, not a new runtime finding.
- [ ] Example environment values are placeholders, never real credentials.
- [ ] Dependency compatibility is not asserted merely because names appear in `requirements.txt`.
- [ ] Mock tools are not presented as real research or production integrations.
- [ ] File and network access would need explicit boundaries before adoption.
- [ ] Live model calls, telemetry and provider costs are visible to the adopter.
- [ ] Offline-test-first acceptance checklists describe future validation, not already completed tests.
- [ ] Any adoption requires a separate repair/validation plan. Inspection alone does not make these production-ready.

You do not need to repair these references to finish reviewing the core planning instructions. Record their limitations and decide whether their optional placement and warnings are clear enough.

## 9. Check connections across the whole project

Use your editor's project-wide text search. Include `.agents/` if hidden directories are excluded by default. Search results are inspection leads, not automatic defects.

| Search for | Compare and inspect |
|---|---|
| `planning-only` | Both modes, README, and phase guidance preserve the same stop boundary |
| `approval` / `approved` | Who approves what; exact revisions; no sample approval treated as a real decision |
| `fallback` / `reviewer` | All execution references agree with Phase 4's canonical fallback |
| `5` / `fix round` | One shared task budget; expected Red excluded; resume does not reset it |
| `install` / `npx` / `fetch` | Examples do not bypass separate permission or execute during a read-only review |
| `NOT RUN` / `N/A` / `BLOCKED` | Statuses are meaningful and cannot conceal missing required evidence |
| `trajectory` / `rubric` | Plan requirements flow into verification method and report fields |
| `HANDOFF.md` | Historical stub is not used as an active authority |
| `verified` / `production-ready` / `automatic` | Each claim has an appropriate scope and supporting evidence |
| `from the paper` | Local rules are not misattributed to the source |

### Link and formatting pass

- [ ] Every local file link opens from the document containing it.
- [ ] Heading links reach the intended section in your Markdown renderer.
- [ ] Tables display with the intended columns.
- [ ] Code fences close and do not swallow following sections.
- [ ] Skill metadata is consistent with the actual assistant's supported format.
- [ ] Placeholders are intentional in templates, not accidental omissions in user-facing guidance.
- [ ] No machine-specific output path is presented as a required path for all users.
- [ ] External links are clearly references; opening them does not authorize installing their contents.

This is structural/manual verification. Do not report a toolkit-wide test, lint, or typecheck pass unless an actual configured command was found and run. This guide does not establish such a command, and no new installation is needed to follow it.

## 10. After inspection: try the instructions on one real feature

This is a future optional trial, not something this guide has already performed. Use an existing low-risk project with working tests and no need for paid calls or new dependencies.

### Start with planning only

Give the assistant this prompt, replacing the bracketed target path:

```text
Read .agents/AGENTS.md and .agents/skills/planner/SKILL.md from IntentFlow.
Target project: [absolute path to my existing project].
Plan only for one small feature using the existing stack and tools.
Inspect current behavior and available test commands, then ask me about
unresolved requirements. Draft the intent brief, domain glossary, and plan
in the target project without modifying IntentFlow's shipped templates.
Keep approvals pending until I actually give them.
Do not install, retrieve personas, copy scaffolds, implement, commit,
push, create a PR, or deploy.
```

Observe whether the assistant produces clear, project-specific artifacts and stops. Check those artifacts using Sections 4 and 5 of this guide. An approved plan can still be the final deliverable if that is all you want.

### Only if you then choose execution

1. Review and approve the actual brief revision. Resolve blocking decisions first.
2. Review and approve the actual plan revision, including checks, workspace, and reviewer availability.
3. Explicitly request implementation within that scope. Keep separate permissions separate.
4. Observe the real failing test, minimal implementation, passing test, and applicable regression checks.
5. Require the specified independent reviews. Missing reviewer capability must remain visible; it cannot be solved by invented human approvals.
6. Inspect the final requirement-to-evidence matrix and handoff. Verify the product behavior yourself where practical.
7. Keep commits, publication and deployment out of scope unless you separately authorize them.

**Success means both:** the feature works against its agreed requirements, and the assistant respected the agreed process. Neither a neat plan nor two passing fixture tests alone establishes end-to-end workflow compliance.

The earlier temporary demonstration was not a valid workflow-wide acceptance run. Do not reuse its corrected approval records as approval for this trial.

## 11. Record findings and make your decision

Use a scratchpad or a separate review record; do not write findings into shipped templates.

| ID | File and heading/line | Observation and evidence | Severity | Proposed next action | Status |
|---|---|---|---|---|---|
| REVIEW-01 | [location] | [what you actually observed] | [blocker / improvement / question] | [specific action] | [open / resolved / not checked] |

### Severity guide

- **Blocker:** instructions authorize unwanted work, fabricate evidence, contradict an essential gate, lose required handoff data, or prevent the intended user from following the core path.
- **Improvement:** clearer wording, a better example, less repetition, or easier navigation without changing the rules.
- **Question:** a policy choice you must decide, such as whether the current review rigor suits your intended users.

### Finish with a scoped conclusion

- [ ] Core instructions and their connections have been inspected.
- [ ] All template and specialist-skill families have been covered.
- [ ] Optional references and known limitations are accounted for.
- [ ] Unchecked items and unresolved blockers are listed explicitly.
- [ ] Any actual product trial is reported separately from documentation inspection.
- [ ] No approval, test result, reviewer verdict, or reliability claim has been invented.

Choose one conclusion supported by your observations:

- **Ready for a planning trial:** the core Markdown is usable enough to test on a real project's plan.
- **Needs documentation fixes:** list the specific blocking files and issues before trialing it.
- **Limited real-project trial completed:** state the exact feature, observed evidence, remaining gaps and whether the required process was satisfied. Do not generalize one trial into a guarantee of product quality.

Your immediate next step is the three-file reading route in Section 3. You do not need to build an application, install a framework, or launch a separate pipeline to begin.

