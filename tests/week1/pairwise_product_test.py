import unittest
from src.week1.pairwise_product import get_maximum_pairwise_product
from src.utils.test.metrics import run_method_under_test


class TestGetMaximumPairwiseProduct(unittest.TestCase):
    def test_when_input_is_three_numbers_should_return_product_of_two_largest(self):
        # Arrange
        numbers = [1, 2, 3]

        # Act
        result = run_method_under_test(get_maximum_pairwise_product, numbers)

        # Assert
        self.assertEqual(result, 6)

    def test_when_input_is_ten_numbers_should_return_product_of_two_largest(self):
        # Arrange
        numbers = [7, 5, 14, 2, 8, 8, 10, 1, 2, 3]

        # Act
        result = run_method_under_test(get_maximum_pairwise_product, numbers)

        # Assert
        self.assertEqual(result, 140)

    def test_when_input_is_all_zeros_should_return_zero(self):
        # Arrange
        numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # Act
        result = run_method_under_test(get_maximum_pairwise_product, numbers)

        # Assert
        self.assertEqual(result, 0)

    def test_when_input_is_all_ones_should_return_one(self):
        # Arrange
        numbers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

        # Act
        result = run_method_under_test(get_maximum_pairwise_product, numbers)

        # Assert
        self.assertEqual(result, 1)

    def test_when_input_has_two_largest_number_should_return_largest_product(self):
        # Arrange
        numbers = [2 * 10**5, 2 * 10**5]

        # Act
        result = run_method_under_test(get_maximum_pairwise_product, numbers)

        # Assert
        self.assertEqual(result, 40000000000)

    def test_when_input_has_two_smallest_number_should_return_largest_product(self):
        # Arrange
        numbers = [0, 0]

        # Act
        result = run_method_under_test(get_maximum_pairwise_product, numbers)

        # Assert
        self.assertEqual(result, 0)

    def test_when_input_is_largest_possible_input_length_should_return_result(self):
        # Arrange
        numbers = [1] * (2 * 10**5)

        # Act
        result = run_method_under_test(get_maximum_pairwise_product, numbers)

        # Assert
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
