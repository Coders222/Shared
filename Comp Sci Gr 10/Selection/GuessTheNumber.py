# this program is a guessing game that generates a number 1-50
# and has the user guess, with each incorrect guess hinting towards the answer
# by saying too high or too low

from random import randint

randnumber = randint(1, 50)

guessing = True
while guessing:  # loops back so the user can keep guessing
    guess = int(input("Guess the number from 1 - 50 "))
    if not 1 <= guess <= 50:  # check if number is valid
        print("Please enter a number 1 - 50! ")
        continue
    if guess == randnumber:  # check if guess is the number
        print("You got the number!")
        guessing = False
    else:  # checks if the number is too low or too high and gives user the hint
        if guess < randnumber:
            print("Too low!")
        else:
            print("Too High!")