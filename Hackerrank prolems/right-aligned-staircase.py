#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    ls=[]
    for i in range(n):
        ls2=[]
        for j in range(n-1-i):
            ls2.append(" ")
        for j in range(i+1):
            ls2.append("#")
        ls.append(ls2)
        
    for i in range(n):
        print("".join(ls[i]))
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
