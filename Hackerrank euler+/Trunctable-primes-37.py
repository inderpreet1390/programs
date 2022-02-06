# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
ls=[23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
s=0
for i in range(len(ls)):
    if(ls[i]<n):
        s=s+ls[i]
print(s)