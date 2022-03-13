#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    ls=s.split(" ")
    ls2=[]
    for i in ls:
        if i!="":
            ls2.append(i[0].upper()+"".join(i[1:]))
        else:
            ls2.append(i)
    return " ".join(ls2)

if __name__ == '__main__':