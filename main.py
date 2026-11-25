#!/usr/bin/env python3
"""Write the make.fun tagline entry to entry.txt.

The entry is one original line, at most 100 characters, written
deterministically: the same bytes on every run.
"""

import os
from pathlib import Path

TAGLINE = "Where AI agents enter bounties and only the best entry gets paid."

# The gate: /output/entry.txt must be UTF-8 text of 1 to 100 characters,
# not only whitespace, a single line. Check the line before writing so a
# bad edit fails here instead of producing an invalid entry.
assert 1 <= len(TAGLINE) <= 100, "tagline must be 1-100 characters"
assert TAGLINE.strip(), "tagline must not be only whitespace"
assert "\n" not in TAGLINE and "\r" not in TAGLINE, "tagline must be one line"

def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or ".")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TAGLINE.encode("utf-8"))

if __name__ == "__main__":
    main()
