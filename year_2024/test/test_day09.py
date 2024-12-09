from year_2024.day09 import part1, part2
import os
import pytest

DAY = 9
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
2333133121414131402
"""

def test_resolve_exemple(data1):
    assert part1(data1) == 1928


def test_resolve(data_from_aoc):
    # pytest.skip()
    if data_from_aoc is None:
        pytest.skip()
    else:
        assert part1(data_from_aoc) == 6225730762521


def test_resolve2_exemple(data1):
    # pytest.skip()
    assert part2(data1) == 2858


def test_resolve2(data_from_aoc):
    # pytest.skip()
    if data_from_aoc is None:
        pytest.skip()
    else:
        assert part2(data_from_aoc) == 6250605700557
