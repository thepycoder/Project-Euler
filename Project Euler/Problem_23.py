from sets import Set

def getdivisors(n):
    s = 0
    for i in range(1, n/2 + 1):
        if n % i == 0:
            s += i
    return s

abu = []
for i in range(1, 28124):
    if getdivisors(i) > i:
        abu.append(i)

t = Set()
for a in abu:
    for b in abu:
        t.add(a + b)

result = 0
for c in range(1, 28124):
    if c not in t:
        result += c

print result