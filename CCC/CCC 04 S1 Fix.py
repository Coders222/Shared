collections = int(input())

answers = []

for i in range(collections):
    leave = False
    george = False
    matrix = [input(), input(), input()]
    for e in range(len(matrix)):
        for x in range(len(matrix) - 1):
            kfc = ''.join(list(matrix[x + 1])[:len(matrix[0])])
            popeyes = ''.join(list(matrix[x + 1])[-len(matrix[0]):])
            if len(matrix[0]) > len(kfc):
                continue
            if matrix[0] == kfc:
                answers.append("No")
                george = True
                break
            if matrix[0] == popeyes:
                answers.append("No")
                george = True
                break
        if george:
            leave = True
            break
        matrix.append(matrix[0])
        del matrix[0]
    if leave:
        continue
    else:
        answers.append("Yes")
    


for i in answers:
    print(i)


'''

2
abba
aab
bab
a
ab
aa

'''
