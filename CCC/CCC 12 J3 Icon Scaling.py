
top = list("*x*")
middle = [" ", "x", "x"]
bottom = ["*", " ", "*"]

bruh = [top, middle, bottom]
num = int(input())

matrix = []
for i in bruh:
    new = []
    for e in i:
        new.append(e * num)
    matrix.append(new)

final = []

counter = 0
for i in matrix:
    for m in range(num):
        final.append(matrix[counter])
    counter += 1

for i in final:
    print(''.join(i))


