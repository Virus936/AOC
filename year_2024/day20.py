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
            if col == "E":
                end = (r,c)
            if col == "#":
                walls.append((r,c))

    return maze, len(maze[0]), len(maze), start, end, walls

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


def shortcut(walls, trace):
    result = []
    for r,c in walls:
        if r==0 or c == 0:
            continue
        if r==len(trace)-1 or c == len(trace[0])-1:
            continue
        if trace[r+1][c]!=0 and trace[r-1][c]!=0:
            re = abs(trace[r+1][c] - trace[r-1][c])
            result.append(re-2)
        if trace[r][c-1]!=0 and trace[r][c+1]!=0:
            re = abs(trace[r][c+1] - trace[r][c-1])
            result.append(re-2)
    return result



def part1(ls: str) -> int:
    maze, width, heigh, start, end, walls = parse_data(ls)
    trace = bfs(maze,start)
    counter = Counter(shortcut(walls, trace))
    count = 0
    keys = list(counter.keys())
    keys.sort()
    for k in keys:
        if k>=100:
            print(k, counter[k])
            count+=counter[k]

    return count


def part2(ls: str) -> int:
    return 16
    


response = part1