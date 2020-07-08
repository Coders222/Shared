import itertools

key = input()
msg = input()

alphabet = list("abcdefghijklmnopqrstuvwxyz")

key = key.lower()
msg = msg.lower()
bruh = []
for i in msg:
    if i in alphabet:
        bruh.append(i)

# output has to be in all caps, no spaces or symbols

matrix = []

count = 0
for i in range(len(key)):
    lst = [bruh[count::len(key)]]
    count += 1
    matrix.append(*lst)

new = []
counter = 0
for i in matrix:  # for list in matrix
    lst = []
    letter = alphabet.index(key[counter])
    for e in i:  # for each element in the list
        ind = alphabet.index(e)
        lst.append(alphabet[(ind + letter) % len(alphabet)])
    new.append(lst)
    counter += 1

# x = itertools.zip_longest(i for i in matrix)
for e in new:
    for i in range(len(new[0]) - len(e)):
        e.insert(len(e) + 1, "")


final = []

for i in new:
    for e in i:
        final.append("rona")


counts = 0
for i in new:
    another = 0
    for letter in i:
        final[counts + another] = letter
        another += len(key)
    counts += 1


final = ''.join(final).upper()
print(final)
