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
    r = [list(map(int, li.split())) for li in brut_data.strip().splitlines()]
    return r[0]


# def turn_stone(stone):
#     response = [stone]
#     if stone == 0:
#         return [1]
#     if len(str(stone))%2==0:
#         return list(map(int,[
#             str(stone)[:len(str(stone))//2],
#             str(stone)[len(str(stone))//2:],
#             ]))
#     return [stone*2024]


memo = {}


def turn_stone(stone, times):
    if (stone, times) in memo:
        return memo[(stone, times)]
    response = []
    if times == 0:
        return 1
    if stone == 0:
        response = [1]
    elif len(str(stone)) % 2 == 0:
        response = list(
            map(
                int,
                [
                    str(stone)[: len(str(stone)) // 2],
                    str(stone)[len(str(stone)) // 2 :],
                ],
            )
        )
    else:
        response = [stone * 2024]

    resp = 0
    for s in response:
        resp += turn_stone(s, times - 1)

    memo[(stone, times)] = resp
    return resp


def blink(stones):
    resp = []
    for stone in stones:
        resp.extend(turn_stone(stone))
    return resp


def part1(ls: str) -> int:
    stones = parse_data(ls)
    resp = 0
    for stone in stones:
        resp += turn_stone(stone, 25)

    return resp


def part2(ls: str) -> int:
    stones = parse_data(ls)
    resp = 0
    for stone in stones:
        resp += turn_stone(stone, 75)

    return resp


response = part2
