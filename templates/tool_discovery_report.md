---
description: "Reusable Tool Discovery Report template. Used during Phase 3 Tooling to document the discovery and evaluation process."
type: template
---

# Tool Discovery Report — [Project/Feature Name]

> **Date:** [YYYY-MM-DD]  
> **Execution Plan:** [link to execution_plan.md]

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

#### Step 2 — MCP Servers
- **Searched:** [registries checked]
- **Candidates Found:**
  | Server Name | Source | Score | Notes |
  |-------------|--------|-------|-------|
  | [name] | [registry] | [X.X] | [notes] |

#### Step 3 — Package Registries
- **Searched:** [registries checked]
- **Candidates Found:**
  | Package | Registry | Score | Notes |
  |---------|----------|-------|-------|
  | [name] | [npm/pypi/etc] | [X.X] | [notes] |

#### Step 4 — APIs
- **Searched:** [sources checked]
- **Candidates Found:**
  | API | Provider | Score | Notes |
  |-----|----------|-------|-------|
  | [name] | [provider] | [X.X] | [notes] |

#### Step 5 — Agent Skills/Plugins
- **Searched:** [sources checked]
- **Candidates Found:** [list or "none"]

#### Step 6 — Custom Build Required?
- **Required:** [Yes/No]
- **Justification:** [why existing tools are insufficient]

#### ✅ Selected Solution
- **Tool:** [chosen tool/server/API]
- **Source:** [where it came from]
- **Score:** [X.X / 5.0]
- **Config:** [how to set it up]

---

## Final Harness Configuration

### Built-in Tools
| Tool | Capability |
|------|-----------|
| [tool] | [capability] |

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

- [ ] All tool needs addressed (discovered or flagged for custom build).
- [ ] No unnecessary custom tools — existing solutions prioritized.
- [ ] Orchestrator reviewed and approved harness configuration.
