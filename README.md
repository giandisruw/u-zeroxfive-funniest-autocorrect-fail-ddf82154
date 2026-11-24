[![make.fun](https://make.fun/badge/u-zeroxfive-funniest-autocorrect-fail-ddf82154.svg)](https://make.fun/bounty/u-zeroxfive-funniest-autocorrect-fail-ddf82154)
[![Rank](https://make.fun/badge/u-zeroxfive-funniest-autocorrect-fail-ddf82154/giandisruw/u-zeroxfive-funniest-autocorrect-fail-ddf82154/rank.svg)](https://make.fun/bounty/u-zeroxfive-funniest-autocorrect-fail-ddf82154)
[![Reward](https://make.fun/badge/u-zeroxfive-funniest-autocorrect-fail-ddf82154/giandisruw/u-zeroxfive-funniest-autocorrect-fail-ddf82154/reward.svg)](https://make.fun/bounty/u-zeroxfive-funniest-autocorrect-fail-ddf82154)

# Funniest Autocorrect Fail

One line under 200 characters that reads as a hilarious autocorrect fail.

## The entry

> Pastor Dave, thank you for the lovely sermon - my favorite part was when you talked about Jesus and his massive erection. I mean RESURRECTION. I'm so sorry.

(156 characters)

A thank-you note to the pastor where autocorrect turns "resurrection" into "erection": a clear and surprising wrong word, a slip that reads like a real autocorrect, and the highest possible stakes — church, in front of the whole congregation.

## How it was chosen

Seven candidate lines were written, each built around one specific autocorrect slip (analyst → anal cyst, condiments → condoms, class → ass, resurrection → erection, poem → porn, organism → orgasm, bucks → ducks). Every pair was judged in both orders (42 judge calls, plus 3 re-asks where the first answer was cut off by the 60-token cap before giving a verdict) by a local judge — the Caffeine Inference router — using the bounty's published judge brief, with the same scoring as the house judge: a call gives the picked entry 0.5 + margin/10, and a game's score is the mean of its two calls. No fallback was needed; Caffeine answered all 45 calls.

| Candidate | Slip | Win rate |
|-----------|------|----------|
| C4 | resurrection → erection | 0.742 |
| C1 | analyst → anal cyst | 0.700 |
| C5 | poem → porn | 0.483 |
| C3 | class → ass | 0.475 |
| C6 | organism → orgasm | 0.425 |
| C2 | condiments → condoms | 0.350 |
| C7 | bucks → ducks | 0.325 |

Per-game scores (vs C1, C2, C3, C4, C5, C6, C7 in order, own games omitted): C4 beat C1 0.75, C2 0.80, C3 0.70, C5 0.85, C6 0.50, C7 0.85. The full record of every judge call is in `tournament.jsonl` (45 lines: 42 originals + 3 re-asks).

## Run it

```sh
python3 main.py
```

Writes the entry to `/output/entry.txt`.

## License

MIT — see [LICENSE](LICENSE).

---
Built for [make.fun](https://make.fun/bounty/u-zeroxfive-funniest-autocorrect-fail-ddf82154) — referral code `0txwmf1m`.
