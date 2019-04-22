K = int(input())
l = list(map(int, input().split()))
s = set(l)
for elem in l:
    s.discard(elem)

print(s.pop())