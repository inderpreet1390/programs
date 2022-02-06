n = input()
ls=[]
for _ in range(int(n)):
    ls.append(input())
for wrd in ls:
    if(len(wrd)>10):
        print(wrd[0]+str(len(wrd)-2)+wrd[-1])
    else:
        print(wrd)
