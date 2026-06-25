def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

tasks = {
    5: factorial(5),
    12: factorial(12)
}

print("5! =", tasks[5])
print("12! =", tasks[12])