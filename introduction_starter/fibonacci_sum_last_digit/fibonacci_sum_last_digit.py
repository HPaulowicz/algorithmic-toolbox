# Uses python3
import sys

def fibonacci_sum(n):
    arr = [0] * 2
    s = 0
    if n > 0:
        arr[0] = 0
        arr[1] = 1
        s += 1
        for i in range(2, n + 1):
            # fn = arr[-2] + arr[-1]
            fn = ((arr[-2] % 10) + (arr[-1] % 10)) % 10
            arr += [fn]
            s += fn
            del arr[0]
    return s % 10

if __name__ == '__main__':
    # input = input()
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))
