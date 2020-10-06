from random import randint

a = randint(1, 6)
b = randint(1, 6)

counter = 1

while a + b != 9:
    print(a, b)
    a = randint(1, 6)
    b = randint(1, 6)
    counter += 1

print(a, b)
print(counter)
