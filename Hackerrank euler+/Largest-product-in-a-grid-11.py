#!/bin/python3

import sys


grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)
n=20
mx=0
for i in range(n):
    for j in range(n-3):
        t=(grid[i][j])*(grid[i][j+1])*(grid[i][j+2])*(grid[i][j+3])
        if(t>mx):
            mx=t
for i in range(n-3):
    for j in range(n):
        t=grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]
        if t>mx:
            mx=t
for i in range(n-3):
    for j in range(n-3):
        t=grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
        if t>mx:
            mx=t
for i in range(3,n):
    for j in range(n-3):
        t=grid[i][j]*grid[i-1][j+1]*grid[i-2][j+2]*grid[i-3][j+3]
        if t>mx:
            mx=t
print(mx)
