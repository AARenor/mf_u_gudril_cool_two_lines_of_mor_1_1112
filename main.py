#!/usr/bin/env python3
"""Write one short text for make.fun bounty
u-gudril-cool-two-lines-of-morning-light-ade94fc5."""

import os
import sys
from pathlib import Path

TEXT = "The cat has not moved since six.\nThe square of light has, and takes her with it."


def output_dir() -> Path:
    override = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR")
    if override:
        return Path(override)
    return Path("/output")


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"text length out of range: {len(TEXT)}"
    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    destination = target / "entry.txt"
    destination.write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
