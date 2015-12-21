import time

def get_file(path = "22_names.txt"):
    namen = open(path, "r").read()
    namen2 = namen.replace('"', '')
    namen3 = namen2.split(",")
    namen3.sort()
    return namen3

def score(namen3):
    totaal = 0
    place = 1
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for word in namen3:
        som = 0
        for i in range(0, len(word)):
            value = a.find(word[i])
            som += value+1
        totaal += som*place
        place += 1
    return totaal

if __name__ == '__main__':
    start_time = time.time()
    print score(get_file())
    print time.time() - start_time, "seconds"
