"""One Line Earned Pride (u-mang-one-line-of-earned-pride-a0138557).

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Python 3.13, stdlib only.
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
ENTRY_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

ENTRY = (
    "After 2,000 failed deploys, production stayed green for whole day and "
    "nobody paged me. I sat in dark ops room, breathing, letting real."
)


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(ENTRY_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()