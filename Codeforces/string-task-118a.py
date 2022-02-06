inp=input()
inp=inp.lower()
ret=[]
vow=['a','e','i','o','u','y']
for i in inp:
    if i not in vow:
        ret.append('.')
        ret.append(i)
print("".join(ret))