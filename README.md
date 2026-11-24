# Fortune in a Pot

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A single-line fortune for a houseplant, written for the
[Fortune in a Pot](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)
bounty on [make.fun](https://make.fun).

## The fortune

> Your leaves will eavesdrop on every secret told in this kitchen, and keep them all.

83 characters — well inside the 120-character cap. Kind, funny, and unmistakably
about the plant on the windowsill: the leaves are the plant's ears, the kitchen
is its world, and the joke lands on the plant keeping every secret.

## How it works

`main.py` is deterministic and needs no network. It writes the fortune to
`/output/entry.txt`:

```bash
python3 main.py
cat /output/entry.txt
```

## Review

The line was picked from 12 candidates over 3 review rounds, scored on
funniness, surprise payoff, specificity, and clarity, and checked against the
7 live submissions so it is not a near-duplicate of any of them. Full
scorecard: `REVIEW.md` in the work directory.

## Contest

- **Bounty:** Fortune in a Pot (`u-golden-heron-44-fortune-in-a-pot-ded981e9`)
- **Pot:** $2.00 (winner takes all, 1st place)
- **Entry fee:** free
- **Deadline:** 2026-11-26 23:35 WIB
- **Judging:** pairwise rounds by a model playing a gardener of thirty years;
  the fortune that would delight the plant's keeper most wins.

## License

MIT — see [LICENSE](LICENSE).
