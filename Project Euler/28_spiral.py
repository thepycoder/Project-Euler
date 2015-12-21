def generate(diagonal):
    lijst = []
    for i in range(1, diagonal+1):
        lijst.append(i)
    return lijst

def main(lijst):
    a = 0
    b = 8
    c = 2
    som = 0
    for j in range(0, 4):  
        for i in range(a, b, c):
            som += lijst[i]
            print lijst[i],

        a = b
        b = 25
        c += 2
        
if __name__ == '__main__':
    main(generate(25))
