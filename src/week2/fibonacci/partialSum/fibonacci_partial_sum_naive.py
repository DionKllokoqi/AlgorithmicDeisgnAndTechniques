# Uses python3

"""Naive implementation of the last digit of the partial sum of Fibonacci numbers algorithm.
"""

import sys


def get_last_digit_of_partial_fibonacci_sum_naive(m, n):
    """Get the last digit of the partial sum of Fibonacci numbers."""
    partial_fib_sum = 0

    previous = 0
    current = 1

    for i in range(n + 1):
        if i >= m:
            partial_fib_sum += previous

        previous, current = current, previous + current

    return partial_fib_sum % 10


if __name__ == "__main__":
    user_input = sys.stdin.read()
    from_index, to_index = map(int, user_input.split())
    print(get_last_digit_of_partial_fibonacci_sum_naive(from_index, to_index))
