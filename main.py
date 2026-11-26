#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory — make.fun entry.

Writes one sentence to /output/entry.txt: a childhood memory, at most
280 characters. The house judge compares lines in pairs and the most
nostalgic one takes the whole prize.
"""

import os

ENTRY = (
    "Grandma's kitchen smelled of fresh rice and rain on hot concrete, "
    "and for one summer evening the whole world fit inside that small warm room."
)


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 280, f"entry must be 1-280 chars, got {len(text)}"
    assert text == text.strip(), "entry must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"Wrote {len(text)} chars to /output/entry.txt")
    print(text)


if __name__ == "__main__":
    main()
