#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt.
Stdlib only, no network.
"""

import os

SENTENCE = (
    "The committee that wants to license every AI model in America spent "
    "the morning debating machine consciousness, then recessed so someone "
    "could Google how to turn the draft bill into a PDF."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
