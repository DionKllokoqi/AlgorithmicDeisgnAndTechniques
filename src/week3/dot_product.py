# Uses python3
import sys


def sort_list(to_sort_list):
    retList = []
    tmpList = to_sort_list[:]

    while len(retList) != len(to_sort_list):
        tmpMax = float("-inf")
        tmpMaxIndex = 0
        for i in range(len(tmpList)):
            if tmpList[i] > tmpMax:
                tmpMax = tmpList[i]
                tmpMaxIndex = i
        retList.append(tmpMax)
        tmpList.pop(tmpMaxIndex)
    return retList


def max_dot_product(a, b):
    tmpProfits = sort_list(a)
    tmpClicks = sort_list(b)
    res = 0

    for i in range(len(a)):
        res += tmpProfits[i] * tmpClicks[i]
    return res


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1 : (n + 1)]
    b = data[(n + 1) :]
    print(max_dot_product(a, b))
