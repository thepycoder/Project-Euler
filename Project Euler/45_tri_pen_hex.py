def main():
    tri = []
    pen = []
    hexa = []
    
    for a in range(284, 2000000):
        tri.append(a*(a+1)/2)
    for b in range(165, 2000000):
        pen.append(b*(3*b-1)/2)
    for c in range(143, 2000000):
        hexa.append(c*(2*c-1))

    for number in tri:
        if number in pen:
            print number
            if number in hexa:
                print "found! ", number

if __name__ == '__main__':
    print main()

    
