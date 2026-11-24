#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line of plain text to /output/entry.txt: a review
of planet Earth left by an alien tourist. Pure stdlib, deterministic,
no network at runtime.
"""

ENTRY = (
    "The locals bred wolves into sofa ornaments, then follow them around "
    "collecting their droppings in little bags like treasure. "
    "Four stars, would visit again."
)


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
