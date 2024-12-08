from collections import Counter
from collections import defaultdict
from typing import Iterator
from itertools import product
import re
from copy import deepcopy
from functools import cmp_to_key

# response = sorted(c, key=cmp_to_key(lambda a, b: 1 if b in graph[a] else -1))
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
CLOCKWISE = "^>v<"


def transpose(ls: Iterator):
    return list(map(list, zip(*ls)))


def intify(ls: list[str]) -> list[int]:
    return list(map(int, ls))


def parse_data(brut_data: str) -> list[int]:
    lines = brut_data.splitlines()
    graph = defaultdict(list)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c != ".":
                graph[c].append((i, j))
    return len(lines), len(lines[0]), graph


def antinode_from_antena_pair(antenna1, antenna2, nrow, ncol):
    antinodes = set()
    if antenna1 == antenna2:
        return antinodes
    x1, y1 = antenna1
    x2, y2 = antenna2

    dx = x1 - x2
    dy = y1 - y2

    x1 += dx
    x2 -= dx
    y1 += dy
    y2 -= dy

    if 0 <= x1 < nrow and 0 <= y1 < ncol:
        antinodes.add((x1, y1))
    if 0 <= x2 < nrow and 0 <= y2 < ncol:
        antinodes.add((x2, y2))
    return antinodes


def compute(antennas, nrow, ncol, part=1):
    antinodes = set()
    for antenna1, antenna2 in product(antennas, repeat=2):
        if part == 1:
            antinodes.update(antinode_from_antena_pair(antenna1, antenna2, nrow, ncol))
        elif part == 2:
            antinodes.update(
                antinode_beam_from_antena_pair(antenna1, antenna2, nrow, ncol)
            )
    return antinodes


def antinode_beam_from_antena_pair(antenna1, antenna2, nrow, ncol):
    antinodes = set()
    if antenna1 == antenna2:
        return antinodes
    x1, y1 = antenna1
    x2, y2 = antenna2

    dx = x1 - x2
    dy = y1 - y2

    while True:
        if 0 <= x1 < nrow and 0 <= y1 < ncol:
            antinodes.add((x1, y1))
        if 0 <= x2 < nrow and 0 <= y2 < ncol:
            antinodes.add((x2, y2))

        x1 += dx
        y1 += dy
        x2 -= dx
        y2 -= dy
        if not (0 <= x1 < nrow and 0 <= y1 < ncol) and not (
            0 <= x2 < nrow and 0 <= y2 < ncol
        ):
            break
    return antinodes


def part1(ls: str) -> int:
    nrow, ncol, graph = parse_data(ls)
    total = set()
    for _, antennas in graph.items():
        total.update(compute(antennas, nrow, ncol))
    return len(total)


def part2(ls: str) -> int:
    nrow, ncol, graph = parse_data(ls)
    total = set()
    for antennas in graph.values():
        total.update(compute(antennas, nrow, ncol, 2))
    return len(total)


response = part2
