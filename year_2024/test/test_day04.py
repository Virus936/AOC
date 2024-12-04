from year_2024.day04 import part1, part2
import os
import pytest

DAY = 4
PATH_EXEMPLE = (
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    + f"/inputs/day{DAY}.txt"
)


@pytest.fixture
def data():
    return """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


def test_resolve_exemple(data):
    assert part1(data) == 18


def test_resolve(data):
    with open(PATH_EXEMPLE, "r") as f:
        data = f.read()
    assert part1(data) == 2297


def test_resolve2_exemple(data):
    assert part2(data) == 9


def test_resolve2(data):
    with open(PATH_EXEMPLE, "r") as f:
        data = f.read()
    assert part2(data) == 1745
