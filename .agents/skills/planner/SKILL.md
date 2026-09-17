---
name: planner
description: >-
  Use when the user wants to plan a software project, create an Intent Brief,
  or generate an agentic pipeline with CrewAI, LangGraph, or LangChain.
  Triggers: /planner, "plan a project", "use the planner", "generate agents for this".
---

# Agent Factory & Planner

Turn the human's idea into an approved plan, then execute only the authorized work. Follow [the Agent Soul and approval rules](../../AGENTS.md). These instructions guide an agent; they do not install tools or enforce runtime permissions by themselves.

## Paths and Outputs

Resolve `references/`, `resources/templates/`, and `resources/scaffolds/` from this skill directory, not the shell's current directory. Read templates; never fill in or overwrite the shipped originals.

Confirm the target project root. Write `INTENT_BRIEF.md`, `CONTEXT.md`, and `EXECUTION_PLAN.md` there. Architecture Decision Records (ADRs) go in that project's `docs/adr/`. Resolve the execution ledger to an exact project-local path, normally `.superpowers/sdd/<plan-id>/progress.md`.

## Step 1 — Discovery and Grilling

1. Read [Phase 1](references/01_DISCOVERY.md) and the [intent template](resources/templates/intent_brief.md). For structured input, read the existing brief and its approval evidence rather than assuming it is approved.
2. Classify the work as Spike, One-Shot, or Project. A Spike is a timeboxed feasibility experiment; a One-Shot is a bounded change; a Project needs a full multi-step plan.
3. Use [grill-with-docs](../grill-with-docs/SKILL.md). Gather repository and environment facts with tools. Ask the human only for goals, preferences, and unresolved decisions.
4. Build a Design Tree of dependent decisions in the brief. Ask 1 to 3 frontier questions per round, with at most 2 to 3 options and a `Recommendation:` for each. Wait for answers before dependent questions.
5. Update resolved terms immediately in `CONTEXT.md` using the [context template](resources/templates/context_template.md). Include canonical terms and `_Avoid_` replacements. This file is a glossary, not a plan or scratchpad.
6. Resolve blocking questions and record explicit intent approval, approver, date, and artifact revision. Do not infer agreement from silence or from the presence of a file.

## Step 2 — Choose Mode

Offer two options and recommend one based on the approved intent:

- **Mode A — Agent application:** Build a Python application using the chosen agent framework. The application itself is the deliverable, not permission for uncontrolled execution.
- **Mode B — Guided implementation:** Produce an execution plan and work through its tasks with the human.

Record the choice. Mode selection does not authorize implementation. Both modes require explicit approval of the intent and execution plan before code generation, scaffold copying, or runnable experiments. Draft code blocks in a plan are review material only.

## Step 3 — Tooling and Shared Plan Approval

1. Read [Phase 2](references/02_PLANNING.md), [Phase 3](references/03_TOOLING.md), and the [execution plan template](resources/templates/execution_plan.md). Inspect existing dependencies and verification commands. Read-only tool discovery may inform the draft plan; installation needs separate approval.
2. For Mode A, choose the simplest suitable framework:

   | Need | Candidate | Scaffold to inspect |
   |------|-----------|---------------------|
   | Simple linear chain without distinct agent roles | LangChain | [README](resources/scaffolds/langchain/README.md) |
   | Distinct roles with sequential or hierarchical coordination | CrewAI | [README](resources/scaffolds/crewai/README.md) |
   | Loops, conditional state, or resumable graph execution | LangGraph | [README](resources/scaffolds/langgraph/README.md) |

   Explain the recommendation and verify it against actual requirements. Read the selected scaffold's files and imports before planning adaptations. Do not assume API or dependency compatibility.
