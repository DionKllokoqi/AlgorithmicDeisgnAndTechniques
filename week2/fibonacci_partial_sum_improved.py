# Uses python3
import sys

def get_pisanno_fib(n):
    # pisano period of 10 is 60
    pPeriod = 60

    rem = n % pPeriod
    if rem == 0:
        return 0
    
    # last digits start to repeat after 60 fib numbers
    previous    = 0
    current     = 1

    for _ in range(rem - 1):
        previous, current = current, (previous + current)
    
    return current
    

def fibonacci_partial_sum_improved(from_, to):
    if to <= 1:
        return to

    # partial sum = fib(to + 2) - fib(from_ + 1)
    start_index = from_ + 1
    end_index = to + 2

    fib_start = get_pisanno_fib(start_index)
    fib_end = get_pisanno_fib(end_index)

    result = fib_end - fib_start
    return result % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_improved(from_, to))