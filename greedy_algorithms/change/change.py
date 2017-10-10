# Uses python3
import sys

def get_change(m):
    #write your code here
    values = [1, 5, 10]
    items = 0
    change = m
    for i in range(0, len(values)):
        max_value = max(values)
        rem = change // max_value
        change = change - (max_value * rem)
        values.remove(max_value)
        items += rem
    return items

if __name__ == '__main__':
    m = int(sys.stdin.read())
    # m = int(input())
    print(get_change(m))
