# Implement Atoi
# Question
# Difficulty: MediumAccuracy: 32.58%Submissions: 269K+Points: 4Average Time: 15m
# Given a string s, the objective is to convert it into integer format without utilizing any built-in functions. Refer the below steps to know about atoi() function.


class Solution:
    def myAtoi(self, s):
        # Code here
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
            i=ord(j) - ord('0')
            
            if(i==0 and flag==0):
                continue
            elif(i!=0):
                flag=1
                o=o*10+i
            elif(i==0 and flag==1):
                o=o*10
        o=o*sign
        if(o<-2**31 -1):
            return -2**31
        elif(o>2**31 -1):
            return 2**31 -1
        else:
            return o