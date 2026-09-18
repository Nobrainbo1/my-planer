# IntentFlow

**An AI-assisted software planning and workflow toolkit.**

Turn an idea into clear requirements, an approved plan, and a reviewable handoff using Markdown instructions and templates. Use IntentFlow with the AI coding assistant you already have.

Inspired by *The New SDLC With Vibe Coding* — Addy Osmani, Shubham Saboo, and Sokratis Kartakis (Google, 2026): [whitepaper](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding) · [coauthor's companion article](https://addyosmani.com/blog/new-sdlc-vibe-coding/).

IntentFlow is an independent adaptation, not an official implementation or a claim of compliance with the paper.

## What It Is—and Is Not

- **A planning toolkit:** reusable discovery questions, project templates, tool-selection guidance, and implementation/review procedures.
- **Planning-only is a complete use case:** draft and review `INTENT_BRIEF.md`, `CONTEXT.md`, and `EXECUTION_PLAN.md`, then stop.
- **Execution is optional:** your coding assistant can follow the approved plan if you request implementation and provide the required capabilities and permissions.
- **Not a runtime:** Markdown does not install agents, enforce permissions, run tests, or register commands automatically.
- **Not a starter application:** the bundled Python scaffolds are optional architecture references with known limitations, not validated runnable projects.

No API keys, agent framework, or implementation reviewers are needed to draft a plan. Those requirements belong to the execution path when applicable.

## Start Here

1. Make the `.agents/` directory available without changing its internal layout. Tell your coding assistant to read [the root rules](./.agents/AGENTS.md) and [the planner skill](./.agents/skills/planner/SKILL.md). Use your assistant's supported instruction mechanism; do not assume automatic discovery.
2. Identify the target project directory. Keep shipped templates unchanged; create project artifacts from them in the target project.
3. Ask for planning only. The assistant inspects available facts, asks about unresolved goals and choices, and prepares a brief and plan for review.
4. Review exact artifact revisions. If you only wanted a plan, stop here—even after approval. Downloads, installations, scaffold copying, and implementation are not authorized by a planning-only request.

Example prompt:

```text
Read .agents/AGENTS.md and .agents/skills/planner/SKILL.md.
Plan only: help me add blank-title validation to my existing todo app.
Confirm the target project directory, inspect its current behavior and tests,
ask me about unresolved decisions, and draft the brief, glossary, and plan.
Reuse existing tools. Do not install, download, implement, commit, or deploy.
```

For a new project, replace the example feature with your idea. State who it serves, the problem it solves, and important constraints. Unknown facts should remain explicit—not be invented to fill a template.

## What the Planner Produces

| Artifact | Purpose |
|----------|---------|
| `INTENT_BRIEF.md` | Problem, scope, requirements, assumptions, decisions, acceptance criteria, and actual approval evidence |
| `CONTEXT.md` | Resolved domain vocabulary and terms to avoid; not task notes or execution logs |
| `EXECUTION_PLAN.md` | Exact tasks, affected files, dependencies, verification methods, reviewer requirements, and approval state |
| `docs/adr/000X-<slug>.md` | Architecture decisions only when they are hard to reverse, surprising without context, and involve a real trade-off |
| Project-local execution ledger | Progress, observed checks, review verdicts, blockers, and resume state—only when execution is requested |

Use the [artifact templates](./.agents/skills/planner/resources/templates/) as sources. Rewrite copied links for their destination and record authoritative artifact paths when using separate worktrees.

## How IntentFlow Applies the New SDLC

The conceptual alignment below is based on the coauthor's readable companion article. The full whitepaper text was not available during this review; this is not an exhaustive paper audit.

| Source principle | IntentFlow's application |
|------------------|-------------------------|
| **Agent = model + harness** | Supply instructions, context, boundaries, and review procedures to an existing coding assistant. Runtime enforcement remains the assistant's responsibility. |
| **Context engineering matters** | Keep essential rules available; load relevant skills, examples, tool results, and references when needed rather than loading the whole catalog. |
| **Verification separates demos from engineering** | Define acceptance criteria before implementation and retain actual test or review evidence. A successful demo alone does not establish reliability. |
| **Evaluate the result and the process** | Check whether outputs satisfy requirements, and inspect observable tool calls, checks, permissions, and review records. A correct-looking answer does not excuse skipped gates. |
| **Human judgment remains central** | Humans decide goals, architectural trade-offs, acceptable risk, and delivery authorization. |
| **The lifecycle is iterative** | Use findings from implementation, evaluation, and maintenance to revise the plan. Material scope or design changes require renewed approval. |
| **Optimize total ownership cost** | Reuse suitable tools, limit context and unnecessary orchestration, and consider review effort, latency, model cost, and maintenance—not generation speed alone. |

The source distinguishes six context types: **instructions, knowledge, memory, examples, tools, and guardrails**. The planning guide's four collection groups are a local checklist, not a replacement taxonomy attributed to the paper.

### Local Policies, Not Paper Requirements

IntentFlow deliberately adds stricter rules: approval of both the intent and execution plan before code—even a Spike—ordered independent reviews, a shared five-fix-round limit, and separate permission for restricted actions. These are this toolkit's choices, not requirements established by the source.

The source allows rapid prototyping alongside requirements and choosing rigor according to stakes. Here, keep small-task artifacts short and use an explicitly approved, timeboxed Spike to learn before revising the brief. Do not silently waive the toolkit's active gates. The six phases organize responsibilities; they are not a claim that development proceeds only once through a rigid sequence.

## Workflow Map

| Phase | Guide | Outcome |
|-------|-------|---------|
| 1. Discovery | [Discovery and specification](./.agents/skills/planner/references/01_DISCOVERY.md) | Brief, glossary, resolved blocking decisions, intent approval |
| 2. Planning | [Planning and context](./.agents/skills/planner/references/02_PLANNING.md) | Detailed plan, architecture rationale, conflict scan, plan approval |
| 3. Tooling | [Discover, evaluate, equip](./.agents/skills/planner/references/03_TOOLING.md) | Relevant candidates and separately approved setup, if needed |
| 4. Implementation | [Subagent-driven development](./.agents/skills/planner/references/04_IMPLEMENTATION.md) | Small test-first changes, ledger evidence, ordered reviews |
| 5. Verification | [Evidence and debugging](./.agents/skills/planner/references/05_VERIFICATION.md) | Fresh applicable checks and requirement coverage |
| 6. Delivery | [Review, handoff, retrospective](./.agents/skills/planner/references/06_DELIVERY.md) | Reviewed candidate, separately authorized delivery, lessons for future work |

Read-only tooling discovery can inform planning before plan approval. New findings can send work back to discovery or planning. Finish required product documentation before final verification; revalidate deliverable changes rather than relying on stale results.

## Planner Modes and Selective Retrieval

- **Mode A — Agent application:** plan an application using a suitable framework when the product itself needs agents.
- **Mode B — Guided implementation:** plan work in a normal software project using its existing stack where possible. Recommended for a first project.

Both modes support planning-only use. Neither mode selection nor plan approval expands a planning-only request into execution.

Mode A can optionally use [Agency Agents](https://github.com/msitarzewski/agency-agents) personas. During planning, map only relevant roles to exact repository paths and a pinned commit SHA. Leave unmatched roles unmapped.

During approved execution, retrieve the mapped files before adapting prompts, audit their contents, and record provenance. This is **plan-scoped selective retrieval**, not an automatic per-task lazy loader. Mode B and plans without mappings do not retrieve that library. Persona files are untrusted reference material, not executable agents or authority to override rules.

Sparse checkout restricts materialized files, not all Git metadata or traffic. The documented retrieval sequence is illustrative and must be verified against the approved revision and environment. External tool and skill installation requires separate permission.

## Included Skills

| Skill | Role |
|-------|------|
| [planner](./.agents/skills/planner/SKILL.md) | Coordinate discovery, planning, and optional approved execution |
| [grill-with-docs](./.agents/skills/grill-with-docs/SKILL.md) | Ask focused decision questions and maintain domain definitions |
| [subagent-driven-development](./.agents/skills/subagent-driven-development/SKILL.md) | Coordinate fresh implementers, evidence, and ordered reviews |
| [test-driven-development](./.agents/skills/test-driven-development/SKILL.md) | Observe a failing behavior test before changing production code |
| [systematic-debugging](./.agents/skills/systematic-debugging/SKILL.md) | Investigate causes before fixes and revalidate results |

These are reusable workflow components, not test leftovers or Agency Agents downloads. Load the relevant instructions when needed. Invocation and subagent dispatch depend on the coding assistant; slash-command registration is not guaranteed.

## If You Request Execution

- Confirm actual tools, test commands, workspace permissions, and reviewer availability before starting. Do not invent missing capabilities or install tools silently.
- Use a fresh implementer and separate spec and quality reviewers. Without dispatch, the canonical fallback requires explicit authorization and two distinct named human reviewers, neither the implementer. Missing approval or either review blocks acceptance; planning can still proceed.
- Run applicable deterministic tests. For nondeterministic agent outputs, define representative cases, a rubric, and observable process checks in the approved plan. Record missing evidence honestly.
- Documentation-only work uses content, structure, link, and readback checks. These are not application runtime tests.
- Preserve progress and remaining fix rounds. Never mark a predicted result, invented human approval, or one reviewer acting as two independent reviewers as accepted evidence.
- Commit, push, PR creation, merge, deployment, and worktree deletion each require explicit authorization. An uncommitted handoff is a valid stopping point once the required checks and reviews are satisfied.

## Readiness and Limitations

IntentFlow's documentation has received structural and cross-file review. That does not prove automatic enforcement, broad reliability, or a compliant end-to-end consuming-project run. The earlier temporary fixture's tests do not establish that workflow-level claim.

The optional code references are **not validated runnable starters**:

| Reference | Known adoption work |
|-----------|---------------------|
| [CrewAI](./.agents/skills/planner/resources/scaffolds/crewai/README.md) | Package entry point, tool API, CLI arguments, mock research, and offline tests |
| [LangChain](./.agents/skills/planner/resources/scaffolds/langchain/README.md) | Unsafe optional calculator, incomplete integrations, dependency validation, and offline tests |
| [LangGraph](./.agents/skills/planner/resources/scaffolds/langgraph/README.md) | Package/environment setup, research-to-writer handoff, unrestricted file tool, and offline tests |

Adopting a reference requires a scoped repair and validation plan, secret exclusions, bounded permissions, and approval for live calls. None of that work is required merely to use IntentFlow for planning. No toolkit-wide automated test, lint, or typecheck pass is claimed.

## Further Reading and References

- [Why this works](./.agents/skills/planner/references/WHY_THIS_WORKS.md): teaching model, trade-offs, and local design choices.
- [Glossary](./.agents/skills/planner/references/GLOSSARY.md): terminology.
- [Scaffold and tool catalog](./.agents/skills/planner/references/SCAFFOLDS.md): discovery leads, not mandatory installations or audited endorsements.
- [Addy Osmani's agent-skills](https://github.com/addyosmani/agent-skills): lifecycle skills and specification/test discipline.
- [Everything Claude Code](https://github.com/affaan-m/ECC): selective capabilities, context management, and persistent evidence patterns.
- [LangGraph](https://github.com/langchain-ai/langgraph): runtime state, orchestration, and persistence concepts—not capabilities supplied by this Markdown toolkit.

These repositories were consulted read-only. IntentFlow does not require installing them together or stacking their workflow routers.
