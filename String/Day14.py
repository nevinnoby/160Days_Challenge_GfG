s="1231231231311133"

flag=0
o=0
sign=1
if(s[0]=='+'):
    sign=1
    s=s[1:]
elif(s[0]=='-'):
    sign=-1
    s=s[1:]
for j in s:
    if(ord(j) < ord('0') or ord(j) > ord('9')):
        break
    
    
    i=ord(j)-ord('0')

    
    if(i==0 and flag ==0):
        continue
    
    elif(i!=0):
        flag=1
        o=o*10+i
    elif(i==0 and flag==1):
        o=o*10
o=o*sign
if(o>2**31 -1):
    print(2**31 -1) 
elif(o<-2**31 -1):
    print(-2**31)
else:
    print(o)