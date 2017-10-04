# Uses python3
import sys

def fibonacci_sum(n):
    if n > 2:
        fibonacci = [0, 1, 1]
        sequence = [0, 1, 1]

        m = 10

        for i in range(3, n + 1):
            fibonacci.append(((fibonacci[-2] ) + (fibonacci[-1] )) % m)

            sequence[0] = fibonacci[-3]
            sequence[1] = fibonacci[-2]
            sequence[2] = fibonacci[-1]

            if sequence == [0, 1, 1]:
                n_mod = n // (i - 2)
                sequence_sum = sum(fibonacci[0:(i - 2)])
                ramainder_sum = sum(fibonacci[0:(n + 1 - ((i - 2) * n_mod))])
                _sum = (sequence_sum * n_mod) + ramainder_sum
                return _sum % m

        return sum(fibonacci) % m
    else:
        return n

if __name__ == '__main__':
    # input = input()
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))
