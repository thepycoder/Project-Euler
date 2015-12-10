eenheden = {"0": "", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven",
            "8": "eight", "9": "nine"}
specials = {"10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen", "15": "fifteen",
            "16": "sixteen", "17": "seventeen", "18": "eighteen", "19": "nineteen"}
tienden = {"0": "", "1": "ten", "2": "twenty", "3": "thirty", "4": "forty", "5": "fifty", "6": "sixty", "7": "seventy",
           "8": "eighty", "9": "ninety"}

sum = "onethousand".__len__()

for i in range(1, 1000):  # cycle from 1 to and incl 1000
    number = str(i)
    text = ""

    if number.__len__() > 0:
        if 20 > int(number[-2:]) > 9:
            text = specials.get(number[-2:]) + text
        else:
            text = eenheden.get(number[-1:]) + text
            if number.__len__() > 1:
                text = tienden.get(number[-2:-1]) + text
        if number.__len__() > 2:
            temp = eenheden.get(number[:-2]) + "hundred"
            if number[1:] != "00":
                temp += "and"
            text = temp + text

    print text
    sum += text.__len__()

print sum
