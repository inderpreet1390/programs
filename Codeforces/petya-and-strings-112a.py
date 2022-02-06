str1=input()
str2=input()

str1=str1.lower()
str2=str2.lower()

asci1=[ord(c) for c in str1]
asci2=[ord(c) for c in str2]

for i in range(len(asci1)):
    if(asci1[i]>asci2[i]):
        print('1')
        break
    elif(asci1[i]<asci2[i]):
        print('-1')
        break
    elif(asci1[i]==asci2[i] and i==(len(asci1)-1)):
        print('0')
        break
