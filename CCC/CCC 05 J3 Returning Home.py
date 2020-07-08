direction = input()
place = input()

directions = []
places = []

directions.append(direction)
places.append(place)


bruh = {
    "R": "LEFT",
    "L": "RIGHT"
}
while place != "SCHOOL":
    direction = input()
    place = input()
    directions.append(direction)
    places.append(place)

places.reverse()
directions.reverse()
places.remove(places[0])
places.append("HOME")



final = []

for i in range(len(directions)):
    if i == len(directions) - 1:
        final.append("Turn " + bruh.get(directions[i]) + " into your " + places[i] + ".")
    else:
        final.append("Turn " + bruh.get(directions[i]) + " onto " + places[i].upper() + " street.")

for i in final:
    print(i)

'''
R
QUEEN
R
FOURTH
R
SCHOOL

Turn LEFT onto FOURTH street.
Turn LEFT onto QUEEN street.
Turn LEFT into your HOME.
'''
