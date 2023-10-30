import sys
import closest
import random

# method takes a list of x and y coordinates
# and turns these into a list of points
def list_of_points(x, y):

    P = [closest.Point(x[i], y[i]) for i in range(len(x))]
    return P


# Method is responsible for comparing the
# distance calculated by the brute force
# algorithm and an efficient algorithm.
def min_distance_vals(x, y):

    P = list_of_points(x, y)
    P.sort(key=lambda point: point.x)
    Q = closest.copy.deepcopy(P)
    Q.sort(key=lambda point: point.y)

    retVal_1 = closest.closestUtil(P, Q, len(x))
    retVal_2 = closest.bruteForce(P, len(x))

    return retVal_1, retVal_2


# method is used to generate random tests
# for the min_distance_vals method and output
# the results
def test_generator():

    while True:

        n = random.randint(0, 4)
        x = [0] * n
        y = [0] * n
        for i in range(n):
            x[i] = random.randint(-1000, 1000)
            y[i] = random.randint(-1000, 1000)

        retVal_1, retVal_2 = min_distance_vals(x, y)
        if retVal_1 == retVal_2:
            print("OK")
        else:
            print(f"Closest Util: {retVal_1}, BruteForce: {retVal_2}")
            for i in range(n):
                print(f"xVal: {x[i]}, yVal: {y[i]}")
            return


if __name__ == "__main__":
    test_generator()
