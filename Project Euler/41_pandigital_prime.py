import sys

def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False
    return True

def test(num):
    num = str(num)
    check = []
    for digit in range(1, len(num)+1):
        if str(digit) in num:
            check.append(1)
        else:
            check.append(0)
    if 0 in check:
        return False
    else:
        #print "found!", num
        return True
        

if __name__ == '__main__':
    lijst = []
    for num in range(0, 9999999):
        if isprime(num):
            if test(num):
                m = num
    print m
