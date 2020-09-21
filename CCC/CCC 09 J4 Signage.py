length = int(input())

words = ["WELCOME", "TO", "CCC", "GOOD", "LUCK", "TODAY"]

finished = False

final = []

bigman = 0
curiousgeorge = 0

cock = True

while cock:
    bruh = length
    zucc = []
    numnum = 0
    count = -1
    for i in range(len(words) - bigman):
        if len(words[i + bigman]) + count + 1 <= bruh:
            count += len(words[i + bigman]) + 1
            numnum += 1
    bigman += numnum
    for i in range(numnum):
        if i == numnum - 1:
            zucc.append(words[i + curiousgeorge])
        else:
            zucc.append(words[i + curiousgeorge] + ".")
    curiousgeorge += numnum
    necktwist360 = ''.join(zucc)
    ind = 1
    droppa = 0
    for i in range(bruh - len(necktwist360)):
        if len(zucc) == 1:
            for m in range(bruh - len(necktwist360)):
                zucc.append(".")
            break
        if len(zucc) == 2:
            for m in range(bruh - len(necktwist360)):
                zucc.insert(1, ".")
            break
        else:
            zucc.insert(ind, ".")
            ind += 2
            if ind == numnum * 2 - 1:
                droppa += 1
                ind = 1 + droppa
    if "TODAY" in zucc:
        cock = False
    zucc = ''.join(zucc)
    final.append(zucc)

# dots must be submitted in a way where the last words
# must have dots behind them
for i in final:
    print(i)


# insert "." before each word starting from last to first

''' 
WELCOME.TO.CCC
GOOD...LUCK...
TODAY.........

+ droppa ^^ wrong

WELCOME.TO.CCC
GOOD......LUCK
TODAY.........





'''