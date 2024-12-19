from collections import Counter, defaultdict
from typing import Iterator, List, Tuple
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
    keys, words = brut_data.strip().split("\n\n")
    return tuple(keys.split(', ')), words.splitlines()


from functools import lru_cache


@lru_cache
def is_valid(keys:Tuple[str], word:str):
    if word in keys:
        return True
    for key in keys:
        if not word.startswith(key):continue
        inside = is_valid(keys, word[len(key):])
        if inside:
            return True
    return False


@lru_cache
def count_valid(keys:Tuple[str], word:str):
    if word in keys:
        return 1+count_valid(tuple([k for k in keys if k!=word]), word)
    resp = 0
    for key in keys:
        if not word.startswith(key):continue
        count = count_valid(keys, word[len(key):])
        resp+=count
    return resp


def part1(ls: str) -> int:
    keys, words = parse_data(ls)
    return sum(is_valid(keys, word) for word in words)


def part2(ls: str) -> int:
    keys, words = parse_data(ls)
    return sum(count_valid(keys, word) for word in words)
    


response = part1