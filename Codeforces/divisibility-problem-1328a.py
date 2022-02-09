t=int(input())
ls=[]
for _ in range(t):
    a,b=input().split()
    a,b=int(a),int(b)
    if(a%b==0):
        ls.append(0)
    else:
        n=int(a/b)+1
        ls.append((n*b)-a)
for i in ls:
    print(i)
