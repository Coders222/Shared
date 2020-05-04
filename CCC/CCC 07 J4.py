message = input()
test = input()
message = message.lower()
test = test.lower()

# what if there are 2 "K"s

correct = True

new1 = []
new2 = []

for i in message:
    if i != " ":
        new1.append(i)

for i in test:
    if i != " ":
        new2.append(i)

alphabet = list("abcdefghijklmnopqrstuvwxyz")

for i in alphabet:
    if new1.count(i) == new2.count(i):
        continue
    else:
        correct = False
        break

if correct:
    print("Is an anagram.")
else:
    print("Is not an anagram.")

