year = int(input())


codeine = True

while codeine:
    new = year + 1
    listed = list(str(new))
    condition = True
    for i in listed:
        if listed.count(i) == 1:
            pass
        else:
            condition = False
    if condition:
        print(new)
        break
    bruh = True
    while bruh:
        for i in listed:
            if listed.count(i) > 1:
                year += 1
                break
        break
    continue







    

