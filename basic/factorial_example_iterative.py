x = int(input())
y = x
factorial = 1
while x > 0:
    factorial *= x
    x -= 1

print("The factorial of {} is (ie. {}!) = {}".format(y, y, factorial))