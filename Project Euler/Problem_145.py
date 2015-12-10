def reverse(n):
    return int(str(n)[::-1])

def isodd(n):
    for c in str(n):
        if int(c) % 2 == 0:
            return False
    return True


answer = 0
for i in range(1, 1001):
    if not str(i)[-1:] == "0":
        if isodd(i + reverse(i)):
            answer += 1

print answer