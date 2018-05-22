# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    print(n // 3)
    return summands

if __name__ == '__main__':
    # input = sys.stdin.read()
    input = input()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')

# 6 - 3 : 1 2 3
# 8 - 3 : 1 2 5
# 2 - 1 : 2