import sys
from gcd_naive import gcd_naive
from gcd_euclid import gcd_euclid

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_euclid(a, b) == gcd_naive(a, b))