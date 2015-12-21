import sys

def faculteit(getal):
    getal = int(getal)
    prod = 1
    while getal != 0:
        prod *= getal
        getal -= 1
    return prod

def som(prod):
    som = 0
    prod = str(prod)
    for i in range(0, len(prod)):
        som += int(prod[i])
    return som

if __name__ == '__main__':
        getal = sys.argv[1]
        print som(faculteit(getal))
        
