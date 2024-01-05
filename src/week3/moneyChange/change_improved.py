# Uses python3

"""Module to get the minimum number of coins needed to change the input.
"""

import sys


def get_change(m):
    """Method gets the minimum number of coins needed to change the input value
    into coins with denominations 1, 5, and 10.

    Args:
        m (int): The input value.

    Returns:
        int: The minimum number of coins needed to change the input value into
    """

    min_coins = 0

    if m >= 10:
        min_coins += m // 10
        m %= 10
    if m >= 5:
        min_coins += m // 5
        m %= 5
    if m >= 1:
        min_coins += m

    return min_coins


if __name__ == "__main__":
    user_input = int(sys.stdin.read())
    print(get_change(user_input))
