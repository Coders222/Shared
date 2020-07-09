quarters = int(input())
plays1 = int(input())
plays2 = int(input())
plays3 = int(input())

counter = 0

while quarters != 0:
    plays1 += 1
    quarters -= 1
    counter += 1
    if plays1 % 35 == 0:
        quarters += 30
    if quarters == 0:
        break
    plays2 += 1
    quarters -= 1
    counter += 1
    if plays2 % 100 == 0:
        quarters += 60
    if quarters == 0:
        break
    plays3 += 1
    quarters -= 1
    counter += 1
    if plays3 % 10 == 0:
        quarters += 9


print("Martha plays " + str(counter) + " times before going broke.")

