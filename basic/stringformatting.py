def computeBinaryWidth(number):
    # PSEUDOCODE
    # width := 0
    # IF number == 0 THEN
    #   width := 1
    # ELSE
    #   WHILE number > 0
    #     number := number / 2
    #     width := width + 1
    #   ENDWHILE
    # ENDIF
    # RETURN width
    width = 0
    if number == 0:
        width = 1
    else:
        while number > 0:
            number //= 2
            width += 1
    return width

def print_formatted(number):
    # step 1: find w, width of binary value of 'number'
    # step 2: loop from i=1 to i='number'
    # step 3: for each loop, print on the same line the following:
    #           space-padded decimal value of 'number' with width 'w', 
    #           space-padded octal value of 'number' with width 'w', 
    #           space-padded hexadecimal value of 'number' with width 'w', 
    #           space-padded binary value of 'number' with width 'w'

    # PSEUDOCODE
    # width := CALL computeBinaryWidth(number)
    # FOR counter FROM 1 TO number
    #   PRINT Format(number, width, decimal) \
    #         Format(number, width, octal) \
    #         Format(number, width, hexadecimal) \
    #         Format(number, width, binary) 
    # ENDFOR
    binaryWidth = computeBinaryWidth(number)
    for i in range(1, number+1):
        print("{:>{width}d} {:>{width}o} {:>{width}X} {:>{width}b}".format(i, i, i, i, width=binaryWidth))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)