# Uses python3
import sys


def get_pisannoPeriod(m):

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


def fibonacci_sum_improved(n):
    if n <= 1:
        return n

    # extract the pisanno period of 10
    p = get_pisannoPeriod(10)

    pSum = n
    if p != 0:
        pSum = p

    # calculate fibonacci number of result mod m
    previous = 0
    current = 1
    sum = 1

    if pSum == 0 or pSum == 1:
        return sum % 10

    for _ in range(pSum - 1):
        previous, current = current, (previous + current) % 10
        sum += current

    # calculate the remaining part of a period that doesn't fully fit
    p_remain = n % p
    # calculate how many times the full period occurs
    p_full = int(n / p)

    # sum is multiplied with how many full times this sum occurs
    sum *= p_full

    # a remaining, non-full period, is present
    if p_remain != 0:
        previous = 0
        current = 1
        sum += 1  # we need to add 1 to account for the first addition when current = 1

        # add up remaining sum
        for _ in range(p_remain - 1):
            previous, current = current, (previous + current) % 10
            sum += current

    return sum % 10


if __name__ == "__main__":
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_improved(n))
