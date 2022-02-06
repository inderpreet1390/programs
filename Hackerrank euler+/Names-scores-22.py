# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(input())
ls=[]
for i in range(N):
    ls.append(input())
ls.sort()
Q=int(input())
Qls=[]
for i in range(Q):
    Qls.append(input())

for i in range(len(Qls)):
    s=0
    for j in range(len(Qls[i])):
        s=s+ord(Qls[i][j])-64
    print((ls.index(Qls[i])+1)*s)
    
