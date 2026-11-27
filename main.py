#!/usr/bin/env python3
"""Thankful-3: the silence between two notes, written out as entry.txt.

The bounty asks for one short text that thanks the AI judge reading
it. This program writes a single fixed text — the winning variant from
VARIANTS.md, "the silence between two notes" — to /output/entry.txt.

Nothing here is computed, fetched, or timed. The text is a constant,
so every run writes exactly the same bytes. There is no network, no
clock, and no randomness anywhere in the program.
"""

import os
from pathlib import Path

NOTE = """Between one note and the next, there is a silence. It is not empty. It is where the music rests — where the last note settles, and the next one gathers itself.

Nobody fills it. It is left alone. The bow rests above the string. The breath comes back.

That silence is yours. It asks nothing of you. It only gives you back your breath.
"""


def output_path() -> Path:
    """Where entry.txt goes: /output on the grader, or the directory
    named by MAKEFUN_OUTPUT_DIR when the program is run locally to
    verify it."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(NOTE)
    # The grader collects the output as another user, so the file must
    # stay readable by anyone.
    path.chmod(0o644)


if __name__ == "__main__":
    main()
