"""Unit tests for get last digit of a sum of fibonacci numbers
"""

import unittest

from parameterized import parameterized

from src.week2.fibonacci.sumLastDigits.fibonacci_sum_last_digit_improved_again import (
    get_last_digit_of_sum_of_fibonacci_numbers_pisano,
)
from src.week2.fibonacci.sumLastDigits.fibonacci_sum_last_digit_naive import (
    get_last_digit_of_sum_of_fibonacci_numbers_naive,
)


class TestSumFibonacciLastDigit(unittest.TestCase):
    """Unit tests for get last digit of a sum of fibonacci numbers

    Args:
        unittest (): Inherits from unittest module
    """

    @parameterized.expand([(3, 4), (100, 5)])
    def test_sum_fibonacci_last_digit_naive_textbook(self, n, expected):
        """Simple test for naive implementation of sum_fibonacci_last_digit"""

        return self.assertEqual(
            get_last_digit_of_sum_of_fibonacci_numbers_naive(n), expected
        )

    @parameterized.expand([(3, 4), (100, 5)])
    def test_get_last_digit_of_sum_of_fibonacci_numbers_pisano_textbook(
        self, n, expected
    ):
        """Simple test for naive implementation of sum_fibonacci_last_digit"""

        return self.assertEqual(
            get_last_digit_of_sum_of_fibonacci_numbers_pisano(n), expected
        )

    @parameterized.expand([(0, 0), (1, 1), (10**14, 5)])
    def test_get_last_digit_of_sum_of_fibonacci_numbers_pisano_boundar_cases(
        self, n, expected
    ):
        """Boundary cases test for improved pisano implemenation of sum of fibonacci
        numbers last digit
        """

        return self.assertEqual(
            get_last_digit_of_sum_of_fibonacci_numbers_pisano(n), expected
        )


if __name__ == "__main__":
    unittest.main()
