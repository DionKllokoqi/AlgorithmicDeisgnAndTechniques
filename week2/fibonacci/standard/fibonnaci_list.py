# Uses python3


def calc_fib_list(n):
    if n <= 1:
        return n

    fibArray = [0, 1]
    for i in range(2, n + 1):
        fibArray.append(fibArray[i - 1] + fibArray[i - 2])

    return fibArray[n]


if __name__ == "__main__":
    n = int(input())
    print(calc_fib_list(n))
