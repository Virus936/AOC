from year_2024.day05 import part1, part2
import os
import pytest

DAY = 5
PATH_EXEMPLE = (
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    + f"/inputs/day{DAY}.txt"
)


@pytest.fixture
def data():
    return """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


def test_resolve_exemple(data):
    assert part1(data) == 143


def test_resolve(data):
    default_data = "no data"
    try:
        with open(PATH_EXEMPLE, "r") as f:
            data = f.read()
    except FileNotFoundError:
        data = default_data
    assert part1(data) == 5374


def test_resolve2_exemple(data):
    assert part2(data) == 123


def test_resolve2(data):
    default_data = "no data"
    try:
        with open(PATH_EXEMPLE, "r") as f:
            data = f.read()
    except FileNotFoundError:
        data = default_data
    assert part2(data) == 4260
