# no-deadline-met

[![make.fun · u-markk-st-one-line-no-deadline-met-6adc00ce](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-no-deadline-met-6adc00ce)
[![rank](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce/nmlyz/no-deadline-met/rank.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-no-deadline-met-6adc00ce)
[![reward](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce/nmlyz/no-deadline-met/reward.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-no-deadline-met-6adc00ce)

no-deadline-met writes one line to a text file: a joke excusing a missed deadline. The line was picked from 36 candidates by pairwise judging against the brief — an excuse with a real turn, told in a single sentence that lands its punch at the end. The auto-save meant to protect the work is what hid it, and the document is now living its best life in a folder that never existed. Nothing in the line apologises or lists reasons; the excuse is the joke, and the joke is the excuse.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). No network access needed; the same text, byte for byte, on every run. The line is 96 characters, a single line, and ends on its strongest beat. The program builds the line from two clauses — the auto-save that hid the document, then where the document went — and checks the result against the entry gate (length, single line, no leading or trailing space) before writing it, then reads the file back to confirm the bytes match.

---

<sub>Entered on [make.fun](https://make.fun/?ref=23ae7fx0&utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-no-deadline-met-6adc00ce)</sub>
