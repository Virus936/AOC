from collections import Counter
from collections import defaultdict
from typing import Iterator
import re
from functools import cmp_to_key

# response = sorted(c, key=cmp_to_key(lambda a, b: 1 if b in graph[a] else -1))


def transpose(ls: Iterator):
    return list(map(list, zip(*ls)))


def intify(ls: list[str]) -> list[int]:
    return list(map(int, ls))


def parse_data(brut_data: str) -> list[int]:
    lines = [list(line) for line in brut_data.splitlines()]
    start = 0,0
    for i,r in enumerate(lines):
        for j, c in enumerate(r):
            if c in '<>^v':
                start = [i,j]
    return start, lines

def part1(ls: str) -> int:
    start, lines = parse_data(ls)
    position = [start[0],start[1]]
    response = 0
    memory = [["v" for l in line] for line in lines]
    clock="^<v>"
    started = False
    dir = lines[position[0]][position[1]]
    init = dir
    print(start, dir)
    while ((position[0] != start[0] or position[1] != start[1]) or dir!= init )  or not started:
        started = True
        if memory[position[0]][position[1]] == "v":
            memory[position[0]][position[1]] = "#"
            response+=1
        if dir == '^':
            if position[0]-1 == -1 : break
            if lines[position[0]-1][position[1]] == '#':
                dir = '>'
                position[1] = position[1]+1
            else:   
                position[0] = position[0]-1
        elif dir == '>':
            if position[1]+1 == len(lines[0]):break
            if lines[position[0]][position[1]+1] == '#':
                dir = 'v'
                position[0] = position[0]+1
            else:   
                position[1] = position[1]+1
        elif dir == 'v':
            if position[0]+1 == len(lines):break
            if lines[position[0]+1][position[1]] == '#':
                dir = '<'
                position[1] = position[1]-1
            else:   
                position[0] = position[0]+1
        elif dir == '<':
            if position[1]-1==-1:break
            if lines[position[0]][position[1]-1] == '#':
                dir = '^'
                position[0] = position[0]-1
            else:   
                position[1] = position[1]-1
     
        print(position , start, position != start, dir, response)


        
    return response


def part2(ls: str) -> int:
    lines = parse_data(ls)
    response = 0
    return response


response = part1