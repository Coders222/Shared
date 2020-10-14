bidenvote = 0

for i in range(20):
    biden = int(input("1. Trump or 2. Biden (type the number) "))
    if biden == 1:
        bidenvote += 1

print("Biden: " + ("|" * bidenvote))
print("Trump: " + ("|" * (20 - bidenvote)))





