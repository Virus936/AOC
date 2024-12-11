from collections import Counter, defaultdict
from typing import Iterator
from itertools import product, combinations
from copy import deepcopy
from functools import cmp_to_key
import re

# response = sorted(c, key=cmp_to_key(lambda a, b: 1 if b in graph[a] else -1))
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIR_8 = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
CLOCKWISE = "^>v<"


def transpose(ls: Iterator):
    return list(map(list, zip(*ls)))


def intify(ls: list[str]) -> list[int]:
    return list(map(int, ls))


#### MAZE ####
def trace(ls):
    return [["." for l in li] for li in ls.splitlines()]


def pprint(trace):
    print("")
    for tr in trace:
        print("".join(tr))
    print("")


##############


def parse_data(brut_data: str) -> list[int]:
    lines = [["."] + list(map(int, l)) + ["."] for l in brut_data.strip().splitlines()]
    lines = [["."] * len(lines[0])] + lines + [["."] * len(lines[0])]

    starts = []

    for r, line in enumerate(lines):
        for c, p in enumerate(line):
            if p == ".":
                continue
            if int(p) == 0:
                starts.append((r, c))
    return starts, lines


def dfs(start, end, map):
    x, y = start
    response = 0
    for dx, dy in DIR:
        if map[x + dx][y + dy] == ".":
            continue
        if int(map[x + dx][y + dy]) != int(map[x][y]) + 1:
            continue
        if end == (x + dx, y + dy):
            return 1
        response += dfs((x + dx, y + dy), end, map)
    return response


def dp_all(start, map, memo: dict = {}):
    x, y = start
    if map[x][y] == 9:
        return 1
    if start in memo:
        return memo[start]
    memo[start] = 0
    for dx, dy in DIR:
        if map[x + dx][y + dy] == ".":
            continue
        if map[x + dx][y + dy] == map[x][y] + 1:
            memo[start] += dp_all((x + dx, y + dy), map, memo)
    return memo[start]


def dp_count(start, map, memo: dict = {}):
    x, y = start
    resp = set()
    if map[x][y] == 9:
        resp.add(start)
        return resp
    if start in memo:
        return memo[start]
    memo[start] = set()
    for dx, dy in DIR:
        if map[x + dx][y + dy] == ".":
            continue
        if map[x + dx][y + dy] == map[x][y] + 1:
            memo[start].update(dp_count((x + dx, y + dy), map, memo))
    return memo[start]


def part1(ls: str) -> int:
    starts, map = parse_data(ls)
    return sum(len(dp_count(start, map, {})) for start in starts)


def part2(ls: str) -> int:
    starts, map = parse_data(ls)
    return sum(dp_all(start, map, {}) for start in starts)


response = part2
