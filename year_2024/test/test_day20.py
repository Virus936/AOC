
from year_2024.day20 import part1, part2
import os
import pytest

DAY = 20
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

###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############

"""

def test_resolve_exemple(data1):
    assert part1(data1) ==0


def test_resolve(data_from_aoc):
    if data_from_aoc is None:
        pytest.skip()
    else:
        assert part1(data_from_aoc) == 260


def test_resolve2_exemple(data1):
    assert part2(data1) == 16

def test_resolve2(data_from_aoc):
    if data_from_aoc is None:
        pytest.skip()
    else:
        assert part2(data_from_aoc) == 639963796864990
