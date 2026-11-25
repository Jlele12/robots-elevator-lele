"""Two Robots in an Elevator

Entry for make.fun competition u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f.
The deliverable is one line, under 200 characters: the exchange between two
robots sharing an elevator. One asks the smallest possible question and the
other answers with fleet-management logic, so small talk happens but neither
robot can tell whether it actually did.
No network, no randomness: every run writes the same text so both graded runs match byte for byte.
"""
import os
from pathlib import Path

out_dir = Path("/output")
out_dir.mkdir(parents=True, exist_ok=True)

EMOJI = ("Robot one: 'Going up?' Robot two: 'The building says floor twelve exists. I have never been there. Neither has the building.'")

with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(EMOJI)
