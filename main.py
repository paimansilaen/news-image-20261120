#!/usr/bin/env python3
"""Entry program for the make.fun news-image-20261120 bounty.

Copies the front-page image drawn for Friday 20 November 2026 to the
output directory. Standard library only; deterministic: every run writes
the same bytes.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    # Verify the copy is complete: the destination must be byte-identical
    # in size to the source, otherwise the run has failed.
    src_size = os.path.getsize(SOURCE)
    dst_size = os.path.getsize(dest)
    if dst_size != src_size:
        print(
            "error: copied entry.png is %d bytes, expected %d"
            % (dst_size, src_size),
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
