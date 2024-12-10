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
    lines =[ ['.']+list(l)+['.'] for l in brut_data.strip().splitlines()]
    lines = [['.']*len(lines[0])] + lines + [['.']*len(lines[0])] 

    ends, starts = [], []
    for r,line in enumerate(lines):
        for c, p in enumerate(line):
            if p=='.':continue
            if int(p) == 9:
                ends.append((r,c))
            if int(p) == 0:
                starts.append((r,c))
    return ends,starts,lines


def dfs(start,end, map):
    x,y = start
    response=0
    for dx, dy in DIR:
        if map[x+dx][y+dy] == '.':
            continue
        if int(map[x+dx][y+dy]) != int(map[x][y])+1:
            continue
        if end == (x+dx,y+dy):
            return 1
        response+=dfs((x+dx,y+dy), end, map)
    return response

def part1(ls: str) -> int:
    ends, starts, map = parse_data(ls)
    return sum(
        bool(dfs(start,end,map)) 
        for start,end in product(starts,ends)
        )


def part2(ls: str) -> int:
    ends, starts, map = parse_data(ls)
    return sum(
        dfs(start,end,map) 
        for start,end in product(starts,ends)
        )


response = part2
