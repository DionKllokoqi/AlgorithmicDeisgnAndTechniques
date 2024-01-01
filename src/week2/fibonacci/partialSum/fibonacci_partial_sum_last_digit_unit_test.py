"""Unit tests for getting the last digit of the sum of a partial set of Fibonacci numbers.
"""

import unittest

from parameterized import parameterized

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


if __name__ == "__main__":
    unittest.main()
