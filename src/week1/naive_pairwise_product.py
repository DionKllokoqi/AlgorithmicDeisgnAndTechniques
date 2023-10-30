# Uses python3


def get_maximum_pairwise_product_naive(n, a):
    product = 0

    for i in range(n):
        for j in range(i + 1, n):
            product = max(product, a[i] * a[j])

    return product


if __name__ == "__main__":
    n = int(input())
    a = [int(x) for x in input().split()]

    print(get_maximum_pairwise_product_naive(n, a))
