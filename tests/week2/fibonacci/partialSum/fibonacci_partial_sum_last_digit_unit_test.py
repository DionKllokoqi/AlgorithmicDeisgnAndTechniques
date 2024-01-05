"""Unit tests for getting the last digit of the sum of a partial set of Fibonacci numbers.
"""

import unittest

from parameterized import parameterized

from src.week2.fibonacci.partialSum.fibonacci_last_digit_of_partial_sum_improved import (
    get_last_digit_of_partial_fibonacci_sum_improved,
)
from src.week2.fibonacci.partialSum.fibonacci_partial_sum_naive import (
    get_last_digit_of_partial_fibonacci_sum_naive,
)


class TestGetLastDigitOfPartialSumOfFibonacciNumbersShould(unittest.TestCase):
    """Test cases for getting the last digit of the sum of a partial set of Fibonacci numbers.

    Args:
        unittest (): Inherits methods from the TestCase class.
    """

    @parameterized.expand([(3, 7, 1), (10, 10, 5), (10, 200, 2)])
    def test_get_last_digit_of_partial_fibonacci_sum_naive_textbook(
        self, m, n, expected
    ):
        """Test get_last_digit_of_partial_fibonacci_sum_naive() with textbook example."""

        self.assertEqual(get_last_digit_of_partial_fibonacci_sum_naive(m, n), expected)

    @parameterized.expand([(3, 7, 1), (10, 10, 5), (10, 200, 2)])
    def test_get_last_digit_of_partial_fibonacci_sum_improved_textbook(
        self, m, n, expected
    ):
        """Test get_last_digit_of_partial_fibonacci_sum_improved() with textbook example."""

        self.assertEqual(
            get_last_digit_of_partial_fibonacci_sum_improved(m, n), expected
        )

    @parameterized.expand([(0, 0, 0), (0, 10**18, 5), (10**18, 10**18, 5)])
    def test_get_last_digit_of_partial_fibonacci_sum_improved_edge_cases(
        self, m, n, expected
    ):
        """Test get_last_digit_of_partial_fibonacci_sum_improved() with edge cases."""

        self.assertEqual(
            get_last_digit_of_partial_fibonacci_sum_improved(m, n), expected
        )


if __name__ == "__main__":
    unittest.main()
