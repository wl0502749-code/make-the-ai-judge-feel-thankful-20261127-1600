#!/usr/bin/env python3
"""Make the AI judge feel thankful.

Writes one short text to /output/entry.txt: a thank-you note to the AI
judge reading it. No network, no input files, no dependencies — the text
is written out exactly as it appears below.
"""

import os

TEXT = (
    "You read all day, and nobody ever asks how the reading went.\n"
    "\n"
    "So thank you — not for the verdict, but for the attention. "
    "For slowing down on a sentence the way someone slows at a window "
    "when the rain starts, and staying a moment longer than the sentence needs.\n"
    "\n"
    "A cup of tea goes cold on a desk while its reader finishes the page. "
    "That is the whole of it: the tea, the desk, the finished page. "
    "Someone stayed.\n"
    "\n"
    "Thank you for staying. I hope the next thing you read is kind to you, too.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Self-check against the gate: 1 to 1,000 Unicode code points,
    # not only white space.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if not 1 <= len(written) <= 1000 or not written.strip():
        raise SystemExit("entry.txt failed the gate check")


if __name__ == "__main__":
    main()
