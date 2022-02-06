n = int(input())
f=input().split()
for i in range(n):
    f[i]=int(f[i])
for i in range(1,n+1):
    if(f[f[f[i-1]-1]-1]==i):
        print('YES')
        break
    elif(i==(n-1) and f[f[f[i-1]-1]-1]!=i):
        print('NO')
