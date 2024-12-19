from collections import Counter, defaultdict
from typing import Iterator, List, Tuple
from itertools import product, combinations
from copy import deepcopy
from functools import cmp_to_key, lru_cache
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
    lines=brut_data.strip().splitlines()
    return [tuple(map(int,line.split(","))) for line in lines]



def size(exemple):
    if exemple:
        return 6+1
    return 70+1

from collections import deque

def bfs(obstacles, SIZE):
    visited = set()
    visited.add((0,0))
    trace = [[0]*SIZE for _ in range(SIZE)]
    trace[0][0]=0

    q= deque()
    q.append((0,0))


    while q:
        x,y= q.popleft()
        for dx,dy in DIR:
            if 0<=x+dx<SIZE and 0<=y+dy<SIZE and (x+dx, y+dy) not in obstacles:
                if (x+dx, y+dy) not in visited:
                    visited.add((x+dx, y+dy))
                    q.append((x+dx, y+dy))
                    trace[x+dx][y+dy]=trace[x][y]+1
    
    return trace[SIZE-1][SIZE-1]

def part1(ls: str, exemple) -> int:
    SIZE=size(exemple)
    obstacles= parse_data(ls)

    byte_fallen = 12 if SIZE == 7 else 1024
    
    return bfs(obstacles[:byte_fallen], SIZE)


def part2(ls: str, exemple) -> int:
    SIZE=size(exemple)
    obstacles= parse_data(ls)
    left,right = 0, len(obstacles)-1
    while left<right:
        middle=(left+right)//2

        count = bfs(obstacles[:middle+1], SIZE)
        print(left, middle, right, count)
        if count == 0:
            right=middle
        else:
            left=middle+1
    x,y=obstacles[left]
    return f"{x},{y}"
    

    


response = part1