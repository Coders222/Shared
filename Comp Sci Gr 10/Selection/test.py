year = "2007"

year = int(year[-2:])

x = year // 19
y = year // 4
print(x)
print(y)
print(year)

r = 19 * year
print(r)
r -= x
print(r)
r %= 30
print(r)

print()
s = 6 * year
print(s)
s -= y
print(s)
s -= r
print(s)
s %= 7
print(s)

"""
r = (19 * year - x) % 30
s = (6 * year - y - r) % 7
"""

print(r)
print(s)
