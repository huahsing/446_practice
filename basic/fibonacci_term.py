# find the n-th term in a fibonacci series, assume the first term is 0-th term

print("Input the needed n-th term for the fibonacci series, assuming the first term is 0-th term")
T = int(input())
while T < 0:
    print("Error: input must be greater or equals to 0, please input the n-th term needed")
    T = int(input())

if T <= 1:
    print("The value of {}-th is {}".format(T, T))
else:
    currentTermCounter = 2
    currentTerm = 1
    termMinusOne = 1 # 1-th term
    termMinusTwo = 0 # 0-th term
    while currentTermCounter <= T:
        currentTerm = termMinusOne + termMinusTwo
        termMinusTwo = termMinusOne
        termMinusOne = currentTerm
        currentTermCounter += 1
    print("The value of {}-th is {}".format(T, currentTerm))
