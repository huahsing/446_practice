firstDigitList = [int(d) for d in input()]
firstDigitList.reverse()
secondDigitList = [int(d) for d in input()]
secondDigitList.reverse()
firstLen = len(firstDigitList)
secondLen = len(secondDigitList)
firstNewDigitList = []
secondNewDigitList = []
iter = 0
if firstLen <= secondLen:
    upperBound = firstLen
else:
    upperBound = secondLen

while iter < upperBound:
    if firstDigitList[iter] < secondDigitList[iter]:
        secondNewDigitList.append(secondDigitList[iter])
    elif firstDigitList[iter] > secondDigitList[iter]:
        firstNewDigitList.append(firstDigitList[iter])
    else:
        firstNewDigitList.append(firstDigitList[iter])
        secondNewDigitList.append(secondDigitList[iter])
    iter += 1

# only one of the below while loops will execute
while iter < firstLen:
    firstNewDigitList.append(firstDigitList[iter])
    iter += 1

while iter < secondLen:
    secondNewDigitList.append(secondDigitList[iter])
    iter += 1
    
firstNewDigitList.reverse()
secondNewDigitList.reverse()

if len(firstNewDigitList) > 0:
    print(int("".join(map(str, firstNewDigitList))))
else:
    print("YODA")

if len(secondNewDigitList) > 0:
    print(int("".join(map(str, secondNewDigitList))))
else:
    print("YODA")
    