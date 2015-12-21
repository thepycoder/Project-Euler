import time

lijst = [1, 1]

def generate():
    i = 2
    while len(str(lijst[-1])) < 1000:
        lijst.append(lijst[i-2] + lijst[i-1])
        i += 1
    return i

if __name__ == '__main__':
    start_time = time.time()
    print generate()
    print time.time() - start_time, "seconds"
