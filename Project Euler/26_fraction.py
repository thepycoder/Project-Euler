from fractions import Fraction
for d in range(1, 1001):
    num = float(Fraction(1, d))
    lnum = list(num)
    print lnum
