n=int(input())
ls=[]
for _ in range(n):
    ls.append(int(input()))
s=1
for i in range(1,len(ls)):
    if(ls[i]!=ls[i-1]):
        s=s+1
print(s)
