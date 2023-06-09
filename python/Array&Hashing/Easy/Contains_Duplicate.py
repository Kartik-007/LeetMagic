"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

"""

#Basic Approach
#Traverse array while keeping track of numbers seen by adding them to a dictionary and changing value to 1.
#If we see a number which is in the list of the keys of the dictionary then we return true else we initialise it in the dictionary.
#If we go through the whole list nums without seeing the number then we return false

#My Solution

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictt = {}
        for num in nums:
            if num in dictt.keys():
                return True
            else:
                dictt[num] = 1
        
        return False
    
#Time: O(N)
#Space: O(N)
      
#Using set

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
      
#Alternate approach
class Solution(object):
    def containsDuplicate(self, nums):
        return True if len(nums) > len(set(nums)) else False
   
