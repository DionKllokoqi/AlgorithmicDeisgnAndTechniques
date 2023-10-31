import unittest
from parameterized import parameterized
from src.utils.test.metrics import run_method_under_test
from src.week2.fibonacci.huge.fibonacci_huge import get_last_fibonacci_digit_huge


class TestLastFibonnaciDigitHuge(unittest.TestCase):
    @parameterized.expand(
        [
            (3, 2),
            (331, 9),
            (327305, 5),
        ]
    )
    def test_when_input_is_from_textbook_should_return_correct_answer(
        self, n, expected
    ):
        # Act
        result = run_method_under_test(get_last_fibonacci_digit_huge, n)

        # Assert
        self.assertEqual(result, expected)

    def test_when_input_is_zero_should_return_zero(self):
        # Arrange
        n = 0

        # Act
        result = run_method_under_test(get_last_fibonacci_digit_huge, n)

        # Assert
        self.assertEqual(result, 0)

    def test_when_input_is_one_should_return_one(self):
        # Arrange
        n = 1

        # Act
        result = run_method_under_test(get_last_fibonacci_digit_huge, n)

        # Assert
        self.assertEqual(result, 1)

    def test_when_input_is_largest_number_should_return_correct_answer(self):
        # Arrange
        n = 10**7

        # Act
        result = run_method_under_test(get_last_fibonacci_digit_huge, n)

        # Assert
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
