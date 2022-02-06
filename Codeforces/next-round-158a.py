n,k=input().split()
ls=list(input().split())
s=0
for score in ls:
    if(int(score)>=int(ls[int(k)-1]) and int(score)>0):
        s=s+1
print(s)