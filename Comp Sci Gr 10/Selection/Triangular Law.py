# this program calculates if a triangle is possible with 3 given lengths


a = int(input())
b = int(input())
c = int(input())

lst = [a, b, c]  # checks any sides are invalid
if min(lst) == 0 or min(lst) < 0:
    print("Invalid input")


# maybe the third condition is not needed but i really don't want to do math
# checks if 2 sides are bigger than the third
if a + b > c and b + c > a and c + a > b:
    print("Yes, this is a possible triangle")
else:
    print("No this is not a possible triangle ")

