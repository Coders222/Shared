message = input().lower()

alphabet = list("abcdefghijklmnopqrstuvwxyz")

vowels = list("aeiou")
consonants = list("bcdfghjklmnpqrstvwxyz")

message = list(message)
new = []


for i in message:
    if i in vowels:
        new.append(i)
        continue
    new.append(i)
    ind = alphabet.index(i)
    peeper = 0
    dolphin = 0
    heatcheck = False
    coldcheck = False
    for e in range(len(alphabet) - ind - 1):  # for the letters on the right
        if alphabet[ind + e + 1] in vowels:
            dolphin += alphabet.index(alphabet[ind + e + 1]) - ind
            break
        elif e == len(alphabet) - ind - 2:
            heatcheck = True

    for e in range(ind):
        if alphabet[ind - (e + 1)] in vowels:  # vowels on the left
            peeper += ind - alphabet.index(alphabet[ind - (e + 1)])
            break
        elif e == ind - 1:
            coldcheck = True

    bruh = True

    if heatcheck:
        new.append(alphabet[ind - peeper])
        bruh = False
    elif coldcheck:
        new.append(alphabet[ind + dolphin])
        bruh = False

    if bruh:
        if dolphin == 0:
            new.append(alphabet[ind - peeper])
        elif peeper == 0:
            new.append(alphabet[ind + dolphin])
        elif dolphin < peeper:
            new.append(alphabet[ind + dolphin])
        elif peeper < dolphin:
            new.append(alphabet[ind - peeper])
        else:
            new.append(alphabet[ind - peeper])

    notz = True

    if i == "z":
        new.append(i)
        notz = False
    if notz:
        for e in range(len(alphabet) - ind - 1):
            if alphabet[ind + e + 1] in consonants:
                new.append(alphabet[ind + e + 1])
                break

new = ''.join(new)
print(new)









