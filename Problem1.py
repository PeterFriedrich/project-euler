# username is  peter_friedrich

# If we list all the natural numbers below 10 that are multiples
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.
# --------------------------------------------------------------------
# Cycle through all the numbers between 1 and 1000, and test if
# They are a multiple of 3 or 5

#List to be summed
num = []

# Loop for testing and grabbing numbers
for i in range(0,1000):
    # test for 3
    if i%3 == 0 or i%5 == 0:
        num.append(i)

print(sum(num))
