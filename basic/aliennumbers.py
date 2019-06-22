T = int(input())

for i in range(T):
    alienNum, sourceLang, targetLang = input().split()
    
    sourceLangCharDict = {}
    sourceBase = 0
    for x in sourceLang:
        sourceLangCharDict[x] = sourceBase
        sourceBase += 1

    targetLangCharIndexer = [x for x in targetLang]
    targetBase = len(targetLangCharIndexer)

    alienNumDigitCharList = [x for x in alienNum]
    alienNumDigitCharList.reverse()
    alienNumInDecimal = 0
    for digitPosition in range(len(alienNumDigitCharList)):
        alienNumInDecimal += (sourceLangCharDict[alienNumDigitCharList[digitPosition]] * (sourceBase**digitPosition))

    '''
    101101 (binary): --> base = 2
    1 * 2**0 = 1
    0 * 2**1 = 0
    1 * 2**2 = 4
    1 * 2**3 = 8
    0 * 2**4 = 0
    1 * 2**5 = 32
    1 + 0 + 4 + 8 + 0 + 32 = 45
    '''

    tmp = alienNumInDecimal
    translatedNum = []
    while tmp > 0:
        digit = tmp % targetBase
        translatedNum.append(targetLangCharIndexer[digit])
        tmp //= targetBase

    translatedNum.reverse()
    print("".join(translatedNum))
