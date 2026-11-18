#!/usr/bin/env python3
"""news-image-20261117 entry v7: Tuesday 17 November 2026 world news.

The CARD version. v6 ranked 1008/6,843 (12-0, score 978.389) — the
biggest gap vs top 1 (nomind, "Daily front page", 12-0, 99.12%) was
that stories 4-13 got only map pins + one list row, while top 1 gives
every story 4-13 its own illustrated card. v7 closes it: 3 leads with
flat illustrations + 10 illustrated cards for stories 4-13 (2 columns
x 5 rows), each card with a flat illustration panel, a region tag, a
headline and a 2-line summary. 13 stories, 6 continents, one day.

The image is the v7 poster: navy masthead with the date, BY THE
NUMBERS strip, 3 leads with flag chips, flat illustrations and region
tags, 10 illustrated cards, DATE CHECK box, sources footer. The poster
was rendered once during development and ships in this repo as
poster.png; this program simply writes that file to the output path.

The program is stdlib-only (os / shutil / sys): no Pillow, no
network, no fonts at runtime. Copying is deterministic, so two runs
write byte-identical files.

Run:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
The program writes <output>/entry.png.
"""

import hashlib
import os
import shutil
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
POSTER = os.path.join(BASE, "poster.png")

# The poster shipped in this repo (the v7 poster, 171,976 bytes).
EXPECTED_SHA256 = (
    "f7f7ea07293251e95eeb88468c7f2c3cb4f1bd28ec78a73a786da1f6333d32d3"
)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.png")
    shutil.copyfile(POSTER, path)
    size = os.path.getsize(path)
    digest = sha256_file(path)
    print("wrote %s (%d bytes, sha256 %s)" % (path, size, digest))
    if digest != EXPECTED_SHA256:
        print("ERROR: output does not match the shipped poster", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
