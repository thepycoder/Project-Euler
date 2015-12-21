answer = 0
for i in range(2, 999999):
    total = 0
    num = str(i)
    for digit in num:
        total += int(digit)**5
    if total == i:
        answer += i
        print "found!", i

print "answer:", answer
