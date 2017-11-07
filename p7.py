# build a seive of eratosthenes to get the 10 001st prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.

# What is the 10 001st prime number
# --------------------------------------------------------------

# primality test function from wikipedia
def isprime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i = i + 6
    return True


count = 0
num = 0
# check numbers, increasing count until the final prime is found
while count != 10001:
    num += 1
    if isprime(num):
        count += 1

print(num)
