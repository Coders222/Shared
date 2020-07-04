flightreacts = int(input())

friends = [i for i in range(flightreacts + 1)]


rounds = int(input())

matrix = []
for i in range(rounds):
    index = int(input())
    matrix.append(index)

ind = 0
nese = [friends]

for i in matrix:
    bruh = []
    bruh.append(0)
    for m in range(len(nese[ind]) - 1):
        if nese[ind].index(nese[ind][m + 1]) % i != 0:
            bruh.append(nese[ind][m + 1])
    nese.append(bruh)
    ind += 1

nese[-1].remove(0)

# scott
for i in nese[-1]:
    print(i)

