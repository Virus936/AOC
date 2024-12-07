from year_2024.day07 import part1, part2
import os
import pytest

DAY = 7
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
    return """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""




def test_resolve_exemple(data1):
    assert part1(data1) == 3749


def test_resolve(data_from_aoc):
    # pytest.skip()
    if data_from_aoc is None:
        pytest.skip()
    else:
        assert part1(data_from_aoc) == 14711933466277


def test_resolve2_exemple(data1):
    # pytest.skip()
    assert part2(data1) == 11387


def test_resolve2(data_from_aoc):
    # pytest.skip()
    if data_from_aoc is None:
        pytest.skip()
    else:
        assert part2(data_from_aoc) == 286580387663654
