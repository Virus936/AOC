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
    maze = brut_data.strip().splitlines()
    walls = []
    for r, row in enumerate(maze):
        for c, col in enumerate(row):
            if col == "S":
                start = (r,c)
            if col == "#":
                walls.append((r,c))

    return maze, start, walls

from collections import deque

def bfs(maze, s):
    q = deque()
    q.append(s)
    heigh = len(maze)
    width = len(maze[0])
    visited = [[0]*width for _ in range(heigh)]
    x,y = s
    visited[x][y]=1
    while q:
        x,y = q.popleft()
        for dx,dy in DIR:
            if maze[x+dx][y+dy] == '#':
                continue
            if visited[x+dx][y+dy] != 0:
                continue
            visited[x+dx][y+dy] = visited[x][y]+1
            q.append((x+dx,y+dy))
    return visited


def shortcut6(trace, TEMP):
    response = defaultdict(int)
    for r,row in enumerate(trace):
        for c,col in enumerate(row):
            if col==0:
                continue

            for dr in range(-TEMP,0):
                    for dc in range(-TEMP-dr,TEMP+dr+1):
                        if 0<=r+dr<len(trace) and 0<=c+dc<len(trace[0]):
                            if trace[r+dr][c+dc] == 0:
                                continue
                            if trace[r+dr][c+dc] - trace[r][c] - abs(dr) - abs(dc) >0:
                                response[trace[r+dr][c+dc] - trace[r][c] - abs(dc) - abs(dr)]+=1
            for dr in range(0,TEMP+1):
                    for dc in range(-TEMP+dr,TEMP-dr+1):
                        if 0<=r+dr<len(trace) and 0<=c+dc<len(trace[0]):
                            if trace[r+dr][c+dc] == 0:
                                continue
                            if trace[r+dr][c+dc] - trace[r][c] - abs(dr) - abs(dc) >0:
                                response[trace[r+dr][c+dc] - trace[r][c] - abs(dc) - abs(dr)]+=1
    return response


def part1(ls: str) -> int:
    maze, start, _ = parse_data(ls)
    trace = bfs(maze,start)
    counter = shortcut6(trace, 2)
    return sum(value for key,value in counter.items() if key>=100)



def part2(ls: str) -> int:
    maze, start, _ = parse_data(ls)
    trace = bfs(maze,start)
    counter = shortcut6(trace, 20)
    return sum(value for key,value in counter.items() if key>=100)
    

response = part2