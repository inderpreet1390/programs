# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n=int(input())
ls=[]
for i in range(n):
    q=list(input().split())
    ls.append(q)
for i in range(n):
    a=ls[i][0]
    b=ls[i][1]
    A="A"
    B="B"
    ni=int(ls[i][2])
    c=math.ceil(ni/(len(a)+len(b)))
    ls2=[]
    str1=A+B
    ls2.append(A)
    ls2.append(B)
    ls2.append(A+B)
    for j in range(1,c+2):
        str1=ls2[j]+str1 
        ls2.append(str1)
    print(ls2) 