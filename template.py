# Advent of Code template by @MathisHammel

# TODO
#  - Make a snapshot of the file when a submission is correct
#  - Display the rank when submission is accepted
#  - Utility function to rotate/flip a 2D array
#  - Cycle length detector/extrapolator to make loops faster
#  - Put examples in cache
#  - Warning if DAY is not the current day

import os
import requests

from nogit.aoc_secrets import AOC_COOKIE  # Put your session cookie in this variable

YEAR = "2024"


def get_input(day):
    cache_file = f"year_{YEAR}/inputs/day{day}.txt"
    if os.path.isfile(cache_file):
        print("Reading from cache file")
        return open(cache_file).read()
    print("Fetching from the web")
    req = requests.get(
        f"https://adventofcode.com/{YEAR}/day/{day}/input",
        headers={"cookie": "session=" + AOC_COOKIE},
    )
    if "Please don't repeatedly request" in req.text:
        print("Error: Problem not open yet.")
        return None
    with open(cache_file, "w") as fo:
        fo.write(req.text)
    return req.text


def get_example(day, offset=0):
    req = requests.get(
        f"https://adventofcode.com/{YEAR}/day/{day}",
        headers={"cookie": "session=" + AOC_COOKIE},
    )
    return (
        req.text.split("<pre><code>")[offset + 1]
        .split("</code></pre>")[0]
        .replace("<em>", "")
        .replace("</em>", "")
        .replace("&gt;", ">")
        .replace("&lt;", "<")
    )


def submit(day, answer, level=1, skip_confirm=False):
    if not skip_confirm:
        input(
            f"Day {day} - You are about to submit the follwing answer:\n>>>>>>>>>>>>>>>>> {answer}\nPress enter to continue or Ctrl+C to abort."
        )
    data = {"level": str(level), "answer": str(answer)}

    response = requests.post(
        f"https://adventofcode.com/{YEAR}/day/{day}/answer",
        headers={"cookie": "session=" + AOC_COOKIE},
        data=data,
    )
    if "You gave an answer too recently" in response.text:
        print("VERDICT : TOO MANY REQUESTS")
    elif "not the right answer" in response.text:
        if "too low" in response.text:
            print("VERDICT : WRONG (TOO LOW)")
        elif "too high" in response.text:
            print("VERDICT : WRONG (TOO HIGH)")
        else:
            print("VERDICT : WRONG (UNKNOWN)")
    elif "seem to be solving the right level." in response.text:
        print("VERDICT : INVALID LEVEL")
        if level == 1:
            print("Retrying on level 2")
            submit(day, answer, 2, skip_confirm=True)
        else:
            print("Retrying on next day")
            submit(day + 1, answer, 1, skip_confirm=True)
    else:
        print("VERDICT : OK !")


def ints(s):
    return list(map(int, s.split()))


DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1))  # Clockwise URDL
DIR8 = (
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
)  # Clockwise from U

# Assembler interpreter
"""
prog = s.splitlines()
pc = 0
regs = []
while 0 <= pc < len(prog):
    op = prog[pc]
    if op == 1:
        ...
    elif op == 2:
        ...
    else:
        assert False
    pc += 1
"""

# Graphs
"""
import networkx as nx
G = nx.Graph()
# G.add_edge(5, 1)
nx.shortest_path(G, 1, 5)
"""

"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
from datetime import datetime

DAY = datetime.now().day
import sys

if len(sys.argv) > 1:
    DAY = sys.argv[1]

s = get_input(DAY)
# s = get_example(DAY)

import collections
import math

ans = 0

from year_2024.day01 import response as response01
from year_2024.day02 import response as response02
from year_2024.day03 import response as response03
from year_2024.day04 import response as response04
from year_2024.day05 import response as response05
from year_2024.day06 import response as response06
from year_2024.day07 import response as response07
from year_2024.day08 import response as response08
from year_2024.day09 import response as response09
from year_2024.day10 import response as response10
from year_2024.day11 import response as response11
from year_2024.day12 import response as response12
from year_2024.day19 import response as response19

responses = [
    response01,
    response02,
    response03,
    response04,
    response05,
    response06,
    response07,
    response08,
    response09,
    response10,
    response11,
    response12,
    13,
    14,
    15,
    16,
    17,
    18,
    response19,
]

ans = responses[int(DAY) - 1](s)

submit(DAY, ans)
