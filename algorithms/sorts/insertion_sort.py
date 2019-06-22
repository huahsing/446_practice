import DebugUtility

def sort1(numList, reverse=False):
    d = DebugUtility.debugUtil()
    if len(numList) > 1:
        sortedTail = 0
        unsortedHead = 1
        unsortedTail = len(numList) - 1
        while unsortedHead <= unsortedTail:
            curIdx = unsortedHead
            item = numList[curIdx] # item is the number taken out and to be inserted into correct position of sorted list
            leftIdx = sortedTail
            # finding the new position of item and inserting it
            while leftIdx >= 0 and numList[leftIdx] > item:
                # swap left and right(current index)
                numList[curIdx] = numList[leftIdx]
                numList[leftIdx] = item
                curIdx -= 1
                leftIdx -= 1
            sortedTail += 1
            unsortedHead += 1

def sort(numList, reverse=False):
    d = DebugUtility.debugUtil()
    d.debugPrompt("[Insertion sort] original list: {}".format(numList))
    if len(numList) > 1:
        unsortedHead = 1
        while unsortedHead < len(numList):
            item = numList[unsortedHead] # item is the number taken out and to be inserted into correct position of sorted list
            newPos = unsortedHead # initialize new position to head of unsorted list
            # finding the new position of item and inserting it
            while newPos > 0 and numList[newPos - 1] > item:
                # right-shifting
                numList[newPos] = numList[newPos - 1]
                newPos -= 1
            # once we exited while loop, it means we have found the new position
            # insert into new position
            numList[newPos] = item
            unsortedHead += 1
