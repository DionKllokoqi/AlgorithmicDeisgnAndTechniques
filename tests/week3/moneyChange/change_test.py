"""Unit tests for money change problem.
"""

import pytest

from src.week3.moneyChange.change_improved import get_change


@pytest.mark.parametrize("money, expected", [(2, 2), (28, 6)])
def test_get_change_from_textbook(money, expected):
    """Test get_change() with textbook examples."""
    assert get_change(money) == expected
