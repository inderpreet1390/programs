# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
d=OrderedDict()
n=int(input())
for _ in range(n):
    s=input().split()
    if(" ".join(s[:-1]) not in d.keys()):
        d[" ".join(s[:-1])]=int(s[-1])
    else:
        d[" ".join(s[:-1])]=d[" ".join(s[:-1])]+int(s[-1])
for i in d:
    print(i,d[i])