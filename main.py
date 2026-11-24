#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching a ridiculous invention that fixes a tiny
everyday annoyance to /output/entry.txt.

Stdlib only, deterministic, no network.
"""

import os

ENTRY = (
    "The Guilt-Trip Plant Pot waters itself and then texts your mum anyway, "
    "so the plant survives and you still get told off."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read-back verification: the file must hold exactly the pitch, one
    # sentence inside the competition gate of 1 to 220 characters.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt does not match the pitch"
    assert 1 <= len(written) <= 220, "entry outside the 1-220 character gate"
    assert written.count(".") == 1 and written.endswith("."), "entry is not one sentence"


if __name__ == "__main__":
    main()
