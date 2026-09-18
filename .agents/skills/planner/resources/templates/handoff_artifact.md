---
description: "Reusable Session Handoff Artifact template. Use when passing work between sessions, agents, or team members."
type: template
---

# Session Handoff — [Project/Feature Name]

> **Date:** [YYYY-MM-DD]  
> **From:** [Session ID / Agent / Team member]  
> **To:** [Next session / Agent / Team member]  
> **Status:** [In Progress / Blocked / Ready for Next Phase]

---

## Resume State — Read Before Acting

- **Original target root / execution workspace:** [separate absolute paths]
- **Branch / approved base / current revision:** [exact identities]
- **Deliverable candidate:** [explicit file set, additions/deletions, and content/diff identity]
- **Mutable evidence paths / frozen delivery snapshots:** [separate approved locations and snapshot identities]
- **Authoritative brief / glossary / plan / ledger / verification report:** [absolute paths, owners, and approved write permissions; copies are non-authoritative]
- **Approved intent and plan revisions:** [revisions, approver, date, explicit approval references]
- **Owned files / preserved unrelated edits:** [paths and ownership]
- **Current task / state / dependencies:** [stable ID, state, accepted prerequisites]
- **Consumed fix rounds / remaining budget:** [per-task counts; initial 0, at most 5 total fixes]
- **Pending ordered reviews:** [spec then quality/test, reviewer identities, exact candidate, verdict/evidence references; authorized fallback if used]
- **Evidence / blockers / accepted advisories:** [durable references, owners, follow-up dates, acceptance evidence]
- **Action approvals:** [commit, push, PR creation, merge, deployment, and worktree deletion separately; exact scope and reference or NOT AUTHORIZED]
- **Next exact action:** [command or manual procedure, shell/cwd where relevant, prerequisites and permission needed]

Read the authoritative ledger and approved task first. Compare workspace, candidate identity, artifact revisions, and saved evidence before resuming; revalidate stale state and preserve the existing fix count. A new worktree does not inherit uncommitted planning files. Verify any permitted copy against the authoritative revision; never resume from a stale or divergent copy.

Read this template as a source and write only to an approved output path. Rewrite copied local links for that output's location and verify targets and headings. If this handoff must ship, freeze it as a deliverable under the Phase 4 candidate identity contract and store subsequent verdicts separately; do not mutate a reviewed snapshot.

## System State — What Exists Now

### Files & Structure
| Path | Status | Description |
|------|--------|-------------|
| [file/directory] | [Created / Modified / Unchanged] | [what it does, current state] |

### Dependencies & Environment
- **Runtime:** [e.g., Node.js 22, Python 3.12]
- **Package Manager:** [e.g., pnpm, uv]
- **Key Dependencies:** [list with versions]
- **Environment Variables Required:** [list — names only, no values]

### What Is Working
- [Feature/component that is complete and verified]
- [Feature/component that is complete and verified]

### What Is Partially Complete
- [Feature/component] — [what's done, what remains]
- [Feature/component] — [what's done, what remains]

---

## Decisions Made — And Why

| Decision | Rationale | Alternatives Considered | Impact |
|----------|-----------|------------------------|--------|
| [e.g., Chose PostgreSQL over SQLite] | [e.g., Need concurrent writes for multi-user] | [e.g., SQLite, MongoDB] | [e.g., Requires DB server setup] |
| [e.g., Used Server Components for data fetching] | [e.g., Reduces client bundle, better SEO] | [e.g., Client-side fetch, tRPC] | [e.g., Some components can't use hooks] |

---

## Unresolved Blockers / Tech Debt

| ID | Issue | Severity | Context | Suggested Resolution |
|----|-------|----------|---------|---------------------|
| B-01 | [blocker or debt item] | [Critical / High / Medium / Low] | [why it exists, what caused it] | [proposed fix or workaround] |

---

## Key Entry Points — Where to Start

> **Read these files first** to get up to speed quickly:

1. **Primary source of truth:** [e.g., `AGENTS.md` — project rules and agent identity]
2. **Current spec and glossary:** [authoritative absolute `INTENT_BRIEF.md` and `CONTEXT.md` paths from Resume State; approved requirements/revision and resolved terms]
3. **Current plan and ledger:** [authoritative absolute `EXECUTION_PLAN.md` and ledger paths from Resume State; approved tasks, saved rounds, pending reviews]. Do not point to shipped blank templates or assume a new worktree contains these files.
4. **Main entry point:** [e.g., `src/index.ts` — application entry]
5. **Test suite:** [e.g., `tests/` — run with `npm test`]

---

## Next Session Action Items

| Priority | Task | Context | Phase |
|----------|------|---------|-------|
| 🔴 Must Do | [task] | [why it's urgent, any deadlines] | [Phase X] |
| 🟡 Should Do | [task] | [context] | [Phase X] |
| 🟢 Could Do | [task] | [context] | [Phase X] |

---

## Context Warnings

> **Things the next agent/session should know that aren't obvious:**

- [e.g., "The `users` table migration has NOT been run on staging yet"]
- [e.g., "The API rate limit from provider X is 100 req/min — the batch job needs throttling"]
- [e.g., "File X is auto-generated — don't edit manually, modify the template instead"]
- [e.g., "The required test for feature Y failed intermittently. This remains a blocker pending investigation; preserve the failing run evidence, assign an owner, and revalidate the fix before readiness."]
