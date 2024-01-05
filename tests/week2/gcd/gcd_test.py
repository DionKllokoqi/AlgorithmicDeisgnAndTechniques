import unittest
from parameterized import parameterized
from src.week2.gcd.gcd_euclid import gcd_euclid


class TestGcdEuclid(unittest.TestCase):
    @parameterized.expand(
        [
            (18, 35, 1),
            (28851538, 1183019, 17657),
        ]
    )
    def test_when_input_is_from_textbook_should_return_correct_answer(
        self, a, b, expected
    ):
        # Act
        result = gcd_euclid(a, b)

        # Assert
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
