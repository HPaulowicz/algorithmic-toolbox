# Uses python3
import sys

def get_max_index(weights, values):
    max_i = 0
    max = 0
    for i in range(0, len(weights)):
        if ((weights[i] != 0) and (values[i] / weights[i] > max)):
            max = float(values[i] / weights[i])
            max_i = i
    return max_i

def get_optimal_value(capacity, weights, values):
    value = 0.0
    for i in range(0, len(weights)):
        if (capacity == 0):
            return value
        index = get_max_index(weights, values)
        a = min(capacity, weights[index])
        value += a * values[index] / weights[index]
        weights[index] -= a
        capacity -= a
    return round(value, 4)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    # data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

