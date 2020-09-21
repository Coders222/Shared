bruh = int(input())

matrix = []
for i in range(bruh):
	k = list(map(int, input().split(' ')))
	matrix.append(k)


final = []
for i in matrix:
	year = 2007 - i[0]
	if year > 18:
		final.append("Yes")
		continue
	elif year == 18:
		if i[1] < 2:
			final.append("Yes")
			continue
		elif i[1] <= 2:
			if i[2] <= 27:
				final.append("Yes")
				continue
			

	final.append("No")
for i in final:
	print(i)


