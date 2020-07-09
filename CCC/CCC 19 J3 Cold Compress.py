msgs = int(input())

finale = []
for i in range(msgs):
    text = input()
    text = list(text)
    counts = []
    chars = []
    chars.append(text[0])
    final = []
    for e in range(len(text)-1):
        if text[e] != text[e+1]:
            chars.append(text[e+1])

    count = 1
    for chara in range(len(text) - 1):  # chara goes back to zero because you break
        if text[chara] != text[chara + 1]:  # if it is different
            counts.append(count)
            count = 0
        count += 1
    counts.append(count)

    for count, character in zip(counts, chars):
        final.append(str(count) + ' ' + str(character))
    finale.append(final)

for i in finale:
    print(*i)


# not perfect yet, last input from test case 1 does not match
# https://dmoj.ca/problem/ccc19j3
# 1 3 1 . 1 1 1 4 1 1 4 5
# counts: 1, 1, 1, 1, 1, 4


'''
    for char in chars:
        count = 1
        for chara in range(len(text)-1):  # chara goes back to zero because you break
            if text[chara] != text[chara + 1]: # if it is different
                counts.append(count)
                count = 0
            count += 1

'''
