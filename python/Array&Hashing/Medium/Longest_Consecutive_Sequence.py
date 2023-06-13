"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""

#Basic Approach
#Put everything into set
#Check if numbers have left neighbors aka they are the start of sequences
#If they don't then we check how many consecutive elements are in the set and update longest
# If they aren't start of sequences then we skip them

#Solution (Using set and left neighbor)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

# Time = O(n)
# Space = O(n)


#Basic Approach
#Sort the list and remove the duplicates using itertools library
#Iterate through this non duplicated list and then check for consecutive numbers

#My orginal solution(not valid)

import itertools
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxSeq = 0
        count = 1
        sortList = list(sorted(nums))
        nonDup = [key for key, group in itertools.groupby(sortList)]
        if len(nums) == 0:
            return 0
        prev = nonDup[0]
        for i in range(0, len(nonDup)):
            if i == 0:
                continue
            if nonDup[i] != (prev + 1):
                if count > maxSeq:
                    maxSeq = count

                count = 1
                prev = nonDup[i]
            else:
                count += 1
                prev = nonDup[i]
        if count > maxSeq:
            maxSeq = count
        return maxSeq
      
# Time = O(n log n) cause of sorting
# Space = O(n) 
