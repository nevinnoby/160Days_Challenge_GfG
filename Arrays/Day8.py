# Question
# Stock Buy and Sell – Max one Transaction Allowed
# Difficulty: EasyAccuracy: 49.33%Submissions: 59K+Points: 2
# Given an array prices[] of length n, representing the prices of the stocks on different days. The task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then return 0.

class Solution:
    def maximumProfit(self, prices):
        # code here
        n=len(prices)
        min,max,ans,profit=0,0,0,0
        min=prices[0]
        for x in prices:
            if(x<min):
                min=x
            profit=x-min
            if(profit>max):
                max=profit
            
        return max
                