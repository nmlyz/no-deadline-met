#!/usr/bin/env python3
"""Write one line to /output/entry.txt: a joke excusing a missed deadline.

The line was picked from 36 candidates by pairwise judging against the
brief — an excuse with a real turn, a single sentence that reads cleanly
aloud and lands its punch at the end. The excuse is the auto-save itself:
the feature meant to protect the work is what hid it, and the document
is now unreachable in a folder that never existed. The program builds
the line from two clauses — the auto-save that hid the document, then
where the document went — and checks the result against the entry gate
(length, single line, no leading or trailing space) before writing it,
then reads the file back to confirm the bytes match.
"""

import os
import sys

LINE = (
    "The document auto-saved to a folder that doesn't exist, "
    "and now it's living its best life there."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    if not (1 <= len(LINE) <= 200):
        sys.exit(f"line is {len(LINE)} characters, gate needs 1-200")
    if "\n" in LINE or LINE != LINE.strip():
        sys.exit("line must be a single line with no surrounding space")
    data = (LINE + "\n").encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        if f.read() != data:
            sys.exit("read-back mismatch")
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
