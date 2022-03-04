t=int(input())
for _ in range(t):
    s=input()
    ls=[]
    ls.append(s[0])
    for i in range(1,len(s)-1,2):
        ls.append(s[i])
    ls.append(s[-1])
    print("".join(ls))