def sortCupsByRadius(elem):
    return elem[1] # returns radius of cup


N = int(input())

listOfCups = []

for i in range(N):
    elem = [] # first value will be colour, second value will be radius
    s1, s2 = input().split()
    if s1.isdigit():
        s1 = int(s1) // 2
        elem.append(s2)
        elem.append(s1)
    else:
        s2 = int(s2)
        elem.append(s1)
        elem.append(s2)

    listOfCups.append(elem)

listOfCups.sort(key=sortCupsByRadius)
for i in listOfCups:
    print(listOfCups[i][0])
    
        

