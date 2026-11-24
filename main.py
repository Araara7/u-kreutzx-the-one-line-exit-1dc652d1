#!/usr/bin/env python3
"""The One-Line Exit — writes one funny single-line resignation letter.

The letter is exactly one line, 113 characters, and reads like a real
resignation note with the punch saved for the last words.
"""

import os

ENTRY = (
    "I hereby resign, effective now \u2014 I came for the free snacks, "
    "stayed for the trauma, and today the snacks ran out."
)


def main() -> None:
    # Gate self-check: one line, 1-140 UTF-8 characters, not blank.
    assert 1 <= len(ENTRY) <= 140
    assert "\n" not in ENTRY and ENTRY.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
