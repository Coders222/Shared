time = input()
time = list(time)


cities = ["Ottawa", "Victoria", "Edmonton", "Winnipeg", "Toronto", "Halifax", "St. John's"]


final = []

for i in range(4 - len(time)):
    time.insert(0, "0")

count = 0
for i in cities:
    hours = int(time[0] + time[1])
    minutes = time[2] + time[3]
    if count == 0:
        if hours == 0:
            final.append(str(minutes) + " in " + i)
        else:
            final.append(str(hours) + str(minutes) + " in " + i)
    if count == 1:  # 0100
        if hours - 3 <= 0:
            hours += 24
            if hours - 3 == 0:
                final.append(str(minutes) + " in " + i)
            elif hours - 3 == 24:
                final.append(str(minutes + " in " + i))
            else:
                final.append(str(hours - 3) + str(minutes) + " in " + i)
        else:
            final.append(str(hours - 3) + str(minutes) + " in " + i)
    if count == 2:  # 1:45
        if hours - 2 <= 0:
            hours += 24
            if hours - 2 == 0:
                final.append(str(minutes) + " in " + i)
            elif hours - 2 == 24:
                final.append(str(minutes + " in " + i))
            else:
                final.append(str(hours - 2) + str(minutes) + " in " + i)
        else:
            final.append(str(hours - 2) + str(minutes) + " in " + i)
    if count == 3:  # 145
        if hours - 1 <= 0:
            hours += 24
            if hours - 1 == 0:
                final.append(str(minutes) + " in " + i)
            elif hours - 1 == 24:
                final.append(str(minutes + " in " + i))
            else:
                final.append(str(hours - 1) + str(minutes) + " in " + i)
        else:
            final.append(str(hours - 1) + str(minutes) + " in " + i)
    if count == 4:
        if hours == 0:
            final.append(str(minutes) + " in " + i)
        else:
            final.append(str(hours) + str(minutes) + " in " + i)
    if count == 5:
        if hours + 1 >= 24:
            hours -= 24
            if hours + 1 == 0:
                final.append(str(minutes) + " in " + i)
            elif hours + 1 == 24:
                final.append(str(minutes + " in " + i))
            else:
                final.append(str(hours + 1) + str(minutes) + " in " + i)
        else:
            final.append(str(hours + 1) + str(minutes) + " in " + i)
    if count == 6:
        chinese = int(minutes)  # 22:40
        if chinese + 30 >= 60:
            hours += 1  # 2:45
            chinese = chinese + 30 - 60   # 2:15
            if hours + 1 >= 24:
                hours -= 24
                if hours == 0:
                    final.append(str(minutes) + " in " + i)
                if minutes == 0:
                    final.append(str(hours + 1) + "00" + " in " + i)
                else:
                    final.append(str(hours + 1) + str(chinese) + " in " + i)
            if chinese == 0:
                final.append(str(hours + 1) + "00 in " + i)
            else:
                final.append(str(hours + 1) + str(chinese) + " in " + i)
        else:
            if hours + 1 == 24:
                final.append(str(minutes + " in " + i))
            else:
                final.append(str(hours + 1) + str(chinese + 30) + " in " + i)
    count += 1


# MINUTES IS STRING
for i in final:
    print(i)

# yeah its coded badly and some numbers may not work idk suck a cock. unstable

