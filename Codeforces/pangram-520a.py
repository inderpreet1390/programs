n=int(input())
s=input()
s=s.lower()
if(len(set(list(s))))==26:
    print("YES")
else:
    print("NO")