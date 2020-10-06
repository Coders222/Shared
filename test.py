cases = int(input())

matrix = [input().split() for i in range(cases)]
time = [int(i[0]) for i in matrix]
pos = [int(i[1]) for i in matrix]

print(sorted(zip(time, pos)))

