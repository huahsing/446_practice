N, M = map(int, input().split())

centreStartPattern = ".|"
centreEndPattern = "."
centreRepeatPattern = "..|"

for row in range(N):
    # check for centre row
    if row == N // 2:
        dashCountOnEachSide = (M - len("WELCOME")) // 2
        for _ in range(dashCountOnEachSide): # loop to print dashes on left side
            print("-", end="")
        print("WELCOME", end="") # print centre WELCOME message
        for _ in range(dashCountOnEachSide): # loop to print dashes on right side
            print("-", end="")
        print("") # to go to next line
    else:
        # check for first half rows before centre row
        if row < N // 2:
            centreRepeatPatternCount = row * 2
        else: # second half rows after centre row
            centreRepeatPatternCount = (N - row - 1) * 2

        dashCountOnEachSide = ( M - len(centreStartPattern) - len(centreEndPattern) 
                                - len(centreRepeatPattern) * centreRepeatPatternCount ) // 2

        for _ in range(dashCountOnEachSide):
            print("-", end="") # loop to print dashes on left side

        print(centreStartPattern, end="") # print ".|"

        for _ in range(centreRepeatPatternCount):
            print(centreRepeatPattern, end="") # loop to print "..|" repeatedly

        print(centreEndPattern, end="") # print "."

        for _ in range(dashCountOnEachSide):
            print("-", end="") # loop to print dashes on right side

        print("") # to go to next line
