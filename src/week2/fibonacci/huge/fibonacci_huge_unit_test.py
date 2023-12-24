"""Unit tests for pisano series calculation

Returns:
    int: Remained of fibonacci number n modulo m
"""

import unittest

from parameterized import parameterized

from src.week2.fibonacci.huge.fibonacci_huge_improved import (
    get_fibonacci_huge_improved as get_fibonacci_huge_improved_again,
)
from src.week2.fibonacci.huge.fibonacci_huge_improved_again import (
    get_fibonacci_huge_improved,
)
from src.week2.fibonacci.huge.fibonacci_huge_naive import get_fibonacci_huge_naive


class TestFibonacciHuge(unittest.TestCase):
    """Unit tests for pisano series calculation

    Args:
        unittest (): Inherits from unittest module
    """

    def test_fibonacci_huge_naive(self):
        """Simple test for naive implementation of fibonacci_huge"""

        return self.assertEqual(get_fibonacci_huge_naive(7, 3), 1)

    @parameterized.expand(
        [(7, 3, 1), (2015, 3, 1), (239, 1000, 161), (2816213588, 239, 151)]
    )
    def test_fibonacci_huge_improved_again_textbook(self, n, m, expected):
        """Test for improved implementation of fibonacci_huge"""

        return self.assertEqual(get_fibonacci_huge_improved_again(n, m), expected)

    @parameterized.expand([(0, 1, 0), (1, 1, 1)])
    def test_fibonacci_huge_improved_again_boundary_cases(self, n, m, expected):
        """Test for improved implementation of fibonacci_huge"""

        return self.assertEqual(get_fibonacci_huge_improved_again(n, m), expected)

    @parameterized.expand(
        [(7, 3, 1), (2015, 3, 1), (239, 1000, 161), (2816213588, 239, 151)]
    )
    def test_fibonacci_huge_improved_textbook(self, n, m, expected):
        """Test for improved implementation of fibonacci_huge"""

        return self.assertEqual(get_fibonacci_huge_improved(n, m), expected)

    @parameterized.expand([(0, 1, 0), (1, 1, 1)])
    def test_fibonacci_huge_improved_boundary_cases(self, n, m, expected):
        """Test for improved implementation of fibonacci_huge"""

        return self.assertEqual(get_fibonacci_huge_improved(n, m), expected)


if __name__ == "__main__":
    unittest.main()
