# Uses python3
import sys
import random


def partition3(a, l, r):
    # set pivot
    x = a[l][0]
    j_1 = l
    for i in range(l + 1, r + 1):
        if a[i][0] < x:
            # current element < pivot. Switch element to left side of array
            # where the elements are smaller than the pivot.
            j_1 += 1
            a[i], a[j_1] = a[j_1], a[i]
    # switch pivot with last element < than it
    a[l], a[j_1] = a[j_1], a[l]

    j_2 = j_1
    # add all elements that are equal to the pivot after it
    for i in range(j_1 + 1, r + 1):
        if a[i][0] == x:
            j_2 += 1
            a[i], a[j_2] = a[j_2], a[i]

    # return indices of last element < pivot and of last element = pivot
    return j_1, j_2


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m_1, m_2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m_1 - 1)
    randomized_quick_sort(a, m_2 + 1, r)


def binary_search_start_points(a, x):
    indices = []
    left, right = 0, len(a)
    while left < right:
        mid = left + (right - left) // 2
        if a[mid] <= x:
            indices.extend(range(left, mid + 1))
            left = mid + 1
        else:
            right = mid
    return indices


def binary_search_end_points(a, x):
    indices = []
    left, right = 0, len(a)
    while left < right:
        mid = left + (right - left) // 2
        if a[mid] > x:
            indices.extend(range(mid, right))
            right = mid
        else:
            left = mid + 1
    return indices


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)

    # 1. Order segments via their starting points from lowest to highest O(nlogn)
    # 2. Binary search of appropriate segments for each point is O(logn)
    # 3. Going through each point is O(n)
    # 4. All in all complexity O(nlogn)

    # quicksort3 the starts and the ends
    segment_list_starts = []
    segment_list_ends = []
    # add segments to a list for easier manipulation
    for i in range(len(starts)):
        segment_list_starts.append(starts[i])
        segment_list_ends.append(ends[i])

    # sort the segments via their starting position
    segment_list_starts.sort()
    segment_list_ends.sort()

    for i in range(len(points)):
        # get all indices of the starts that are <= point
        segments_start_before_point = binary_search_start_points(
            segment_list_starts, points[i]
        )
        segments_end_after_point = binary_search_end_points(
            segment_list_ends, points[i]
        )

        segments_start_after_point = len(segment_list_starts) - len(
            segments_start_before_point
        )
        segments_end_before_point = len(segment_list_ends) - len(
            segments_end_after_point
        )

        cnt[i] = len(starts) - segments_start_after_point - segments_end_before_point

    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2 : 2 * n + 2 : 2]
    ends = data[3 : 2 * n + 2 : 2]
    points = data[2 * n + 2 :]
    # use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=" ")
