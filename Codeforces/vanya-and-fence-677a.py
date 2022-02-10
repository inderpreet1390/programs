n,h=input().split()
n,h=int(n),int(h)
ls=list(input().split())
w=0
for i in ls:
    if int(i)>h:
        w=w+2
    else:
        w=w+1
print(w)