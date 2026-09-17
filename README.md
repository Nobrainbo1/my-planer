# Agentic Engineering Workflow Template
**Framework:** Agentic SDLC  
**Origin:** Inspired by *"The New SDLC With Vibe Coding"* — Addy Osmani, Shubham Saboo, Sokratis Kartakis (Google, 2026)  
**Purpose:** A universal, harness-agnostic foundation for orchestrating AI agents through a full software development lifecycle.

---

## Philosophy

> **"Structure scales, vibes don't."**  
> **"Generation is solved. The craft is now specifying, constraining, and verifying."**

This template transforms you from a "vibe coder" (ad-hoc prompt-and-ship) into an **Agentic Engineer** — an orchestrator who designs intent, governs execution, and validates output.

An AI agent is not just a model. It is a **Model + Harness**. The model is the engine; the **harness** — instructions, rule files, tools, sandboxes, observability — is where engineering happens. This template IS the harness blueprint.

---

## Structure

This workflow is a **modular system of Markdown files**, each handling one phase of the Agentic SDLC. They are designed to be read by any top AI coding harness:

| File | Phase | Purpose |
|------|-------|---------|
| [`WHY_THIS_WORKS.md`](./.agents/skills/planner/references/WHY_THIS_WORKS.md) | **Start here** | The thinking behind every design decision — teaches you to build workflows without AI |
| [`GLOSSARY.md`](./.agents/skills/planner/references/GLOSSARY.md) | Reference | Plain-English definitions of AI coding terms (model, harness, context, handoff, etc.) |
| [`AGENTS.md`](./.agents/AGENTS.md) | Global | Universal agent rules, identity & orchestrator mindset |
| [`SCAFFOLDS.md`](./.agents/skills/planner/references/SCAFFOLDS.md) | Reference | Catalog of scaffolds, skills, MCP servers, and harnesses by project type |
| [`01_DISCOVERY.md`](./.agents/skills/planner/references/01_DISCOVERY.md) | Phase 1 | Scope classification, discovery interviews, live domain glossary, intent approval |
| [`02_PLANNING.md`](./.agents/skills/planner/references/02_PLANNING.md) | Phase 2 | Exact execution tasks, architecture decision gates, preflight conflict checks |
| [`03_TOOLING.md`](./.agents/skills/planner/references/03_TOOLING.md) | Phase 3 | Tool, skill, and optional persona discovery and evaluation |
| [`04_IMPLEMENTATION.md`](./.agents/skills/planner/references/04_IMPLEMENTATION.md) | Phase 4 | Fresh subagents, ordered independent reviews, TDD, persistent execution ledger |
| [`05_VERIFICATION.md`](./.agents/skills/planner/references/05_VERIFICATION.md) | Phase 5 | Fresh evidence, systematic debugging, security checks, requirement coverage |
| [`06_DELIVERY.md`](./.agents/skills/planner/references/06_DELIVERY.md) | Phase 6 | Whole-branch review, approved delivery, handoff, retrospective |
| [`templates/`](./.agents/skills/planner/resources/templates/) | — | Intent brief, context, execution plan, ADR, tool discovery, handoff, verification, task log, retrospective |

## Reading Order — For Humans

Use the links in the Structure table. Phase and supporting references live in `.agents/skills/planner/references/`; shipped templates live in `.agents/skills/planner/resources/templates/`.

1. `WHY_THIS_WORKS.md` — understand the thinking behind every phase.
2. `README.md` (this file) — see the full structure.
3. `GLOSSARY.md` — look up terms as you go.
4. `.agents/AGENTS.md` — understand agent identity and your role as orchestrator.
5. `01_DISCOVERY.md` — draft project-local `INTENT_BRIEF.md`, maintain live `CONTEXT.md`, and obtain explicit intent approval.
6. `02_PLANNING.md` — draft project-local `EXECUTION_PLAN.md` and obtain explicit approval of both exact artifact revisions before any code, including a Spike.
7. `SCAFFOLDS.md` and `03_TOOLING.md` — read-only discovery can inform planning; installation needs separate approval.
8. `04_IMPLEMENTATION.md` — execute approved tasks with SDD and TDD.
9. `05_VERIFICATION.md` — collect evidence before shipping.
10. `06_DELIVERY.md` — obtain delivery approvals and write a project-local retrospective from the template; preserve shipped originals.

