from typing import Iterator
import re


def transpose(ls: Iterator):
    return list(map(list, zip(*ls)))


def parse_data(brut_data: str) -> list[int]:
    lines = brut_data.splitlines()
    return [line for line in lines]


def part1(ls: str) -> int:
    table = parse_data(ls)
    n_rows = len(table)
    n_cols = len(table[0])
    counter = 0
    # matche_h = re.findall(r"XMAS",ls)
    # matche_r = re.findall(r"SAMX",ls)
    # counter+=len(matche_h) + len(matche_r)
    # table2 = transpose(list(table))
    # table2 = ''.join([''.join(line) for line in table2])
    # matche_h = re.findall(r"XMAS",table2)
    # matche_r = re.findall(r"SAMX",table2)
    # counter+=len(matche_h) + len(matche_r)

    for i in range(len(table)):
        for j in range(len(table[0])):
            if j + 3 < n_cols and table[i][j] + table[i][j + 1] + table[i][
                j + 2
            ] + table[i][j + 3] in ["SAMX", "XMAS"]:
                counter += 1
            if i + 3 < n_rows and table[i][j] + table[i + 1][j] + table[i + 2][
                j
            ] + table[i + 3][j] in ["SAMX", "XMAS"]:
                counter += 1
            if i < len(table) - 3 and j < len(table[0]) - 3:
                word = (
                    table[i][j]
                    + table[i + 1][j + 1]
                    + table[i + 2][j + 2]
                    + table[i + 3][j + 3]
                )
                if word in ["XMAS", "SAMX"]:
                    counter += 1
            if i > 2 and j < len(table[0]) - 3:
                word = (
                    table[i][j]
                    + table[i - 1][j + 1]
                    + table[i - 2][j + 2]
                    + table[i - 3][j + 3]
                )
                if word in ["XMAS", "SAMX"]:
                    counter += 1

    return counter


def part2(ls: str) -> int:
    table = parse_data(ls)
    n_rows = len(table)
    n_cols = len(table[0])
    counter = 0

    for i in range(n_rows - 2):
        for j in range(n_cols - 2):
            if (
                table[i][j] + table[i + 1][j + 1] + table[i + 2][j + 2] == "MAS"
                and table[i + 2][j] + table[i + 1][j + 1] + table[i][j + 2] == "MAS"
            ):
                counter += 1
            if (
                table[i][j] + table[i + 1][j + 1] + table[i + 2][j + 2] == "SAM"
                and table[i + 2][j] + table[i + 1][j + 1] + table[i][j + 2] == "SAM"
            ):
                counter += 1
            if (
                table[i][j] + table[i + 1][j + 1] + table[i + 2][j + 2] == "MAS"
                and table[i + 2][j] + table[i + 1][j + 1] + table[i][j + 2] == "SAM"
            ):
                counter += 1
            if (
                table[i][j] + table[i + 1][j + 1] + table[i + 2][j + 2] == "SAM"
                and table[i + 2][j] + table[i + 1][j + 1] + table[i][j + 2] == "MAS"
            ):
                counter += 1
    return counter


response = part2
