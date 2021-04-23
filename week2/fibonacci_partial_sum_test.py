import sys

from fibonacci_partial_sum_improved import fibonacci_partial_sum_improved as fib_improved
from fibonacci_partial_sum_naive import fibonacci_partial_sum_naive as fib_naive

if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fib_improved(from_, to) == fib_naive(from_, to))