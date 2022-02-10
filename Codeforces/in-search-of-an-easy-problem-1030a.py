n=int(input())
ls=input().split()
h=0
for i in ls:
    if int(i)==1:
        h=1
        break
if(h==1):
    print("hard")
else:
    print("easy")