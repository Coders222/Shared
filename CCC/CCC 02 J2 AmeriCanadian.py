yes = True

matrix = []

while yes:
	ok = input().lower()
	if ok == "quit!":
		break
	else:
		matrix.append(ok)

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
final = []

for i in matrix:
	if len(i) > 4:
		i = list(i)
		if i[-1] == "r":
			if i[-2] == "o":
				if i[-3] not in vowels:
					i.insert(-1, 'u')
	final.append(''.join(i))		

for i in final:
	print(i)