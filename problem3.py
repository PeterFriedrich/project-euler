# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# ----------------------------------------------------------------

n = int(input('insert number to be factorized: '))

i = 2
factors = []

for i in range(2,n):
    if n % i == 0:
        ct = 0
        while n % i == 0:
            n = n/i
            factors.append(i)
            ct += 1
        print(i,ct)

factors.append(n)
del factors[-1]
print(factors)
