# Uses python3
"""Script is used to find the last digit of a sum of the first n Fibonacci numbers."""

import sys


def get_last_digit_of_sum_of_fibonacci_numbers_naive(n):
    """Naive implementation of get last digit of a sum of fibonacci numbers

    Args:
        n (int): Number of fibonacci numbers to sum

    Returns:
        int: Last digit of a sum of fibonacci numbers
    """
    if n <= 1:
        return n

    previous = 0
    current = 1
    fib_sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        fib_sum += current

    return fib_sum % 10


if __name__ == "__main__":
    user_input = sys.stdin.read()
    num = int(user_input)
    print(get_last_digit_of_sum_of_fibonacci_numbers_naive(num))
