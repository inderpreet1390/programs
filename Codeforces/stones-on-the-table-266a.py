n=int(input())
inp=input()
c=0
for i in range(n-1):
    if(inp[i]==inp[i+1]):
        c += 1
print(c)