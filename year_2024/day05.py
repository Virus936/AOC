from collections import Counter
from collections import defaultdict
from typing import Iterator
import re
from functools import cmp_to_key


def transpose(ls: Iterator):
    return list(map(list, zip(*ls)))


def intify(ls: list[str]) -> list[int]:
    return list(map(int, ls))


def parse_data(brut_data: str):
    lines1, lines2 = brut_data.split("\n\n")
    lines1 = lines1.splitlines()
    lines2 = [line.split(",") for line in lines2.splitlines()]
    graph = defaultdict(list)
    for line in lines1:
        start, end = line.split("|")
        graph[start].append(end)
    return graph, lines2


def find_correct_or_not(graph, lines):
    correct = []
    not_correct = []
    for line in lines:
        start = line[0]
        good = True
        for el in line[1:]:
            if el not in graph[start]:
                good = False
            start = el
        if good:
            correct.append(line)
        else:
            not_correct.append(line)
    return correct, not_correct


def order(c, graph):
    return sorted(c, key=cmp_to_key(lambda a, b: 1 if b in graph[a] else -1))


def part1(ls: str) -> int:
    graph, lines = parse_data(ls)
    correct, _ = find_correct_or_not(graph, lines)
    response = 0
    for c in correct:
        response += int(c[len(c) // 2])
    return response


def part2(ls: str) -> int:
    graph, lines = parse_data(ls)
    _, not_correct = find_correct_or_not(graph, lines)
    response = 0
    for c in not_correct:
        response += int(order(c, graph)[len(c) // 2])
    return response


response = part2
