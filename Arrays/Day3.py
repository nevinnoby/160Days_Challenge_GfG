# Question
# Reverse an Array
# Difficulty: EasyAccuracy: 55.32%Submissions: 116K+Points: 2
# You are given an array of integers arr[]. Your task is to reverse the given array.

# Note: Modify the array in place.

class Solution:
    def reverseArray(self, arr):
        # code here
        n=len(arr)
        temp=[0]*n
        for i in range(0,n,1):
            temp[n-i-1]=arr[i]
        for i in range(0,n,1):
            arr[i]=temp[i]
        
        
