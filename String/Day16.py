s1 = "aab"
s2 = "abb"
n=0
if(len(s1)==len(s2)):
    for i in s1:
        for j in s2:
            if(i==j):
                n=n+1
                s2=s2.replace(i,"",1)
                break
            elif(j==len(s2) and i !=j):
                print ('false')
    if(n==len(s1)):
        print('true')
    else:
        print('false')
else:
    print('false')