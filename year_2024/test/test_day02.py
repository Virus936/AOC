from year_2024.day02 import part1, part2
import os

import pytest

DAY = 2
PATH_EXEMPLE = (
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    + f"/inputs/day{DAY}.txt"
)


@pytest.fixture
def data():
    # return "37 40 42 43 44 47 51"
    return """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


def test_resolve_exemple(data):
    assert part1(data) == 2


def test_resolve(data):
    with open(PATH_EXEMPLE, "r") as f:
        data = f.read()
    assert part1(data) == 490


def test_resolve2_exemple(data):
    assert part2(data) == 4


def test_resolve2(data):
    with open(PATH_EXEMPLE, "r") as f:
        data = f.read()
    assert part2(data) == 536
