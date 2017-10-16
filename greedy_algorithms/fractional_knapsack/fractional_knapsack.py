# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    vpus = []
    for i in range(0, len(values)):
        vpu = float(values[i] / weights[i])
        vpus.append([vpu, values[i], weights[i]])

    remaining_capacity = capacity

    sorted_values = sorted(vpus, key=lambda x: x[0], reverse=True)

    for i in range(0, len(sorted_values)):
        if remaining_capacity > 0:

            wgt = sorted_values[i][2]
            val = sorted_values[i][1]
            vpu = sorted_values[i][0]

            item_remainder = remaining_capacity // wgt

            if item_remainder > 0:
                remaining_capacity = remaining_capacity - wgt
                value = value + val
            else:
                remaining_capacity = 0
                value = value + (vpu * capacity)

    return round(value, 4)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    # data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

# 3 50 60 20 100 50 120 30
# 1 10 500 30
# 1 1000 500 30
# 3 100 60 20 100 50 120 30
