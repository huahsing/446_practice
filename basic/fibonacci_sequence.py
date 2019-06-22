# list the fibonacci sequence up till the n-th term, assuming the first term is 0-th term

print("list the fibonacci sequence up till the n-th term, assuming the first term is 0-th term")
T = int(input())
while T < 0:
    print("Error: input must be greater or equals to 0, please input the n-th term needed")
    T = int(input())

fibonacci_list = ["0", "1"]
if T == 0:
    print("0")
else:
    if T > 1:
        currentTermCounter = 2
        currentTerm = 1
        termMinusOne = 1 # 1-th term
        termMinusTwo = 0 # 0-th term
        while currentTermCounter <= T:
            currentTerm = termMinusOne + termMinusTwo
            termMinusTwo = termMinusOne
            termMinusOne = currentTerm
            fibonacci_list.append(str(currentTerm))
            currentTermCounter += 1
    
    print(" ".join(fibonacci_list))

