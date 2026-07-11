#!/usr/bin/env python3
"""Lightweight repo health checks for the Cursor DE Agent demo workflow."""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = ("README.md", "TESTING.md", "VALIDATION.md")
FORBIDDEN_ROOT_FILES = (".env",)


def check_required_files() -> list[str]:
    failures: list[str] = []
    for name in REQUIRED_FILES:
        path = REPO_ROOT / name
        if path.is_file():
            print(f"PASS  {name} exists")
        else:
            failures.append(f"FAIL  {name} is missing")
    return failures


def check_forbidden_files() -> list[str]:
    failures: list[str] = []
    for name in FORBIDDEN_ROOT_FILES:
        path = REPO_ROOT / name
        if path.exists():
            failures.append(f"FAIL  {name} must not exist in repo root")
        else:
            print(f"PASS  no {name} in repo root")
    return failures


def main() -> int:
    print(f"Validating repo: {REPO_ROOT}")
    print("-" * 40)

    failures = check_required_files() + check_forbidden_files()

    for message in failures:
        print(message)

    print("-" * 40)
    if failures:
        print(f"Validation failed ({len(failures)} check(s))")
        return 1

    print("All checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
