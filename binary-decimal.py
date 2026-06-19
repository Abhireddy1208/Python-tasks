binary = [[1, 0, 1, 1]]
decimal = 0
power = len(binary[0]) - 1
for i in binary[0]:
    decimal = decimal + i * (2 ** power)
    power -= 1
print("Decimal:", decimal)