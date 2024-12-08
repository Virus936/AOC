from year_2024.day08 import part1, part2
import os
import pytest

DAY = 8
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
    return """............
........0...
.....0......
.......0....
....0.......
......A.....
..........i.
.....5......
........A...
.........A..
............
............"""


@pytest.fixture
def data2():
    return """T.........
...T......
.T........
..........
..........
..........
..........
..........
..........
.........."""


@pytest.fixture
def data3():
    return """.....
.T...
.....
....."""


def test_resolve_exemple(data1):
    assert part1(data1) == 14


def test_resolve(data_from_aoc):
    # pytest.skip()
    if data_from_aoc is None:
        pytest.skip()
    else:
        assert part1(data_from_aoc) == 357


def test_resolve2_exemple(data1, data2, data3):
    assert part2(data3) == 0
    assert part2(data2) == 9
    assert part2(data1) == 34


def test_resolve2(data_from_aoc):
    # pytest.skip()
    if data_from_aoc is None:
        pytest.skip()
    else:
        assert part2(data_from_aoc) == 1266
