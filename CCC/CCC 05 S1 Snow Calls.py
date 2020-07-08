cases = int(input())

bruh = {
    "A": "2",
    "B": "2",
    "C": "2",
    "D": "3",
    "E": "3",
    "F": "3",
    "G": "4",
    "H": "4",
    "I": "4",
    "J": "5",
    "K": "5",
    "L": "5",
    "M": "6",
    "N": "6",
    "O": "6",
    "P": "7",
    "Q": "7",
    "R": "7",
    "S": "7",
    "T": "8",
    "U": "8",
    "V": "8",
    "W": "9",
    "X": "9",
    "Y": "9",
    "Z": "9"

}
matrix = []
for i in range(cases):
    nums = input()
    nums = list(nums)
    new = []
    for e in nums:
        if e != "-":
            new.append(e)
    cock = []
    for e in new:
        cock.append(bruh.get(e, e))
    final = []
    for p in range(10):
        final.append(cock[p])
    final.insert(3, "-")
    final.insert(7, "-")
    final = "".join(final)
    matrix.append(final)

for i in matrix:
    print(i)
