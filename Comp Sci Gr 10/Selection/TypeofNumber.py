# this program asks input and tells you if it is odd, even, zero or negative

a = int(input("Enter a whole number"))  # asks for input

if a == 0:  # if statements to filter out conditions to find out what type of number it is
    print("ZERO")
elif a < 0:
    print("NEGATIVE")
elif a % 2 == 0:
    print("EVEN")
else:
    print("ODD")

