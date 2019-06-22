def fibonacci_term(T):
    if T <= 1:
        return T
    else:
        return fibonacci_term(T-1) + fibonacci_term(T-2)


# find the n-th term in a fibonacci series, assume the first term is 0-th term
print("Input the needed n-th term for the fibonacci series, assuming the first term is 0-th term")
T = int(input())
while T < 0:
    print("Error: input must be greater or equals to 0, please input the n-th term needed")
    T = int(input())

print(fibonacci_term(T))