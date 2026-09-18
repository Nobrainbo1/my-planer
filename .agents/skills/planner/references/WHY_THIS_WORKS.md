---
description: "The thinking behind every design decision. Read this first to understand WHY the template is structured this way — so you can build your own workflows without AI."
alwaysApply: false
---

# Why This Works — The Thinking Behind the Template

> **For:** You, the human orchestrator. This document teaches the mental model, not the steps.
> After reading this (~20 minutes), you should be able to design your own workflow on a whiteboard — no AI needed.

**Source boundary:** Source concepts below are verified against Addy Osmani's [The New Software Lifecycle](https://addyosmani.com/blog/new-sdlc-vibe-coding/), his summary of the coauthored whitepaper, not a direct review of the Kaggle original. Teaching models and workflow policies are local adaptations, not source quotations.

---

## Part 1: The Core Mental Model (5 min)

### Two Useful Failure Categories

As a teaching simplification, the failures this template is built to prevent fall into two groups:

1. **Built the wrong thing.** The requirements were wrong, vague, or misunderstood. You coded for 2 hours, then realized the spec was off.
2. **Built it broken.** The requirements were right, but the implementation has bugs, security holes, or doesn't actually meet the spec.

This is a simplification, not a universal law — projects also fail for reasons outside this template's control (staffing, funding, market fit). Each phase in this template exists to prevent one of these two failure modes.

### The Three Decision Types

For teaching purposes, this template groups decisions into three types. Its 6 phases map to them:

```
WHAT decisions          HOW decisions           DID-IT-WORK decisions
(Define the problem)    (Solve the problem)     (Verify the solution)
     │                       │                         │
     ├── Phase 1: DISCOVERY  ├── Phase 3: TOOLING      ├── Phase 5: VERIFICATION
     └── Phase 2: PLANNING   └── Phase 4: IMPLEMENTATION └── Phase 6: DELIVERY
```

**Why two phases per type?** Because each type has a *thinking* step and a *doing* step:
- WHAT: *What do we want?* (Discovery) → *How do we get there?* (Planning)
- HOW: *What tools do we need?* (Tooling) → *Write the code* (Implementation)
- DID IT WORK: *Does it pass tests?* (Verification) → *Is it shipped and learned from?* (Delivery)

### The Cost Trade-off — Why Early Feedback Matters

Early discovery can reduce downstream rework, but repair cost does not follow a fixed phase-by-phase curve. A spec edit may expose a large redesign; a late defect may have a small fix. This is a qualitative teaching model, not measured repair times or savings from the source.

**The insight:** Compare total cost of ownership (TCO), including planning, context and model usage, review, rework, operations, and maintenance. The source's economic crossover is illustrative, not a measured constant. Structured work does not guarantee lower TCO; measure the trade-off for the project's risks and lifespan.

### On Paper (No AI)

If you had no AI at all, here's the workflow on a notebook:

