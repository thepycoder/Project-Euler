def generate(num):
    chain = [num]
    count = 0
    while chain[count] > 1:
        if num%2 == 0:
            num = num/2
            chain.append(num)
        else:
            num = 3*num+1
            chain.append(num)
        count += 1
    return chain

def find_longest(limit):
    #long_chain = []
    m = 0
    start = 0
    for num in range(1, limit):
        chain = generate(num)
        if len(chain) > m:
            m = len(chain)
            #long_chain = chain
            start = num
    return start

if __name__ == '__main__':
    print find_longest(1000000)
        
