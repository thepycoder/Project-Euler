s = False


def gethand(handstring):
    handstring = handstring.replace("T", "10")
    handstring = handstring.replace("J", "11")
    handstring = handstring.replace("Q", "12")
    handstring = handstring.replace("K", "13")
    handstring = handstring.replace("A", "14")
    cards = handstring.split(" ")
    splitcards = []
    for i in cards:
        splitcards.append(int(i[:-1]))
        splitcards.append(i[-1:])
    player1 = sorted(splitcards[0:10])
    player2 = sorted(splitcards[10:20])
    return [player1, player2]


def royalflush(playerhand):
    rf = [10, 11, 12, 13, 14]
    f = 0
    for r in rf:
        if r in playerhand:
            f += 1
    if f == 5 and playerhand.count(playerhand[5]) == 5:
        print "royal"
        s = True
        return 90000000000000 + score(playerhand[0:5])
    else:
        return 0


def straightflush(playerhand):
    global s
    f = 0
    high = 0
    for r in range(0, 4):
        if playerhand[r] == playerhand[r+1] - 1:
            high = playerhand[r+1]
            f += 1
    if f == 4 and not s:
        print "straight flush"
        s = True
        return 80000000000000 + 100000000000*high + score(playerhand[0:5])
    else:
        return 0


def fourofakind(playerhand):
    global s
    for r in playerhand[0:5]:
        if playerhand.count(r) == 4 and not s:
            print "four of a kind"
            s = True
            return 70000000000000 + 100000000000*r + score(playerhand[0:5])
    return 0


def fullhouse(playerhand):
    global s
    values = playerhand[0:5]
    #  print values, values.count(values[0]), values.count(values[4])
    if (values.count(values[0]) == 3 and values.count(values[4]) == 2) and not s:
        print "fullhouse 1"
        s = True
        return 60000000000000 + 100000000000*values[0] + 1000000000*values[4] + score(values)
    elif (values.count(values[0]) == 2 and values.count(values[4]) == 3) and not s:
        print "fullhouse 2"
        s = True
        return 60000000000000 + 100000000000*values[4] + 1000000000*values[0] + score(values)
    else:
        return 0


def flush(playerhand):
    global s
    if playerhand.count(playerhand[5]) == 5 and not s:
        print "flush"
        s = True
        return 50000000000000 + score(playerhand[0:5])
    else:
        return 0


def straight(playerhand):
    global s
    f = 0
    high = 0
    for r in range(0, 4):
        if playerhand[r] == playerhand[r+1] - 1:
            high = playerhand[r+1]
            f += 1
    if f == 4 and not s:
        print "straight"
        s = True
        return 40000000000000 + 100000000000*high + score(playerhand[0:5])
    else:
        return 0


def threeofakind(playerhand):
    global s
    for r in playerhand[0:5]:
        x = playerhand[0:5]
        blub = filter(lambda a: a != r, x)
        if playerhand.count(r) == 3 and blub[0] != blub[1] and not s:
            print "three of a kind"
            s = True
            return 30000000000000 + 100000000000*r + score(playerhand[0:5])
    return 0


def twopairs(playerhand):
    global s
    doubles = []
    pairs = []
    for r in playerhand[0:5]:
        if r in doubles:
            pairs.append(r)
        else:
            doubles.append(r)
    if pairs.__len__() == 2 and pairs[0] != pairs[1] and not s:  # otherwise three of a kind will trigger this too
        print "two pairs"
        s = True
        return 200000000000000 + 100000000000*doubles[0] + 100000000000*doubles[1] + score(playerhand[0:5])
    else:
        return 0



def onepair(playerhand):
    global s
    doubles = []
    pairs = []
    for r in playerhand[0:5]:
        if r in doubles:
            pairs.append(r)
        else:
            doubles.append(r)
    if pairs.__len__() == 1 and not s:
        print "one pair"
        s = True
        return 10000000000000 + 100000000000*pairs[0] + score(playerhand[0:5])
    else:
        return 0


def highcard(playerhand):
    return score(playerhand[0:5])


def score(values):
    sc = 0
    sc += values[4]*100000000
    sc += values[3]*1000000
    sc += values[2]*10000
    sc += values[1]*100
    sc += values[0]*1

    return sc


def determinewinner(playerhand):
    global s
    playerhands = gethand(playerhand)
    p1 = playerhands[0]
    p2 = playerhands[1]

    print p1, p2

    scorep1 = royalflush(p1) + straightflush(p1) + fourofakind(p1) + fullhouse(p1) + flush(p1) + straight(p1) + threeofakind(p1) + twopairs(p1) + onepair(p1)
    if scorep1 == 0:
        scorep1 = highcard(p1)

    s = False

    scorep2 = royalflush(p2) + straightflush(p2) + fourofakind(p2) + fullhouse(p2) + flush(p2) + straight(p2) + threeofakind(p2) + twopairs(p2) + onepair(p2)
    if scorep2 == 0:
        scorep2 = highcard(p2)

    s = False

    print scorep1, scorep2
    if scorep1 > scorep2:
        print "player 1 wins"
        return True
    else:
        print "player 2 wins"
        return False


totalscore = 0
f = open("test.txt", "r")
for line in f:
    if determinewinner(line.rstrip()):
        totalscore += 1

print "player 1 wins " + str(totalscore) + " times"

