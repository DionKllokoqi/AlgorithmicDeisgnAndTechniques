"""Stress test for maximum pairwise product problem.
"""

from random import randint

from src.week1.naive_pairwise_product import get_maximum_pairwise_product_naive
from src.week1.pairwise_product import get_maximum_pairwise_product


def max_pairwise_stress_test(N, M):
    """Stress test for maximum pairwise product problem.

    Args:
        N (int): The maximum number of elements in the array.
        M (int): The maximum value of an element in the array.
    """
    while True:
        n = randint(2, N)
        a = [None] * n

        for i in range(n):
            a[i] = randint(0, M)

        print(a)

        result1 = get_maximum_pairwise_product_naive(n, a)
        result2 = get_maximum_pairwise_product(a)

        if result1 == result2:
            print("OK")
        else:
            print("Wrong answer: ", result1, result2)
            return


if __name__ == "__main__":
    elements = int(input())
    max_value = int(input())
    max_pairwise_stress_test(elements, max_value)
