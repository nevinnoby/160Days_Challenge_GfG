# Question
# Second Largest
# Difficulty: EasyAccuracy: 26.72%Submissions: 957K+Points: 2
# Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

# Note: The second largest element should not be equal to the largest element.

#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        n=len(arr)
        arr.sort()
     
        
        for i in range(n-2,-1,-1):
            if(arr[i]!=arr[n-1]):
                return arr[i]
        
                
        return -1