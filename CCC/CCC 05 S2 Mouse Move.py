dimensions = input().split()

matrix = []
yes = True
while yes:
	bruh = input().split()
	if bruh == ["0", "0"]:
		break
	matrix.append(bruh)


x = 0
y = 0

final = []
for i in matrix:
	ok = []
	x += int(i[0])
	y += int(i[1])
	if x > int(dimensions[0]):
		x = int(dimensions[0])
	elif x < 0:
		x = 0
	if y > int(dimensions[1]):
		y = int(dimensions[1])
	elif y < 0:
		y = 0
	ok.append(x)
	ok.append(y)
	final.append(ok)

for i in final:
	print(*i)