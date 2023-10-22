# Uses python3
import sys


def merge(a, left, ave, right):
    B = a[left:ave]
    C = a[ave:right]
    A = []

    # compare elements in the two lists, arrange them to the
    # new one until both are empty
    while B and C:
        b = B[0]
        c = C[0]
        if b >= c:
            A.append(c)
            C.pop(0)
        else:
            A.append(b)
            B.pop(0)

    # add any remaining elements to the end of the sorted list
    if B:
        A.extend(B)
        B = []
    if C:
        A.extend(C)
        C = []

    # sort the elements of the original list
    index = 0
    for i in range(left, right):
        a[i] = A[index]
        index += 1


def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)

    # here we need to make some kind of calculation to merge and
    # mergesort the array a and determine the nr of inversions
    i = left
    j = ave

    # count the number of inversions to be made between the two sides
    # left and right side are sorted. if at any point a[i] > a[j], then
    # there will be ave - i inversions, since each element from i to ave
    # will also be larger than a[j]
    while i < ave and j < right:
        if a[i] > a[j]:
            number_of_inversions += ave - i
            j += 1
        else:
            i += 1

    # sort and merge the lists
    merge(a, left, ave, right)

    return number_of_inversions


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
