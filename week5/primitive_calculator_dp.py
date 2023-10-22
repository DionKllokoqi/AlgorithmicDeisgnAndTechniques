# Uses python3
import sys


def optimal_sequence(n):

    # List of parent for each number
    parents = [None] * (n + 1)
    # Sequence of number of operations to get to each number from 1 to n
    min_num_of_operations = [0] + [float("inf")] * n

    # Find the optimal solution for each number from 1 to n
    for i in range(1, n + 1):
        current_parent = i - 1
        current_min_op = min_num_of_operations[current_parent] + 1

        # If i is divisible by 3, we can get to the current
        # i from i // 3 by multiplying it with 3
        # => steps to get to i = steps to get to i // 3 + 1
        if (i % 3) == 0:
            parent = i // 3
            num_ops = min_num_of_operations[parent] + 1
            if num_ops < current_min_op:
                current_min_op, current_parent = num_ops, parent

        # If i is divisible by 2, we can get to the
        # current i from i // 2 by multiplying it with 2
        # => steps to get to i = steps to get to i // 2 + 1
        if (i % 2) == 0:
            parent = i // 2
            num_ops = min_num_of_operations[parent] + 1
            if num_ops < current_min_op:
                current_min_op, current_parent = num_ops, parent

        min_num_of_operations[i], parents[i] = current_min_op, current_parent

    k = n
    reversed_sequence = []
    while k > 0:
        current_parent = k
        reversed_sequence.append(current_parent)
        k = parents[k]

    reversed_sequence.reverse()
    return reversed_sequence


inputVal = sys.stdin.read()
n = int(inputVal)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=" ")
