

while True:
    choice = int(input("Welcome to McDonalds, press 1 for drink, 2 for burgers, and 3 for sides "))
    if not 1 <= choice <= 3:  # catches invalid input
        print("Invalid Input")
    else:
        if choice == 1:
            a = int(input("1. Sprite, 2. Coke, 3. Mountain Dew, 4. Nestea, 5. Fanta 6. Exit. Type the number "))
            lst = ["Sprite", "Coke", "Mountain Dew", "Nestea", "Fanta"] # 2 lists, a takes the index of 2 lists to print
            v2 = list(i for i in range(1, 6))
            if not 1 <= a <= 5:  # checks for invalid input
                print("Invalid input")
            if a == 6:
                break
            print(lst[a - 1], "costs $" + str(v2[a - 1]) + " for a can")
        elif choice == 2:  # same as the top
            b = int(input("1. Big Mac 2. Quarter Pounder 3. Mc Fllet 4. Mc Chicken 5. Jr Burger 6. Exit. Type the number "))
            lst = ["Big Mac", "Quarter Pounder", "Mc Fillet", "Mc Chicken", "Jr Burger"]
            v2 = list(i for i in range(5, 10))
            if not 1 <= b <= 5:
                print("Invalid input")
            if b == 6:  # I added this, basically this checks if its 6
                break  # break means to break the loop, rn its while True which means forever because there is no
                       # counter argument, this tells it to break, otherwise it will continue because its infinite
            print(lst[b - 1], "costs $" + str(v2[b - 1]), "each")
        else:
            c = int(input("1. Fries 2. Onion Rings 3. Poutine 4. Caeser Salad 5. Hash Brown 6. Exit. Type the number "))
            lst = ["Fries", "Onion Rings", "Poutine", "Caeser Salad", "Hash Brown"]
            v2 = list(i for i in range(2, 7))
            if not 1 <= c <= 5:
                print("Invalid input")
            if c == 6:
                break
            print(lst[c - 1], "costs $" + str(v2[c - 1]), "each")



