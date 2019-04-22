#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()
    aDict = {}
    for c in range( ord('a'), ord('z')+1):
        aDict[chr(c)] = 0

    for c in s:
        aDict[c] += 1
    
    count = 0
    for i in sorted(aDict, key=aDict.get, reverse=True):
        print(i, aDict[i])
        count += 1
        if count == 3:
            break

