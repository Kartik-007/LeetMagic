"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

"""

#Basic Approach
# a + b + c = 0
#Sort the numbers and pick unique values of a's
#For every a apply 2 ptr approach for two sum || to find b and c where lptr is b and rptr is c
#If 3sum 0 then add to res, increment l and r to ensure different b and c to avoid duplicates
#If 3sum less then increment l else decrement r

#Solution

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        toreturn = []
        #sort so we can use 2ptr approach on the second and third values of the triplet
        sort = sorted(nums)
        for i in range(len(sort)):
            #don't allow the first value to be the same as we would get the same triplet
            if (i > 0 and sort[i] == sort[i-1]):
                continue
            #set l and r pointers same as two sum || to find 2nd and 3rd values in triplet
            lptr = i + 1
            rptr = len(sort) - 1
            while (lptr < rptr):
                threesum = sort[i] + sort[lptr] + sort[rptr]
                #Add to list of sum is 0
                if threesum == 0:
                    toreturn.append([sort[i], sort[lptr], sort[rptr]])
                    #Move l and r until the next l and r are not the same as the ones in the valid solution
                    while lptr < rptr and sort[lptr] == sort[lptr + 1]:
                        lptr += 1
                    while lptr < rptr and sort[rptr] == sort[rptr - 1]:
                        rptr -= 1
                    #Actually increment them to the new values when found
                    lptr += 1
                    rptr -= 1
                    #If sum too low then increase l
                elif threesum < 0:
                    lptr += 1
                    #I sum too much decrease r
                else:
                    rptr -= 1
        return toreturn
    
# Time = O(n^2) + O(n log n) --> O(n^2)
# Space = O(n) as sorting requires memory
