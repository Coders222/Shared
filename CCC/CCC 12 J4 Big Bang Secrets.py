num = int(input())
message = input().lower()

alphabet = list("abcdefghijklmnopqrstuvwxyz")

final = []

count = 1

shift = 0
ind = 0
# burger
for i in message:
    shift = (count * 3) + num
    ind = alphabet.index(i)
    ind = (ind + 24 - shift + 2) % 26
    final.append(alphabet[ind].upper())
    count += 1


print(''.join(final))
# reconvert message into uppercase
