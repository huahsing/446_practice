import itertools
import sys

while True:
    try:
        s = [x for x in input()]
        s = list(itertools.permutations(s))
        print(len(s))
    except EOFERROR:
        break
