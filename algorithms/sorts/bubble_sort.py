import DebugUtility

# bubble sort a number list in ascending order
def sort(numList, reverse=False):
        d = DebugUtility.debugUtil()
        d.debugPrompt("[Bubble sort] original list: {}".format(numList))
        _numOfComparisons = 0
        _numOfSwaps = 0
        swapMade = True
        n = len(numList)
        while swapMade:
                swapMade = False
                # length of list = N
                # Indices: 0, 1, 2, 3, 4 ... N-2, N-1
                n -= 1
                # for position in range( len(numList) - 1):
                for position in range(n):
                        d.debugPrompt("[Bubble sort] Comparing {}(pos={}) and {}(pos={})".format(numList[position], position, numList[position+1], position+1))
                        _numOfComparisons += 1
                        if (not reverse and numList[position] > numList[position+1]) or \
                                (reverse and numList[position] < numList[position+1]):
                                d.debugPrompt("   ==> we should swap")
                                _numOfSwaps += 1
                                tmp = numList[position+1]
                                numList[position+1] = numList[position]
                                numList[position] = tmp
                                swapMade = True
                                d.debugPrompt("   list after comparison: {}".format(numList))
                                d.debugPrompt("[Bubble sort] sorted list: {}".format(numList))
                                print("[Bubble sort] Number of comparisons = {}, number of swaps = {}".format(_numOfComparisons, _numOfSwaps))
