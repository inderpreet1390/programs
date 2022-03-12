s=input()
z=0
o=0
for i in range(1,len(s)):
    d=False
    n=int(s[i])
    n1=int(s[i-1])
    if(n==n1==1):
        o=o+1
    elif(n==n1==0):
        z=z+1
    elif(n!=n1):
        z=0
        o=0
    if(z==6 or o==6):
        print("YES")
        break
if(z!=6 and o!=6):
    print("NO")