
a = int(input())
b = int(input())

def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

lcm = (a * b) // gcd(a, b)
print(lcm)
