def processAValue(number):
    # your code goes here
    newNumber = number*2
    newNumber = newNumber % 10
    newNumber = newNumber + number^3
    return newNumber

def anotherFunction():
    return "abc"

if __name__ == '__main__':
    n = int(input())
    # i = n * 2
    i = processAValue(n)
    x = processAValue(97)
    y = processAValue(1456)
    j = anotherFunction()
    print(i)
    print(j)