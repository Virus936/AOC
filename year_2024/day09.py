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


def trace(ls):
    return [["." for l in li] for li in ls.splitlines()]


def pprint(trace):
    print("")
    for tr in trace:
        print("".join(tr))
    print("")


def fill_disk(disk,ls):
    i=0
    dot=False
    for l in ls:
        disk.extend([None if dot else i]*int(l))
        dot = not dot
        if dot:
            i+=1


def part1(ls: str) -> int:
    ls = ls.strip()
    disk = []
    fill_disk(disk, ls)
    move_disk(disk)
    return compute_checksum(disk)

def move_disk(disk):
    start,end = 0,len(disk)-1
    while start<=end:
        if disk[start] is not None:
            start+=1
            continue
        if disk[end] is None:
            end-=1
            continue
        disk[start],disk[end] = disk[end],disk[start]



def compute_checksum(disk):
    ans=0
    for i in range(len(disk)):
        if disk[i] is None:
            continue
        ans+=i*disk[i]

    return ans


def part2(ls: str) -> int:
    ls = ls.strip()
    disk = []
    fill_disk(disk, ls)


    move_disk_2(disk)
    return compute_checksum(disk)


def check_none_and_fill(disk):
    current=disk[0]
    l=0
    r=1
    empty_blocks=[]
    blocks=[]
    for i,d in enumerate(disk+['impoaaible']):
        if d == current:
            r=i+1
            continue
        if current is None:
            empty_blocks.append((l,r))
        else:
            blocks.append((l,r))
        l=i
        r=i+1
        current=d
    return empty_blocks,blocks


def move_disk_2(disk):
    emptys, filled = check_none_and_fill(disk)
    for fill in filled[::-1]:
        emptys, _ = check_none_and_fill(disk)
        for empty in emptys:
            size_fill = fill[1]-fill[0]
            if empty[0]>fill[0]:continue
            if size_fill>empty[1]-empty[0]:continue
            for i in range(empty[0], empty[0]+size_fill):
                disk[i]=disk[fill[0]]
            for i in range(fill[0],fill[1]):
                disk[i]=None


response = part2
