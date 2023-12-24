# Uses python3
"""Script to calculate the fibonacci number n mod m

Returns:
    int: result of fibonacci number n mod m
"""

import sys


def get_fibonacci(n):
    """Implementation of fibonacci number calculation

    Args:
        n (int): fibonacci number n

    Returns:
        int: n-th fibonacci number
    """
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current


def get_fibonacci_huge_improved(n, m):
    """Improved implementation of Fibonacci Huge

    Args:
        n (int): fibonacci number n
        m (int): modulo to divide by

    Returns:
        int: result of fibonacci number n mod m
    """
    if n <= 1:
        return n

    previous = 1
    current = 1
    period = 0

    for index in range(1, n - 1):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            period = index + 1
            break

    if period == 0:
        return current % m

    return get_fibonacci(n % period) % m


if __name__ == "__main__":
    user_input = sys.stdin.read()
    n, m = map(int, user_input.split())
    print(get_fibonacci_huge_improved(n, m))
