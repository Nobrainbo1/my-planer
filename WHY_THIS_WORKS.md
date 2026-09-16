---
description: "The thinking behind every design decision. Read this first to understand WHY the template is structured this way — so you can build your own workflows without AI."
alwaysApply: false
---

# Why This Works — The Thinking Behind the Template

> **For:** You, the human orchestrator. This document teaches the mental model, not the steps.
> After reading this (~20 minutes), you should be able to design your own workflow on a whiteboard — no AI needed.

---

## Part 1: The Core Mental Model (5 min)

### The Two Things That Always Go Wrong

Every failed software project fails for one of two reasons:

1. **Built the wrong thing.** The requirements were wrong, vague, or misunderstood. You coded for 2 hours, then realized the spec was off.
2. **Built it broken.** The requirements were right, but the implementation has bugs, security holes, or doesn't actually meet the spec.

That's it. Every phase in this template exists to prevent one of these two failures.

### The Three Decision Types

All software work consists of three types of decisions. The 6 phases map directly to them:

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

### The Cost Curve — Why Order Matters

This is the single most important concept from the paper:

```
Cost to fix a mistake:

Phase 1 (Discovery)  │█                           ← Costs 5 minutes (change a sentence)
Phase 2 (Planning)   │██                          ← Costs 30 minutes (revise a plan)
Phase 3 (Tooling)    │████                        ← Costs 1 hour (swap a tool)
Phase 4 (Implement)  │████████                    ← Costs 3 hours (rewrite code)
Phase 5 (Verify)     │████████████████            ← Costs 1 day (debug + fix + retest)
Phase 6 (Delivery)   │████████████████████████████ ← Costs 1 week (rollback + hotfix)
```

**The insight:** Spending 15 extra minutes in Phase 1 saves 3 hours in Phase 4. A spec change is a sentence edit. A code change is a rewrite. That's why discovery comes first — not because it's "proper", but because it's *cheaper*.

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

**The key insight:** A spec is not bureaucracy — it's a *cheaper way to find mistakes*. Changing a sentence in a spec costs 5 minutes. Changing 500 lines of code costs 5 hours. The spec forces you to think through the problem *before* the expensive work starts.

**The MoSCoW trick:** When you list requirements, force yourself to categorize each as Must/Should/Could/Won't. This prevents scope creep — you decide *before coding* what you'll cut if time runs short.

**On paper:** Write three things: (1) What does this do? (2) Who is it for? (3) How will I know it's done?

---

### Phase 2: PLANNING — "How do we get there?"

**What goes wrong without it:** You jump into coding without understanding the architecture. You build Component A, then realize it needs data from Component B that doesn't exist yet. Or you pick a framework that doesn't support a critical requirement.

**The key insight:** Planning is not about predicting the future perfectly — it's about *making your assumptions visible*. When you write "I assume the database is PostgreSQL", you give your future self (or your agent) a chance to catch wrong assumptions early.

**Why HIGH vs LOW detail?** Different audiences need different views. A stakeholder needs "we're building a web app with auth, payments, and dashboards" (HIGH). An engineer needs "the auth module uses NextAuth with JWT, the payment module wraps Stripe API v3, and the dashboard uses Recharts" (LOW). Same plan, different zoom levels.

**The 4 Dimensions of Context:** This comes from the paper. Every agent session has 4 types of context to manage:

| Dimension | What It Is | Example |
|-----------|-----------|---------|
| **Instruction** | Rules the agent follows | AGENTS.md, system prompt, skills |
| **Codebase** | The existing code | File tree, function signatures, dependencies |
| **Tool/Skill** | What the agent can DO | MCP servers, CLI tools, installed skills |
| **Session** | What's happened SO FAR | Conversation history, decisions made |

**On paper:** Draw boxes for each component. Draw arrows for data flow. List your assumptions. Pick your tech stack.

---

### Phase 3: TOOLING — "What tools do we need?"

**What goes wrong without it:** You build custom tools that already exist. You spend 3 hours writing a database migration script when there's a well-maintained npm package that does exactly the same thing. Or you miss a critical tool (like a linter) and only discover you need it when code quality issues pile up.

**The key insight:** *"Discover before you build."* The ecosystem of existing tools (MCP servers, agent skills, npm packages, APIs) is enormous and growing weekly. Your custom tool should be the *last resort*, not the first instinct.

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

