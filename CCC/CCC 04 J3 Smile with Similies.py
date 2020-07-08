adj = int(input())
nounz = int(input())

adjs = []
nouns = []

for i in range(adj):
    adjective = input()
    adjs.append(adjective)
for i in range(nounz):
    noun = input()
    nouns.append(noun)

final = []

for i in adjs:
    for e in nouns:
        final.append(i + " as " + e )

for i in final:
    print(i)

