def ispalindrome(str):
    a=0
    for i in range(len(str)):
        if(str[i]!=str[len(str)-i-1]):
            a=1
            break
    if(a==0):
        return True
    else:
        return False
print(ispalindrome('aabaa'))