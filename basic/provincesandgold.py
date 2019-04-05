x, y, z = map(int, input().split())

T = x*3 + y*2 + z

if T >= 8:
    print("Province or Gold")
elif T >= 6:
    print("Duchy or Gold")
elif T >= 5:
    print("Duchy or Silver")
elif T >= 3:
    print("Estate or Silver")
elif T >= 2: 
    print("Estate or Copper")
else:
    print("Copper")
