bruh = input().split()

weeks = ['Sun', 'Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat']

counter = 1

yoink = True
matrix = []

watchdogs2 = True
farcry6 = True
wasd = True

while yoink:
    new = []
    cuck = False
    if watchdogs2:
        for i in range(int(bruh[0]) * 4 - 2):
            new.append(" ")

        watchdogs2 = False
    if farcry6:
        for i in range(7 - int(bruh[0]) + 1):
            new.append(str(counter))
            new.append(" ")
            new.append(" ")
            new.append(" ")
            counter += 1
        farcry6 = False

    if wasd:
        del(new[-3:-1])
        new.pop()
        matrix.append(''.join(new))
        wasd = False
        continue

    if counter + 1 >= 10:
        new.append(" ")
    else:
        new.append(" ")
        new.append(" ")

    bounce = 0
    for i in range(7):
        if counter > int(bruh[1]):
            yoink = False
            cuck = True
            break
        if counter + 1 >= 10:
            new.append(str(counter))
            new.append(" ")
            new.append(" ")
            bounce += 1

        else:
            new.append(str(counter))
            new.append(" ")
            new.append(" ")
            new.append(" ")
        counter += 1

    if counter >= 10:
        del(new[-2:-1])
        new.pop()

    else:
        del(new[-3:-1])
        new.pop()
    if cuck:
        for i in range(27 - (bounce * 4 - 1)):
            new.append(" ")
    yep = ''.join(new)
    matrix.append(yep)

print(*weeks)
for i in matrix:
    print(i)
print()

print(matrix)