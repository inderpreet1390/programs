#TLE on test 3
instr=input()
dub='WUB'
ls=[]
i=0
while(i+3!=len(instr)):
    if(instr[i:i+3]==dub):
        i=i+3
        continue
    else:
        for k in range(i,len(instr)):
            if(instr[k:k+3]!=dub):
                ls.append(instr[k])
            else:
                ls.append(" ")
                i=k
                break
    
print("".join(ls))