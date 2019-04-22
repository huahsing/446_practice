numList = list(map(int, input().split()))
alphaOrderStr = input()

numList.sort()
smallestAlphabet = 'A'
largestAlphabet = 'C'
aDict = {}
iterCnt = 0
for i in range( ord(smallestAlphabet), ord(largestAlphabet) + 1 ):
    aDict[i] = numList[iterCnt]
    iterCnt += 1

outputStr = ""
for c in alphaOrderStr:
    outputStr =  outputStr + str(aDict[ord(c)]) + " "

outputStr.strip()
print(outputStr)