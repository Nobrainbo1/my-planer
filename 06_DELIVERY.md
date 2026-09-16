---
description: "Phase 6: Delivery, Handoff & Retrospective. Package the work, deploy, and capture learnings for future iterations."
phase: 6
checkpoint: true
---

# Phase 6: Delivery, Handoff & Retrospective

> **Goal:** Package the verified implementation for deployment, create a clear handoff document, and conduct a retrospective to improve the workflow for the next iteration.

> **Paper Concept:** The paper emphasizes that agentic engineering is an **iterative discipline**. Each project should feed learnings back into the harness configuration, improving agent performance over time.

> **💡 Why This Phase Exists:** Without this, you ship and immediately forget everything you learned. Next project, same mistakes. The retrospective loop makes the template *improve itself* — after every project, you update the rules, add new skills, remove tools that didn't work. Project 10 runs smoother than project 1 because the workflow evolved. This phase also handles **handoffs** — passing context to the next session or team member, because the model is stateless and starts every new session knowing nothing. **On paper:** Write down what went well, what went wrong, and what to change next time.

---

## Step 6.1 — PR / Changeset Packaging

Whether using Git PRs, patch files, or direct deployment, create a structured summary of all changes.

```markdown
### Change Package Summary

#### Title
[Concise title describing the overall change]

#### Description
[2-3 paragraph description of what was built, why, and how it relates to the original Intent Brief]

#### Change Statistics
- **Files created:** [count]
- **Files modified:** [count]
- **Files deleted:** [count]
- **Total lines added:** [count]
- **Total lines removed:** [count]
- **Tests added:** [count]
- **Dependencies added:** [list with versions]
- **Dependencies removed:** [list]

#### Changes by Component
| Component | Files Changed | Summary |
|-----------|--------------|---------|
| [e.g., API Layer] | [list] | [what changed] |
| [e.g., Frontend] | [list] | [what changed] |
| [e.g., Database] | [list] | [what changed] |
| [e.g., Configuration] | [list] | [what changed] |

#### Verification Evidence
- Unit tests: ✅ [X/Y passing]
- Integration tests: ✅ [X/Y passing]
- Lint: ✅ Clean
- Security audit: ✅ No critical issues
- Performance: ✅ Targets met

#### Breaking Changes
- [ ] None
- [ ] Yes — [describe breaking changes and migration path]

#### Rollback Plan
[How to undo these changes if something goes wrong in production]
```

---

## Step 6.2 — Deployment Checklist

```markdown
### Deployment Checklist

#### Pre-Deployment
- [ ] All verification checks pass (Phase 5).
- [ ] Environment variables configured for target environment.
- [ ] Database migrations ready (if applicable).
- [ ] Feature flags configured (if applicable).
- [ ] Monitoring and alerting set up for new endpoints/features.
- [ ] Rollback plan documented and tested.

#### Deployment Steps
1. [Step 1: e.g., Run database migrations]
2. [Step 2: e.g., Deploy backend service]
3. [Step 3: e.g., Deploy frontend build]
4. [Step 4: e.g., Verify health checks]
5. [Step 5: e.g., Enable feature flag]

#### Post-Deployment Verification
- [ ] Health check endpoints responding.
- [ ] Core user flows working (manual smoke test).
- [ ] Error rates normal (no spike in monitoring).
- [ ] Performance within expected range.
- [ ] Logs clean (no unexpected errors).
```

#### 🛑 FINAL CHECKPOINT — Deployment Approval

```
🛑 CHECKPOINT REQUEST — Ready for Deployment

[SUMMARY] All verification passed. Change package documented.
[ENVIRONMENT] [staging / production]
[RISK LEVEL] [Low / Medium / High]
[ROLLBACK PLAN] [documented above]

[DECISION NEEDED] Approve deployment?
```

---

## Step 6.3 — Documentation Update

```markdown
### Documentation Deliverables

- [ ] **README.md** — Updated with new features, setup instructions, and usage.
- [ ] **CHANGELOG.md** — Entry added for this release.
- [ ] **API Documentation** — Updated with new endpoints (if applicable).
- [ ] **Architecture Documentation** — Updated if architecture changed.
- [ ] **Runbook / Ops Guide** — Updated with new operational procedures (if applicable).
```

### CHANGELOG Entry Template
```markdown
## [Version] — [Date]

### Added
- [New feature or capability]

### Changed
- [Modified behavior or refactored component]

### Fixed
- [Bug fix description]

### Removed
- [Deprecated feature or file removed]

### Security
- [Security-related changes]
```

---

## Step 6.3.5 — Session Handoff Artifact

If the project spans multiple sessions, or if work is being passed to another agent or team member, create a **Handoff Artifact** before ending the session.

> **Why this matters:** Models are stateless — the next session starts with zero context. A handoff artifact is the bridge between sessions. Without it, the next agent wastes time rediscovering decisions, re-reading files, and potentially contradicting prior work.

```markdown
### Handoff Checklist

- [ ] System state documented (what exists, what's working, what's partial)
- [ ] Key decisions recorded with rationale
- [ ] Unresolved blockers and tech debt listed
- [ ] Entry points identified (files to read first)
- [ ] Next action items prioritized
- [ ] Context warnings noted (non-obvious gotchas)
```

> Use the template at [`templates/handoff_artifact.md`](./templates/handoff_artifact.md) to structure the handoff.

**When to create a handoff:**
- Context window approaching ~70% capacity (create handoff *before* compaction)
- End of a work session (even if the project isn't complete)
- Before switching to a different agent or model
- When handing off to a human team member

---

## Step 6.4 — Retrospective

The most important step for long-term improvement. Capture learnings and feed them back into the workflow.

The retrospective should cover:
- **What went well** — tools, processes, and decisions that saved time or prevented issues
- **What could be improved** — friction points, rework, and missed opportunities
- **What surprised you** — unexpected behaviors, edge cases, or learnings
- **Agent performance metrics** — autonomy rate, escalation count, self-corrections, time saved
- **Workflow improvements** — concrete actions to apply to the template for the next project
- **Tools & harness learnings** — what worked, what didn't, what's missing
- **Decision log** — key decisions and rationale for future reference

> Use the template at [`templates/retrospective.md`](./templates/retrospective.md) for the full structure.

---

## Step 6.5 — Harness Evolution

Based on the retrospective, update the workflow template itself.

```markdown
### Harness Updates

#### Rules to Add to AGENTS.md
- [New rule based on lessons learned]

#### New Tools to Add to Phase 3 Defaults
- [Tool discovered during this project that should be standard]

#### Templates to Update
- [Which template file] — [what to add/change]

#### Workflow Process Changes
- [Any phase-level changes to the workflow itself]
```

---

## Phase 6 Output

- ✅ Change package documented and ready for deployment.
- ✅ Deployment executed (or artifacts handed off).
- ✅ Documentation updated.
- ✅ Session handoff artifact created (if multi-session).
- ✅ Retrospective completed.
- ✅ Workflow improvements captured and applied.

---

> **🔄 CYCLE COMPLETE.** Return to [Phase 1: Discovery](./01_DISCOVERY.md) for the next feature, iteration, or project.
