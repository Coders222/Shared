cards = list(input())


clubs = []
diamonds = []
hearts = []
spades = []
classes = ["C", "H", "D", "S"]
for i in range(len(cards)):
    if cards[i] == "C":
        for e in range(len(cards) - i - 1):
            if cards[e + i + 1] in classes:
                break
            else:
                clubs.append(cards[e + i + 1])
                clubs.append(" ")
        if len(clubs) >= 2:
            del clubs[-1]

    if cards[i] == "D":
        for e in range(len(cards) - i - 1):
            if cards[e + i + 1] in classes:
                break
            else:
                diamonds.append(cards[e + i + 1])
                diamonds.append(" ")
        if len(diamonds) >= 2:
            del diamonds[-1]
    if cards[i] == "H":
        for e in range(len(cards) - i - 1):
            if cards[e + i + 1] in classes:
                break
            else:
                hearts.append(cards[e + i + 1])
                hearts.append(" ")
        if len(hearts) >= 2:
            del hearts[-1]
    if cards[i] == "S":
        for e in range(len(cards) - i - 1):
            if cards[e + i + 1] in classes:
                break
            else:
                spades.append(cards[e + i + 1])
                spades.append(" ")
        if len(spades) >= 2:
            del spades[-1]

matrix = [clubs, diamonds, hearts, spades]
pointer = []

for i in matrix:
    points = 0
    bruh = [i for i in i]
    new = []
    for e in bruh:
        if e != " ":
            new.append(e)
    if len(new) == 0:
        points += 3
    elif len(new) == 1:
        points += 2
    elif len(new) == 2:
        points += 1
    for e in i:
        if e == "A":
            points += 4
        elif e == "K":
            points += 3
        elif e == "Q":
            points += 2
        elif e == "J":
            points += 1
    pointer.append(points)


print("Cards Dealt Points")
print("Clubs " + ''.join(clubs) + " " + str(pointer[0]))
print("Diamonds " + ''.join(diamonds) + " " + str(pointer[1]))
print("Hearts " + ''.join(hearts) + " " + str(pointer[2]))
print("Spades " + ''.join(spades) + " " + str(pointer[3]))
print("Total " + str(sum(pointer)))
print(bruh)



