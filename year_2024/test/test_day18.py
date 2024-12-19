
from year_2024.day18 import part1, part2
import os
import pytest

DAY = 18
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


5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0

"""

def test_resolve_exemple(data1):
    assert part1(data1, True) ==22


def test_resolve(data_from_aoc):
    if data_from_aoc is None:
        pytest.skip()
    else:
        assert part1(data_from_aoc, False) == 262


def test_resolve2_exemple(data1):
    assert part2(data1, True) == "6,1"

def test_resolve2(data_from_aoc):
    if data_from_aoc is None:
        pytest.skip()
    else:
        assert part2(data_from_aoc, False) == 639963796864990
