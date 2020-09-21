import math

numerator = int(input())

denominator = int(input())

if numerator % denominator == 0:
	print(round(numerator / denominator))
else:
	leftover = round(numerator % denominator)
	whole = math.floor(numerator / denominator)
	yes = True
	while yes:  # not time effecient if it is a huge fraction, do leftover /= leftover / x, denominator /= denominator / x and then run bool yes again
		if denominator % leftover == 0:
			denominator /= leftover
			leftover = 1
			break
		elif numerator / denominator == 0.5:
			leftover = 1
			denominator = 2
			break
		elif leftover % 7 == 0 and denominator % 7 == 0:
			denominator /= 7
			leftover /= 7
			continue
		elif leftover % 5 == 0 and denominator % 5 == 0:
			denominator /= 5
			leftover /= 5
			continue
		elif leftover % 3 == 0 and denominator % 3 == 0:
			denominator /= 3
			leftover /= 3
			continue
		elif leftover % 2 == 0 and denominator % 2 == 0:
			denominator /= 2
			leftover /= 2
			continue
		else:
			break
	
	if whole == 0:
		print(str(round(leftover)) +  "/" + str(round(denominator)))
	else:
		print(str(whole), str(round(leftover)) +  "/" + str(round(denominator)))
