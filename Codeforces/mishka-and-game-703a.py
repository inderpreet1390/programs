n=int(input())
m=0
c=0
for _ in range(n):
    ms,cs=input().split()
    ms,cs=int(ms),int(cs)
    if(ms>cs):
        m=m+1
    elif(cs>ms):
        c=c+1
if(m>c):
    print("Mishka")
elif(c>m):
    print("Chris")
else:
    print("Friendship is magic!^^")