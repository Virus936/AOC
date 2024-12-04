from year_2024.day03 import part1, part2
import os
import pytest

DAY = 3
PATH_EXEMPLE = (
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    + f"/inputs/day{DAY}.txt"
)


@pytest.fixture
def data():
    # return "37 40 42 43 44 47 51"
    return (
        """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
    )


def test_resolve_exemple(data):
    assert part1(data) == 161


def test_resolve(data):
    with open(PATH_EXEMPLE, "r") as f:
        data = f.read()
    assert part1(data) == 184576302


def test_resolve2_exemple(data):
    assert part2(data) == 48


def test_resolve2(data):
    with open(PATH_EXEMPLE, "r") as f:
        data = f.read()
    assert part2(data) == 118173507
