keypad = [
    list("ABCDEF"),
    list("GHIJKL"),
    list("MNOPQR"),
    list("STUVWX"),
    ['Y', 'Z', "SPACE", "-", ".", "ENTER"]
]

ramadan = input()
ramadan = list(ramadan.upper())

for i in range(len(ramadan)):
    if ramadan[i] == " ":
        ramadan[i] = "SPACE"

ramadan.append("ENTER")

matrix = []

for i in ramadan:
    necktwist360 = []
    listed = 0
    for list in keypad:
        coord = 0
        for element in list:
            if i == element:
                necktwist360.append(listed)
                necktwist360.append(coord)
            coord += 1
        listed += 1
    matrix.append(necktwist360)


count = 0
shit = [0, 0]

for i in matrix:  # each list in matrix
    for e in range(len(i)):
        count += abs(i[e] - shit[e])  # abs converts any negative number to positive
    shit = i



print(count)




