d=input()
s=input()
l1=list('qwertyuiop')
l2=list('asdfghjkl;')
l3=list('zxcvbnm,./')
lf=[]
if(d=='R'):
    for i2,i in enumerate(s):
        if i in l1:
            idx=l1.index(i)
            if(idx!=0):
                lf.append(l1[idx-1])
            else:
                lf.append(l1[0])
        elif i in l2:
            idx=l2.index(i)
            if(idx!=0):
                lf.append(l2[idx-1])
            else:
                lf.append(l2[0])
        elif i in l3:
            idx=l3.index(i)
            if(idx!=0):
                lf.append(l3[idx-1])
            else:
                lf.append(l3[0])
elif(d=='L'):
    for i in range(len(s)):
        if i in l1:
            idx=l1.index(i)
            if(idx!=len(l1)-1):
                lf.append(l1[idx+1])
            else:
                lf.append(len(l1)-1)
        elif i in l2:
            idx=l2.index(i)
            if(idx!=len(l2)-1):
                lf.append(l2[idx+1])
            else:
                lf.append(len(l2)-1)
        elif i in l3:
            idx=l3.index(i)
            if(idx!=len(l3)-1):
                lf.append(l3[idx+1])
            else:
                lf.append(len(l3)-1)
print("".join(lf))

#wrong anwser on test 3