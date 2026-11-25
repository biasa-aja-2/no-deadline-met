"""One-line deadline excuse for make.fun.

Writes a single-line joke excusing a missed deadline to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Pure stdlib, deterministic, no network, no randomness.
"""
import os
import sys

LINE = "I outsourced the deadline to future me, and future me just filed for bankruptcy."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
