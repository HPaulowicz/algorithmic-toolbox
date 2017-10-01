# Uses python3
import sys

def lcm(a, b):
    in_a = a
    in_b = b

    while b:
        a, b = int(b), int(a%b)
    return int((in_b / a) * in_a)

if __name__ == '__main__':
    input = raw_input()
    # input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
