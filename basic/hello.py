# output a string to the terminal
print("hello world")

# assign an integer value of '5' to variable a
a = 5

# assign an float/real value of '5.5' to variable b
b = 5.5

# assign a string to variable c
c = "i love python"

d = a**2
print("1st print of d=a**2 is", d)
print("2nd print of a**2", a**2)

print("a / 2 is", a/2)
print("a // 2 is", a//2)
print("a % 2 is", a%2)

aBoolValue = True
print("line 22: aBoolValue is", aBoolValue)
aBoolValue = False
print("line 24: aBoolValue is", aBoolValue)

print("line 26: a==5 is", a==5)
print("line 27: a==6 is", a==6)

anotherIntValue = 99
print(anotherIntValue)

# Start: anotherIntValue =  a - a * anotherIntValue
# Step 1: anotherIntValue = a - 5 * 99
# Step 2: anotherIntValue = a - 495
# Step 3: anotherIntValue = 5 - 495
# Step 4: anotherIntValue = -490
anotherIntValue = a - a * anotherIntValue
print(anotherIntValue)

anotherIntValue = (a - a) * anotherIntValue
print(anotherIntValue)


print("anotherIntValue - a is less than 10", (anotherIntValue - a < 10) )
print("anotherIntValue - a is more than 10", (anotherIntValue - a > 10) )

if anotherIntValue - a < 10:
    print("line 48: anotherIntValue - a is less than 10")
else:
    print("line 50: anotherIntValue - a is greater than or equal to 10")
    print("This line (51) is still part of the else block")
print("this line (52) is no longer part of the else block")

if anotherIntValue - a >= 10:
    print("line 55: anotherIntValue - a is greater than or equal to 10")
else:
    print("line 57: anotherIntValue - a is less than 10")
    print("This line (58) is still part of the else block")
print("this line (59) is no longer part of the else block")


# to check even vs odd number, we can use the modulus operator
if a % 2 == 0:
    print("a is an even number")
else:
    print("a is an odd number")
