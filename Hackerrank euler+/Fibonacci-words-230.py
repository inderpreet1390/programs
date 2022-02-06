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
    ni=int(ls[i][2])
    c=math.ceil(ni/(len(a)+len(b)))
    ls2=[]
    str1=a+b
    ls2.append(a)
    ls2.append(b)
    ls2.append(a+b)
    for j in range(1,c+2):
        str1=ls2[j]+str1 
        ls2.append(str1)
    for j in range(len(str1)):
        if j==ni-1:
            print(str1[j]) 