# Add Binary Strings
# Question
# Given two binary strings s1 and s2 consisting of only 0s and 1s. Find the resultant string after adding the two Binary Strings.
# Note: The input strings may contain leading zeros but the output string should not have any leading zeros.

#User function Template for python3
class Solution:
	def addBinary(self, s1, s2):
		# code here
		sum_b=0
		sum_b=bin(int(s1,2) + int(s2,2))[2:]
        return sum_b

