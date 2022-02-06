# Enter your code here. Read input from STDIN. Print output to STDOUT
def toStr(n,base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base,base) + convertString[n%base]

n,k=input().split()
n,k=[int(n),int(k)]
s=0
for i in range(n+1):
    if(str(i)==str(i)[::-1]):
        b=toStr(i,k)
        if(b==b[::-1]):
            s=s+i
print(s)
