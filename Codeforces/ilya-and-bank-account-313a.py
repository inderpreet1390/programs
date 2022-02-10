n=int(input())
if(n>=0):
    print(n)
else:
    if(str(n)[-1]>=str(n)[-2]):
        print(int(str(n)[:-1]))
    else:
        print(int(str(n)[:-2]+str(n)[-1]))