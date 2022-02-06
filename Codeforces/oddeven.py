n,k=input().split()
n,k=[int(n),int(k)]
l=[]
for i in range(1,n+1,2):
    l.append(i)
for i in range(2,n+1,2):
    l.append(i)
print(l[k-1])