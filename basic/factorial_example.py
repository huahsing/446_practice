def computeFactorial(inputNumber):
    if inputNumber <= 1:
        return 1
    else:
        nextNumber = computeFactorial(inputNumber-1)
        return inputNumber * nextNumber

# 0xFFFFFFFF
# .
# 0x00001030  computeFactorial (inputNumber=1) + return address of previous computeFactorial
# 0x00001028  computeFactorial (inputNumber=2) + return address of previous computeFactorial
# 0x00001020  computeFactorial (inputNumber=3) + return address of previous computeFactorial
# 0x00001018  computeFactorial (inputNumber=4) + return address of previous computeFactorial
# 0x00001010  computeFactorial (inputNumber=5) + return address of previous computeFactorial
# 0x00001008  computeFactorial (inputNumber=6) + return address of main
# 0x00001000  main for computeFactorial.py variables (x=6) + return address (?)
# .
# 0x00000002
# 0x00000001
# 0x00000000

x = int(input())
print("The factorial of {} is (ie. {}!) = {}".format(x, x, computeFactorial(x)))
