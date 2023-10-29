import sys

from fibonacci_sum_last_digit_naive import fibonacci_sum_naive as fib_sum_naive
from fibonacci_sum_last_digit_inter import fibonacci_sum_inter as fib_sum_inter
from fibonacci_sum_last_digit_improved import fibonacci_sum_improved as fib_sum_improved

if __name__ == "__main__":
    input = sys.stdin.read()
    n = int(input)
    # print(fib_sum_improved(n) == fib_sum_naive(n))
    print(fib_sum_improved(n) == fib_sum_inter(n))
