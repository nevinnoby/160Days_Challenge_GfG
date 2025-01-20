# Question
# Rotate Array
# Difficulty: MediumAccuracy: 37.06%Submissions: 440K+Points: 4
# Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.


#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        n=len(arr)
        temp=[0]*n
        
        if(d<n):
            for i in range(0,n-d,1):
                temp[i]=arr[d+i]
            for i in range(0,d,1):
                temp[n-d+i]=arr[i]
        
        # for i in range(0,n,1):
        #         arr[i]=temp[i]
                
        else:
            d=d%n
            for i in range(0,n-d,1):
                temp[i]=arr[d+i]
            for i in range(0,d,1):
                temp[n-d+i]=arr[i]
        for i in range(0,n,1):
                arr[i]=temp[i]