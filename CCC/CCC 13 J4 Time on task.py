time = int(input())

chores = int(input())


matrix = []

for i in range(chores):
    chore = int(input())
    matrix.append(chore)


timespent = 0
count = 0


wtf = 0

codeine = True
while codeine:
    bool = True
    timespent += min(matrix)
    if timespent > time:
        codeine = False
        continue
    while bool:
        wtf = min(matrix)
        count += 1
        bool = False



    matrix.remove(wtf)
    bool = True

print(count)
# matrix.remove(min(matix))