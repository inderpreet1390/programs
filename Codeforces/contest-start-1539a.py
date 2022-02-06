k=int(input())
ls=[] #no. of test cases
for _ in range(k):
    ls.append(input().split())
print(ls)
for i in  range(k):
    n=int(ls[i][2]) #for calculation of finish times
    ls2=[] #finish times
    ls3=[] #start times
    s=0 #final dissatsifaction
    for j in range(int(ls[i][0])):
        n=n+(j*int(ls[i][1])) 
        ls3.append(j*int(ls[i][1])) #appending j*duration
        ls2.append(n) #appending duration+ j*timeinterval
    for j in range(int(ls[i][0])):
        for k in range(j,int(ls[i][0])):
            if (ls2[j]>=ls3[k] and ls2[j]<ls2[k]): #means partiicipant started but didnt finish yet after ls2[j]th participant finished
                s=s+1
    print(s)