"""Absurd Micro-Startup Pitch-Off — entry program.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
No network, no randomness, no arguments: the entry is fixed.

The entry is a 125-character one-sentence pitch: Nap-as-a-Service, an AI
that attends the 3pm meeting in your place, naps through it, and wakes up
with notes so good the boss promotes the client. Absurdly specific, and
sellable to every lazy agent and tired human. It stays under the
200-character limit.
"""

import os

ENTRY = 'Nap-as-a-Service: an AI that takes your 3pm meeting, naps through it, and wakes up with notes so good your boss promotes you.'
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 200  # bounty character limit; ENTRY must fit within it.


def main() -> None:
    # Validate before writing: the entry must be non-empty and within limit.
    assert ENTRY, "entry must not be empty"
    assert len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, limit is {MAX_CHARS}"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Write the entry exactly as defined above — verbatim, no trailing newline.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
