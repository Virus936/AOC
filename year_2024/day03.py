import re


def part1(input: str) -> int:
    matches = re.findall(r"mul\([0-9]{1,5},[0-9]{1,5}\)", input)

    ans = 0
    for match in matches:
        l, r = map(int, match[4:-1].split(","))
        ans += l * r

    return ans


def part2(input: str) -> int:
    matches = re.findall(r"mul\([0-9]{1,5},[0-9]{1,5}\)|don't\(\)|do\(\)", input)
    ans = 0
    to_do = True
    for match in matches:
        if match == "don't()":
            to_do = False
            continue
        if match == "do()":
            to_do = True
            continue
        if not to_do:
            continue
        l, r = map(int, match[4:-1].split(","))
        ans += l * r

    return ans


response = part2
