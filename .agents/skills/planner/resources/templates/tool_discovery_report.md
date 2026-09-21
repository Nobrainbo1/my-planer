---
description: "Reusable Tool Discovery Report template. Used during Phase 3 Tooling to document the discovery and evaluation process."
type: template
---

# Tool Discovery Report — [Project/Feature Name]

> **Date:** [YYYY-MM-DD]  
> **Output:** [exact approved target-project report path]
> **Host OS & Shell:** [e.g., Windows 11 (pwsh), macOS Sonoma (zsh), Ubuntu (bash)]
> **Active AI Harness:** [e.g., Antigravity, Claude Code, Cursor, Cline/Roo Code]
> **Execution Plan:** `EXECUTION_PLAN.md` [authoritative absolute path and approved revision]
> **Outcome:** [reuse existing tools / proposed additions / blocked]

Read this template as a source; never fill in the shipped original. Rewrite copied local links relative to the generated output and verify exact filename case and heading targets. No new tooling is a valid outcome. If an existing tool is adequate, record it and mark later searches unnecessary with a reason.

---

## Tool Needs Inventory

| ID | Capability Needed | Category | Priority |
|----|------------------|----------|----------|
| T-01 | [capability] | [category] | Must Have |
| T-02 | [capability] | [category] | Should Have |

---

## Discovery Results

### T-01: [Capability Name]

#### Step 1 — Built-in Tools
- **Checked:** [Yes/No]
- **Available:** [Yes/No — tool name]
- **Adequate:** [Yes/No — reason]

#### Step 2 — Agent Skills/Plugins
- **Searched:** [sources checked]
- **Candidates Found:** [list or "none"]

#### Step 2c — AXI CLIs (Agent eXperience Interface — axi.md)
- **Searched:** [axi.md catalog, npm-axi, gh-axi, etc.]
- **Candidates Found:**
  | AXI Tool | Command / Source | Token Savings | Notes |
  |----------|------------------|---------------|-------|
  | [name]   | [npx runner/CLI] | [~40% vs MCP] | [notes] |

#### Step 3 — MCP Servers (Ecosystem Fallback)
- **Searched:** [registries checked]
- **Candidates Found:**
  | Server Name | Source | Score | Notes |
  |-------------|--------|-------|-------|
  | [name] | [registry] | [X.X] | [notes] |

#### Step 4 — Package Registries
- **Searched:** [registries checked]
- **Candidates Found:**
  | Package | Registry | Score | Notes |
  |---------|----------|-------|-------|
  | [name] | [npm/pypi/etc] | [X.X] | [notes] |

#### Step 5 — APIs
- **Searched:** [sources checked]
- **Candidates Found:**
  | API | Provider | Score | Notes |
  |-----|----------|-------|-------|
  | [name] | [provider] | [X.X] | [notes] |

#### Step 6 — Custom Build Required?
- **Required:** [Yes/No]
- **Justification:** [why existing tools are insufficient]

#### ✅ Selected Solution
- **Tool:** [chosen tool/server/API]
- **Source:** [where it came from]
- **Score:** [X.X / 5.0]
- **OS & Harness Compatibility:** [Verified on Host OS & Active Harness / Degraded / Postponed Hazard]
- **Config:** [proposed setup; no secret values]
- **Pinned source/version and evaluation evidence:** [exact source identity; functionality, trust, security, permissions, side effects, caveats]
- **Proposed action:** [exact install/configuration/retrieval command, shell, cwd, destination, and affected files; or no action]
- **Plan impact:** [owning tasks/tests; updated preflight and renewed intent/plan approval if material; or none]
- **Separate install approval:** [approver, date, explicit message/reference for this action; NOT AUTHORIZED or N/A with reason]
- **Other required permissions:** [action, exact scope and approval reference; or none]
- **Actual action and validation:** [timestamp, command/cwd, exit code, output reference; NOT RUN until observed]

Evaluate before installation or adoption. A score or harness approval is not install permission. Do not run discovery commands that download or execute unapproved packages. New custom tooling or scaffold implementation must be approved in the plan and handed off to the execution agent.

---

## Final Harness Configuration

### Environment & Harness Profile
- **Host OS & Shell:** [e.g., Windows 11 / pwsh]
- **Active AI Harness:** [e.g., Antigravity]
- **Platform Hazard Check:** [Passed — no unverified native daemons or proprietary harness hooks]
- **Active Tool Budget:** [X / 5 max (Budget Enforced)]

### Built-in Tools
| Tool | Capability |
|------|-----------|
| [tool] | [capability] |

### AXI CLIs (Agent eXperience Interface)
| Tool / Command | Capability | Token Overhead | Config Required |
|----------------|-----------|----------------|-----------------|
| [e.g. gh-axi]  | [GitHub ops] | Low (~40% less) | [None / token]  |

### MCP Servers
| Server | Capability | Protocol | Config Required |
|--------|-----------|----------|-----------------|
| [server] | [capability] | stdio/sse | [config notes] |

### External Packages/APIs
| Name | Type | Capability | Auth |
|------|------|-----------|------|
| [name] | Package/API | [capability] | [auth method] |

### Custom Tools (to be built)
| Name | Capability | Justification | Est. Effort |
|------|-----------|---------------|-------------|
| [name] | [capability] | [why custom] | [S/M/L] |

---

## Approval

- [ ] All tool needs addressed by available tools or approved custom-build tasks with satisfied prerequisites; unavailable capability remains explicitly blocked.
- [ ] OS & Harness compatibility verified for all proposed tools (no platform hazards or unverified harness hooks).
- [ ] Anti-Bloat Tool Budget respected (≤ 3–5 active tools).
- [ ] No unnecessary custom tools — existing solutions prioritized; no new tooling is a valid outcome.
- [ ] Candidates evaluated before installation or adoption; separate action approvals and actual validation evidence recorded.
- [ ] Material changes returned to planning for renewed approval and preflight before affected execution.
- [ ] Orchestrator reviewed and approved harness configuration.

**Harness approval:** [approver, date, exact configuration revision, explicit message/reference; not installation permission]
