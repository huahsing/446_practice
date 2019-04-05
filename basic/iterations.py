i = int(input("enter start value: "))
j = int(input("enter end value: "))

print("while loop: counting even numbers from %d to %d: " % (i, j), end="")
k = i
while k < j:
    if k % 2 == 0:
        print(k, end = " ")
    k += 1
print("")

print("for loop: counting even numbers from %d to %d: " % (i, j), end="")
for k in range(i, j):
    if k % 2 == 0:
        print(k, end = " ")
print("")

# example for 'break' and 'continue' keywords
# 'break' causes execution to exit the loop
print("while loop: counting odd numbers from %d to %d but stop counting if it's divisible by 13: " % (i, j), end="")
k = i
while k < j:
    if k % 13 == 0:
        break
    if k % 2 == 1:
        print(k, end = " ")
    k += 1
print("")

print("for loop: counting multiples of 3 from %d to %d but skip if it's a multiple of 4: " % (i, j), end="")
for k in range(i, j):
    if k % 4 == 0:
        continue
    if k % 3 == 0:
        print(k, end = " ")
print("")
