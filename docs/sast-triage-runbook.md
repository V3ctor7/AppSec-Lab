# SAST Triage Runbook

## Purpose
Standard procedure for triaging CodeQL findings.

## Step 1: Validate the Finding
For every alert, identify:
- **Source** — where does untrusted data enter? (e.g., `request.args.get()`)
- **Sink** — where does it reach a dangerous function? (e.g., `cursor.execute()`)
- **Flow** — is there any sanitization/validation between them?

If data flows from source to sink with no sanitization → **True Positive**

## Step 2: Classify

| Classification | Action |
|---|---|
| True Positive | Create remediation ticket |
| False Positive | Close with documented justification |
| Needs Investigation | Escalate to dev team for context |

## Step 3: Assess Contextual Severity
- Is the endpoint public-facing or internal-only?
- Is authentication required?
- What data is at risk (PII, credentials, public data)?

## Step 4: Create Remediation Ticket
Include:
- Vulnerability type and CWE
- File path and line number
- Recommended fix with code example
- OWASP/CWE reference link

## Step 5: Track SLAs

| Severity | Remediation SLA |
|---|---|
| Critical | 7 days |
| High | 30 days |
| Medium | 90 days |
| Low | Next release cycle |

## Step 6: Verify Closure
- Confirm fix is merged
- Verify CodeQL rescan shows alert resolved
- Close ticket with evidence

## Common Vulnerability Patterns

### SQL Injection (CWE-89)
- **Source:** User input from request parameters
- **Sink:** String concatenation in SQL query
- **Fix:** Parameterized queries

### Command Injection (CWE-78)
- **Source:** User input
- **Sink:** `subprocess` with `shell=True`
- **Fix:** Use list arguments, remove `shell=True`

### XSS (CWE-79)
- **Source:** User input
- **Sink:** Reflected directly in HTML response
- **Fix:** HTML-encode output

### Path Traversal (CWE-22)
- **Source:** User input for filename
- **Sink:** `open()` file read/write
- **Fix:** Validate path, use `os.path.basename()`
