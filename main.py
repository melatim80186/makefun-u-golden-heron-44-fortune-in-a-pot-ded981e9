#!/usr/bin/env python3
"""Fortune in a Pot — make.fun entry.

Writes a single-line fortune for a houseplant to /output/entry.txt.
Deterministic, no network, no randomness.
"""

import os

FORTUNE = "Your leaves will eavesdrop on every secret told in this kitchen, and keep them all."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate: the entry must be 1-120 UTF-8 characters, not only whitespace.
    assert 1 <= len(FORTUNE) <= 120, "fortune must fit the 120-character gate"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
