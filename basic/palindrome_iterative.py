s = input()
startIdx = 0
endIdx = len(s) - 1
isPalindrome = True

while startIdx < endIdx:
    if s[startIdx] != s[endIdx]:
        isPalindrome = False
        break
    else:
        startIdx += 1
        endIdx -= 1

if isPalindrome:
    print("\"{}\" is a palindrome".format(s))
else:
    print("\"{}\" is not a palindrome".format(s))