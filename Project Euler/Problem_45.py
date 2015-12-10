from cmath import sqrt


def triangle(n):
    return n*(n+1)/2

def pentagonal(n):
    return n*(3*n - 1) / 2

def hexagonal(n):
    return n*(2*n - 1)

for i in range(2, 41000):
    v = pentagonal(i)
    n1 = (1+sqrt(1+8*v))/4
    n2 = (-1+sqrt(1+8*v))/2

    if n1 % 1 == 0 and n2 % 1 == 0:
        print "found: " + str(v)

print 'done'