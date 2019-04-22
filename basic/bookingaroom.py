r, n = map(int, input().split())
if r == n:
    print("too late")
else:
    allRooms = set([x for x in range(1, r+1)])
    bookedRooms = set()
    for i in range(n):
        bookedRooms.add(int(input()))
    print(allRooms.difference(bookedRooms))
