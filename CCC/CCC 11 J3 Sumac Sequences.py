num1 = int(input())
num2 = int(input())

if num1 - num2 < 0:
    print(0)
counter = 0
array = [num1, num2]
bruh = 2

while array[0 + counter] - array[1 + counter] >= 0:
    num1 = array[1 + counter]
    num2 = array[0 + counter] - array[1 + counter]  # num1 - num2
    if num1 == 0 and num2 == 0:
        break
    array.append(num2)
    counter += 1
    bruh += 1

print(bruh)
