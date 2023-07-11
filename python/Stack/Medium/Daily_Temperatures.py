"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
"""

#Basic Approach
#Create ans list filled with 0's
#Enumerate through the list and if stack is not empty and current temp is greater than the temp at the top of the stack, pop from stack
#Calculate difference in indices as we store t and i and append diff to answer for idx th day
#Append new temp and idx to stack

#Solution

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                t, i = stack.pop()
                ans[i] = (idx - i)
            stack.append((temp, idx))
        
        return ans



#Time O(n) 
#Space O(n) for stack
    
