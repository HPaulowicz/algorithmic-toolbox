# Uses python3

import sys

def calc_fib(n):
    arr = [0] * (n+2)
    arr[0] = 0
    arr[1] = 1
    for i in range(2, n+1):
        arr[i] = arr[i-2] + arr[i-1]
    return arr[n]

if __name__ == "__main__":
    input = input()
    # input = sys.stdin.read()
    n = int(input)
    print(calc_fib(n))
