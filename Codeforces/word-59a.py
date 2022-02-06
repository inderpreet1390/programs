s=input()
n=0
for i in range(len(s)):
    if(s[i].isupper()):
        n=n+1
if(n>(len(s)/2)):
    print(s.upper())
else:
    print(s.lower())