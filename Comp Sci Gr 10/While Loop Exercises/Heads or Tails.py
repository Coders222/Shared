from random import randint

guess = input("Guess the flip, heads = 1 tails = 0. Input heads or tails ")
yes = randint(0, 1)
if yes == 0:
    yes = "heads"
else:
    yes = "tails"

while guess != yes:
    yes = randint(0, 1)
    if yes == 0:
        yes = "heads"
    else:
        yes = "tails"
    guess = input("Wrong try again ")

print("You got the flip!")