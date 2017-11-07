#2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20?
#-------------------------------------------------------------------

# take a number, divide it by all the numbers from 1 to 10,
# return it if it gives no remainder

# go up by 20s cuz other end digits won't be divisible

num = 0
count = 0

# while loop with counter to coninually count up the number
while True:
        # check if 1-20 can divide into the number, add a count for each
        for i in range(1,21):
            if num == 0:
                break
            elif num % i == 0:
                count += 1
            else:
                count = 0
                break
        # if counter is 20, its the number
        if count == 20:
            print(num)
            break
        else:
            num += 20
