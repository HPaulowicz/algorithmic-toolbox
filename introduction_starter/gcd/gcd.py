# Uses python3
import sys

def euclide_gcd(a, b):
    while b:
        a, b = b, a%b
    return a

if __name__ == "__main__":
    input = input()
    # input = sys.stdin.read()
    a, b = map(int, input.split())
    print(euclide_gcd(a, b))
