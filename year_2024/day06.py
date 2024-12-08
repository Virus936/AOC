from collections import Counter
from collections import defaultdict
from typing import Iterator
from itertools import product
import re
from functools import cmp_to_key

# response = sorted(c, key=cmp_to_key(lambda a, b: 1 if b in graph[a] else -1))
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def transpose(ls: Iterator):
    return list(map(list, zip(*ls)))


def intify(ls: list[str]) -> list[int]:
    return list(map(int, ls))


def parse_data(brut_data: str) -> list[int]:
    lines = [list(line) for line in brut_data.splitlines()]
    start = 0, 0
    for i, r in enumerate(lines):
        for j, c in enumerate(r):
            if c in "^>v<":
                start = i, j
    return start, lines


def parcourir(start, lines):
    nrow, ncol = start
    dir = 0
    while True:
        yield nrow, ncol, dir

        dir_row, dir_col = DIR[dir]

        is_extra_row = not 0 <= nrow + dir_row < len(lines)
        is_extra_col = not 0 <= ncol + dir_col < len(lines[0])
        if is_extra_row or is_extra_col:
            break

        if lines[nrow + dir_row][ncol + dir_col] == "#":
            dir = (dir + 1) % 4
            dir_row, dir_col = DIR[dir]
        else:
            nrow += dir_row
            ncol += dir_col


def part1(ls: str) -> int:
    start, lines = parse_data(ls)
    response = 0
    mem = set()
    for r, c, _ in parcourir(start, lines):
        if (r, c) in mem:
            continue
        mem.add((r, c))
        response += 1
    return response


from copy import deepcopy


def part2(ls: str) -> int:
    start, lines = parse_data(ls)
    response = 0
    memo = set()

    for i, j, _ in parcourir(start, lines):
        if (i, j) in memo:
            continue
        memo.add((i, j))

        new_lines = deepcopy(lines)
        new_lines[i][j] = "#"
        mem = set()
        for nrow, ncol, dir in parcourir(start, new_lines):
            if (nrow, ncol, dir) in mem:
                response += 1
                break
            mem.add((nrow, ncol, dir))

    return response


response = part1