1. **Write what you want** in 3-5 sentences. Ask "what would convince me this is done?" (that's your Definition of Done).
2. **Sketch the plan** — boxes and arrows on paper. Name the components, draw the data flow.
3. **List the tools** — what libraries, APIs, frameworks will you use? Google for existing solutions before building custom.
4. **Code it.** Test as you go. When stuck, step back and check if you're solving the right problem.
5. **Test it.** Run it against your Definition of Done. Fix what fails.
6. **Ship it.** Write down what you learned for next time.

That's the entire template in 6 steps. Everything else is detail.

---

## Part 2: Why Each Phase Exists (10 min)

### Phase 1: DISCOVERY — "What are we actually building?"

**What goes wrong without it:** You start coding based on a vague idea. Two hours in, you realize you're solving the wrong problem, or you missed a critical constraint (like "it has to work offline").

**The key insight:** A spec is not bureaucracy — it's a *cheaper way to find mistakes*. Changing a sentence in a spec is usually far cheaper than changing 500 lines of code. The spec forces you to think through the problem *before* the expensive work starts.

**The MoSCoW trick:** When you list requirements, force yourself to categorize each as Must/Should/Could/Won't. This prevents scope creep — you decide *before coding* what you'll cut if time runs short.

**On paper:** Write three things: (1) What does this do? (2) Who is it for? (3) How will I know it's done?

---

### Phase 2: PLANNING — "How do we get there?"

**What goes wrong without it:** You jump into coding without understanding the architecture. You build Component A, then realize it needs data from Component B that doesn't exist yet. Or you pick a framework that doesn't support a critical requirement.

**The key insight:** Planning is not about predicting the future perfectly — it's about *making your assumptions visible*. When you write "I assume the database is PostgreSQL", you give your future self (or your agent) a chance to catch wrong assumptions early.

**Why HIGH vs LOW detail?** Different audiences need different views. A stakeholder needs "we're building a web app with auth, payments, and dashboards" (HIGH). An engineer needs "the auth module uses NextAuth with JWT, the payment module wraps Stripe API v3, and the dashboard uses Recharts" (LOW). Same plan, different zoom levels.

**The Four Context Collection Groups:** These are a local checklist, not the source's taxonomy. Osmani's summary names six source types: instructions, knowledge, memory, examples, tools, and guardrails. The mapping is many-to-many:

| Local Group | Source Types Collected | Example |
|-----------|-----------|---------|
| **Instruction** | Instructions, guardrails | AGENTS.md, standards, approval rules |
| **Codebase** | Knowledge, examples | Architecture, dependencies, similar implementations, fixtures |
| **Tool/Skill** | Tools, instructions, guardrails | MCP definitions, skill instructions, scoped permissions |
| **Session** | Memory, knowledge | Decisions, ledger state, current findings |

**Static vs dynamic context** is a separate, deliberate architectural decision. Keep core rules and guardrails available every turn; retrieve task-specific skills, documents, and tool results on demand. Review and version this boundary to balance token cost against missing essential context.

**On paper:** Draw boxes for each component. Draw arrows for data flow. List your assumptions. Pick your tech stack.

---

### Phase 3: TOOLING — "What tools do we need?"

**What goes wrong without it:** You build custom tools that already exist. You spend 3 hours writing a database migration script when there's a well-maintained npm package that does exactly the same thing. Or you miss a critical tool (like a linter) and only discover you need it when code quality issues pile up.

**The key insight:** *"Discover before you build."* Reuse adequate existing tools and project structure; no new tooling is a valid result. Evaluate candidates before installation, then obtain separate action approval. Material tool or scaffold changes return to planning for renewed approval and preflight; implement approved custom tooling through Phase 4.

**Why skills before MCP before packages?** Because of how close each tool type is to your workflow:
1. **Skills** change agent *behavior* — they're instructions, not external tools. Cheapest to try.
2. **MCP servers** add *capabilities* without code changes. Medium effort.
3. **Packages** require integration code. More effort.
4. **APIs** require network calls, auth, error handling. Even more effort.
5. **Custom tools** require building + testing + maintaining. Most effort.

**On paper:** For each capability you need, search Google/GitHub for 5 minutes before deciding to build it yourself.

---

### Phase 4: IMPLEMENTATION — "Write the code."

**What goes wrong without it (the process):** Code without a loop just keeps going in one direction. If the first approach is wrong, you end up with 500 lines of wrong code instead of catching it at line 50.

**The key insight: Builder-Validator.** This is a local implementation of the verification ideas in the paper. The agent is split into two roles that alternate:

```
Builder writes code → Validator checks it → Builder fixes issues → Validator re-checks → ...
```

This is like having a junior developer (Builder) paired with a senior reviewer (Validator). The Builder generates; the Validator verifies. Neither is useful alone — generation without verification is vibe coding; verification without generation is just complaining.

**Local policy — fix budget and human review:** The five-round limit, escalation rules, and human-review fallback below are template policy, not source prescriptions.

**Why a shared five-round fix budget?** A bounded correction loop prevents endless retries. Each task gets one initial attempt, excluded from the budget, then at most 5 total fix rounds shared across build, test, spec review, and quality/test review. Expected TDD Red is not a fix round. Persist the count across sessions and phases; stop and escalate after 5 failed fix rounds, with no automatic sixth round. See the [Phase 4 policy](./04_IMPLEMENTATION.md).

For fix rounds 4–5, request a higher-tier model if available. Record actual availability and selection; never claim a model switch that did not occur. If unavailable, record the limitation and use a fresh reviewer at the available tier. If subagent review is unavailable, acceptance remains blocked unless the [canonical human-review fallback](./04_IMPLEMENTATION.md#401--canonical-fallback-when-fresh-agents-are-unavailable) is authorized and both ordered reviews approve the candidate.

Escalate security issues, scope changes, destructive actions, and missing permissions immediately, regardless of the remaining budget.

**On paper:** Code a small piece. Test it. Investigate failures before fixing them. Track the shared fix count and seek human help when the budget is exhausted; safety concerns cannot wait.

---

### Phase 5: VERIFICATION — "Does it actually work?"

**What goes wrong without it:** "It works on my machine." The code passes the happy path but fails on edge cases, has a security vulnerability, or silently breaks an existing feature.

**The key insight: "Evals, not vibes."** A local phrasing of the paper's point that verification — not AI use itself — separates vibe coding from engineering: don't *feel* like it works, *prove* it works. Every requirement from Phase 1 should trace to a test in Phase 5. If you can't point to proof, you don't know it works.

The paper distinguishes **output evaluation** (is the final result correct?) from **trajectory evaluation** (was the path sound — the tool calls, checks, and permissions used?). This template evaluates on observed evidence: recorded test runs, reviewer verdicts, and permission checks — never hidden or claimed reasoning. An answer that looks right but skipped its checks is treated as unverified.

**The Spec Compliance Matrix:** This is the bridge between Phase 1 and Phase 5. For each requirement, you ask: "Where is the code that implements this? Where is the test that proves it works?" If any cell is empty, that requirement is unverified.

**On paper:** Go through your Definition of Done checklist from Phase 1. For each item, check: does it pass? Yes → next. No → fix it.

---

### Phase 6: DELIVERY — "Ship it and learn from it."

**What goes wrong without it:** You ship and immediately forget everything you learned. Next project, you make the same mistakes. The workflow never improves.

**The key insight: The retrospective loop.** Record evidence-backed improvements to rules, skills, tools, and phases. Apply them only under separately approved scope, not automatically. Required product documentation is completed during implementation and verified before delivery; a retrospective is not permission for late deliverable edits.

**On paper:** After shipping, write down: (1) What went well? (2) What went wrong? (3) What would I change for next time?

---

## Part 3: Design Decisions You Should Question (5 min)

### Load-Bearing Decisions (Don't Change These)

These structural choices hold the system together:

- **Phases form an iterative feedback loop.** Tooling, implementation, verification, and delivery findings can return work to discovery and planning. Material changes require revised artifacts, renewed approval, and preflight before affected implementation.
- **Checkpoints exist (local policy).** Both intent and execution plan require explicit human approval before implementation. Iteration does not waive either approval or separate action permissions.
- **Spec is source of truth.** All code traces back to the spec. Without this, there's no way to verify "done."
- **Discovery before creation.** Searching for existing tools before building custom ones. This saves massive amounts of time.

### Preference Decisions (Change These Freely)

These are style choices — the system works fine if you swap them:

- **6 phases vs fewer.** For quick prototypes, merge Discovery+Planning into one step, and Verification+Delivery into one step. That gives you 4 phases: Spec → Tool → Build → Ship.
- **Markdown format.** You could do all of this in Notion, Google Docs, YAML, or sticky notes. Markdown is just the most harness-compatible format right now.
- **File-per-phase structure.** You could put everything in one big file. Separate files just make it easier for agents to load only what they need (progressive disclosure).
- **MoSCoW prioritization.** Use whatever prioritization you like — numbered priority, T-shirt sizing, whatever works for your team.

### Scale the Process, Keep the Gates

- **Hackathons / prototypes:** Use a timeboxed Spike with a brief intent and small execution plan. Obtain explicit approval of both before experiment code or scaffolding. Spike findings can inform revised requirements and a revised plan; obtain renewed approval for material changes before affected implementation.
- **Emergency fixes:** Use a focused One-Shot specification and plan. Read-only diagnosis can start immediately; implementation still needs both approvals and fresh verification.
- **Tiny tasks:** Keep the intent and plan short, but retain explicit approvals, acceptance criteria, and applicable verification. Combine phase work where useful; never omit its approval or evidence requirements.

### How to Create Your Own Phase

If you ever need a phase this template doesn't have, use this formula:

1. **Name a failure mode.** What goes wrong without this phase?
2. **Define the input.** What does this phase receive from the previous phase?
3. **Define the output.** What does this phase produce for the next phase?
4. **Design the checkpoint.** What question does the human answer to approve the output?
5. **Write the steps.** What must happen between input and output?

---

## Reading Order — For Humans Learning the System

```
📖 RECOMMENDED PATH

1. You're here:       WHY_THIS_WORKS.md        (20 min — the thinking)
2. Then skim:         README.md                 (5 min — the structure)
3. Then read:         AGENTS.md                 (5 min — agent identity + orchestrator mindset)
4. Browse:            GLOSSARY.md               (reference — look up terms as needed)
5. Try one project:   01_DISCOVERY.md → create target-project INTENT_BRIEF.md from the source template
6. Continue:          02_PLANNING.md → create target-project EXECUTION_PLAN.md from the source template
7. As needed:         SCAFFOLDS.md, 03_TOOLING.md (when you need tools)
8. During building:   04_IMPLEMENTATION.md
9. Before shipping:   05_VERIFICATION.md → 06_DELIVERY.md
10. After shipping:   06_DELIVERY.md → retrospective at an approved target-project path
```

Template sources live under the planner skill's `resources/templates/`: [intent brief](../resources/templates/intent_brief.md), [execution plan](../resources/templates/execution_plan.md), and [retrospective](../resources/templates/retrospective.md). Read these originals; never fill them in. Write live artifacts only to approved target-project paths. Rewrite copied links relative to each output and verify their targets and headings. Keep one authoritative artifact map across worktrees; a new worktree does not inherit uncommitted planning files.

---

## Key Vocabulary

For a complete dictionary of AI coding terms, see [`GLOSSARY.md`](./GLOSSARY.md) — adapted from Matt Pocock's [Dictionary of AI Coding](https://github.com/mattpocock/dictionary-of-ai-coding).
