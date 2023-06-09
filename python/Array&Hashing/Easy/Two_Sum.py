"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""

#Basic Approach
#Iterate over the list nums and check if the value target - the current number you are exists in a dictionary keys
#If that number exists then append the current index and the index of that number which is the value in the dictionary stored at the key target - the current
#If there is no such number then add the current number where the key is the current number and the value is the index

#My Solution

from collections import Counter
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        l = []
        for idx in range (len(nums)):
            if target - nums[idx] in a.keys():
                l.append(idx)
                l.append(a[target - nums[idx]])
                return l
            
            a[nums[idx]] = idx
        
        return l
    
#Time: O(N)
#Space: O(N)
      
