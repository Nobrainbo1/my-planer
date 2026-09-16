---
description: "Reusable Task Execution Log template. Used during Phase 4 to track the Builder-Validator loop."
type: template
---

# Task Execution Log — [Task ID]

> **Date:** [YYYY-MM-DD]  
> **Task:** [Task Name]  
> **Status:** [In Progress / Blocked / Complete]

---

## 1. Builder Output
- **Files Created:** [list]
- **Files Modified:** [list]
- **Files Deleted:** [list]
- **Tests Written:** [list]

## 2. Validator Results
| Check | Status | Notes |
|-------|--------|-------|
| Syntax | ✅ Pass / ❌ Fail | [notes] |
| Type Check | ✅ Pass / ❌ Fail | [notes] |
| Lint | ✅ Pass / ❌ Fail | [notes] |
| Unit Tests | ✅ Pass (X/Y) / ❌ Fail | [notes] |
| Build | ✅ Pass / ❌ Fail | [notes] |

## 3. Self-Correction Attempts (if any)
| Attempt | Error | Fix Applied | Result |
|---------|-------|-------------|--------|
| 1 | [error] | [fix] | [Pass/Fail] |

## 4. Critic Review (Spec Compliance)
- [ ] Functional requirements met
- [ ] Non-functional requirements met
- [ ] No unplanned side effects
- **Verdict:** ✅ Compliant / ❌ Needs Revision
