---
description: "Reusable Verification Report template. Used during Phase 5 for final QA."
type: template
---

# Verification Report — [Project/Feature Name]

> **Date:** [YYYY-MM-DD]  
> **Orchestrator:** [Your Name]  
> **Status:** ✅ Pass / ❌ Fail

---

## 1. Automated Test Results
- **Unit Tests:** [X/Y passing] ([coverage %])
- **Integration Tests:** [X/Y passing]
- **E2E Tests:** [X/Y passing]

## 2. Quality & Security Scans
- **Linter / Formatter:** [Clean / X Warnings]
- **Type Checker:** [Clean / X Errors]
- **Dependency Audit:** [No vulnerabilities / X issues]
- **Secret Scan:** [No secrets found / X issues]

## 3. Manual Verification (Orchestrator)
| Flow / Feature | Tested By | Status | Notes |
|----------------|-----------|--------|-------|
| [Core flow 1] | [Name] | Pass / Fail | [notes] |
| [Core flow 2] | [Name] | Pass / Fail | [notes] |

## 4. Definition of Done Checklist
- [ ] All code implemented and tested
- [ ] Build succeeds without errors
- [ ] CI/CD pipeline green (if applicable)
- [ ] Documentation updated
- [ ] Code reviewed and approved

## 5. Final Verdict
**Decision:** [Proceed to Phase 6 / Return to Phase 4 for fixes]
