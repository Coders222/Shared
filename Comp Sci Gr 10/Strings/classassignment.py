

"""sentence = input()
while sentence != "done" and sentence != "DONE":
    ind1 = sentence.find(" ")
    ind2 = sentence.rfind(" ")
    sentence = list(sentence)
    if ind1 == -1:
        print(''.join(sentence))

    elif ind1 == ind2:
        sentence.insert(ind1, " ")
        print(''.join(sentence))

    else:
        sentence.insert(ind1, " ")
        sentence.insert(ind2 + 1, " ")
        print("".join(sentence))
    sentence = input()"""

# 2

sentence = input("Enter a sentence: ")
while sentence.lower() == "done":
    while sentence[0] == " ":
        sentence = sentence[1:]

    firstSpace = sentence.find(" ")

    if firstSpace == -1:
        print(sentence)
    else:

        sentence = sentence[0:firstSpace] + " " + sentence[firstSpace:]
        lastSpace = sentence.rfind(" ")
        if lastSpace + 1 != firstSpace:
            sentence = sentence[:lastSpace] + " " + sentence[lastSpace:]
        print(sentence)

    sentence = input("Enter a sentence: ")

