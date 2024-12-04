from collections import Counter
from typing import Iterator


def transpose(ls: Iterator):
    return list(map(list, zip(*ls)))


def intify(ls: list[str]) -> list[int]:
    return list(map(int, ls))


def parse_data(brute_data: str):
    lines = brute_data.splitlines()
    return transpose((intify(d.split()) for d in lines))


def part1(ls: str, parser=parse_data) -> int:
    left, right = parser(ls)

    return sum(abs(l - r) for l, r in zip(sorted(left), sorted(right)))


def part2(ls: str, parser=parse_data) -> int:
    left, right = parser(ls)

    r_count = Counter(right)
    return sum(l * r_count[l] for l in left)


response = part2
