n=int(input())
s=input()
a=0
for i in range(n):
    if(s[i]=='A'):
        a=a+1
d=n-a
if(d>a):
    print('Danik')
elif(a>d):
    print('Anton')
elif(a==d):
    print('Friendship')