rows = int(input())
columns = int(input())

matrix = []

for i in range(rows):
    matrix.append(input().split())


beenthere = [[1, 1]]

bruh = True

escaped = False
while bruh:
    leave = False
    ind = 0
    stander = []
    stander.append([1, 1])
    rowind = 1
    columnind = 1
    moist = True
    while moist:
        if stander[-1] == [rows, columns]:
            leave = True
            escaped = True
            break

        if rowind * columnind == int(matrix[stander[ind][0] - 1][stander[ind][1] - 1]):
            if rows * columns < int(matrix[stander[ind][0] - 1][stander[ind][1] - 1]):  # to save time
                beenthere.append([rowind, columnind])
                break
            if [rowind, columnind] not in stander:  # prevents endless loops
                if [rowind, columnind] not in beenthere:
                    stander.append([rowind, columnind])
                    ind += 1
                    columnind = 1
                    rowind = 1
                    continue

        columnind += 1
        if columnind > columns:
            rowind += 1
            columnind = 1
        if rowind > rows:
            break

    if len(stander) == 1:
        break
    if leave:
        break
    beenthere.append(stander[-1])


if escaped:
    print("yes")
if not escaped:
    print("no")

'''

5
5
12 3 8 16 0
9 8 4 7 11
25 17 1 2 28
9 4 3 12 19
8 10 10 4 3

'''


