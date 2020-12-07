# 1

"""
lst = input().split()

another = []
for i in range(1, len(lst)):
    another.append(lst[i])

another.append(lst[0])
print(another)
"""

# 2

"""
lst = input().split()

print(lst[::-1])
"""

# 3

"""
lst = input().split()

count = 0

for i in lst:
    if int(i) == 13:
        break
    count += int(i)

print(count)
"""

# 4

"""
lst = input().split()

biggest = int(lst[0])
smallest = int(lst[0])

for i in range(1, len(lst)):
    if int(lst[i]) > biggest:
        biggest = int(lst[i])
    elif int(lst[i]) < smallest:
        smallest = int(lst[i])

print(biggest - smallest)"""

# OR
# 4

lst = input().split()

for i in range(len(lst)):
    lst[i] = int(lst[i])


print(max(lst) - min(lst))
#idk whys it highlighted but it works