n=int(input())
l=input().split()
for i in range(len(l)):
    l[i]=int(l[i])
r=0
if(l[0]<0):
    s=0
    r=1
else:
    s=l[0]
for i in range(1,len(l)):
    if(l[i]<0):
        if(s>0):
            s=s+l[i]
        else:
            s=0
            r=r+1
    else:
        s=s+l[i]
print(r)
        