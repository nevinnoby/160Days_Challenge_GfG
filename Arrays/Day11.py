# Question
# Maximum Product Subarray
# Difficulty: MediumAccuracy: 18.09%Submissions: 426K+Points: 4
# Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product that we can get in a subarray of arr[].

# Note: It is guaranteed that the output fits in a 32-bit integer.

def maxProduct(self,arr):
    # code here
    
    max_=arr[0]
    min_=arr[0]
    ans=arr[0]
    for i in range(1,len(arr)):
        if(arr[i]<0):
            max_ ,min_=min_ ,max_
        max_=max(arr[i],max_*arr[i])
        min_=min(arr[i],min_*arr[i])
        ans=max(ans,max_)
    return ans
	         