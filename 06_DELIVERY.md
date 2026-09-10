---
description: "Phase 6: Delivery, Handoff & Retrospective. Package the work, deploy, and capture learnings for future iterations."
phase: 6
checkpoint: true
---

# Phase 6: Delivery, Handoff & Retrospective

> **Goal:** Package the verified implementation for deployment, create a clear handoff document, and conduct a retrospective to improve the workflow for the next iteration.

> **Paper Concept:** The paper emphasizes that agentic engineering is an **iterative discipline**. Each project should feed learnings back into the harness configuration, improving agent performance over time.

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

#### 🛑 FINAL CHECKPOINT — Deployment Approval
```
🛑 CHECKPOINT REQUEST — Ready for Deployment

[SUMMARY] All verification passed. Change package documented.
[ENVIRONMENT] [staging / production]
[RISK LEVEL] [Low / Medium / High]
[ROLLBACK PLAN] [documented above]

[DECISION NEEDED] Approve deployment?
```
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

## Step 6.4 — Retrospective

The most important step for long-term improvement. Capture learnings and feed them back into the workflow.

```markdown
### Project Retrospective

#### What Went Well
- [e.g., "The tool discovery phase saved significant time by finding an existing MCP server for database access."]
- [e.g., "The Builder-Validator loop caught 12 issues before human review."]
- [e.g., "High-Level planning let us align with stakeholders before committing to tech decisions."]

#### What Could Be Improved
- [e.g., "The Intent Brief lacked specific edge case definitions, causing rework in Phase 4."]
- [e.g., "Agent hit retry limit 3 times on CSS layout issues — needs better UI testing tools."]
- [e.g., "Planning phase took too long — consider starting with High-Level and drilling down only where needed."]

#### Workflow Improvements to Apply
| Improvement | Action | Apply To |
|-------------|--------|----------|
| [e.g., Add CSS-specific test tools] | Add Storybook visual testing to 03_TOOLING.md | Phase 3 |
| [e.g., Edge case template] | Add edge case section to Intent Brief template | Phase 1 |
| [e.g., Increase retry limit for UI tasks] | Update AGENTS.md retry table | AGENTS.md |

#### Agent Performance Metrics
| Metric | Value |
|--------|-------|
| Tasks completed autonomously (no escalation) | [X / Y] |
| Tasks requiring escalation | [X / Y] |
| Total self-correction cycles | [count] |
| Avg self-corrections per task | [count] |
| False positives (agent flagged issue that wasn't real) | [count] |
| Missed issues (found in human review) | [count] |
| Total time (wall clock) | [duration] |
| Estimated time without agent | [duration] |
```

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
- ✅ Retrospective completed.
- ✅ Workflow improvements captured and applied.

---

> **🔄 CYCLE COMPLETE.** Return to [Phase 1: Discovery](./01_DISCOVERY.md) for the next feature, iteration, or project.
