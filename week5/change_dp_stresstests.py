import sys
import change_dp


def change_dp_test():
    m = 0

    while True:
        print(f"Change for m: {m} = {change_dp.get_change(m)}")
        m += 1


if __name__ == "__main__":
    change_dp_test()
