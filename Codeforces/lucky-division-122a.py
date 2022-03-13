n=int(input())
fl=True
for i in set(str(n)):
    if(i!=4 or i!=7):
        fl=False
        break
if(fl):
    print("YES")
else:
    if(n%4==0 or n%7==0 or n%47==0 or n%447==0 or n%477==0):
        print("YES")
    else:
        print("NO")