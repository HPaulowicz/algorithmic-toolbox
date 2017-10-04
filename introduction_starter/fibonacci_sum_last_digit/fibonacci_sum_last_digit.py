# Uses python3
import sys

def fibonacci_sum(n):
    if n > 0:
        fibonacci = [0, 1, 1]
        sequence = [0, 1, 1]

        m = 10

        for i in range(3, n + 1):
            fibonacci.append(((fibonacci[-2] % m) + (fibonacci[-1] % m)) % m)

            sequence[0] = fibonacci[-3]
            sequence[1] = fibonacci[-2]
            sequence[2] = fibonacci[-1]

            print(fibonacci)
            print(sequence)

            if sequence == [0, 1, 1]:
                return fibonacci[n % (i - 2)] % m

        return fibonacci[-1] % m
    else:
        return 0

if __name__ == '__main__':
    input = input()
    # input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))
