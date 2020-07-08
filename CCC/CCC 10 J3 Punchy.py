import math

spain = True

a = 0
b = 0

final = []
while spain:
    command = input().split()
    if command == ["7"]:
        spain = False
    if "1" in command:
        if command[1] == 'A':
            a = int(command[2])
        if command[1] == 'B':
            b = int(command[2])
    elif "2" in command:
        if command[1] == "A":
            final.append(a)
        if command[1] == "B":
            final.append(b)
    elif "3" in command:
        if command[1] == "A" and command[2] == "A":
            a = a + a
        if command[1] == "B" and command[2] == "B":
            b = b + b
        sum = a + b
        if command[1] == "A":
            a = sum
        if command[1] == "B":
            b = sum
    elif "4" in command:
        if command[1] == "A" and command[2] == "A":
            a = a * a
        if command[1] == "B" and command[2] == "B":
            b = b * b
        sum = a * b
        if command[1] == "A":
            a = sum
        if command[1] == "B":
            b = sum
    elif "5" in command:
        if command[1] == "A" and command[2] == "A":
            a = a - a
        if command[1] == "B" and command[2] == "B":
            b = b - b
        sum = a - b
        if command[1] == "A":
            a = sum
        if command[1] == "B":
            b = b - a
    elif "6" in command:
        if command[1] == "A" and command[2] == "A":
            a = a / a
        if command[1] == "B" and command[2] == "B":
            b = b / b
        sum = math.floor(a / b)
        if command[1] == "A":
            a = sum
        if command[1] == "B":
            b = math.floor(b / a)

for i in final:
    print(i)
''' 

1 X n means set the variable X to the integer value n;
2 X means output the value of variable X to the screen;
3 X Y means calculate X+Y and store the value in variable X;
4 X Y means calculate X×Y and store the value in variable X;
5 X Y means calculate X−Y and store the value in variable X;
6 X Y means calculate the quotient of XY and store the value in variable X as an integer, discarding the remainder.
7 means stop execution of this program.

'''
