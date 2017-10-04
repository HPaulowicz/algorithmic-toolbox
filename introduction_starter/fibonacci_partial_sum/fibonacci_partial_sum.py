# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10

def fibonacci_partial_sum(a, n):
    if n > 2:
        fibonacci = [0, 1, 1]
        sequence = [0, 1, 1]

        m = 10

        for i in range(3, n + 1):
            fibonacci.append((fibonacci[-2] + fibonacci[-1]) % m)

            sequence[0] = fibonacci[-3]
            sequence[1] = fibonacci[-2]
            sequence[2] = fibonacci[-1]

            if sequence == [0, 1, 1]:
                n_mod = n // (i - 2)
                a_mod = a // (i - 2)
                # sequence_sum = sum(fibonacci[0:(i - 2)])
                # remainder_sum = sum(fibonacci[0:(n + 1 - ((i - 2) * n_mod))])
                # _sum = (sequence_sum * n_mod) + remainder_sum

                short_sequence_sum = sum(fibonacci[0:(i - 2)])
                short_remainder_sum = sum(fibonacci[0:(a + 1 - ((i - 2) * a_mod))])
                short_sum = (short_sequence_sum * a_mod) + short_remainder_sum

                long_sequence_sum = sum(fibonacci[0:(i - 2)])
                long_remainder_sum = sum(fibonacci[0:(n + 1 - ((i - 2) * n_mod))])
                long_sum = (long_sequence_sum * n_mod) + long_remainder_sum

                _sum = abs((long_sum ) - (short_sum ))

                return _sum, long_sum, short_sum

        return sum(fibonacci[a:n+1]) % m
    else:
        return n


if __name__ == '__main__':
    input = input()
    # input = sys.stdin.read()
    a, n = map(int, input.split())
    print(fibonacci_partial_sum_naive(a, n))
    print(fibonacci_partial_sum(a, n))