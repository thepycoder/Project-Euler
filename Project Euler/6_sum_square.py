def som():
    som = 0
    for i in range(1, 101):
        som += i**2
    return som

def macht():
    macht = 0
    for i in range(1, 101):
        macht += i
    macht = macht**2
    return macht

if __name__ == '__main__':
    print som()
    print macht()
    oplossing = abs(som() - macht())
    print oplossing
