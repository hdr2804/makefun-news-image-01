#!/usr/bin/env python3
"""news-image-01 entry: write the day's-news picture to the output dir.

The picture (art.png, beside this file) sums up the world news of Friday
13 November 2026 in one image. This program copies it byte-for-byte to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(os.path.join(HERE, "art.png"), dst)
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")


if __name__ == "__main__":
    sys.exit(main())
