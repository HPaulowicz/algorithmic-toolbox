# Uses python3

def mpp(n, a):
    a = sorted(a)
    return a[n-1]*a[n-2]

if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    assert (len(a) == n)
    print(mpp(n, a))
