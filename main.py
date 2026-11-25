#!/usr/bin/env python3
"""The Internet in One Word — make.fun bounty entry.

Writes a single word describing the whole internet to /output/entry.txt.
"""

import os

# The entry word: one word, 1-30 characters, nothing else.
ENTRY_WORD = "unhinged"


def main() -> None:
    # Guard: the gate requires UTF-8 text of 1-30 characters, a single word.
    word = ENTRY_WORD.strip()
    assert 1 <= len(word) <= 30, "entry word must be 1-30 characters"
    assert len(word.split()) == 1, "entry must be exactly one word"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
