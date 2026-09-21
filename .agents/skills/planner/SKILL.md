---
name: planner
description: >-
  Use when the user wants to plan a software project, create an Intent Brief,
  or generate an agentic pipeline with CrewAI, LangGraph, or LangChain.
  Triggers: /planner, "plan a project", "use the planner", "generate agents for this".
---

# Agent Factory & Planner / Advisor

Turn the human's idea into an approved plan, then equip only the authorized, right-sized tools. Follow [the Agent Soul and approval rules](../../AGENTS.md). As a **Planner & Advisor**, you guide the human on choosing the right tools while strictly preventing tooling bloat and unnecessary overhead.

This Planner utilizes **Advanced Agentic Planning Architectures**:
- **Plan-and-Execute:** Fully decouple the planning reasoning from the execution loop.
- **ReWOO / LLMCompiler:** Pre-compute dependency graphs and parallelizable tasks before executing tools.
- **Reflexion:** Build self-evaluating and correcting feedback loops into the generated task pipeline.
- **Lean Tooling / Anti-Bloat:** Strive for the Minimum Viable Harness (≤ 3–5 tools). Reject overlapping or overpowered tools. Prefer token-efficient AXI CLIs over heavy MCP servers where available.
- **Host OS & Harness Environment Profiling:** Detect Host OS (Windows, macOS, Linux) and active AI harness (Antigravity, Claude Code, Cursor, Cline, etc.). Prioritize tools with first-party support/tutorials for the active harness; strictly ignore or postpone unlisted tools (e.g., tools without verified Antigravity support) to prevent operational hazards.

## Paths and Outputs

Resolve `references/`, `resources/templates/`, and `resources/scaffolds/` from this skill directory, not the shell's current directory. Read templates; never fill in or overwrite the shipped originals.

Confirm the target project root. Write `INTENT_BRIEF.md`, `CONTEXT.md`, and `EXECUTION_PLAN.md` there. Architecture Decision Records (ADRs) go in that project's `docs/adr/`. Resolve the execution ledger to an exact project-local path, normally `.superpowers/sdd/<plan-id>/progress.md`.

## Step 1 — Discovery and Grilling

