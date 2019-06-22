from sorts import bubble_sort
from sorts import insertion_sort
from random import randint
from random import seed

seed(1)

print("Create some test values for \'sorting_test\'.")
N = int(input("Enter the sample size N: "))
minNum = int(input("Enter the smallest integer in range: "))
maxNum = int(input("Enter the largest integer in range: "))
listToBeSorted = []

for i in range(N):
    listToBeSorted.append( randint(minNum, maxNum) )

# bubble_sort.enableDebug()

print("[sorting_test] list before sorting:", listToBeSorted)
#bubble_sort.sort(listToBeSorted)
#bubble_sort.sort(listToBeSorted, True)
insertion_sort.sort(listToBeSorted)
print("[sorting_test] list after sorting:", listToBeSorted)