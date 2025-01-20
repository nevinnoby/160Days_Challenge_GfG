# Question
# Move All Zeroes to End
# Difficulty: EasyAccuracy: 45.51%Submissions: 274K+Points: 2
# You are given an array arr[] of non-negative integers. Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.

#User function Template for python3
class Solution:
	def pushZerosToEnd(self,arr):
		n=len(arr)
    	temp=[0]*n
        j=0
    	for i in range(0,n,1):
            if(arr[i]!=0):
                temp[j]=arr[i]
                j=j+1
        for i in range(0,n,1):
    	     arr[i]=temp[i]