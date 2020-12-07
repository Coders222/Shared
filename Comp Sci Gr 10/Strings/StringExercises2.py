# This program gives you a series of options to modify a inputted string with a inputted substring.
# The first option counts how many instances of a inputted substring, the second option removes every instance
# of a certain substring, and the last option replaces each instance of a inputted substring with an inputted
# substitute

print("Please choose 1 for counting a substring\n2 for removing a substring\n3 for substituting a substring")
option = int(input("Choose an option: 1, 2, 3, 4: "))


# invalid input catch
while not 1 <= option <= 4:  # only works for numbers entered
    print("Sorry invalid input, try again: ")
    print("Please choose 1 for counting a substring \n 2 for removing a substring \n 3 for substituting a substring")
    option = int(input("Choose an option: 1, 2, 3, 4: "))

while option != 4:
    string = input("Enter a string: ")
    substring = input("Enter a substring: ")

    if len(substring) > len(string):
        print("Please enter a valid substring")
        continue

    if option == 1:
        count = 0
        index = string.lower().find(substring.lower())
        while index != -1:
            string = string[:index] + string[index + len(substring):]  # removes the substring from the string
            index = string.lower().find(substring.lower())  # looks for the substring until there isn't one anymore
            count += 1
        print(count)

    elif option == 2:
        index = string.lower().find(substring.lower())
        while index != -1:
            string = string[:index] + string[index + len(substring):]  # removes substring from string
            index = string.lower().find(substring.lower())  # keeps looking for substring until there isn't one anymore
        print(string)

    elif option == 3:
        replacement = input("What is the replacement letter? ")
        x = 0
        if substring[0].lower() == replacement[0].lower():
            substringIndex = string.lower()[x:].find(substring.lower())
            index = substringIndex + x
            # the [x:] part helps me skips some parts of the
            # string because the find function will find the earliest instance of the substring and the replacement is
            # equal to it. Without it, the find function will find the same index over and over again ("Aa" for the
            # test case on the pdf)
            while substringIndex != -1:
                string = string[:index] + replacement + string[index + len(substring):]
                # replaces earliest instance of substring with the replacement value
                x = len(string[:index + len(replacement)])
                # the increment to skip over the characters including the replacement from this loop and back
                substringIndex = string.lower()[x:].find(substring.lower())
                # had to create a substringIndex var because the index would always be over -1 since x is added to it
                # after, therefore the while loop condition would be useless and just act as a while true
                index = substringIndex + x
                # finds the next substring that skips the part where it ends with the replacement added
                # then adds back the length of the part skipped so its index correlates to its index in the string
                if x == len(string):
                    break
                # eventually x will become the length of the new string because x will equal to
                # len(string[:the last found instance of the substring's index + len(replacement))
                # this will break out of the while statement, the while index != 1 statement doesn't really matter
                # and acts as a while True. This is difficult to avoid since the loop would still loop over
                # since x will eventually equal to the len of the string, the find function would be stuck looking in
                # string[len(str):] and keeps finding the last character which starts with the same char as replacement

        else:
            index = string.lower().find(substring.lower())
            while index != -1:
                string = string[:index] + replacement + string[index + len(substring):]
                index = string.lower().find(substring.lower())
        print(string)

    else:
        print("Invalid input please try again: ")

    option = int(input("Choose an option: 1, 2, 3, 4: "))

    # invalid input catch again
    while not 1 <= option <= 4:
        print("Sorry invalid input, try again: ")
        option = int(input("Choose an option: 1, 2, 3, 4: "))

# closing remarks
print("Ok bye")

