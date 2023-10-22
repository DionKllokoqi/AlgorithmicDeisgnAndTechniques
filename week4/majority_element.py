# Uses python3
import sys


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left == right - 1:
        return a[left]

    mid = left + (right - left) // 2
    leftVal = get_majority_element(a[:mid], 0, mid)
    rightVal = get_majority_element(a[mid:], 0, len(a[mid:]))

    if leftVal == rightVal:
        return leftVal
    if a.count(leftVal) > len(a) // 2:
        return leftVal
    if a.count(rightVal) > len(a) // 2:
        return rightVal
    return -1


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
