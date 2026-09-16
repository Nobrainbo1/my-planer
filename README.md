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
| [`WHY_THIS_WORKS.md`](./WHY_THIS_WORKS.md) | **Start here** | The thinking behind every design decision — teaches you to build workflows without AI |
| [`GLOSSARY.md`](./GLOSSARY.md) | Reference | Plain-English definitions of AI coding terms (model, harness, context, handoff, etc.) |
| [`AGENTS.md`](./AGENTS.md) | Global | Universal agent rules, identity & orchestrator mindset |
| [`SCAFFOLDS.md`](./SCAFFOLDS.md) | Reference | Catalog of scaffolds, skills, MCP servers, and harnesses by project type |
| [`01_DISCOVERY.md`](./01_DISCOVERY.md) | Phase 1 | Intent definition, constraints, stakeholder alignment |
| [`02_PLANNING.md`](./02_PLANNING.md) | Phase 2 | Context engineering, execution plan, detail-level toggle |
| [`03_TOOLING.md`](./03_TOOLING.md) | Phase 3 | Tool & skill discovery, evaluation, and creation (MCP, Skills, APIs) |
| [`04_IMPLEMENTATION.md`](./04_IMPLEMENTATION.md) | Phase 4 | Builder-Validator loop, Actor-Critic pattern |
| [`05_VERIFICATION.md`](./05_VERIFICATION.md) | Phase 5 | Self-review, evals, security scanning, DoD checklist |
| [`06_DELIVERY.md`](./06_DELIVERY.md) | Phase 6 | PR packaging, deployment, handoff, retrospective |
| [`templates/`](./templates/) | — | Intent brief, execution plan, tool discovery, handoff, verification, task log, retrospective |

## Reading Order — For Humans

```
📖 If you're learning this system, read in this order:

1. WHY_THIS_WORKS.md        → 20 min — understand the thinking behind every phase
2. README.md (this file)    →  5 min — see the full structure
3. GLOSSARY.md              →  reference — look up terms as you go
4. AGENTS.md                →  5 min — understand agent identity + your role as orchestrator
5. 01_DISCOVERY.md          →  try it — fill out templates/intent_brief.md for a real project
6. 02_PLANNING.md           →  fill out templates/execution_plan.md
7. SCAFFOLDS.md + 03_TOOLING→  when you need tools — browse the catalog
8. 04_IMPLEMENTATION.md     →  during building
9. 05_VERIFICATION.md       →  before shipping
10. 06_DELIVERY.md          →  ship it, then fill out templates/retrospective.md
```

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

## How to Use This Template

### Quick Start — Minimal Path
For small projects or simple scripts, you don't need all 6 phases. Use this 3-step minimum:
1. **Drop `AGENTS.md`** into your project root.
2. **Write a quick `intent_brief.md`** (Phase 1) so the agent knows what to build.
3. **Point the agent at `04_IMPLEMENTATION.md`** and say "Build this."

### Full Workflow — For New Projects
1. **Copy this entire `template_workflow/` directory** into your project root (or a `.workflow/` subdirectory).
2. **Start at `01_DISCOVERY.md`** — fill out the Intent Brief template for your project.
3. **Progress sequentially** through each phase, using checkpoints to pause and review.
4. **Customize** — as the project matures, the templates in `templates/` become your project-specific specs.

### Full Workflow — For Existing Projects
1. **Start at `03_TOOLING.md`** — audit your existing toolchain and fill gaps.
2. **Use `02_PLANNING.md`** to create a structured plan for the next feature or refactor.
3. **Follow `04_IMPLEMENTATION.md`** through `06_DELIVERY.md` for execution.

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
                    🛑 CHECKPOINT 1: Plan Approval
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
6. **Scaffold Awareness** — Know the ecosystem of existing frameworks, MCP servers, and starter templates (see [`SCAFFOLDS.md`](./SCAFFOLDS.md)). Discover before you build.
7. **Bounded Autonomy** — Set clear limits on what agents can do without approval. The most reliable systems give agents freedom within strict guardrails.
8. **Retrospective Discipline** — After every project, evolve the harness. Update rules, add skills, remove friction. The workflow improves with every cycle.

### The Complexity Ladder
Start simple and only escalate when necessary:
```
Single Agent → Sequential Pipeline → Orchestrator-Worker → Parallel Fan-Out → Hierarchical Multi-Agent
```
Most projects should start at "Single Agent" and only move right when task complexity demands it.
