x = 5
y = 22/7
z = "a string"
print("Line 4:", x , y, z)
print("Line 5:", x , y, z, sep="")
print("Line 6:", x , y, z, end="")
print("Line 7:", x , y, z)

print("Line 9: %d %f %s" % (x, y, z)) # d --> integer, f --> float, s --> string
print("Line 10: %f %f %s" % (x, y, z)) 
print("Line 11: %d %.2f %s" % (x, y, z)) 

print("Line 13: {} {} {}".format(x, y, z))
print("Line 14: {2} {0} {1}".format(x, y, z))
print("Line 15: {} {:.2} {}".format(x, y, z))