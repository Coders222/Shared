
# 1

"""
sum = 0
for i in range(10):
    word = input()
    sum += len(word)

print("The average word length is " + str(num / 10))
"""

# 2


"""word = input("Enter a word: ")
while word != "wow":
    if len(word) == 1:
        print(word, "has only 1 character.")
        word = input("Enter a word: ")
        continue
    print("Output: " + word[::len(word) - 1] + ", " + word[1:-1:])
    word = input("Enter word: ")"""

# 3

"""word = input("Enter word: ")
while word != "wow":
    if len(word) == 1:
        print(word, "only has 1 character")
        word = input("Enter a word: ")
    elif len(word) % 2 == 0:
        print(word[::2])
        word = input("Enter a word: ")
    else:
        print(word[1::2])
        word = input("Enter a word: ")"""

# 4

"""word = input("Enter a word: ")
while word != "wow":
    middle = len(word) // 2
    if len(word) == 1:
        print(word, "has only 1 character")
        word = input("Enter a word: ")
    elif len(word) % 2 == 0:
        print("The middle letters are", word[middle - 1:middle + 1])  # start and STOP at but not including
        word = input("Enter a word: ")
    else:
        print("The middle letter is", word[middle])
        word = input("Enter a word: ")
"""
# 5

"""word = input("Enter a word: ")
while word != "wow":
    if len(word) == 1:
        print(word, "only has 1 character.")
        word = input("Enter a word: ")
        continue
    print("Output: " + "-".join(list(word)))
    word = input("Enter a word: ")"""

# 6

word = input("Enter a word: ")
while word != "wow":
    if len(word) == 1:
        print(word, "has only 1 character")
        word = input("Enter a word: ")
        continue
    elif word[::-1] == word:
        print("This is a palindrome.")
        word = input("Enter a word: ")
        continue
    print("The reverse word is " + word[::-1])
    word = input("Enter a word: ")