1. Read [Phase 1](references/01_DISCOVERY.md) and the [intent template](resources/templates/intent_brief.md). For structured input, read the existing brief and its approval evidence rather than assuming it is approved.
2. Classify the work as Spike, One-Shot, or Project. A Spike is a timeboxed feasibility experiment; a One-Shot is a bounded change; a Project needs a full multi-step plan.
3. Use [grill-with-docs](../grill-with-docs/SKILL.md). Gather repository and environment facts with tools (Host OS, terminal shell, and Active AI Harness). Ask the human only for goals, preferences, and unresolved decisions.
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
2. **Apply Lean Tooling & Environment Compatibility Protocol:**
   - **Environment Profiling:** Inspect Host OS and Active AI Harness. Tools with tutorials/verified support for the active harness (e.g., Claude Code, Cursor) are prioritized. Unlisted tools without verified support for the active harness (e.g., Antigravity) are postponed or ignored to prevent operational hazards. Tools requiring native Unix daemons (e.g., `tmux` in Firstmate) are blocked on native Windows unless inside WSL.
   - **Enforce Anti-Bloat Tool Budget:** Keep active tools capped (≤ 3–5 active tools/skills per phase). Do not equip tools "just in case".
   - **Prefer AXI over MCP:** Check for [AXI CLIs](https://axi.md/) (`gh-axi`, `chrome-devtools-axi`, `sqlite-axi`, etc.) before installing heavy MCP servers. AXI tools cut token costs by ~40% and eliminate persistent JSON-RPC daemon overhead. Use MCP only as an ecosystem fallback when no AXI exists.
   - **Right-Size the Execution Scaffold:**
     - For small projects/spikes: Single agent (Cursor, Aider, Roo Code).
     - For strict quality & TDD: **Superpowers** (`obra/superpowers`).
     - For large parallel multi-task production pipelines: **Firstmate** (`kunchenguid/firstmate`) (requires Unix/WSL). Warn the human that Firstmate is overpowered and introduces excessive overhead for small projects.
     - For PR gating: Recommend **no-mistakes** (`kunchenguid/no-mistakes`) only when using unopinionated harnesses (Aider, Claude Code, Cline). **Skip `no-mistakes` if using Superpowers** to prevent redundant review loops and worktree conflicts.
3. For Mode A, choose the simplest suitable framework:

   | Need | Candidate | Scaffold to inspect |
   |------|-----------|---------------------|
   | Simple linear chain without distinct agent roles | LangChain | [README](resources/scaffolds/langchain/README.md) |
   | Distinct roles with sequential or hierarchical coordination | CrewAI | [README](resources/scaffolds/crewai/README.md) |
   | Loops, conditional state, or resumable graph execution | LangGraph | [README](resources/scaffolds/langgraph/README.md) |

    Explain the recommendation and verify it against actual requirements. Read the selected scaffold's files, imports, and readiness warnings before planning adaptations. These are unvalidated reference layouts, not runnable starters. Include setup, safety repairs, offline tests, and dependency validation as approved tasks before live execution. Reuse an existing project's stack by default; no new scaffold or tool is a valid outcome.
4. For Mode A, offer the optional [Agency Agents](https://github.com/msitarzewski/agency-agents) persona library. It is an MIT-licensed catalog of hundreds of specialized agent persona files (identity, workflow, deliverables, metrics) in division folders such as `engineering/`, `design/`, `product/`, `testing/`, and `security/`. Browse its README read-only and map every pipeline agent you plan to create to the one most relevant persona file. Record the mapping in `EXECUTION_PLAN.md` as exact repository paths pinned to a commit SHA. Offer only relevant agents; do not plan to copy the whole roster. If no persona fits a pipeline agent, leave it unmapped and write its role from the intent.
5. Write for a junior engineer with zero codebase context. Include exact files, insertion anchors, proposed code blocks or diffs, contracts, prerequisites, shell/cwd, commands, and expected results. Use DRY (reuse rather than duplicate) and YAGNI (omit speculative features).
6. Break work into bite-sized tasks. Specify requirement IDs, ownership, dependencies, and expected verification criteria for each task.
7. Stress-test architecture with the grilling protocol. Create an ADR only when all three gates pass: hard to reverse, surprising without context, and a real trade-off. Otherwise keep the rationale in the plan. Use the [ADR template](resources/templates/adr_template.md).
8. Run the preflight scan for file collisions, contract discrepancies, and circular dependencies. Resolve and rescan all blocking findings. Assign an explicit integration task if work is parallel.
9. Obtain explicit approval of the exact plan and intent revisions. Changed scope or architecture requires renewed approval. Do not generate implementation code.

For planning-only requests in either mode, stop here and hand over the brief, glossary, and plan with their actual approval status and outstanding execution prerequisites. Do not retrieve personas, install dependencies, copy scaffolds, or start implementation. Plan approval alone does not expand a planning-only request into execution.

## Step 4 — In-Project Tool Installation & Handoff Transition

1. **Pre-Install Conflict, Bloat & OS Safety Check**: Follow [Phase 3 §3.7](references/03_TOOLING.md#step-37--in-project-tool-installation--conflict-safety-check). Inspect for OS/platform hazards (e.g., native Windows vs Unix daemons), harness incompatibility (e.g., unverified Antigravity hooks), port/stdio collisions, `.env` collisions, scaffold rule collisions (`AGENTS.md`), redundant PR gatekeepers (`no-mistakes` vs Superpowers), and excessive fleet overhead (`firstmate` on small projects).
2. **Install Approved Tools**: With explicit human approval, install tools directly in the project folder:
   - Mandatory: configure [`rtk-ai/rtk`](https://github.com/rtk-ai/rtk) for token and log optimization.
   - Configure approved AXI runners or MCP servers in `.cursor/mcp.json` or `.claude/mcp.json`.
   - Install approved project dependencies and create `.env.example`.
3. **Transition `AGENTS.md` (Prevent Rule Conflict)**:
   - Archive planner reference documents (`references/`, templates) into `.planning/` so the workspace is clean.
   - Update `AGENTS.md` from "Planner Only" mode to "Execution Mode" (or yield root governance if an external harness like ECC provides its own rules), authorizing the coding agent to build the tasks in `EXECUTION_PLAN.md`.
4. **Handoff**: The project folder is now fully equipped and ready for the execution agent (ECC, Superpowers, Firstmate, Cursor, Cline, etc.) to begin building.

*End of Planner instructions. Remind the user they are ready to build!*
