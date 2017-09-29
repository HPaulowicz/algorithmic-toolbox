# Uses python2.7
n = int(input())
a = [int(x) for x in str(raw_input()).split()]

assert len(a) == n

max_index_one = int(-1)

for i in range(0, n):
    if (max_index_one == -1) or (a[i] > a[max_index_one]):
        max_index_one = i

max_index_two = int(-1)

for j in range(0, n):
    if (a[j] != a[max_index_one] or j != max_index_one) and ((max_index_two == -1) or (a[j] > a[max_index_two])):
        max_index_two = j

result = long(a[max_index_one] * a[max_index_two])

print(result)