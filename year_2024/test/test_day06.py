from year_2024.day06 import part1, part2
import os
import pytest

DAY = 6
PATH_EXEMPLE = (
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    + f"/inputs/day{DAY}.txt"
)


@pytest.fixture
def data():
    return """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


def test_resolve_exemple(data):
    assert part1(data) == 41


def test_resolve(data):
    try:
        with open(PATH_EXEMPLE, "r") as f:
            data = f.read()
        assert part1(data) == 4711
    except FileNotFoundError:
        assert True


def test_resolve2_exemple(data):
    assert part2(data) == 6


def test_resolve2(data):
    try:
        with open(PATH_EXEMPLE, "r") as f:
            data = f.read()
        assert part2(data) == 0

    except FileNotFoundError:
        assert True
