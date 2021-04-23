# Uses python3
import sys

def gcd_euclid(a, b):

    if b == 0:
        return a
    r = a % b
    return gcd_euclid(b, r)

def lcm_improved(a, b):

    if a == 0 and b == 0:
        return 0
    gcd = gcd_euclid(a, b)
    return (a * b) // gcd

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_improved(a, b))