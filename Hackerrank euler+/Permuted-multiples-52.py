# Enter your code here. Read input from STDIN. Print output to STDOUT
N,K=input().split()
N,K=[int(N),int(K)]
ls=[]
for i in range(125874,N+1):
    nm=sorted(list(str(i)))
    t=0
    for j in range(2,K+1):
        if(sorted(list(str(i*j)))!=nm):
            t=1
            break
    if(t==0):
        ls.append(i)
retls=[]
for num in ls:
    retls=[]
    for i in range(1,K+1):
        retls.append(str(i*num))
        retls.append(" ")
    print(("").join(retls))
    
