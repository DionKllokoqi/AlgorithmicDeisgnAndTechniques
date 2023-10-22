from random import *
from naive_pairwise_product import get_maximum_pairwise_product_naive
from pairwise_product import get_maximum_pairwise_product


def StressTest(N, M):
    while True:
        n = randint(2, N)
        a = [None] * n

        for i in range(n):
            a[i] = randint(0, M)

        print(a)

        result1 = get_maximum_pairwise_product_naive(n, a)
        result2 = get_maximum_pairwise_product(a)

        if result1 == result2:
            print("OK")
        else:
            print("Wrong answer: ", result1, result2)
            return


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    StressTest(n, m)
