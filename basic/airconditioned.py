def sortByU(x):
    return x[1]

def sortByL(x):
    return x[0]

N = int(input())
l = []
for i in range(N):
    x = list(map(int, input().split()))
    l.append(x)

l.sort(key=sortByU)
roomTemp = l[0][1]
roomCnt = 1
for i in range(1, N):
    if l[i][0] <= roomTemp <= l[i][1]:
        continue
    roomCnt += 1
    roomTemp = l[i][1]
print(roomCnt)