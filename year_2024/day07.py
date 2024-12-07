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


def can_do(key,values,part):
    n = len(values)-1
    for combi in product(range(part),repeat=n):
        result = values[0]
        for i, op in enumerate(combi):
            if op == 0:
                result+=values[1+i]
            if op == 1:
                result*=values[i+1]
            if op == 2:
                temp=str(result)
                temp+=str(values[i+1])
                result=int(temp)
        if result == key:
            return True
    return False


def part1(ls: str) -> int:
    lines = parse_data(ls)
    response = 0
    for key, values in lines:
        key = int(key)
        values = list(map(int, values.split()))
        if can_do(key, values, 2):
            response+=key
    return response


def part2(ls: str) -> int:
    lines = parse_data(ls)
    response = 0
    for key, values in lines:
        key = int(key)
        values = list(map(int, values.split()))
        if can_do(key,values,3):
            response+=key
    return response


response = part1
