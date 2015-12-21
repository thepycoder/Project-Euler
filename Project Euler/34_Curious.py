def faculty(num):
    num = int(num)
    fac = 1
    while num != 0:
        fac *= num
        num -= 1
    return fac

def is_curious(number):
    number = str(number)
    total = 0
    answer = 0
    for digit in number:
        total += faculty(int(digit))
    if int(number) == total:
        print "found!", number
        return int(number)

if __name__ == '__main__':
    for i in range(3, 999999):
        is_curious(i)
