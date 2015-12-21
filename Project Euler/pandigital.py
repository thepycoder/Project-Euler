import sys

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
    num = sys.argv[1]
    print test(num)
