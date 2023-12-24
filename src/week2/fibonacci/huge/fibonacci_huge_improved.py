# Uses python3
"""Script to calculate the fibonacci number n mod m

Returns:
    int: result of fibonacci number n mod m
"""

import sys


def get_fibonacci_huge_improved(n, m):
    """Improved implementation of Fibonacci Huge"""
    p = get_pisano_period(m)

    remainder = n
    if p != 0:
        remainder = n % p

    previous = 0
    current = 1

    if remainder == 0 or remainder == 1:
        return remainder
    for _ in range(remainder - 1):
        previous, current = current, previous + current

    # return result
    return current % m


def get_pisano_period(m):
    """Calculate pisano period for m

    Args:
        m (int): modulo to divide by

    Returns:
        int: pisano period for m
    """
    if m >= 2:
        previous = 0
        current = 1

        # The maximum possible length of the Pisano period is mm,
        # because there are only m possible values for the remainder
        # of a number modulo m, and there are only mm possible
        # pairs of consecutive remainders. Why are there only mm
        # possible pairs of remainders? Well, since the period must
        # start with 01, there are only mm possible pairs of remainders.
        for i in range(m * m):
            previous, current = current, (current + previous) % m

            if previous == 0 and current == 1:
                return i + 1
    else:
        return 0


if __name__ == "__main__":
    user_input = sys.stdin.read()
    n, m = map(int, user_input.split())
    print(get_fibonacci_huge_improved(n, m))
