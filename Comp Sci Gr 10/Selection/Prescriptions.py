# This program takes in weight and prints out how many mg of dosage you need

def filterr(a):
    if a < 0 or a == 0:
        print("Invalid input")
        return True
    else:
        return False
# function to check if input is valid
# ok now i think an if statement wouldve been better
# since its only one input

dose = 0
bruh = True
while bruh:
    weight = float(input("What is your weight in kg? "))
    yes = filterr(weight)
    if yes:  # if the weight is below or equal to 0, it will ask the question again
        print("Please enter a valid weight!")
        continue
    else:
        bruh = False
    if weight < 16:  # Conditions to check how much dosage you need
        dose = weight * 0.6
    elif weight < 25:
        dose = weight * 0.75
    elif weight < 40:
        dose = weight * 0.83
    elif weight < 65:
        dose = weight * 1.2
    else:
        dose = weight * 1.3

print("You need a dose of " + str(round(dose, 2)) + "mg")