---

## Harness Compatibility

These files use **standard Markdown with optional YAML frontmatter**, making them natively readable by:

| Harness | Config Location | Notes |
|---------|----------------|-------|
| **Cursor** | `.cursor/rules/*.mdc` | Copy relevant sections into `.mdc` files with globs |
| **Cline / Roo Code** | `.clinerules/*.md` | Drop files directly into `.clinerules/` |
| **Claude Code** | `CLAUDE.md` | Merge into root `CLAUDE.md` |
| **GitHub Copilot** | `.github/copilot-instructions.md` | Merge into instructions file |
| **Antigravity** | `.gemini/config/skills/` or `AGENTS.md` | Use as skills or drop `AGENTS.md` at root |
| **Windsurf** | `.windsurfrules` | Merge into rules file |
| **Any LLM** | System prompt | Paste relevant phases into context |

---

## Skills

| Skill | Purpose |
|-------|---------|
| [planner](./.agents/skills/planner/SKILL.md) | Orchestrate discovery, approved planning, execution, and delivery |
| [grill-with-docs](./.agents/skills/grill-with-docs/SKILL.md) | Standalone discovery interviews, live domain glossary, and architecture decisions |
| [subagent-driven-development](./.agents/skills/subagent-driven-development/SKILL.md) | Standalone task execution with fresh implementers and ordered independent reviews |
| [test-driven-development](./.agents/skills/test-driven-development/SKILL.md) | Standalone Red/Green/Refactor discipline |
| [systematic-debugging](./.agents/skills/systematic-debugging/SKILL.md) | Standalone evidence-led root-cause diagnosis and verified fixes |

Invocation depends on harness discovery and configuration; these files do not guarantee slash-command registration. If a skill is not discovered, explicitly ask the harness to read its linked `SKILL.md`. Standalone use does not bypass approval gates.

## Planner Modes and Optional Personas

- **Mode A — Agent application:** Build an agent application using the simplest suitable framework: CrewAI, LangGraph, or LangChain.
- **Mode B — Guided implementation:** Create an approved execution plan and work through its tasks with the human.

