# module to find out if a number has 2 factors with three digits

def isthree(comp):
    for i in range(100,999):
        check = comp//i
        modcheck = comp % i
        if 100 < check < 999 and modcheck == 0 :
            return comp
