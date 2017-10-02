# Python 2.7

def naive_gcd(a, b):
    result = 0
    for i in range(1, a+b):
        if a % i == 0 and b % i == 0:
            result = i
    return result

# print naive_gcd(int(input()), int(input()))

def euclide_gcd(a, b):
    while b:
        a, b = b, a%b
    return a

print(euclide_gcd(int(input()), int(input())))
