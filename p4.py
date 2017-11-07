# A palindromic number reads the same both ways. The largest
# palindrome made from the product of two 2-digit numbers
# is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# Palindrome function
def isPal(num):
    numAux = num
    revnum = 0

    # takes number and divides by ten to pull of the right digit
    while numAux > 0:
        rDigit = numAux % 10
        # appends the right digit to the left of a new number
        revnum = revnum * 10 + rDigit
        numAux = numAux // 10

    # compare both numbers to see if equal
    if num == revnum:
        return True
    else:
        return False

pal = []

# loop to put all palindromes in a list
for i in range(10000,998001):
    if isPal(i):
        pal.append(i)

lenpal = int(len(pal))
print(lenpal)
final = []

# Function to find out if composite of two 3 digit factors
def isthree(comp):
    for i in range(100,999):
        check = comp//i
        modcheck = comp % i
        if 100 < check < 999 and modcheck == 0 :
            return comp

# check the palindrome list and return list with number if true
for i in range(0,lenpal):
    final.append(isthree(pal[i]))

print(final)
