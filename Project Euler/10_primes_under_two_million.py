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

def main():
    som = 0
    number = 1

    while number < 2000000:
        if isprime(number) == False:
            number += 1
        else:
            som += number
            #print number
            number += 1
    return som

if __name__ == '__main__':
    print main()
