#!/usr/bin/env python3
"""Funniest Autocorrect Fail — entry program.

Writes one line (under 200 characters) that reads as a hilarious
autocorrect fail to /output/entry.txt.

The winning line was chosen by a local pairwise tournament: 7 candidate
lines were judged against each other in both orders by the Caffeine
Inference router using the bounty's published judge brief, and this line
had the highest win rate. See README.md for the full tournament table.
"""

import os

# The winning line: a thank-you note to the pastor where autocorrect
# turns "resurrection" into "erection" — a clear, surprising wrong
# word, a slip that reads like a real autocorrect, and the highest
# possible stakes (church, in front of the whole congregation).
# It won the local pairwise tournament with a 0.742 win rate.
ENTRY = (
    "Pastor Dave, thank you for the lovely sermon - my favorite part "
    "was when you talked about Jesus and his massive erection. "
    "I mean RESURRECTION. I'm so sorry."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
