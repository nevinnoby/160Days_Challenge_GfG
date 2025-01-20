# Question
# Stock Buy and Sell – Multiple Transaction Allowed
# Difficulty: MediumAccuracy: 13.43%Submissions: 151K+Points: 4
# The cost of stock on each day is given in an array price[]. Each day you may decide to either buy or sell the stock i at price[i], you can even buy and sell the stock on the same day. Find the maximum profit that you can get.

# Note: A stock can only be sold if it has been bought previously and multiple stocks cannot be held on any given day

from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        min,max,ans=0,0,0
        n=len(prices)
        for i in range(1,n,1):
           if(prices[i]>prices[i-1]):
               ans=ans+prices[i]-prices[i-1]
                    
        return ans

