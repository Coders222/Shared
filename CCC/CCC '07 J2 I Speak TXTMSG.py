yup = True

matrix = []
while yup:
    matrix.append(input())
    if matrix[-1] == "TTYL":
        yup = False

bruh = {
    "CU": "see you",
    ":-)": "I'm happy",
    ":-(": "I'm unhappy",
    ";-)": "wink",
    ":-P": "stick out my tongue",
"    (~.~)	": 'sleepy',
    'TA':	'totally awesome',
    'CCC':	'Canadian Computing Competition',
    'CUZ':	'because',
    'TY':	'thank-you',
    'YW':	"you're welcome",
    'TTYL':	'talk to you later',
}

for i in matrix:
    print(bruh.get(i, i))

