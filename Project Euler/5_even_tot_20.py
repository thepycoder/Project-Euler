lijst = [0]
getal = 1

while 0 in lijst:
    lijst = []
    for b in range(1, 21):
        if getal%b == 0:
            lijst.append(1)
        else:
            lijst.append(0)
    getal += 1
    if getal%1000000 == 0:
        print getal

print "het getal is: " + str(getal-1)

