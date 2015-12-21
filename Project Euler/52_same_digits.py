for x in range(1, 200000):
    a = list(str(x))
    a.sort()
    check = 1
    for i in range(2, 7):
        temp = x*i
        temp = str(temp)
        temp = list(temp)
        temp.sort()
        if temp == a:
            check *= 1
        else:
            check *= 0
    if check == 1:
        print "found!", x
