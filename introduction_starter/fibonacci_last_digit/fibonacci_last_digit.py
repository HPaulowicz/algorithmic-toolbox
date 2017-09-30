# Uses python3
import sys

def get_fibonacci_last_digit(n):
    arr = [0] * (n + 2)
    arr[0] = 0
    arr[1] = 1
    for i in range(2, n + 1):
        arr[i] = ((arr[i - 2] % 10) + (arr[i - 1] % 10)) % 10
    return arr[n]

if __name__ == '__main__':
    # input = input()
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
