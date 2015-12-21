m = 0
for a in range(1, 100):
	for b in range(1, 100):
		temp = list(str(a**b))
		total = 0
		for digit in temp:
                    total += int(digit)
                if total > m:
                    m = total
print m
