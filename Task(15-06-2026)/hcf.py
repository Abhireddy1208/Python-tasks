def gcd(a, b):
    small = a if a < b else b
    for i in range(small, 0, -1):
        if a % i == 0 and b % i == 0:
            return i