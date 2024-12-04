from year_2024.day01 import part1, part2
import pytest


@pytest.fixture
def data():
    return """3   4
4   3
2   5
1   3
3   9
3   3
"""


def test_resolve(data):
    assert part1(data) == 11


def test_resolve2(data):
    assert part2(data) == 31
