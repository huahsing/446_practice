N = int(input())
# calculate the number of binary digits for N

x, y, z = "a .b .c".split()
print("x is", x)
print("y is", y)
print("z is", z)

x, y, z = "a .b .c".split(sep=".")
print("x is", x, ", length of x is", len(x))
print("y is", y, ", length of y is", len(y))
print("z is", z, ", length of z is", len(z))

print("{:d} {:b}".format(N, N))
print("{:10d} {:b}".format(N, N))

# I made a typo and I made the correction so it works now
# please study and experiment with the code and try out the 'padding' practice
var_width = 5
print("{:>{width}} {:b}".format(N, N, width=var_width))
print("{:<{width}} {:>{width2}b}".format(N, N, width=var_width+7, width2=var_width))