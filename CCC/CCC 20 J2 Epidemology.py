total = int(input())
infected = int(input())
infects = int(input())

days = 0

count = infected

for i in range(total + 1):
    if count > total:
        print(days)
        break
    elif infects == 1:
        print(round((total - (total % infected)) / infected))
        break
    else:
        infected = infected * infects
        count += infected
        days += 1

