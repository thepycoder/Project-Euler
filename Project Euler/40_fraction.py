a = 1
blub = ''
total = 1
print "generating..."
for i in range(1, 1000000):
	blub += str(i)

print "getting solution..."	
while a != 1000000:
    print a,
    total *= int(blub[a-1])
    a *= 10

print total
