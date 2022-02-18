ls=['H','Q','9']
p=input()
fl=True
for i in p:
    if i in ls:
        print('YES')
        fl=False
        break
if(fl):
    print('NO')