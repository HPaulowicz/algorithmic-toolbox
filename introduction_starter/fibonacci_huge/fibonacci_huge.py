# Uses python3
import sys

def get_fibonacci_huge(n, m):
    if n > 0:
        fibonacci = [0, 1, 1]
        sequence = [0, 1, 1]

        for i in range(3, n + 1):
            fibonacci.append(((fibonacci[-2] % m) + (fibonacci[-1] % m)) % m)

            sequence[0] = fibonacci[-3]
            sequence[1] = fibonacci[-2]
            sequence[2] = fibonacci[-1]

            if sequence == [0, 1, 1]:
                return fibonacci[n % (i - 2)] % m

        return fibonacci[-1] % m

if __name__ == '__main__':
    input = input()
    # input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))