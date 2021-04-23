# Uses python3
import sys

def gcd_euclid(a, b):

    if b == 0:
        return a
    r = a % b
    return gcd_euclid(b, r)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_euclid(a, b))