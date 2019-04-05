Hour, Minute = map(int, input().split())
if Minute >= 45:
    Minute -= 45 # Minute = Minute - 45
else:
    Minute = 60 - (45 - Minute)
    if Hour > 0:
        Hour -= 1
    else:
        Hour = 23

print(Hour, Minute)