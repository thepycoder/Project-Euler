import sys

def main():
    getal = str(2**1000)
    som = 0
    for i in range(0, len(getal)):
        som += int(getal[i])
    return som

if __name__ == '__main__':
    print main()
