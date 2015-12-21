import math

for a in range(1, 1001):
    for b in range(a+1, 1001):
        c = math.sqrt(a**2+b**2)
        if a+b+c == 1000:
            print "found! ", str(a), str(b), str(c)
            print "product: ", str(a*b*c)


