# Uses python3
import sys

def fibonacci_partial_sum(a, n):
    arr = [0] * (n + 2)
    arr[0] = 0
    arr[1] = 1
    for i in range(2, n + 1):
        arr[i] = arr[i - 2] + arr[i - 1]
    return sum(arr[a:n+1]) % 10


if __name__ == '__main__':
    input = input()
    # input = sys.stdin.read()
    a, n = map(int, input.split())
    print(fibonacci_partial_sum(a, n))