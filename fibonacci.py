# Python2.7

def imitate_hand_comp(n):
    arr = [0] * n
    arr[0] = 0
    arr[1] = 1
    for i in range(2, n):
        arr[i] = arr[i-2] + arr[i-1]
    return arr[-1]

print(imitate_hand_comp(int(input())))