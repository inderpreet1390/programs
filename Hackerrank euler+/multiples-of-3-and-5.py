#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())-1
    t=n//3
    f=n//5
    ff=n//15
    s=(3*((t*(t+1)))) + (5*((f*(f+1)))) - (15*((ff*(ff+1))))
    s=s//2
    print(int(s))