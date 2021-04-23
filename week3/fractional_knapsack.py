# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    
    for _ in range(len(weights)):

        if capacity == 0:
            return value
        
        bestItem = BestItem(weights, values)
        if weights[bestItem] == 0:
            return value
            
        a = values[bestItem] / weights[bestItem]
        
        # all the weight of the best item fits into the capacity
        if weights[bestItem] < capacity:
            capacity -= weights[bestItem]
            value += a * weights[bestItem]
            weights[bestItem] = 0
        # not all of the weight of the best item fits into the capacity
        else:
            value += a * capacity
            weights[bestItem] -= capacity
            capacity = 0

    return value

def BestItem(weights, values):

    maxValuePerWeight = 0
    bestItem = 0
    for i in range(len(weights)):

        if weights[i] > 0:
            tmpValuePerWeight = values[i] / weights[i]
            if tmpValuePerWeight > maxValuePerWeight:
                maxValuePerWeight = tmpValuePerWeight
                bestItem = i

    return bestItem


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
