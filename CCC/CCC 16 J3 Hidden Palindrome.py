msg = list(input())

# mom

rev = []
backwardsreversed = []

ind = 0

for i in range(len(msg)):
    rev = list(reversed(msg[ind:]))  # deleting letters from the front
    backwardsreversed = list(reversed(msg[:len(msg) - ind]))  # deleting letters from the back
    msg1 = msg[ind:]
    msg2 = msg[:len(msg) - ind]
    if ''.join(msg1) == ''.join(rev):
        print(len(msg) - ind)
    elif ''.join(msg2) == ''.join(backwardsreversed):
        print(len(msg) - ind)
    ind += 1



print(rev)
