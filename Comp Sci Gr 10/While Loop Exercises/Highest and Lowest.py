
a = int(input())
high = a
low = a

while not a <= 0:
    if a >= high:
        high = a
    else:
        low = a
    a = int(input())

print(high)
print(low)


