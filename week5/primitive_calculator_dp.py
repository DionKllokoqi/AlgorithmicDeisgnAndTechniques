# Uses python3
import sys

def optimal_sequence(n):

    # Intermediate sequence to arrive at n
    optimal_sequence = [1]
    
    # Sequence of number of operations to get to each number from 1 to n
    min_num_of_operations = [0] * (n + 1)

    # For each number, find the optimal way to get there via
    # a calculation with one of the operators
    if n > 1:
        min_num_of_operations[float('inf')] = -1

        # Find the optimal solution for each number from 1 to n
        for i in range(1, n + 1):
            num_of_operations_mult3 = float('inf')
            num_of_operations_mult2 = float('inf')
            num_of_operations_add1  = float('inf')

            # If i is divisible by 3, we can get to the current
            # i from i // 3 by multiplying it with 3
            # => steps to get to i = steps to get to i // 3 + 1
            if (i % 3) == 0:
                num_of_operations_mult3 = min_num_of_operations[i // 3] + 1

            # If i is divisible by 2, we can get to the
            # current i from i // 2 by multiplying it with 2
            # => steps to get to i = steps to get to i // 2 + 1
            if (i % 2) == 0:
                num_of_operations_mult2 = min_num_of_operations[i // 2] + 1

            # We can always get to the current i from the previous i-1 via one extra step
            num_of_operations_add1 = min_num_of_operations[i - 1] + 1

            # Check which is the optimal way
            min_num_of_operations[i] = min(num_of_operations_mult3,
                                          num_of_operations_mult2,
                                          num_of_operations_add1)

    optimal_sequence.append(n)
    return optimal_sequence

inputVal = sys.stdin.read()
n = int(inputVal)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')