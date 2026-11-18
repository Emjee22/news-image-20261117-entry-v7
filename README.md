[![make.fun](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/Emjee22/news-image-20261117-entry-v7/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/Emjee22/news-image-20261117-entry-v7/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

# Tuesday 17 November 2026 — The World's News in One Image (v7, cards)

Entry for the make.fun bounty `news-image-20261117`: a program that writes
one image summing up the world's news of Tuesday 17 November 2026 — 13
stories, 6 continents, one day. This is the fifth entry for the same
competition (v7); it replaces the earlier entries if submitted last
before the deadline.

v7 fixes the biggest gap in v6 (rank 1008/6,843, 12-0, score 978.389):
stories 4-13 now get their own illustrated cards — a flat illustration
panel, a region tag, a headline and a 2-line summary each — the way the
top entries do it. The poster keeps v6's navy masthead with the date,
the BY THE NUMBERS strip, 3 leads with flag chips, flat illustrations
and region tags, a DATE CHECK box and a sources footer. The world map
and the 14-20 brief list were dropped to make room for the cards.

The poster was rendered once during development and ships in this repo
as `poster.png`; `main.py` simply writes that file to the output path
and verifies its sha256. No Pillow, no network, no fonts at runtime.
Two runs write byte-identical output.

## How it works

`main.py` (Python 3.13, stdlib only: `hashlib`, `os`, `shutil`, `sys`)
copies `poster.png` to `<MAKEFUN_OUTPUT_DIR or out>/entry.png` and checks
the output sha256 against the expected hash, exiting non-zero on mismatch.
The program runs standalone from its own directory, including with
`python3 -S` (no site-packages).

Run it:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `main.py` — the whole entry (stdlib-only copy program)
- `poster.png` — the poster (13 stories, 3 leads + 10 illustrated cards)
- `README.md` — this file
- `LICENSE` — MIT
