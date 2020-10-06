def filterr(a):
    if not 0 < a < 12:
        print("Invalid input")
        return True
    else:
        return False


bruh = True

while bruh:
    month = int(input("What is the month in numbers right now? "))
    ok = filterr(month)
    if ok:
        continue
    else:
        bruh = False
    if 3 <= month <= 4:
        print("spring")
    elif 5 <= month <= 8:
        print("summer")
    elif 9 <= month <= 10:
        print("fall")
    else:
        print("winter")