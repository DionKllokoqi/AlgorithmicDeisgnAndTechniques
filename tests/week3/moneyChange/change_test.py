"""Unit tests for money change problem.
"""

import pytest

from src.week3.moneyChange.change_improved import get_change


@pytest.mark.parametrize("money, expected", [(2, 2), (28, 6)])
def test_get_change_from_textbook(money, expected):
    """Test get_change() with textbook examples."""
    assert get_change(money) == expected


def test_get_change_with_largest_input():
    """Test get_change() with largest input."""
    assert get_change(1000) == 100


def test_with_smallest_input():
    """Test get_change() with smallest input."""
    assert get_change(1) == 1


@pytest.mark.parametrize("money, expected", [(5, 1), (6, 2), (7, 3), (8, 4), (9, 5)])
def test_get_change_between_five_and_ten(money, expected):
    """Test get_change() with input between 5 and 10."""
    assert get_change(money) == expected


@pytest.mark.parametrize("money, expected", [(2, 2), (3, 3), (4, 4)])
def test_get_change_between_two_and_four(money, expected):
    """Test get_change() with input between 2 and 4."""
    assert get_change(money) == expected
