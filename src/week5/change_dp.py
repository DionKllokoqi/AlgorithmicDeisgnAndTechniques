# Uses python3
import sys


def get_change(m):

    # List will hold min number of change coins for values 0 - m
    min_num_coins = [0] * (m + 1)
    # Change coins
    coins = [1, 3, 4]

    # Looping through all the money values from 0 to m to find the change for each
    for money in range(1, m + 1):
        min_num_coins[money] = float("inf")
        # For each coin, we calculate the change we would get
        for coin in coins:
            # If current coin is larger than current money value, we cannot get change
            if money >= coin:
                # We add + 1 because we need to account for when (money - coin) = 0 and get_change rets 0
                num_of_coins = min_num_coins[money - coin] + 1
                if num_of_coins < min_num_coins[money]:
                    min_num_coins[money] = num_of_coins

    return min_num_coins[m]


if __name__ == "__main__":
    m = int(sys.stdin.read())
    print(get_change(m))
