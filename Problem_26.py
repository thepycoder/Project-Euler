import math
from decimal import *

getcontext().prec = 1000  # sets the amount of nrs behind the decimal sign

def isRecurring(i, j):
    frac = Decimal(i) / Decimal(j)
    f = str(frac).split(".")[1]
    rec = [f[0], f[0]]
    index = 0

    for c in f:
        #print rec
        if f.__len__() < 1000:
            print str(i) + "/" + str(j) + " is not recurring"
            return 0

        if c == rec[1]:
            if f[99] == c and f[100] == c:
                print str(i) + "/" + str(j) + " is recurring over " + c
                return 1
        else:
            rec[1] = c

            if rec[0].startswith(c):
                if f[index:rec[0].__len__() + 1] == rec[0] + c:
                    print str(i) + "/" + str(j) + " is recurring over " + rec[0]
                    return rec[0].__len__()
            else:
                rec[0] += c

    index += 1


max = 0

for x in range(2, 1000):
    l = isRecurring(1, x)
    if l > max:
        max = l

print "max: " + str(max)