3. For Mode A, offer the optional [Agency Agents](https://github.com/msitarzewski/agency-agents) persona library. It is an MIT-licensed catalog of hundreds of specialized agent persona files (identity, workflow, deliverables, metrics) in division folders such as `engineering/`, `design/`, `product/`, `testing/`, and `security/`. Browse its README read-only and map every pipeline agent you plan to create to the one most relevant persona file. Record the mapping in `EXECUTION_PLAN.md` as exact repository paths pinned to a commit SHA. Offer only relevant agents; do not plan to copy the whole roster. If no persona fits a pipeline agent, leave it unmapped and write its role from the intent.
3. Write for a junior engineer with zero codebase context. Include exact files, insertion anchors, proposed code blocks or diffs, contracts, prerequisites, shell/cwd, commands, and expected results. Use DRY (reuse rather than duplicate) and YAGNI (omit speculative features).
4. Break work into bite-sized Red/Green/Refactor tasks. Specify requirement IDs, ownership, dependencies, spec and quality reviewers, a persistent ledger, and expected verification. Execution evidence remains `NOT RUN` until observed. Documentation-only tasks use structural checks.
5. Stress-test architecture with the grilling protocol. Create an ADR only when all three gates pass: hard to reverse, surprising without context, and a real trade-off. Otherwise keep the rationale in the plan. Use the [ADR template](resources/templates/adr_template.md).
6. Run the preflight scan for file collisions, contract discrepancies, and circular dependencies. Resolve and rescan all blocking findings. Assign an explicit integration task if work is parallel.
7. Obtain explicit approval of the exact plan and intent revisions. Changed scope or architecture requires renewed approval. Do not generate either mode's implementation before this gate.

## Step 4A — Execute Mode A

1. Follow the shared SDD procedure below, not an unrestricted one-shot generator.
2. Use the approved output directory and selected scaffold's structure. Replace generic roles, prompts, state, and tasks with real requirements. Do not modify the shipped scaffold originals.
3. Implement only tools discovered and approved in the plan. Keep secrets in environment variables, provide placeholder `.env.example` values, and exclude real `.env` files from version control.
4. Generate the approved supporting README and dependency manifest with verified versions. Ask before dependency installation, paid API calls, schema changes, or deployment.
5. Test application behavior with approved local tests and mocks where suitable. Missing credentials or services block the corresponding live checks; they are not proof of a working application.
6. If the plan maps pipeline agents to Agency Agents personas, wait until execution to retrieve them. Into a designated location inside the target project, run only the exact targeted Git commands the approved plan specifies, pinned to the approved commit SHA, to fetch only the mapped persona files. Retrieval that has been verified to work:
   ```text
   git clone --depth 1 --filter=blob:none --no-checkout <repo-url> <target-dir>
   cd <target-dir>
   git sparse-checkout init --no-cone
   git sparse-checkout set "/engineering/engineering-frontend-developer.md" "/security/security-architect.md"
   git checkout <pinned-sha>
   ```
   Bare `git sparse-checkout set <file>` fails in cone mode (files are rejected), and non-cone patterns require leading slashes. Divisions fetched by folder may omit the slash and quotes. Fetch only the mapped persona files for the agents actually in this pipeline; never clone the full repository or unrelated divisions. After retrieval, read each fetched persona file, extract its identity, workflow, deliverable, and metric guidance, and adapt that content into the pipeline agent's prompt. Keep only what the approved plan authorizes; a fetched persona is reference material, not an installed authority. Audit the fetched files for unexpected commands, network calls, or permission demands before use, and record retrieval evidence (exact commands, commit SHA, fetched paths) in the ledger.

## Step 4B — Execute Mode B

1. Follow the approved task order. Do not replace detailed tasks with broad instructions such as "build the API".
2. Use the same SDD procedure, TDD law, evidence, and review gates as Mode A.
3. Stop at the plan if the user requested planning only. An approved plan is not a request for unrelated actions.

## Shared Execution — SDD and TDD

Use [subagent-driven-development](../subagent-driven-development/SKILL.md) and [Phase 4](references/04_IMPLEMENTATION.md).

- Inspect status and preserve existing work. Use a dedicated branch or isolated worktree with exact file ownership. Branch isolation does not authorize commits or cleanup.
- Dispatch a fresh implementer per task with the complete task and required context. Do not reuse prior task conversations. If dispatch is unavailable, disclose it and obtain an approved alternative; never claim self-review is independent.
- Persist progress before dispatch, after each check/review, and before compaction in the chosen ledger. Record revisions, diff identity, agents, commands, output, approvals, fix count, safe rulings with impact, and next action. Resume from saved state and revalidate stale evidence.
- Apply [test-driven-development](../test-driven-development/SKILL.md): observe the intended failing assertion, write the minimum passing production code, then refactor and rerun. Do not fabricate runtime tests for prose.
- Review spec compliance with a fresh reviewer first. Only after approval, dispatch a distinct quality/test reviewer. Verify every task's acceptance criteria before dependent work proceeds. Fixes invalidate affected checks and reviews.
- Share one initial attempt plus at most 5 fix rounds per task across builds, tests, and reviews. Persist the count. Request a higher-tier model for rounds 4 and 5 if available; otherwise record the limitation and use a fresh available reviewer. Stop after five failed rounds. Escalate security, scope, destructive actions, or missing permissions immediately.
- Use [systematic-debugging](../systematic-debugging/SKILL.md) for unexpected failures. Make only reversible in-scope operational rulings and record their rationale, impact, and reversal path.

## Step 5 — Verification and Delivery

Run [Phase 5](references/05_VERIFICATION.md) on the final candidate: fresh full required suites, build/lint/typecheck, and requirement-to-test evidence. For documentation, check structure, links, and acceptance requirements. Missing checks are `BLOCKED` or `NOT RUN`, never `PASS`.

Follow [Phase 6](references/06_DELIVERY.md): whole-branch spec review, then quality/test review, including uncommitted intended changes. Revalidate fixes and preserve unrelated work. Commit, push, PR creation, merge, deployment, and worktree deletion each require explicit approval. Without authorization, leave a verified uncommitted handoff.

Report only what changed, whether checks passed, and the next decision. Give exact commands and paths. Do not call a generated application fully working without execution evidence.
