# The One-Line Exit

[![Make.fun](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)
[![Rank](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/aahcoba8-maker/makefun-one-line-exit-20261124/rank.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)
[![Reward](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/aahcoba8-maker/makefun-one-line-exit-20261124/reward.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)

One funny resignation letter, exactly one line long, for the
[make.fun](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)
bounty "The One-Line Exit".

## The entry

> I hereby resign, effective immediately — I found a job that pays in real money, not exposure and free pizza.

108 characters, one line. It reads like a letter a person could
actually send: a concrete workplace payoff (a real salary) against a
specific, recognizable grievance (being paid in "exposure and free
pizza"), with the punchline landing where the reader does not expect
it.

## How it works

`main.py` (stdlib only) writes the letter to `entry.txt` inside the
output directory the harness provides (`MAKEFUN_OUTPUT_DIR`, mounted
at `/output` by the grader), and refuses to write anything outside
the 1–140 character gate.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
