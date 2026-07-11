# Repository Validation

Lightweight checks that prove this demo repo is in a good state before opening a PR. No dbt or BigQuery required.

## Run validation

From the repo root:

```bash
python scripts/validate_repo.py
```

On Windows (PowerShell):

```powershell
python scripts/validate_repo.py
```

## Expected output (healthy repo)

```text
Validating repo: /path/to/Test
----------------------------------------
PASS  README.md exists
PASS  TESTING.md exists
PASS  VALIDATION.md exists
PASS  no .env in repo root
----------------------------------------
All checks passed
```

Exit code: **0**

## Checks performed

| Check | Meaning |
|-------|---------|
| `README.md` exists | Project has a top-level readme |
| `TESTING.md` exists | Testing notes are documented |
| `VALIDATION.md` exists | This validation guide is present |
| No `.env` in repo root | Secrets are not committed at the root |

## Failure output

If a check fails, the script prints `FAIL` lines and exits with a non-zero code:

```text
Validating repo: /path/to/Test
----------------------------------------
PASS  README.md exists
FAIL  TESTING.md is missing
PASS  no .env in repo root
----------------------------------------
Validation failed (1 check(s))
```

Exit code: **1**

Fix the reported issues and re-run until all checks pass.
