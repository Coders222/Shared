# This program is a game of losing and gaining money. Kinda like gambling
# Everytime you gamble, you must pay a fixed fee and you have 3 options
# that either adds money into your funds, lose money, or other punishments
# The game ends when you die, run out of money, or want to walk away with your bank

from random import randint  # importing modules
bank = 3000
increment = 0  # for the diamond mine losing extra 200

print("Hi there, you have $3000 to spend, with $500 spent everytime you play.")  # introduces you to the game

# bools / vars
rent = False
died = False
loaned = False
interest = 0
counter = 0

while bank >= 500 + increment:  # increment is set to 0 when rent is increased, it will have a fixed value of 200 ($700)
    bank -= 500 + increment  # subtract each time you play

    if counter < 5 and loaned:  # weekly payment, 5 * 500 = 2500 (the amount due if you get a loan of $1500)
        bank -= 500  # loaned is a bool so it won't take 500 each time if you did not get a loan
        counter += 1

    if not loaned:  # gets rid of the loan option when you choose it (one time thing)
        site = int(input("You have four options, Lucky Clover, Diamond Mine, Hearts are Wild, or"
                         " borrow $1500. Please type the number: "))
        if not 1 <= site <= 4:  # checks for invalid input
            print("Invalid input!")
            bank += 500 + increment  # adds your funds back in because of invalid input (subtracts this at the start)
            continue  # restarts the loop
    else:  # default prompt after you request a loan
        site = int(input("You have three options, Lucky Clover, Diamond Mine and Hearts are Wild. Please type the "
                         "number: "))
        if not 1 <= site <= 3:  # checks for invalid input
            print("Invalid input!")
            bank += 500 + increment
            continue  # restarts the loop

    random = randint(1, 10)  # random int

    if site == 1:  # site 1 options
        if random == 1:
            print("You got a payload of $1000!")
            bank += 1000
        elif 2 <= random <= 4:  # if random == 2,3,4 (30% chance)
            print("You got a payload of $500!")
            bank += 500
        else:
            print("You've encounter a series of thieves!")
            thief = randint(1, 4)
            if thief == 1:  # all of the below are factors of 10 (5, 2, 10)
                print("A thief stole a fifth of your money!")
                bank *= 0.8
            elif thief == 1:
                print("A thief stole half of your money!")
                bank *= 0.5
            elif thief == 1:
                print("A thief stole a tenth of your money!")
                bank *= 0.9
            else:
                print("A thief stole all your money!")
                bank = 0
                break

    elif site == 2:  # site 2 options
        if random == 1 or random == 2:
            print("You got a payload of $800!")
            bank += 800
        elif 3 <= random <= 6:  # 3,4,5,6 40% chance
            print("You got a payload of $400!")
            bank += 400
        else:
            if not rent:  # bool to not repeat these steps again, rather to go to the else statement
                print("Your rent increased to $700, losing you $200 this week")
                increment = 200
                bank -= 200
                rent = True
            else:
                print("Your rent already has been increased!")

    elif site == 3:  # site 3 options
        if random == 1:
            print("You got a payload of $8000!")
            bank += 8000
        elif 2 <= random <= 5:  # same logic
            print("You got a payload of $300!")
            bank += 300
        else:
            print("You died!")
            died = True  # bool for the bottom
            break
    else:
        print("You get a loan of $1500, but you need to pay 500 each week to $2500 starting next week")
        bank += 1500
        interest = 500
        loaned = True  # bool to True so it won't ask if they want another loan

    print("You have $" + str(bank))  # shows balance after transaction
    again = input("Would you like to play again? yes/no: ")

    while again != "yes" and again != "no":  # checks for invalid input
        print("Invalid input!")
        again = input("Would you like to play again? yes/no: ")

    if again == "no":  # quits program
        print("Ok bye! you left with a total of $" + str(bank))
        died = True
        break

if not died:  # bool to check if they died / quit so it wont print the default statement
    print("You have $" + str(bank) if bank != 0 else "")  # default statement is if u run out of money
    print("You ran out of money!")




