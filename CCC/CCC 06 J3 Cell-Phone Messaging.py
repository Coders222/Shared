string = input()

lst = []
lst.append(string)

counts = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 1,
    "e": 2,
    "f": 3,
    "g": 1,
    "h": 2,
    "i": 3,
    "j": 1,
    "k": 2,
    "l": 3,
    "m": 1,
    "n": 2,
    "o": 3,
    "p": 1,
    "q": 2,
    "r": 3,
    "s": 4,
    "t": 1,
    "u": 2,
    "v": 3,
    "w": 1,
    "x": 2,
    "y": 3,
    "z": 4
}
while string != "halt":
    string = input()
    lst.append(string)

final = []
lst.remove("halt")
matrix = []

for i in lst:
    new = []
    i = list(i)
    for e in i:
        if e in list("abc"):
            new.append("2" * counts.get(e))
        if e in list("def"):
            new.append("3" * counts.get(e))
        if e in list("ghi"):
            new.append("4" * counts.get(e))
        if e in list("jkl"):
            new.append("5" * counts.get(e))
        if e in list("mno"):
            new.append("6" * counts.get(e))
        if e in list("pqrs"):
            new.append("7" * counts.get(e))
        if e in list("tuv"):
            new.append("8" * counts.get(e))
        if e in list("wxyz"):
            new.append("9" * counts.get(e))
    globalelite = []
    for n in new:
        globalelite.append(n)
    for e in range(len(new) - 1):
        bruh = list(new[e])
        if bruh[0] in list(new[e + 1]):
            globalelite.insert(e+1, "filler")
    matrix.append(globalelite)
    addy = globalelite.count("filler")
    blacktarheroin = []
    for e in globalelite:
        if e != "filler":
            blacktarheroin.append(e)
    allah = ''.join(blacktarheroin)
    final.append(len(allah) + (addy * 2))

for i in final:
    print(i)

