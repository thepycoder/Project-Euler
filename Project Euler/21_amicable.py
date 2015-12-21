def divisors(number):
    s = 0
    for i in range(1, number):
	if number%i == 0:
		s += i
    return s

if __name__ == '__main__':
    answer = 0
    checklist = []
    duplicates = []
    for i in range(1, 10000):
        number = i
        cache = divisors(number)
        cache2 = divisors(cache)
        if cache2 == number and cache2 != cache:
            if number not in duplicates:
                duplicates.append(number)
                duplicates.append(cache)
                print "pair found!", cache, cache2
                answer += cache + cache2
    print "answer:", answer

