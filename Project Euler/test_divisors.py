def test (total):
    count = 0
    for i in range(1, total+1/2):
        if total%i == 0:
            count += 1
    return count
            
def s (num):
    total = 0
    while num:
        total += num
        num -= 1
    return total
    
divisors = 0
curr_num = 500000
while divisors < 500:
    divisors = test(s(curr_num))
    curr_num += 1
print s(curr_num-1)
