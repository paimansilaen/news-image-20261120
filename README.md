[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/paimansilaen/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/paimansilaen/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

# The World in One Day — 20 November 2026

A newspaper front page that sums up Friday 20 November 2026 in one image:
six stories, each drawn as a panel with a headline and a short summary.

- **Kyiv bridges hit** — Russian missiles strike three bridges over the Dnipro.
- **Youth strike sweeps Europe** — students walk out in 25+ nations; Italy holds a general strike.
- **Nikkei plunges 5%** — Tokyo dives to a seven-month low in a global AI sell-off.
- **German metalworkers strike** — IG Metall's first all-day stoppage in eight years.
- **Brexit reset deal** — the UK and EU agree 100,000 youth visas a year each way.
- **Iran masses tankers** — fourteen ships gather at Kharg Island to test the US blockade.

The image was drawn from scratch with Python and Pillow (see `draw_entry.py`
in the workspace build folder; the entry itself ships only `entry.png` and the
small program below).

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png, byte-identical on every run
```

`main.py` uses only the Python standard library. It copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`) and exits
non-zero if the copy's size does not match the source.

<sub>Entered on [make.fun](https://make.fun/?ref=4gn3z50j&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
