# Uses python3

"""Improved implementation of the last digit of the partial sum of Fibonacci numbers algorithm.
"""

import sys

from src.week2.fibonacci.fibonacci_efficient import get_fibonacci


def get_sum_of_last_digits(n):
    """Get the sum of the last digits of the first n Fibonacci numbers."""

    pisano_period = 60

    whole_periods = n // pisano_period
    remainder = n % pisano_period

    fib_sum = 0
    if whole_periods > 0:
        for i in range(pisano_period):
            fib_sum += get_fibonacci(i) % 10

        # Since the pisano period repeats, we can just
        # add up one pisano period for n and multiply
        # that by the whole periods.
        fib_sum *= whole_periods

    # Add up the remainder of the pisano period
    for i in range(remainder + 1):
        fib_sum += get_fibonacci(i) % 10

    return fib_sum


def get_last_digit_of_partial_fibonacci_sum_improved(m, n):
    """Get the last digit of the partial sum of Fibonacci numbers.

    Args:
        m (int): Lower index of the partial sum.
        n (int): Upper index of the partial sum.
    """

    upper_sum = get_sum_of_last_digits(n)
    lower_sum = get_sum_of_last_digits(m - 1)

    return (upper_sum - lower_sum) % 10


if __name__ == "__main__":
    user_input = sys.stdin.read()
    from_index, to_index = map(int, user_input.split())
    print(get_last_digit_of_partial_fibonacci_sum_improved(from_index, to_index))
