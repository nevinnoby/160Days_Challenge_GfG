# Question
# Minimize the Heights II
# Difficulty: MediumAccuracy: 15.06%Submissions: 664K+Points: 4
# Given an array arr[] denoting heights of N towers and a positive integer K.

# For each tower, you must perform exactly one of the following operations exactly once.

# Increase the height of the tower by K
# Decrease the height of the tower by K
# Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

# You can find a slight modification of the problem here.
# Note: It is compulsory to increase or decrease the height by K for each tower. After the operation, the resultant array should not contain any negative integers.


#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        # code here
        n=len(arr)
        arr.sort()
        ans=arr[n-1]-arr[0]
        
        for i in range(1,n,1):
            if(arr[i]-k<0):
                continue
            mi=min(arr[0]+k,arr[i]-k)
            ma=max(arr[i-1]+k,arr[n-1]-k)
            ans=min(ans,ma-mi)
        return ans