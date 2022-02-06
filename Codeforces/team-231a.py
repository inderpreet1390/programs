n=input()
ls=[]
for _ in range(int(n)):
    ls.append(input().split())
s=0
for arr in ls:
    if(int(arr[0])+int(arr[1])+int(arr[2])>=2):
        s=s+1
print(s)