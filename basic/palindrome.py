def isPalindrome(string, start, end):
    if start >= end: #base case
        return True
    else:
        firstChar = string[start]
        lastChar = string[end]
        if firstChar != lastChar:
            return False
        else:
            return isPalindrome(string, start+1, end-1)

s = input()
# '\' is an escape sequence
if isPalindrome(s, 0, len(s) - 1):
    print("\"{}\" is a palindrome".format(s))
else:
    print("\"{}\" is not a palindrome".format(s))