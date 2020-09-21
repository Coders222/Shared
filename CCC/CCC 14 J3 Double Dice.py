rounds = int(input())

antonio = []
david = []

for i in range(rounds):
    a, b = input().split()
    antonio.append(int(a))
    david.append(int(b))

ant = 100
dav = 100

for i in range(len(antonio)):
    if antonio[i] > david[i]:
        dav -= antonio[i]
    elif antonio[i] < david[i]:
        ant -= david[i]
    else:
        pass

print(ant)
print(dav)
