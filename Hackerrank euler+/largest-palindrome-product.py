#!/bin/python3

import sys

ls=[]
for i in range(100,1000):
    for j in range(100,1000):
        if(str(i*j)==str(i*j)[::-1]):
            if(str(i*j) not in ls):
                ls.append(i*j)
ls.sort()
    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    for i in range(len(ls)):
        if(ls[i]>=n):
            print(ls[i-1])
            break
    