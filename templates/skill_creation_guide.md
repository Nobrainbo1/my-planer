---
description: "Guide for creating custom SKILL.md files. Use when Phase 3 Tooling identifies a capability gap that no existing skill covers."
type: template
---

# How to Create Custom Skills

> **Purpose:** When the Discovery Protocol (Phase 3) fails to find an existing skill for a capability you need, use this guide to create your own. The format is cross-harness compatible.

> **Principle:** Learn from the best. This guide distills patterns from the 4 most popular skill repositories:
> - [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) — 25 production SDLC skills, slash-command mapped, 70+ harness compatible
> - [thananon/9arm-skills](https://github.com/thananon/9arm-skills) — Opinionated engineering meta-skills (debugging discipline, review methodology, context management)
> - [anthropics/skills](https://github.com/anthropics/skills) — Official Anthropic reference patterns (creative, technical, enterprise)
> - [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) — 817 domain-specific security playbooks

---

## The SKILL.md Anatomy

Every skill has exactly **one required file**: `SKILL.md`. This file has two parts: YAML frontmatter (metadata) and Markdown body (instructions).

### Minimal Skeleton

```markdown
---
name: my-skill-name
description: One-paragraph description that doubles as the trigger condition. The agent reads this to decide WHEN to activate the skill. Be specific about triggers — list the slash commands, user phrases, and situations that should activate it.
---

# Skill Title

Brief one-sentence summary of what the skill does.

## When to Use
- [Situation 1 that should trigger this skill]
- [Situation 2]

## When NOT to Use
- [Situation where this skill should NOT activate]

## Workflow
[Step-by-step instructions the agent follows]

### Step 1: [Name]
[What to do, how to verify]

### Step 2: [Name]
[What to do, how to verify]

## Red Flags
- [Common mistake the agent should watch for and avoid]
```

---

## The Two Critical Fields

### `name` (required)
- **Format:** kebab-case, lowercase, no spaces
- **Rules:** Unique within your skill directory. This becomes the skill identifier.
- **Examples:** `debug-mantra`, `spec-driven-development`, `scrutinize`, `code-review-and-quality`

### `description` (required)
This is the most important field — **it is both a description AND a trigger condition**. The agent reads this to decide when to activate the skill.

**Pattern from the best skills:**

```yaml
description: >
  [What it does] — [core behavior]. 
  [When to trigger] Use when [situation 1], [situation 2], [situation 3]. 
  Also use when the user says "[phrase 1]", "[phrase 2]", or "[phrase 3]".
```

**Real examples from top repos:**

```yaml
# From 9arm-skills — debug-mantra
description: Four-mantra debugging discipline — reproduce, trace the fail path, falsify 
  the hypothesis, cross-reference every breadcrumb. Recite the mantra block verbatim at 
  the start of any debugging session, then apply the four steps in order before proposing 
  any fix. Trigger on /debug-mantra and proactively whenever debugging starts — user 
  reports a bug, says something is broken/throwing/failing, asks to debug/diagnose/investigate 
  an issue, or pastes a stack trace or error log.

# From agent-skills — spec-driven-development
description: Creates specs before coding. Use when starting a new project, feature, or 
  significant change and no specification exists yet. Use when drafting a PRD or requirements 
  document with objectives and scope, or when requirements are unclear, ambiguous, or only 
  exist as a vague idea.

# From 9arm-skills — scrutinize
description: Outsider-perspective end-to-end review of a plan, PR, or code change. First 
  questions intent and whether a simpler/more elegant approach would achieve the same goal, 
  then traces the actual code path (not just the diff) to verify the change does what it 
  claims. Trigger on /scrutinize and proactively whenever the user asks to review, audit, 
  sanity-check, or get a second opinion.
```

**Tips:**
- Front-load the "what it does" (agent sees this first)
- Include explicit trigger phrases the user might say
- Include slash command triggers (e.g., "Trigger on /debug")
- Be specific about when NOT to use it to prevent false activations

---

## Skill Body: Five Patterns That Work

Studied across 850+ skills from the 4 reference repos, these 5 body patterns cover every use case:

### Pattern A: The Mantra (Recite + Apply)
*Best for: Debugging, discipline, consistent methodology*

```markdown
## Recite this — verbatim, as the first thing in your response

> **Mantra:**
> 1. [Principle 1]
> 2. [Principle 2]
> 3. [Principle 3]

Then begin work following each principle in order.

## 1. [Principle 1 Name]
[Detailed instructions, decision criteria, stop conditions]

## 2. [Principle 2 Name]
[Detailed instructions]
```

**Example:** 9arm `debug-mantra` — 4 mantras recited verbatim, then applied in sequence.

### Pattern B: The Gated Workflow (Phase → Checkpoint → Phase)
*Best for: Multi-step processes, SDLC phases, anything requiring human approval*

```markdown
## The Gated Workflow

Do not advance to the next phase until the current one is validated.

### Phase 1: [Name]
[Instructions]
→ Human reviews before proceeding

### Phase 2: [Name]
[Instructions]
→ Human reviews before proceeding
```

**Example:** Osmani `spec-driven-development` — SPECIFY → PLAN → TASKS → IMPLEMENT, each gated.

### Pattern C: The Decision Table (Check → Trigger → Action)
*Best for: Monitoring, guardrails, meta-skills that run continuously*

```markdown
## Before each step — run this

| Check | Trigger fires when... | Do this |
|-------|----------------------|---------|
| **[Check 1]** | [Condition] | [Action] |
| **[Check 2]** | [Condition] | [Action] |

If nothing fires, take the step.
```

**Example:** 9arm `qwenchance` — Looping/Over-thinking/Context-tight checks run before every step.

### Pattern D: The Outsider Review (Question → Trace → Verdict)
*Best for: Code review, plan review, auditing*

```markdown
## Operating stance
- [Perspective to adopt]
- [What NOT to do]

## Workflow (run in order, do not skip)

### 1. Intent — what is this trying to do?
[How to question the change itself]

### 2. Trace — walk the actual code path
[How to verify claims against reality]

### 3. Verdict
[Structured output format]
```

**Example:** 9arm `scrutinize` — outsider review that questions whether the change should exist at all.

### Pattern E: The Playbook (Prerequisites → Steps → Validation)
*Best for: Domain-specific procedures, compliance, security audits*

```markdown
## Prerequisites
- [ ] [Required setup/access]

## Procedure

### Step 1: [Name]
**Command:** `[exact command to run]`
**Expected output:** [what to look for]
**If failed:** [what to do]

### Step 2: [Name]
...

## Validation
- [ ] [Check 1 confirming success]
- [ ] [Check 2]
```

**Example:** Anthropic cybersecurity skills — 817 playbooks following this structure.

---

## Directory Structure

### Minimal (single skill)
```
skills/
└── my-skill/
    └── SKILL.md
```

### With resources
```
skills/
└── my-skill/
    ├── SKILL.md          # Required — instructions + metadata
    ├── scripts/          # Optional — helper scripts
    │   └── analyze.sh
    ├── references/       # Optional — docs the skill can read
    │   └── checklist.md
    └── examples/         # Optional — reference implementations
        └── example.ts
```

### Organized by bucket (recommended for 5+ skills)
```
skills/
├── engineering/          # Daily code work
│   ├── debug-mantra/
│   ├── code-review/
│   └── tdd/
├── productivity/         # Non-code workflow
│   ├── management-talk/
│   └── context-manager/
├── security/             # Security & compliance
│   └── owasp-audit/
└── project-specific/     # This project only
    └── custom-deploy/
```

---

## Harness Installation Paths

| Harness | Skill Location | Auto-discovers? |
|---------|---------------|-----------------|
| **Claude Code** | `~/.claude/skills/` or project `.claude/skills/` | Yes |
| **Cursor** | `.cursor/skills/` | Yes |
| **Antigravity** | `.gemini/config/skills/` | Yes |
| **Gemini CLI** | `~/.gemini/skills/` or project | Yes |
| **Kiro** | `.kiro/skills/` | Yes |
| **OpenCode** | `.opencode/skills/` | Yes |
| **Codex** | Via plugin system | Via `/plugin` |
| **Any agent** | `npx skills add <repo>` | Via CLI |

---

## Quality Checklist for New Skills

Before shipping a custom skill, verify:

- [ ] **Name** is kebab-case and unique.
- [ ] **Description** includes both what it does AND when to trigger.
- [ ] **Trigger conditions** are specific enough to avoid false activations.
- [ ] **"When NOT to use"** section prevents the skill from activating on trivial tasks.
- [ ] **Steps are ordered** — the agent knows which step comes first, and what gate exists between steps.
- [ ] **Stop conditions** are explicit — the agent knows when to stop, escalate, or ask for help.
- [ ] **Red flags / anti-patterns** are listed so the agent avoids common mistakes.
- [ ] **Output format** is defined — the agent knows what its response should look like.
- [ ] **Tested** — manually trigger the skill with 3-5 representative prompts to verify it activates correctly and produces good output.

---

## Starter Templates

### Engineering Skill (Pattern B: Gated)

```markdown
---
name: [your-skill-name]
description: [What it does]. Use when [trigger 1], [trigger 2]. Trigger on /[command].
---

# [Skill Title]

## Overview
[What this skill enforces and why it matters.]

## When to Use
- [Trigger condition 1]
- [Trigger condition 2]

## When NOT to Use
- [Exclusion 1 — e.g., single-line fixes, trivial changes]

## Workflow

### Phase 1: [Analyze / Specify / Gather]
[Instructions for the first phase]

→ **Gate:** Summarize findings. Proceed only after human confirms.

### Phase 2: [Plan / Design]
[Instructions for the second phase]

→ **Gate:** Present plan. Proceed only after human approves.

### Phase 3: [Execute / Implement]
[Instructions for the third phase]

## Red Flags — Do NOT
- [Anti-pattern 1 — e.g., "Do not skip Phase 1 even if the task seems simple"]
- [Anti-pattern 2]

## Verification
- [ ] [How to confirm the skill produced correct output]
```

### Meta / Guardrail Skill (Pattern C: Decision Table)

```markdown
---
name: [your-skill-name]
description: [What it monitors]. Use continuously during [situation]. Trigger on /[command] and proactively when [condition].
---

# [Skill Title]

[One-line purpose.]

## Before each step — run this

| Check | Trigger fires when... | Do this |
|-------|----------------------|---------|
| **[Check 1]** | [Detection condition] | [Corrective action] |
| **[Check 2]** | [Detection condition] | [Corrective action] |

If nothing fires, proceed with the step.

## [Check 1] — detect and handle

[Detailed instructions for detecting and responding to this condition]

## [Check 2] — detect and handle

[Detailed instructions]
```
