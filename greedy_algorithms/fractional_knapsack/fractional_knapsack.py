# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    vpus = []
    for i in range(0, len(values)):
        vpu = float(values[i] / weights[i])
        vpus.append(vpu)

    remaining_capacity = capacity

    while remaining_capacity > 0:
        # print(remaining_capacity)
        index = vpus.index(max(vpus))
        max_items = remaining_capacity // weights[index]
        mod = remaining_capacity % weights[index]
        print(max_items, mod)
        if max_items > 0:
            units_weight = weights[index] * max_items
            remaining_capacity = remaining_capacity - units_weight
            value = float(value + (values[index] * max_items))
        else:
            units_weight = (remaining_capacity / weights[index]) * weights[index]
            remaining_capacity = remaining_capacity - units_weight
            value = float(value + (vpus[index] * capacity))

        del weights[index]
        del values[index]
        del vpus[index]

    return round(value, 4)


if __name__ == "__main__":
    # data = list(map(int, sys.stdin.read().split()))
    data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

#     3 50 60 20 100 50 120 30 ------ 1 10 500 30 ------ 1 1000 500 30
