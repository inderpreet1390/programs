#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    ns=str(num)
    s=0
    for i in range(k-1,len(ns)):
        nt=ns[i-k:i] #check
        t=1
        for j in range(len(nt)):
           t=t*int(nt[j])
        if(t>s and t!=1):
            s=t
    print(s) 