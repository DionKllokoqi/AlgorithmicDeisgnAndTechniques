# Uses python3

"""Get the last digit of a sum of the first n Fibonacci numbers using pisano series
"""

import sys

from src.week2.fibonacci.fibonacci_efficient import get_fibonacci


def get_last_digit_of_sum_of_fibonacci_numbers_pisano(n):
    """Get the last digit of a sum of the first n Fibonacci numbers using pisano series"""

    # The pisano period of 10 is 60. The last digit of the sum
    # of the sum of n fibonacci numbers is the same as the sum
    # of all individual fibonacci numbers modulo 10.
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

    return fib_sum % 10


if __name__ == "__main__":
    user_input = sys.stdin.read()
    num = int(user_input)
    print(get_last_digit_of_sum_of_fibonacci_numbers_pisano(num))
