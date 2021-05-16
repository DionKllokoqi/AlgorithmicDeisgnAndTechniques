# Uses python3
import sys
import random

def partition3(a, l, r):
    # set pivot
    x = a[l]
    j_1 = l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            # current element < pivot. Switch element to left side of array
            # where the elements are smaller than the pivot.
            j_1 += 1
            a[i], a[j_1] = a[j_1], a[i]
    # switch pivot with last element < than it
    a[l], a[j_1] = a[j_1], a[l]

    j_2 = j_1
    # add all elements that are equal to the pivot after it
    for i in range(j_1 + 1, r + 1):
        if a[i] == x:
            j_2 += 1
            a[i], a[j_2] = a[j_2], a[i]

    # return indices of last element < pivot and of last element = pivot
    return j_1, j_2

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m_1, m_2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m_1 - 1)
    randomized_quick_sort(a, m_2 + 1, r)
    #m = partition2(a, l, r)
    #randomized_quick_sort(a, l, m - 1)
    #randomized_quick_sort(a, m + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
