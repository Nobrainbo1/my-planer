---
description: "Reusable Retrospective template. Fill this out at the end of every project or iteration."
type: template
---

# Retrospective — [Project/Feature Name]

> **Date:** [YYYY-MM-DD]  
> **Orchestrator:** [Your Name]  
> **Duration:** [Start Date] → [End Date]

---

## Summary
[2-3 sentence summary of what was built and the outcome]

---

## What Went Well ✅
- [item 1]
- [item 2]
- [item 3]

## What Could Be Improved 🔧
- [item 1]
- [item 2]
- [item 3]

## What Surprised Us 🤔
- [item 1]
- [item 2]

---

## Agent Performance

| Metric | Value |
|--------|-------|
| Total tasks | [X] |
| Completed autonomously | [X / Y] ([Z%]) |
| Required escalation | [X / Y] ([Z%]) |
| Consumed shared fix rounds (total) | [sum of per-task ledger counts; evidence references] |
| Avg shared fix rounds per task | [total divided by task count; not hypothesis count] |
| False positives | [X] |
| Missed issues (caught in human review) | [X] |
| Total wall-clock time | [duration] |
| Estimated time without agent (optional) | [Unknown, or explicitly estimated duration with method and evidence] |
| Estimated time saved (optional) | [Unknown, or calculation from the stated estimate; not a measured saving] |

Use the authoritative ledger for task, fix-round, and escalation counts. Record unavailable models/reviewers, verification gaps, and evidence sources; do not invent metrics. Initial attempts and expected Red are not fix rounds.

Read this template as a source and write only to an approved output path. Proposed harness improvements need separate scope approval before edits or installs; this retrospective grants no implementation authority.

---

## Workflow Improvements

| Improvement | Action | Apply To | Priority |
|-------------|--------|----------|----------|
| [improvement] | [action] | [which file/phase] | [H/M/L] |

---

## Tools & Harness Learnings

### Tools That Worked Well
| Tool | Phase Used | Why It Worked |
|------|-----------|---------------|
| [tool] | [phase] | [reason] |

### Tools That Didn't Work / Were Missing
| Need | What Was Tried | Issue | Recommendation |
|------|---------------|-------|----------------|
| [need] | [tool] | [problem] | [fix/alternative] |

### New Rules for AGENTS.md
- [Rule to add based on lessons learned]

---

## Decisions Log
[Key decisions made during the project and their rationale — for future reference]

| Decision | Rationale | Alternatives Considered | Outcome |
|----------|-----------|------------------------|---------|
| [decision] | [why] | [alternatives] | [result] |
