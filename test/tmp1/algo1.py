def bubble_sort_step_by_step(numList):
    swapMode = True
    print("Original List:", numList)
    while swapMode:
        swapMode = False
        for i in range(len(numList)-1):
            print("Comparing {} and {}".format(numList[i], numList[i+1]))
            if numList[i] > numList[i+1]:
                tmp = numList[i]
                numList[i] = numList[i+1]
                numList[i+1] = tmp
                swapMode = True
                print("Swap performed")
    
    
