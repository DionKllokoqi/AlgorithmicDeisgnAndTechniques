# Uses python3

"""Script to calculate the fibonacci number n mod m


Returns:

    int: result of fibonacci number n mod m

"""
import sys


def get_fibonacci_huge_naive(n, m):
    """Naive implementation of Fibonacci Huge

    Args:
        n (int): fibonacci number n
        m (int): modulo to divide by

    Returns:
        int: result of fibonacci number n mod m
    """
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


if __name__ == "__main__":
    user_input = sys.stdin.read()
    n, m = map(int, user_input.split())
    print(get_fibonacci_huge_naive(n, m))
