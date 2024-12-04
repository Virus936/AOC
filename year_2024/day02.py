def intify(ls: list[str]) -> list[int]:
    return list(map(int, ls.split()))


def parse_data(brut_data: str) -> list[int]:
    lines = brut_data.splitlines()
    return [intify(line) for line in lines]


def is_safe_origin(line):
    count = 0
    count2 = 0

    for i in range(1, len(line)):
        if line[i - 1] > line[i] > line[i - 1] - 4:
            count += 1
        if line[i - 1] < line[i] < line[i - 1] + 4:
            count2 += 1
    if count == len(line) - 1:
        return True
    if count2 == len(line) - 1:
        return True
    return False


def is_safe_extend(line):
    if is_safe_origin(line):
        return True
    for i in range(len(line)):
        if is_safe_origin(line[:i] + line[i + 1 :]):
            return True
    return False


def part1(ls: str) -> int:
    lines = parse_data(ls)
    return sum(is_safe_origin(l) for l in lines)


def part2(ls: str) -> int:
    lines = parse_data(ls)
    return sum(is_safe_extend(l) for l in lines)


response = part1
