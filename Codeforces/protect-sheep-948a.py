r,c=input().split()
r=int(r)
c=int(c)
f=[]
for i in range(c):
    f.append(input().split())
#check sheep near wolf row-wise
for i in range(r):
    for j in range(c-1):
        if(f[i][j]=='S' and f[i][j+1]=='W'):
            print('No')
for i in range(r-1):
    for j in range(c):
        if(f[i][j]=='S' and f[i+1][j]=='W'):
            print('No')
d=0
for i in range(r):
    for j in range(c):
        if(f[i][j]=='W'):
            d=d+1
if(d==0):
    print('Yes')