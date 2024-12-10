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


def parse_data(brut_data: str) -> list[int]:
    lines = brut_data.splitlines()
    return brut_data


#### MAZE ####
def trace(ls):
    return [["." for l in li] for li in ls.splitlines()]


def pprint(trace):
    print("")
    for tr in trace:
        print("".join(tr))
    print("")


##############


def fill_disk(disk, ls):
    for i, l in enumerate(ls):
        disk.extend([None if i % 2 else i // 2] * int(l))


def defragment(disk):
    start, end = 0, len(disk) - 1
    while start <= end:
        if disk[start] is not None:
            start += 1
            continue
        if disk[end] is None:
            end -= 1
            continue
        disk[start], disk[end] = disk[end], disk[start]


def compute_checksum(disk):
    return sum([i * (x or 0) for i, x in enumerate(disk)])


def check_none_and_fill(disk):
    current, l = disk[0], 0
    empty_blocks = []
    blocks = []
    for i, d in enumerate(disk):
        if d == current:
            continue
        if current is None:
            empty_blocks.append((l, i))
        else:
            blocks.append((l, i))
        l, current = i, d
    else:
        if current is None:
            empty_blocks.append((l, i+1))
        else:
            blocks.append((l, i+1))
    return empty_blocks, blocks


def defragment_in_block(disk):
    emptys, filled = check_none_and_fill(disk)
    for fill in filled[::-1]:
        find = False
        for j in range(len(emptys)):
            size_fill = fill[1] - fill[0]
            xe1, xe2 = emptys[j]
            if xe1 > fill[0]:
                continue
            if size_fill > xe2 - xe1:
                continue
            for i in range(xe1, xe1 + size_fill):
                disk[i] = disk[fill[0]]
            for i in range(fill[0], fill[1]):
                disk[i] = None
            find = True
            break
        if find:
            emptys[j] = (xe1 + size_fill, xe2)


def part1(ls: str) -> int:
    ls = ls.strip()
    disk = []
    fill_disk(disk, ls)
    defragment(disk)
    return compute_checksum(disk)


def part2(ls: str) -> int:
    ls = ls.strip()
    disk = []
    fill_disk(disk, ls)
    defragment_in_block(disk)
    return compute_checksum(disk)


response = part2
