
option = int(input("Choose an option: 1, 2, 3, 4: "))
while not 1 <= option <= 4:
    print("Sorry invalid input, try again: ")
    option = int(input("Choose an option: 1, 2, 3, 4: "))

while option != 4:
    if option == 4:
        print("Ok bye")
        break

    string = input("Enter a string: ")
    substring = input("Enter a substring: ")
    substring.lower()
    if option == 1:
        count = 0
        string.lower()
        if len(substring) == 1:
            count = 0
            for i in range(len(string)):
                if string[i] == substring:
                    count += 1
        else:
            index = string.find(substring.lower())
            while index != -1:
                string = string[:index] + string[index + len(substring):]
                index = string.find(substring.lower())
                count += 1
        print(count)

    elif option == 2:
        index = string.lower().find(substring.lower())
        while index != -1:
            string = string[:index] + string[index + len(substring):]
            index = string.lower().find(substring.lower())
        print(string)

    elif option == 3:
        replacement = input("What is the replacement letter? ")
        if substring[0] == string[0]:
            x = 0
            y = 0
            index = string.lower()[x:].find(substring.lower())
            while index != -1:
                string = string[:index + y] + replacement + string[index + len(substring):]
                x += len(string[index + len(replacement):])
                y += len(replacement) + 1
                index = string.lower()[x:].find(substring.lower())
        else:
            index = string.lower().find(substring.lower())
            while index != -1:
                string = string[:index] + replacement + string[index + len(substring):]
                index = string.lower().find(substring.lower())
        print(string)

    else:
        print("Invalid input please try again: ")

    option = int(input("Choose an option: 1, 2, 3, 4: "))
    while not 1 <= option <= 4:
        print("Sorry invalid input, try again: ")
        option = int(input("Choose an option: 1, 2, 3, 4: "))

print("Ok bye")