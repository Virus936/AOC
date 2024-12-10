from year_2024.day10 import part1, part2
import os
import pytest

DAY = 10
PATH_EXEMPLE = (
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    + f"/inputs/day{DAY}.txt"
)


@pytest.fixture
def data_from_aoc():
    try:
        with open(PATH_EXEMPLE, "r") as f:
            return f.read()
    except FileNotFoundError:
        return None


@pytest.fixture
def data1():
    return """
0123
1234
8765
9876
"""

@pytest.fixture
def data2():
    return """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

def test_resolve_exemple(data1, data2):
    assert part1(data1) == 1
    assert part1(data2) == 36


def test_resolve(data_from_aoc):
    if data_from_aoc is None:
        pytest.skip()
    else:
        assert part1(data_from_aoc) == 538


def test_resolve2_exemple(data1,data2):
    # pytest.skip()
    assert part2(data1) == 16
    assert part2(data2) == 81


def test_resolve2(data_from_aoc):
    # pytest.skip()
    if data_from_aoc is None:
        pytest.skip()
    else:
        assert part2(data_from_aoc) == 1110
