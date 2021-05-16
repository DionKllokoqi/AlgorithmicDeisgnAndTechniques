#Uses python3
import sys
import math
import copy

# A class to represent a Point in 2D plane
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# A utility function to find the
# distance between two points
def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) *
                     (p1.x - p2.x) +
                     (p1.y - p2.y) *
                     (p1.y - p2.y))

# A Brute Force method to return the
# smallest distance between two points
# in P[] of size n
def bruteForce(P, n):
    min_val = float("inf")
    for i in range(n):
        for j in range(i + 1, n):
            if (dist(P[i], P[j]) < min_val):
                min_val = dist(P[i], P[j])

    return min_val

# A utility function to find the
# distance beween the closest points of
# strip of given size. All points in
# strip[] are sorted accordint to
# y coordinate. They all have an upper
# bound on minimum distance as d.
# Note that this method seems to be
# a O(n^2) method, but it's a O(n)
# method as the inner loop runs at most 6 times
def stripClosest(strip, size, d):

    # set the minimal distance that serves as an upper bound
    minVal = d

    # Pick all points one by one and
	# try the next points till the difference
	# between y coordinates is smaller than d.
    # Since all the points in the strip have
    # an x coordinate smaller than d to the middle,
    # we need to check only the y distance.
	# It is a proven fact that this loop
	# runs at most 6 times
    for i in range(size):
        j = i + 1
        while j < size and abs(strip[i].y - strip[j].y) < minVal:
            minVal = min(dist(strip[i], strip[j]), minVal)
            j += 1
    
    return minVal

# A recursive function to find the
# smallest distance. The array P contains
# all points sorted according to x coordinate
def closestUtil(P, Q, n):

    # If there are 2 or 3 points,
	# then use brute force
    if n <= 3:
        return bruteForce(P, n)
    
    # find the mid point in the x sorted array that will serve
    # as the dividing line
    mid = n // 2
    midPoint = P[mid]

    # divide points in y sorted array around the vertical line
    # given py the x position of the midpoint
    Pyl = []
    Pyr = []
    for i in range(n):
        if Q[i].x <= midPoint.x and len(Pyl) < mid:
            Pyl.append(Q[i])
        else:
            Pyr.append(Q[i])
    
    # find the closest distance recursively in left and right side
    dl = closestUtil(Pyl, Q, mid)
    dr = closestUtil(Pyr, Q[mid:], n - mid)

    # find the smaller of the two values
    d = min(dl, dr)

    # Build an array strip[] that contains
    # points close (closer than d)
    # to the line passing through the middle point
    strip = []
    for i in range(n):
        if abs(Q[i].x - midPoint.x) < d:
            strip.append(Q[i])
    
    return stripClosest(strip, len(strip), d)


def minimum_distance(x, y):

    # Create list of points
    P = [None] * len(x)
    for i in range(len(x)):
        P[i] = Point(x[i], y[i])
    
    P.sort(key = lambda point: point.x)
    Q = copy.deepcopy(P)
    Q.sort(key = lambda point: point.y)

    return closestUtil(P, Q, len(P))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
