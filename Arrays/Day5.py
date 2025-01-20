# Question
# Next Permutation
# Difficulty: MediumAccuracy: 40.66%Submissions: 184K+Points: 4
# Given an array of integers arr[] representing a permutation, implement the next permutation that rearranges the numbers into the lexicographically next greater permutation. If no such permutation exists, rearrange the numbers into the lowest possible order (i.e., sorted in ascending order). 

# Note - A permutation of an array of integers refers to a specific arrangement of its elements in a sequence or linear order.




#User function Template for python3

#Partially correct
class Solution:
    def nextPermutation(self, arr):
        # code here
        
        n=len(arr)
        flag=0
        for i in range(1,n,1):
            if(arr[n-i-1]<arr[n-i]):
                t=arr.index(arr[n-i-1])
               
                flag=1
                p=n-arr.index(arr[n-i])
                break
        if(flag==1):
            
            for j in range(n-1,t-1,-1):
                if(arr[j]>arr[t]):
                    temp=arr[j]
                    arr[j]=arr[t]
                    arr[t]=temp
                    arr[-p:]=arr[-p:][::-1]
                    break
            
            
        else:
            arr.sort()
            
       
               