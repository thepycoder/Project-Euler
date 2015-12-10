def isprime(n):
    for i in range(2, n/2 + 1):
        if n % i == 0:
            return False
    return True

max = (0, 0, 0)
for a in range(0, 1000):
    for b in range(0, 1000):
        flag = True
        n = 0
        while flag == True:
            v = n**2 + a*n + b
            if not isprime(v):
                flag = False
            else:
                n += 1
                if n > max[0]:
                    max = (n, a, b)
    print a


print max, max[1]*max[2]