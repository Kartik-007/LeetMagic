"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

"""

#Basic Approach
#Have a pointer at the start and end of the list
#If the sum of the numbers of those pointers is greater than the target move left pointer down one
#If the sum is less then move the right pointer up 1

#Solution

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lptr = len(numbers) - 1
        rptr = 0
        while (rptr < lptr):
            if (numbers[rptr] + numbers[lptr]) == target:
                return [rptr + 1, lptr + 1]
            elif (numbers[rptr] + numbers[lptr]) > target:
                lptr = lptr - 1
            elif (numbers[rptr] + numbers[lptr]) < target:
                rptr = rptr + 1
        return []
    
# Time = O(n)
# Space = O(1)

      
