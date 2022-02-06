# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n=int(input())
s=0
for i in range(10, n+1):
   si=str(i)
   su=0
   for j in range(len(si)):
        su=su+math.factorial(int(si[j]))
   if(su%i==0):
        s=s+i
print(s)