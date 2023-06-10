"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

"""

#Basic Approach
#Use a defaultdict to count up the frequencies of each number
#Then use a lambda function in sorted to sort on the values of the dictionary and set reverse ture as we need a descending order
#We now have a sorted list of tuples and can run a for loop k times to add the first index of the tuples(aka the number) to our return list

#Solution

from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lis = []
        c = defaultdict(int)
        for num in nums:
            c[num] += 1

        sortedTups = sorted(c.items(), key=lambda item: item[1], reverse=True)

        for idx in range(0, k):
            
            lis.append(sortedTups[idx][0])
        
        return lis

#Time O(n log n) since we are sorting
#Space O(n)
    
