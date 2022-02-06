import math
n,m,a=input().split()
n,m,a=int(n),int(m),int(a)
r=math.ceil(n/a)
c=math.ceil(m/a)
print(int(r*c))