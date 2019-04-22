

aDict = {'Name': 10, 'Age': 17, 'Class': 9}
for i in sorted(aDict, key=aDict.get):
    print(i)
