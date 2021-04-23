import sys
from lcm_naive import lcm_naive
from lcm_improved import lcm_improved

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b) == lcm_improved(a, b))