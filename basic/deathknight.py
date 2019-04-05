n = int(input())
won = 0
for i in range(n):
    # scan input to get the battle details, then check for 'CD'
    # if 'CD' does not exist, then increment 'won'
    s = input()
    if s.find("CD") == -1:
        won += 1
print(won)