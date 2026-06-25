def armstrong(n):
    original = n
    total = 0
    digits = len(str(n))

    while n > 0:
        digit = n % 10
        total += digit ** digits
        n //= 10

    if total == original:
        return "Armstrong"
    else:
        return "Not Armstrong"

