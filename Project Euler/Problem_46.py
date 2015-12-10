from math import sqrt


def isprime(n):
    for i in range(2, n/2 + 1):
        if n % i == 0:
            return False
    return True

primes = []
for i in range(1, 10000):
    if isprime(i):
        primes.append(i)

def check(n):
    for a in range(1, n):
        for b in primes:
            if b + 2*(a**2) == n:
                #print str(b) + " + 2 x " + str(a) +"^2 = " + str(b + 2*(a**2))
                return True
    return False


for i in range(1, 10000, 2):
    print i
    if not isprime(i):
        if not check(i):
            print "found: " + str(i)
            break