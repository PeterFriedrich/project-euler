
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

max = int(input("Sum primes up to what number? : "))

primesum = 0
for x in range(2, max + 1):
    isPrime = True
    # only go till squareroot
    for y in range(2, int(x **0.5) + 1):
        # break statement as soon as a modulus is nonzero
        if x % y == 0:
            isPrime = False
            break
    if isPrime:
        primesum += x

print(primesum)
