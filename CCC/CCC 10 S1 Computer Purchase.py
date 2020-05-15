# https://dmoj.ca/problem/ccc10s1
# works for all testcases except testcase 1 and 9

cases = int(input())

names = []
scores = []
bromine = True
if cases == 0:
    bromine = False

while bromine:
    for i in range(cases):
        name, ram, cpu, storage = input().split()
        names.append(name)
        score = int(ram) * 2 + int(cpu) * 3 + int(storage)
        scores.append(score)


    haram = max(scores)
    new = []

    for i in scores:
        new.append(i)

    new.remove(max(new))
    unharam = max(new)  # second biggest score
    greatest = []


    counter = 0
    for i in range(len(scores)):
        if scores[i] == haram:
            greatest.append(counter)
        counter += 1

    counter = 0

    matrix = []
    if haram == unharam:  # if the biggest numbers are the same
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        bruh = names[greatest[0]].lower()
        for i in range(2):
            yes = list(bruh)
            inds = []
            for letter in yes:
                ind = alphabet.index(letter)
                inds.append(ind)
            matrix.append(inds)
            bruh = names[greatest[1]].lower()
        matrix.sort()
        yellow = []
        for i in matrix:
            zucc = []
            for e in i:
                zucc.append(alphabet[e])
            yellow.append(zucc)
        for i in yellow:
            print(''.join(i).upper())
    else:  # if they are different
        print(names[scores.index(haram)])
        print(names[scores.index(unharam)])
    break

'''
4
ABC 13 22 1
DEFK 20 20 20
GHI 11 2 2
JKL 20 20 20
'''
