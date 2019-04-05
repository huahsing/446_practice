x = int(input())
y = int(input()) 
import sys

n = int(input())
print([ [i, j] for i in range(x + 1) for j in range(y + 1) if ( ( i + j ) != n ) ])
# print([ [i, j] for j in range(y + 1) for i in range(x + 1) if ( ( i + j ) != n ) ])
# repeated adding [i, j] for the specified ranges and conditions

print(sys.float_info.max)