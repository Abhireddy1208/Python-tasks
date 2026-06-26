#sum of list
numbers = [10, 20, 30, 40, 50]

total = 0

for i in numbers:
    total += i

print("Sum of list:", total)

#product of list

numbers = [10, 20, 30, 40, 50]

product = 1

for i in numbers:
    product *= i

print("Product of list:", product)

#maximum element in list

numbers = [10, 20, 30, 40, 50]

maximum = numbers[0]

for i in numbers:
    if i > maximum:
        maximum = i

print("Maximum:", maximum)


#minmun element in list
numbers = [10, 20, 30, 40, 50]

minimum = numbers[0]

for i in numbers:
    if i < minimum:
        minimum = i

print("Minimum:", minimum)

#length of list without using (len())

numbers = [10, 20, 30, 40, 50]

count = 0

for i in numbers:
    count += 1

print("Length of list:", count)

