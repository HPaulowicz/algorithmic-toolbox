# Uses python3
import sys

def lcm(a, b):
    in_a = a
    in_b = b

    while b:
        a, b = b, a%b
    return int((in_b // a) * in_a)

if __name__ == '__main__':
    input = input()
    # input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
