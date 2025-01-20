# Question
# Majority Element II
# Difficulty: MediumAccuracy: 48.1%Submissions: 120K+Points: 4
# You are given an array of integer arr[] where each number represents a vote to a candidate. Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return an empty array. 

# Note: The answer should be returned in an increasing format.



class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        n=len(arr)
        n1, n2, c1, c2 = 0, 0, 0, 0
        for x in arr:
            if(x==n1):
               c1=c1+1
            elif(x==n2):
                c2=c2+1
            elif(c1==0):
                n1=x
                c1=1
            elif(c2==0):
                n2=x
                c2=1
            else:
                c1=c1-1
                c2=c2-1
        c1,c2=0,0      
        for x in arr:
            if(n1==x):
                c1=c1+1
            elif(n2==x):
                c2=c2+1
        ans=[]
        if(c1>n/3):
            # print(n1,end=" ")
            ans.append(n1)
        if(c2>n/3):
            # print(n2)
            ans.append(n2)
        ans.sort()
        return ans