string = input()

substring = input()

substring = list(substring)

yes = True
for i in range(len(substring)):
    if ''.join(substring) in string:
        print("yes")
        yes = False
        break
    substring.append(substring[0])
    substring.remove(substring[0])

if yes:
    print("no")
