# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
s=set(input().split())
N=int(input())
for _ in range(N):
    wh=input().split()
    if(wh[0]=='intersection_update'):
        s2=set(input().split())
        s.intersection_update(s2)
    elif(wh[0]=='update'):
        s2=set(input().split())
        s.update(s2)
    elif(wh[0]=='symmetric_difference_update'):
        s2=set(input().split())
        s.symmetric_difference_update(s2)
    elif(wh[0]=='difference_update'):
        s2=set(input().split())
        s.difference_update(s2)
ls=[int(x) for x in s]
print(sum(ls))