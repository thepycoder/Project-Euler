def isprime(n):
    for i in range(2, n/2 + 1):
        if n % i == 0:
            return False
    return True


c = 1
i = 1
diff = 2
s = 1

diag = 1
prime = 0
side = 1

while i < 1000000000:
    i += diff
    c += 1
    diag += 1
    if c % 5 == 0:
        # print i, diff, prime, diag, float(prime) / float(diag)
        diff += 2
        c = 1
        #  print prime, diag, float(prime) / float(diag), diff/2
        if float(prime) / float(diag) < 0.1:
            print "gotieeee: " + str(diff/2)
            break

    if isprime(i):
        prime += 1

    s += i