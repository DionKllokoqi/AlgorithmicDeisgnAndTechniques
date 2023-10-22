import closest_stressTest
import sys

if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    retVal_1, retVal_2 = closest_stressTest.min_distance_vals(x, y)
    print(f"ClosestUtil: {retVal_1}, BruteForce: {retVal_2}")
