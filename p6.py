# The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first
# ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum.

# ------------------------------------------------------------------------

# print the sum of the squares of the first ten natural numbers
squares = 0

for i in range(1,101):
    squares += i**2

print("sum of the squares of first ten natural numbers: ",squares)

a = 0
for i in range(1,101):
    a += i

a = a**2
print("The square of the sum: ", a)

print('difference: ',a-squares)
