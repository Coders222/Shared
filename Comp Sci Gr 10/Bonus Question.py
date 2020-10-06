# this program takes in the year of input and tells you when is easter

year = input("What is the year? ")

year = int(year[-2:])  # takes last 2 digits of the year and parses into integer
x = year // 19
y = year // 4

r = (19 * year - x) % 30
s = (6 * year - y - r) % 7

# formulas ^^^^

# conditions to check when is Easter
if r == 28 and r == s + 6:
    print("Easter is on the 18th of April")
elif year == 57:
    print("Easter is on the 21st of April")
elif r + s <= 9:
    print("Easter is on day " + str(r + s + 22), "of March")
else:
    print("Easter is on day " + str(r + s - 9), "of April")











