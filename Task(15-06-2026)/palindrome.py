def palindrome(n):
    original = n
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10

    if original == rev:
        return "Palindrome"
    else:
        return "Not Palindrome"
