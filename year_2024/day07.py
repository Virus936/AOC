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
    lines = [line.split(":") for line in brut_data.splitlines()]
    return lines


def can_do(line, part):
    key, values = line

    key = int(key)
    values = list(map(int, values.split()))

    for combi in product(range(part), repeat=len(values) - 1):
        result = values[0]
        for i, op in enumerate(combi):
            if op == 0:
                result += values[1 + i]
            if op == 1:
                result *= values[i + 1]
            if op == 2:
                result = int(str(result) + str(values[i + 1]))
        if result == key:
            return result
    return 0


def part1(ls: str) -> int:
    lines = parse_data(ls)
    return sum(can_do(line, 2) for line in lines)


def part2(ls: str) -> int:
    lines = parse_data(ls)
    return sum(can_do(line, 3) for line in lines)


response = part1