Mode A can optionally use the [Agency Agents](https://github.com/msitarzewski/agency-agents) persona library. During planning, browse the catalog read-only and map relevant pipeline roles to exact persona file paths and a pinned commit SHA in `EXECUTION_PLAN.md`. Leave roles without a suitable match unmapped.

Retrieve mapped personas only during approved execution using selective Git sparse checkout, then audit and adapt their guidance and record retrieval evidence in the ledger. This is plan-scoped retrieval, not an automatic per-task lazy loader. Mode B and plans without persona mappings do not retrieve this library. Persona documents are reference material, not executable agents or permission to install tools.

The four local workflow skills above are permanent workflow components, not sandbox test artifacts or Agency Agents downloads. Load their instructions when the workflow calls for them; external tool and skill installation requires separate approval. These Markdown instructions depend on the consuming harness for execution and enforcement.

## Integration Status

The eight-task documentation handoff is complete: agent communication rules, discovery interviews, domain glossary, detailed planning and architecture decisions, reusable templates, subagent execution and test-first development, evidence-led verification and delivery, and planner/standalone skill integration. The original session specification is retained only as a retired `HANDOFF.md` stub; the rules, skills, and phase references are the maintained documentation.

Verification covered documentation structure, local links, frontmatter, and cross-file policy consistency. It does not establish runtime enforcement or application correctness. No application test, lint, or typecheck pass is claimed for this documentation integration.

## How to Use This Template

**Shared gate:** Spike, One-Shot, and Project work all require explicit human approval of both project-local `INTENT_BRIEF.md` and `EXECUTION_PLAN.md` before any implementation code, scaffold copying, or runnable experiment. Record approver, date, and exact artifact revisions; file presence, silence, and mode selection are not approval. Changed scope or architecture requires renewed approval. Read-only discovery may inform planning; installation needs separate approval.

Confirm the target project root. Read the shipped [templates](./.agents/skills/planner/resources/templates/) and create project-local artifacts; never fill in or overwrite shipped template or scaffold originals. Maintain live `CONTEXT.md` from the [context template](./.agents/skills/planner/resources/templates/context_template.md): record resolved canonical terms and `_Avoid_` replacements immediately, not at the end. It is a glossary, not a plan or scratchpad.

### Quick Start — Minimal Path
Small tasks use shorter artifacts, not weaker gates:
1. **Load the rules and planner** from `.agents/AGENTS.md` and `.agents/skills/planner/SKILL.md` using your harness's supported instruction mechanism; preserve their relative paths.
2. **Discover and plan** using Phases 1–3. Create `INTENT_BRIEF.md`, live `CONTEXT.md`, and `EXECUTION_PLAN.md` at the target root from template copies. Obtain explicit approval of both exact brief and plan revisions before any code, even for a Spike.
3. **Execute and verify** the approved tasks using the shared SDD/TDD procedure below and Phases 4–6. Keep evidence and obtain separate delivery permissions.

### Full Workflow — For New Projects
1. **Make the workflow available** with its `.agents/` layout intact and load the rules through your harness. Confirm a separate target project root for working artifacts; preserve shipped originals.
2. **Start with Phase 1 discovery** and `grill-with-docs`. Classify the work, resolve blocking decisions, create `INTENT_BRIEF.md`, update live `CONTEXT.md`, and record explicit intent approval.
3. **Use Phases 2–3 to plan**. Choose an agent application or guided implementation, inspect tools read-only, and create `EXECUTION_PLAN.md` with exact files, contracts, Red/Green/Refactor tasks, reviewers, and verification commands. Obtain explicit approval of both exact brief and plan revisions before any code, scaffold copying, or runnable Spike.
4. **Execute Phases 4–6** using the shared SDD/TDD procedure below. Verify the final candidate, obtain delivery permissions, and create project-local handoff and retrospective artifacts from templates without changing shipped originals.

### Full Workflow — For Existing Projects
1. **Inspect the repository read-only** and load the rules. Use Phase 1 to establish or revise `INTENT_BRIEF.md` for the feature or refactor; verify approval evidence rather than assuming an existing brief is approved. Maintain live `CONTEXT.md` as terms are resolved.
2. **Audit tooling and plan with Phases 2–3**. Preserve existing work and shipped originals; write the project-local `EXECUTION_PLAN.md`. Obtain explicit approval of both exact brief and plan revisions before any code, scaffold copying, or runnable Spike. Tool installation needs separate approval.
3. **Execute Phases 4–6** using the shared SDD/TDD procedure below, revalidate affected checks after fixes, and leave a verified handoff unless delivery actions are explicitly authorized.

### Shared Execution — SDD and TDD
- **Subagent-Driven Development (SDD):** Use an isolated workspace and a fresh implementer per approved task. Persist progress and evidence in a project-local ledger, normally `.superpowers/sdd/<plan-id>/progress.md`. Review spec compliance first, then quality/tests with a distinct fresh reviewer. If dispatch is unavailable, disclose it and obtain an approved alternative; self-review is not independent review.
- **Test-Driven Development (TDD):** Observe the intended failing test, write minimum passing production code, then refactor and rerun checks. Documentation-only work uses structural and link checks, not fabricated runtime tests.
- **Verify and deliver:** Run required tests, build, lint, and typecheck on the final candidate. Record missing checks as `BLOCKED` or `NOT RUN`. Use `systematic-debugging` for unexpected failures. Commit, push, PR creation, merge, deployment, and worktree deletion each require explicit approval.

---

## The Agentic SDLC at a Glance

```text
 ┌─────────────────────────────────────────────────────────┐
 │                  ORCHESTRATOR (Human)                   │
 │       Judgment · Verification · Direction · Safety      │
 └───────────────────────────┬─────────────────────────────┘
                             │
 ┌───────────────────────────▼─────────────────────────────┐
 │ 1. DISCOVERY          ▶   2. PLANNING                   │
 │ (Intent & Scope)          (Context & Execution Plan)    │
 └───────────────────────────┬─────────────────────────────┘
                             │
                    🛑 CHECKPOINT 1: Intent + Execution Plan Approval
                             │
 ┌───────────────────────────▼─────────────────────────────┐
 │ 3. TOOLING            ▶   4. IMPLEMENTATION             │
 │ (Discover & Equip)        (Builder-Validator Loop)      │
 └───────────────────────────┬─────────────────────────────┘
                             │
                    🛑 CHECKPOINT 2: Implementation Review
                             │
 ┌───────────────────────────▼─────────────────────────────┐
 │ 5. VERIFICATION       ▶   6. DELIVERY                   │
 │ (Evals & DoD)             (Package & Retrospective)     │
 └───────────────────────────┬─────────────────────────────┘
                             │
                    🛑 CHECKPOINT 3: Deployment Approval
```

---

## Cost Curve Awareness

The paper presents a critical insight about the **CapEx/OpEx tradeoff**:

| Approach | Upfront Cost (CapEx) | Long-term Cost (OpEx) | Best For |
|----------|---------------------|-----------------------|----------|
| **Vibe Coding** | 🟢 Low | 🔴 High (debugging, maintenance, rewrites) | Prototypes, scripts, hackathons |
| **Agentic Engineering** | 🟡 Medium | 🟢 Low (structured, maintainable, governed) | Production systems, team projects |

This template applies Agentic Engineering rigor while preserving the speed of vibe coding for early exploration phases.

---

## What Makes a Good Agentic Engineer (Orchestrator)

The paper's core thesis is that **"generation is solved"** — the new craft is *specifying, constraining, and verifying*. Here is what the research says makes a great orchestrator:

### Mindset Shift
| Old Mindset | New Mindset |
|------------|-------------|
| "I write code" | "I design intent and govern execution" |
| "Prompt better" | "Engineer better context" |
| "Use one AI tool" | "Orchestrate an ensemble of agents" |
| "Ship fast" | "Ship structured — then iterate fast" |
| "Learn the framework" | "Learn to decompose, delegate, and verify" |

### Core Skills

1. **Task Decomposition** — Break complex problems into narrow, specialized sub-tasks that agents can handle independently.
2. **Context Engineering** — Design the complete information package (instructions, codebase maps, tool definitions, memory) that an agent consumes. Quality of context bounds quality of output.
3. **Spec-Driven Development** — Write executable contracts (Intent Briefs, acceptance criteria) instead of conversational prompts. Specs are the source of truth.
4. **Evaluation Design** — Build automated quality gates that monitor agent performance, output accuracy, and cost in real-time. "Evals, not vibes."
5. **Harness Design** — Configure the Model + Harness stack: rules files, tool permissions, sandbox boundaries, and observability.
6. **Scaffold Awareness** — Know the ecosystem of existing frameworks, MCP servers, and starter templates (see [`SCAFFOLDS.md`](./.agents/skills/planner/references/SCAFFOLDS.md)). Discover before you build.
7. **Bounded Autonomy** — Set clear limits on what agents can do without approval. The most reliable systems give agents freedom within strict guardrails.
8. **Retrospective Discipline** — After every project, evolve the harness. Update rules, add skills, remove friction. The workflow improves with every cycle.

### The Complexity Ladder
Start simple and only escalate when necessary:
```
Single Agent → Sequential Pipeline → Orchestrator-Worker → Parallel Fan-Out → Hierarchical Multi-Agent
```
Most projects should start at "Single Agent" and only move right when task complexity demands it.
