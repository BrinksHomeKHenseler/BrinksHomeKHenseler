#!/usr/bin/env python3
"""Parse every YAML file in the repository and fail on syntax errors.

Run locally with:  python3 .github/scripts/check_yaml.py
"""

from __future__ import annotations

import pathlib
import sys

import yaml

SKIP_DIRS = {".git", "node_modules"}


def main() -> int:
    root = pathlib.Path(__file__).resolve().parents[2]
    failed = False

    paths = sorted(
        path
        for pattern in ("*.yml", "*.yaml")
        for path in root.rglob(pattern)
        if not SKIP_DIRS.intersection(path.relative_to(root).parts)
    )

    if not paths:
        print("no YAML files found")
        return 0

    for path in paths:
        rel = path.relative_to(root)
        try:
            list(yaml.safe_load_all(path.read_text(encoding="utf-8")))
        except yaml.YAMLError as exc:
            failed = True
            print(f"::error file={rel}::{exc}")
        else:
            print(f"ok  {rel}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
