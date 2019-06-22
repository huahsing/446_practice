def fibonacci_term(T):
    if T <= 1:
        return T
    else:
        return fibonacci_term(T-1) + fibonacci_term(T-2)

# list the fibonacci sequence up till the n-th term, assuming the first term is 0-th term

print("list the fibonacci sequence up till the n-th term, assuming the first term is 0-th term")
T = int(input())
while T < 0:
    print("Error: input must be greater or equals to 0, please input the n-th term needed")
    T = int(input())

print(fibonacci_sequence_str(T))