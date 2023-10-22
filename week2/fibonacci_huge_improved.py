# Uses python3
import sys


def get_fibonacci_huge_improved(n, m):

    # get pissano period m
    p = get_pisannoPeriod(n, m)

    # calculate n mod pisano period
    remainder = n
    if p != 0:
        remainder = n % p

    # calculate fibonacci number of result mod m
    previous = 0
    current = 1

    if remainder == 0 or remainder == 1:
        return remainder
    for i in range(remainder - 1):
        previous, current = current, previous + current

    # return result
    return current % m


def get_pisannoPeriod(n, m):

    if m >= 2:
        previous = fib1 = 0
        current = fib2 = 1

        for i in range(m * m):
            fib1, fib2 = fib2, (fib1 + fib2)
            previous, current = current, fib2 % m

            # testing condition
            if previous == 0 and current == 1:
                return i + 1
    else:
        return 0


if __name__ == "__main__":
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_improved(n, m))
