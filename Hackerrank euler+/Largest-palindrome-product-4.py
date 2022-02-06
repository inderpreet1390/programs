#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    fnd=0
    for num in range(n,1,-1):
        if(str(num)==str(num)[::-1]):
            for fac in range(100,999):
                if(num%fac==0 and len(str(int(num/fac)))==3):
                    print(num)
                    fnd=1
                    break
            if(fnd==1):
                break
        if(fnd==1):
            break
                    