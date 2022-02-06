n=input()
ls=[]
for _ in range(int(n)):
    ls.append(input())
x=0
for smts in ls:
    if('+' in smts):
        x=x+1
    else:
        x=x-1
print(x)