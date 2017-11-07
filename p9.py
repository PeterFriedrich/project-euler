# A Pythagorean triplet is a set of three natural numbers,
# a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for
# which a + b + c = 1000.
# Find the product abc.#
# ----------------------------------------------------------------

# make sure the numbers are properly ordered
# a < b < c

# make sure they obey a^2 + b^2 = c^ 2

# make sure a + b + c = 1000

# calculate a*b*c
import math

a = 0
b = 0
c2 = 0
final = 0

# if a < b < c store it
# if a^2 + b^2 = c^2
# if a + b + c = 1000
for a in range (0,1000):
    for b in range(a + 1,1000):
        c2 = a**2 + b**2
        c = float(math.sqrt(c2))
        if c.is_integer() and a + b + c == 1000:
            print('a:',a)
            print('b:',b)
            print('c:',c)
            final = a*b*c
            print("The Product is:",final)
