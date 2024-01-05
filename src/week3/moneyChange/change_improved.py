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

    return m


if __name__ == "__main__":
    user_input = int(sys.stdin.read())
    print(get_change(user_input))
