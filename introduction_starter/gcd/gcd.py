# Uses python3
import sys

def gcd_naive(a, b):
    result = 0
    for i in range(1, a + b):
        if a % i == 0 and b % i == 0:
            result = i
    return result

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
