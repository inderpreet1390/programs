a='I hate'
b='I love'
m=' that '
e=' it'
n=int(input())
st=''
for i in range(1,n+1):
    if(i%2!=0):
        st=st+a
    else:
        st=st+b
    if(i!=n):
        st=st+m
st=st+e
print(st)