**The key insight: Builder-Validator.** This is the core pattern from the paper. The agent is split into two roles that alternate:

```
Builder writes code → Validator checks it → Builder fixes issues → Validator re-checks → ...
```

This is like having a junior developer (Builder) paired with a senior reviewer (Validator). The Builder generates; the Validator verifies. Neither is useful alone — generation without verification is vibe coding; verification without generation is just complaining.

**Why 3 retries then escalate?** Because self-correction has diminishing returns. If the agent can't fix a problem in 3 attempts, it's almost certainly missing information, not making random errors. At that point, asking the human is *cheaper* than trying a 4th time.

**On paper:** Code a small piece. Test it. Fix bugs. Repeat. If stuck after 3 attempts, step back and reconsider.

---

### Phase 5: VERIFICATION — "Does it actually work?"

**What goes wrong without it:** "It works on my machine." The code passes the happy path but fails on edge cases, has a security vulnerability, or silently breaks an existing feature.

**The key insight: "Evals, not vibes."** From the paper — don't *feel* like it works, *prove* it works. Every requirement from Phase 1 should trace to a test in Phase 5. If you can't point to proof, you don't know it works.

**The Spec Compliance Matrix:** This is the bridge between Phase 1 and Phase 5. For each requirement, you ask: "Where is the code that implements this? Where is the test that proves it works?" If any cell is empty, that requirement is unverified.

**On paper:** Go through your Definition of Done checklist from Phase 1. For each item, check: does it pass? Yes → next. No → fix it.

---

### Phase 6: DELIVERY — "Ship it and learn from it."

**What goes wrong without it:** You ship and immediately forget everything you learned. Next project, you make the same mistakes. The workflow never improves.

**The key insight: The retrospective loop.** The template is designed to *improve itself*. After every project, you update the rules (AGENTS.md), add new skills, remove tools that didn't work, and refine the phases. Project 10 runs smoother than project 1 because the workflow evolved.

**On paper:** After shipping, write down: (1) What went well? (2) What went wrong? (3) What would I change for next time?

---

## Part 3: Design Decisions You Should Question (5 min)

### Load-Bearing Decisions (Don't Change These)

These structural choices hold the system together:

- **Phases are ordered.** Discovery before Planning before Implementation. The cost curve makes this non-negotiable.
- **Checkpoints exist.** Human review between phases. Without these, the agent can go off-rails for hours before you notice.
- **Spec is source of truth.** All code traces back to the spec. Without this, there's no way to verify "done."
- **Discovery before creation.** Searching for existing tools before building custom ones. This saves massive amounts of time.

### Preference Decisions (Change These Freely)

These are style choices — the system works fine if you swap them:

- **6 phases vs fewer.** For quick prototypes, merge Discovery+Planning into one step, and Verification+Delivery into one step. That gives you 4 phases: Spec → Tool → Build → Ship.
- **Markdown format.** You could do all of this in Notion, Google Docs, YAML, or sticky notes. Markdown is just the most harness-compatible format right now.
- **File-per-phase structure.** You could put everything in one big file. Separate files just make it easier for agents to load only what they need (progressive disclosure).
- **MoSCoW prioritization.** Use whatever prioritization you like — numbered priority, T-shirt sizing, whatever works for your team.

### When to Break All the Rules

- **Hackathons / prototypes:** Skip Phases 1-3 entirely. Just build. The cost curve doesn't apply when you're exploring, not shipping.
- **Emergency fixes:** Skip to Phase 4 (just fix the bug), then do a quick Phase 5 (verify it works). Do the retrospective later.
- **Tiny tasks:** A 10-minute fix doesn't need a spec. Use your judgment.

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
5. Try one project:   01_DISCOVERY.md → fill out templates/intent_brief.md
6. Continue:          02_PLANNING.md → fill out templates/execution_plan.md
7. As needed:         SCAFFOLDS.md, 03_TOOLING.md (when you need tools)
8. During building:   04_IMPLEMENTATION.md
9. Before shipping:   05_VERIFICATION.md → 06_DELIVERY.md
10. After shipping:   templates/retrospective.md (improve the workflow)
```

---

## Key Vocabulary

For a complete dictionary of AI coding terms, see [`GLOSSARY.md`](./GLOSSARY.md) — adapted from Matt Pocock's [Dictionary of AI Coding](https://github.com/mattpocock/dictionary-of-ai-coding).
