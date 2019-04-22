T = int(input())
for i in range(T):
    numStr = input()
    num = int(numStr)
    digits = [int(x) for x in numStr]
    sumOfDigits = 0
    for d in digits:
        sumOfDigits += d
    for a in range(num-1, -1, -1):
        testDigits = [int(x) for x in str(a)]
        testSumOfDigits = 0
        for d in testDigits:
            testSumOfDigits += d
        if(testSumOfDigits+1 == sumOfDigits):
            break
    print(a)