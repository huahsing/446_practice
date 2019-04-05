x = int(input())
y = int(input()) 
n = int(input()) 
ar = [] 
p = 0 

# nested loops
for i in range(x + 1): # outer loop
    for j in range(y + 1): # inner loop
        if i+j != n: # if x is 3, and y is 5, how many times does this line run? --> 24 times
            ar.append([]) 
            ar[p] = [ i , j ] 
            p+=1 
print(ar)