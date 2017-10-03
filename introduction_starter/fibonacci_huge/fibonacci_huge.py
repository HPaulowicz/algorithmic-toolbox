# Uses python3
import sys

def get_fibonacci_huge(n, m):
    arr = [0] * 2
    if n > 0:
        arr[0] = 0
        arr[1] = 1
        sequence = [0, 1,]
        for i in range(2, n + 1):
            fn = arr[-2] + arr[-1]
            arr += [fn]
            sequence.insert(len(sequence), int(arr[-1] % m))
            if sequence[-3:] == [0, 1, 1] and i > 2:
                return arr[n % len(sequence[0:-3])] % m
    return arr[-1] % m

if __name__ == '__main__':
    # input = input()
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
