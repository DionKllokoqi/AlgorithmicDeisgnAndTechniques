# Uses python3
import sys


def get_change(m):

    rem = m
    i = 0
    while True:

        if (rem - 10) >= 0:
            rem -= 10
            i += 1
        elif (rem - 5) >= 0:
            rem -= 5
            i += 1
        elif (rem - 1) >= 0:
            rem -= 1
            i += 1
        else:
            break

    return i


if __name__ == "__main__":
    m = int(sys.stdin.read())
    print(get_change(m))
