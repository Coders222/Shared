weighter = int(input())
cars = int(input())

allcars = []
for i in range(cars):
    weight = int(input())
    allcars.append(weight)

counter = -1

yes = True

total = 0
matrix = []

ind = 4
anotherind = 0
index = 0

while yes:
    if total > weighter:
        break
    elif len(matrix) == 4:
        total -= matrix[0]
        matrix.remove(matrix[0])
        matrix.append(allcars[ind])
        total += allcars[ind]
        ind += 1
        counter += 1
        continue
    elif allcars[index] == allcars[-1]:
        total += allcars[index]
        counter += 1
        continue
    matrix.append(allcars[index])
    index += 1
    total += matrix[anotherind]
    anotherind += 1
    counter += 1

print(counter)

