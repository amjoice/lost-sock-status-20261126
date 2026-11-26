"""Entry program: one lost sock's status update, nothing more.

The sock has spent 1,204 days in the gap behind the washer and has
just been elected mayor by the dust bunnies. The program writes that
single update to /output/entry.txt and stops. Standard library only,
no network, no randomness: the same bytes on every run.
"""

import os

OPENING = "Day 1,204 in the gap behind the washer."
MIDDLE = "Morale is low."
PUNCHLINE = "The dust bunnies have elected me mayor."
ENTRY = OPENING + " " + MIDDLE + " " + PUNCHLINE
OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 120


def check_gate(text):
    """Refuse to emit anything the bounty gate would reject."""
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError("entry length %d outside gate %d-%d" % (len(text), MIN_CHARS, MAX_CHARS))
    if not text.strip():
        raise ValueError("entry is only white space")


def main():
    check_gate(ENTRY)
    folder = os.path.dirname(OUTPUT_PATH)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
