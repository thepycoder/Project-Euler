c = 1
i = 1
diff = 2
s = 1
while i < 1002001:
    i += diff
    c += 1
    if c % 5 == 0:
        diff += 2
        c = 1
    #  print i
    s += i

print "total sum: " + str(s)