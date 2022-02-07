n=int(input())
ls=[1,5,10,20,100]
p=0
for i in range(len(ls)-1,-1,-1):
    t=int(n/ls[i])
    n=n-(t*ls[i])
    p=p+t
    if(n==0):
        break
print(p)
