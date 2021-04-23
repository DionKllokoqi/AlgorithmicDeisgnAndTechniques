# Uses python3
import sys
from fibonacci_last_digit_naive import get_fibonacci_last_digit_naive as get_last_fib_digit_naive
from get_fibonacci_last_digit_improved import get_fibonacci_last_digit_improved as get_last_fib_digit


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_last_fib_digit(n) == get_last_fib_digit_naive(n))