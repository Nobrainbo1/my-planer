---
description: "Reference guide for understanding AI model system prompts and how to use them to get the best performance from each model. Use during Phase 2 (Planning) and Phase 3 (Tooling) when choosing and configuring your AI agent."
type: reference
---

# System Prompt Reference Guide

> **Purpose:** Each AI model has a "personality" shaped by its system prompt — the hidden instructions it receives before your conversation even starts. Understanding these prompts helps you work *with* the model's design, not against it.

> **Source:** [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) — 64,000+ star community archive of system prompts from Claude, ChatGPT, Gemini, Cursor, Grok, and more.

> **Important:** These are leaked/extracted prompts — they may be outdated or from specific experimental versions. Treat them as **educational references**, not exact specifications.

---

## Why This Matters for Orchestrators

System prompts are **different from Skills**. Here's the distinction:

| | System Prompt | SKILL.md |
|-|---------------|----------|
| **What it is** | Hidden instructions baked into the model by its provider | Instructions YOU add to extend what the model can do |
| **Who writes it** | OpenAI, Anthropic, Google, etc. | You, the community, or skill repos |
| **Where it lives** | Inside the API / product (you don't control it) | In your project files (you fully control it) |
| **Purpose** | Define the model's base personality, safety, and capabilities | Add specialized workflows, methodology, domain knowledge |
| **How to use it** | Understand it → write prompts that align with it | Install it → agent auto-discovers and follows it |

**The key insight:** When you understand a model's system prompt, you can write your AGENTS.md, rules, and instructions in a way that **harmonizes** with the model's built-in behavior instead of fighting it.

---

## What Each Model Is Optimized For

Based on studying the leaked prompts, here's what each major model is designed to do well:

### Claude (Anthropic)
**Prompt style:** XML tags, structured thinking, explicit honesty about uncertainty.

| Strength | How to Leverage |
|----------|----------------|
| Structured reasoning | Use XML-style tags like `<context>`, `<task>`, `<constraints>` in your AGENTS.md |
| Long-form analysis | Give it multi-step workflows — Claude thrives on phased approaches |
| Honest uncertainty | Claude will say "I don't know" — this is a feature, not a bug. Trust it. |
| Tool use discipline | Claude's coding prompts enforce "read before edit, verify after change" |
| Careful file editing | Claude Code's system prompt enforces precise line-range edits, not full rewrites |

**Best practice for your AGENTS.md:**
```markdown
<!-- Claude responds well to explicit structure -->
## Rules
1. Always read the file before editing it.
2. Make minimal, targeted changes.
3. Verify changes compile before moving on.
4. If uncertain, ask rather than guess.
```

### ChatGPT / GPT (OpenAI)
**Prompt style:** Natural language instructions, role-based framing, conversation-centric.

| Strength | How to Leverage |
|----------|----------------|
| Conversational flow | Frame tasks as dialogue — "Let's think about X together" |
| Role adoption | Give it a clear role: "You are a senior architect reviewing..." |
| Creative brainstorming | Excellent for Phase 1 Discovery and ideation |
| Code generation speed | Great for rapid prototyping, but verify outputs more carefully |

**Best practice for your AGENTS.md:**
```markdown
## Your Role
You are a senior software engineer working on [project].
Your primary responsibility is [specific task].
Always explain your reasoning before making changes.
```

### Gemini (Google)
**Prompt style:** Detailed system instructions, multi-modal awareness, grounding in search.

| Strength | How to Leverage |
|----------|----------------|
| Large context windows | Can process entire codebases — use for architecture review |
| Web grounding | Ask it to verify claims against current documentation |
| Multi-modal | Can analyze images, diagrams, screenshots alongside code |
| Structured output | Responds well to explicit output format instructions |

**Best practice for your AGENTS.md:**
```markdown
## Context Handling
- Use the full context window when analyzing architecture.
- Cross-reference findings with official documentation.
- When presenting results, use tables and structured formats.
```

### Cursor
**Prompt style:** Codebase-aware instructions, inline editing conventions, diff-centric.

| Strength | How to Leverage |
|----------|----------------|
| Codebase indexing | It already "knows" your project — don't re-explain obvious structure |
| Inline editing | Use `.cursor/rules/*.mdc` for file-scoped rules |
| Diff-aware | Describe changes in terms of what should change, not the full file |
| Tab completion + chat | Use chat for planning, tab for implementation |

---

## How to Use System Prompts in Your Workflow

### During Phase 2: Planning — Choose the Right Model

```
Task Type → Best Model → Why

Spec writing         → Claude       → Structured reasoning, honest about gaps
Rapid prototyping    → GPT/Codex    → Fast generation, conversational
Architecture review  → Gemini       → Large context, multi-modal diagrams
Codebase editing     → Cursor/CC    → Deep codebase indexing
Security audit       → Claude       → Careful, structured analysis
Creative ideation    → GPT          → Conversational brainstorming
Documentation        → Any          → All models handle docs well
```

### During Phase 3: Tooling — Write Model-Aligned Rules

When writing your project's AGENTS.md or rules files, align your instructions with the model's built-in prompting style:

**For Claude-based agents (Claude Code, Cline):**
- Use explicit, numbered steps
- Include "When NOT to do X" anti-patterns
- Leverage its built-in "read → plan → edit → verify" loop
- Reference files by path — Claude's prompt trains it to work with precise file locations

**For GPT-based agents (Copilot, ChatGPT):**
- Use role-based framing ("You are a...")
- Keep instructions conversational but specific
- Include examples of desired output format
- Use markdown headers to organize context

**For Gemini-based agents (Antigravity, Gemini CLI):**
- Be explicit about output format expectations
- Leverage multi-modal capabilities (paste screenshots, diagrams)
- Use structured data formats (tables, JSON) in instructions
- Take advantage of large context windows for full-project analysis

### During Phase 4: Implementation — Model-Specific Tips

| Situation | Claude Tip | GPT Tip | Gemini Tip |
|-----------|-----------|---------|------------|
| Agent is stuck in a loop | It responds well to "Stop. Explain what you're trying to do." | "Let's take a step back and reconsider the approach." | "Summarize what you've tried and what didn't work." |
| Output is too verbose | "Be concise. Code only, no explanation." | "Reply in under 50 words." | "Use bullet points, no prose." |
| Agent hallucinated a fix | "Read the actual error output before trying again." | "Check if this function/API actually exists." | "Verify against the codebase before answering." |
| Need more context | Claude auto-reads files when prompted with paths | GPT needs content pasted or attached | Gemini handles large file inputs well |

---

## Where to Study System Prompts

| Resource | URL | What's There |
|----------|-----|-------------|
| **system_prompts_leaks** | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | 64K+ stars. Claude Code (all versions), ChatGPT, Gemini, Cursor, Grok, Kimi, Perplexity. Organized by provider. |
| **Anthropic/claude-code/** | In the repo above | Full system prompts for Claude Code with every model version (Opus, Sonnet, Fable, Haiku), plus leaked skills, commands, and output styles |
| **Google/** | In the repo above | Gemini system prompts, Antigravity prompts |
| **OpenAI/** | In the repo above | ChatGPT, Codex, GPT agent prompts |

### How to Read a System Prompt

When studying a leaked system prompt, look for these patterns:

1. **Identity block** — "You are..." — defines the model's persona
2. **Tool definitions** — what tools the model can use and how it should use them
3. **Safety guardrails** — what the model is told NOT to do
4. **Output format rules** — how the model structures its responses
5. **Error handling** — how the model is told to handle failures
6. **Context management** — how the model prioritizes information in its window

These same 6 elements are what you should include in YOUR AGENTS.md.

---

## The Connection to This Template

This template's AGENTS.md is essentially **your custom system prompt layer** — it sits on top of whatever system prompt the model provider already gives the model. Understanding the base layer helps you write a better top layer.

```
┌─────────────────────────────┐
│  Your AGENTS.md / Rules     │  ← You control this (this template)
├─────────────────────────────┤
│  Your SKILL.md files        │  ← You control this (skill creation guide)
├─────────────────────────────┤
│  Model's System Prompt      │  ← Provider controls this (study it to align)
├─────────────────────────────┤
│  Model's Base Training      │  ← Provider controls this (can't change)
└─────────────────────────────┘
```

When your instructions **align** with the system prompt, the model performs at its best. When they **conflict**, the model gets confused and output quality drops.
