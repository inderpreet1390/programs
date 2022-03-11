#!/bin/python3

import sys
import math

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    s=1
    for i in range(2,n+1):
        fl=True
        for j in range(2,i):
            if(i%j==0):
                fl=False
                break
        if(fl):
            c=0
            t=1
            for j in range(10):
                t=t*i
                if t<=n:
                    c=c+1
                else:
                    s=s*(t/i)
                    break
            #s=s*i
    print(int(s))    