# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input())
for _ in range(T):
    a=input()
    s=set(input().split())
    b=input()
    s2=set(input().split())
    print(s2.union(s)==s2)