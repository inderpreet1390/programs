# Enter your code here. Read input from STDIN. Print output to STDOUT
s=set(input().split())
n=int(input())
fl=True
for _ in range(n):
    s2=set(input().split())
    if(s2==s):
        fl=False
        break
    else:
        if(s.union(s2)!=s):
            fl=False
            break
print(fl)