from typing import KeysView


k,n,w=input().split()
s=0
for i in range(1,int(w)+1):
    s=s+i*int(k)
d=s-int(n)
if(d<0):
    print('0')
else:
    print(d)