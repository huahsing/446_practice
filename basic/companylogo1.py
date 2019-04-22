s = input()
aDict = {}

for i in range( ord('a'), ord('z') + 1 ):
    aDict[ chr(i) ] = 0

for c in s:
    aDict[c] += 1

sortedKeys = sorted(aDict, key=aDict.get, reverse=True)
for i in range(3):
    print( sortedKeys[i], aDict[ sortedKeys[i] ] )
