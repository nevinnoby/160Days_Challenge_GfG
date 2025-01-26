# Question
# Kadane's Algorithm
# Difficulty: MediumAccuracy: 36.28%Submissions: 1MPoints: 4
# Given an integer array arr[]. You need to find the maximum sum of a subarray.

#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ##Your code here
        sum=0
        maxsum=float('-inf')
        for i in range(0,len(arr)):
            sum=sum+arr[i]
            maxsum=max(maxsum,sum)
            if(sum<0):
                sum=0
        return maxsum
            

