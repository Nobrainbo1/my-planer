---
description: "Phase 5: Verification & Quality Assurance. Comprehensive self-review, automated evals, security scanning, and DoD validation."
phase: 5
checkpoint: false
---

# Phase 5: Verification & Quality Assurance

> **Goal:** Before delivery, validate the entire implementation against the Intent Brief, security standards, performance targets, and the Definition of Done. This phase catches what the Builder-Validator loop in Phase 4 might have missed at the individual task level.

> **Paper Concept:** *"Evals, not vibes."* The paper argues that AI-generated code must be held to the same (or higher) bar as human-written code. Automated evaluation pipelines replace gut-feel verification.

---

## Step 5.1 — Full Test Suite Execution

Run the complete test suite, not just individual task tests.

```markdown
### Full Test Results

#### Unit Tests
- **Runner:** [e.g., vitest, pytest, cargo test]
- **Command:** [e.g., `npm run test:unit`]
- **Results:** [X/Y passing]
- **Coverage:** [X% line, Y% branch]
- **Failing Tests:**
  | Test Name | File | Error | Severity |
  |-----------|------|-------|----------|
  | [test name] | [file] | [error message] | Critical / Warning |

#### Integration Tests
- **Runner:** [e.g., playwright, supertest, httpx]
- **Command:** [e.g., `npm run test:integration`]
- **Results:** [X/Y passing]
- **Failing Tests:**
  | Test Name | File | Error | Severity |
  |-----------|------|-------|----------|
  | [test name] | [file] | [error message] | Critical / Warning |

#### End-to-End Tests (if applicable)
- **Runner:** [e.g., Playwright, Cypress]
- **Command:** [e.g., `npm run test:e2e`]
- **Results:** [X/Y passing]
```

**Decision Gate:**
- All Critical failures must be fixed before proceeding.
- Warning-level failures must be documented with justification if deferred.

---

## Step 5.2 — Code Quality Scan

```markdown
### Code Quality Report

#### Linting
- **Tool:** [e.g., ESLint 9, Ruff, Clippy]
- **Command:** [e.g., `npm run lint`]
- **Errors:** [count]
- **Warnings:** [count]
- **Status:** ✅ Clean / ❌ Has issues

#### Type Checking
- **Tool:** [e.g., TypeScript 5.6, mypy, Rust compiler]
- **Command:** [e.g., `npx tsc --noEmit`]
- **Errors:** [count]
- **Status:** ✅ Clean / ❌ Has issues

#### Code Complexity
- **Cyclomatic complexity hotspots:** [files with high complexity]
- **Largest files:** [files that may need splitting]
- **Dead code:** [any unreachable or unused exports]

#### Formatting
- **Tool:** [e.g., Prettier, Black, rustfmt]
- **Command:** [e.g., `npx prettier --check .`]
- **Status:** ✅ Formatted / ❌ Needs formatting
```

---

## Step 5.3 — Security Audit

```markdown
### Security Audit Report

#### Dependency Vulnerabilities
- **Tool:** [e.g., npm audit, pip-audit, cargo audit]
- **Command:** [e.g., `npm audit`]
- **Critical:** [count]
- **High:** [count]
- **Moderate:** [count]
- **Low:** [count]
- **Action Items:**
  | Package | Vulnerability | Severity | Fix Available | Action |
  |---------|--------------|----------|---------------|--------|
  | [pkg] | [CVE-XXXX-XXXX] | Critical | Yes/No | Upgrade/Replace/Accept |

#### Code Security Review
- [ ] **No hardcoded secrets** (API keys, passwords, tokens) in source code.
- [ ] **Input validation** on all user-facing endpoints and forms.
- [ ] **SQL injection prevention** — parameterized queries or ORM used.
- [ ] **XSS prevention** — output encoding applied where needed.
- [ ] **CSRF protection** — tokens or SameSite cookies in place.
- [ ] **Authentication/Authorization** — access controls verified.
- [ ] **Sensitive data handling** — PII encrypted at rest and in transit.
- [ ] **Error messages** — no stack traces or internal details exposed to users.

#### Secret Scanning
- **Tool:** [e.g., git-secrets, trufflehog, gitleaks]
- **Command:** [e.g., `gitleaks detect`]
- **Findings:** [count — should be 0]
```

---

## Step 5.4 — Performance Validation (if applicable)

```markdown
### Performance Report

#### Benchmarks
| Metric | Target (from NFRs) | Actual | Status |
|--------|-------------------|--------|--------|
| API Response Time (p50) | < 200ms | [X]ms | ✅/❌ |
| API Response Time (p99) | < 500ms | [X]ms | ✅/❌ |
| Page Load Time | < 2s | [X]s | ✅/❌ |
| Memory Usage | < 512MB | [X]MB | ✅/❌ |
| Bundle Size | < 200KB gzipped | [X]KB | ✅/❌ |

#### Load Testing (if applicable)
- **Tool:** [e.g., k6, Artillery, locust]
- **Scenario:** [description of load test]
- **Results:** [summary]
```

---

## Step 5.5 — Spec Compliance Matrix

Map every Functional Requirement from the Intent Brief to its implementation and test.

```markdown
### Spec Compliance Matrix

| Req ID | Requirement | Implemented In | Test | Status |
|--------|-------------|---------------|------|--------|
| FR-01 | [The system must...] | `src/feature.ts` L45-120 | `test/feature.test.ts` | ✅ Met |
| FR-02 | [The system must...] | `src/api/handler.ts` L10-50 | `test/api.test.ts` | ✅ Met |
| FR-03 | [The system should...] | Not implemented | — | ⏭ Deferred (Could Have) |
```

---

## Step 5.6 — Definition of Done Checklist

Run through the DoD defined in Phase 1:

```markdown
### Definition of Done — Final Checklist

- [ ] All "Must Have" functional requirements have corresponding tests.
- [ ] All tests pass (unit, integration, e2e as applicable).
- [ ] Code passes linting and type-checking with zero errors.
- [ ] No critical or high security vulnerabilities (dependency audit).
- [ ] No hardcoded secrets in codebase.
- [ ] Documentation updated:
  - [ ] README reflects current state of the project.
  - [ ] API documentation is accurate (if applicable).
  - [ ] Inline comments explain non-obvious logic.
- [ ] Performance targets met (if specified in NFRs).
- [ ] Change log updated with summary of all modifications.
- [ ] All code formatted consistently.
- [ ] Git history is clean (atomic commits, conventional messages).
```

---

## Step 5.7 — Verification Summary

```markdown
### Verification Summary

| Category | Status | Details |
|----------|--------|---------|
| Unit Tests | ✅/❌ | [X/Y passing, Z% coverage] |
| Integration Tests | ✅/❌ | [X/Y passing] |
| E2E Tests | ✅/❌/⏭ | [results or "not applicable"] |
| Linting | ✅/❌ | [errors/warnings count] |
| Type Checking | ✅/❌ | [errors count] |
| Security Audit | ✅/❌ | [critical/high/moderate counts] |
| Secret Scanning | ✅/❌ | [findings count] |
| Performance | ✅/❌/⏭ | [met targets or "not applicable"] |
| Spec Compliance | ✅/❌ | [X/Y requirements met] |
| DoD Checklist | ✅/❌ | [X/Y items checked] |

### Overall Verdict: ✅ READY FOR DELIVERY / ❌ NEEDS REMEDIATION

[If NEEDS REMEDIATION, list specific blockers and proposed fixes]
```

> **Proceed to [Phase 6: Delivery](./06_DELIVERY.md)** if the verdict is READY FOR DELIVERY.
