start = int(input())
end = int(input())

# these are strings
bruh = [str(i) for i in range(start, end + 1)]
nums = {
    "9": "6",
    "6": "9",
    "1": "1",
    "8": "8",
    "0": "0"

}

counter = 0
matrix = []

for i in bruh:
    yes = list(i)[::-1]
    new = ''
    for e in yes:
        if e in nums:
            new += nums.get(e)
        else:
            new += 'k'
    if new == i:
        counter += 1
        matrix.append(i)

print(counter)
