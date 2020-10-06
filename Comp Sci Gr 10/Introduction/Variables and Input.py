# September 25th Orion Chen

# This program asks user for input on their favourite subject and name to print

"""
name = input("What is your name? ")  # asks for name
subject = input("What is your favourite subject? ")  # asks for favourite subject
print(a, b) # prints both on the same line
"""


# This program asks for your first name and last name and greets you with your input
"""
firstname = input("What is your name? ")  # asks for first name
lastname = input("What is your last name? ")  # asks for last name
print("Hello " + lastname + ", " + firstname + ". How are you?")  # prints both vars in one sentence
"""

# This program asks for your full address and identification to print on one single line neatly with commas
# You can prompt user for input using variables instead but seems overcomplicated / unnecessary

"""
matrix = [input() for i in range(5)]  # asks for input since there 5 items, it takes in 5 inputs
print(*matrix)  # prints every item in the list with spaces
"""

# this program takes 2 integers and outputs the sum, difference, product and quotient

"""
num1 = float(input("Enter the first number: "))  # takes in float, decimals can be added
num2 = float(input("Enter the second number: "))  # ^ takes input for second number
print(str(num1) + " + " + str(num2) + " = " + str(num1 + num2))  # prints sum
print(str(num1) + " - " + str(num2) + " = " + str(num1 - num2))  # prints difference
print(str(num1) + " * " + str(num2) + " = " + str(num1 * num2))  # prints product
print(str(num1) + " / " + str(num2) + " = " + str(num1 / num2))  # prints quotient
"""

# this program converts inches to centimeters (for this case it is used to measure a door)

"""
inches = float(input("What is the length of the door in inches? "))
print("The measurement of " + str(inches) + " inches to cm is " + str(inches * 2.54) + " cm")
"""

# this program takes in your subject, test mark and the marks that it was out of, then
# then outputs all the inputs in order, with a percentage mark on the last line rounded to 1 decimal

"""
subject = input("Subject? ")
mark = int(input("Mark? "))
total = int(input("Test out of what? "))

print("Subject: " + subject)
print("Your test marks: " + str(total) + "\nTotal number of marks on the test: " + str(mark))
print("You got a " + str(round(mark / total * 100, 2)) + "%")
"""

# this program calculates your speed km / hour, using 4 inputs, start and end hours and minutes.
#  it outputs your speed after, cannot "prompt" because of list comprehension, can be swapped with vars
# to prompt

"""
start = [int(input()) for i in range(2)]
end = [int(input()) for e in range(2)]
distance = int(input())

newStart = start[0] * 60 + start[1]
newEnd = end[0] * 60 + end[1]
difference = newEnd - newStart

print("The speed is " + str(round(distance / (difference / 60), 1)) + " km per hour")
"""

# This program calculates a baseball players batting and slugging average

"""
bat = 0
singles = 0
doubles = 0
triples = 0
homeRuns = 0


yes = True
while yes:
    try:
        bat = int(input("How many times did you bat? "))
        singles = int(input("How many singles did you hit? "))
        doubles = int(input("How many doubles did you hit? "))
        triples = int(input("How many triples did you hit? "))
        homeRuns = int(input("How many home runs did you hit? "))
        hits = singles + doubles + triples + homeRuns
        if hits > bat:
            print("You hit more than you actually batted?? Redo")
            continue
        elif min(bat, singles, doubles, triples, homeRuns) < 0:
            print("NO NEGATIVE NUMBERS")
            continue
        yes = False
    except ValueError:
        print("Type a valid number!")

hits = singles + doubles + triples + homeRuns
slug = singles + doubles * 2 + triples * 3 + homeRuns * 4

print("Your batting average is: " + str(round(hits / bat, 2)))
print("Your slugging average is: " + str(round(slug / bat, 2)))
"""

