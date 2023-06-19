"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

"""

#Basic Approach
#Have two pointers l and r on either side of the array
#Caclulate area of a rectangle by taking the minimum of the two l and r
#Check if its the max up until and update maxarea accordingly
#Move minimum of l or r up or down respectively (intuition-> if 1 and 7 are l and r pointer respectively then moving r down will gurantee smaller area)

#Solution

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        lptr = 0
        rptr = len(height) - 1
        while (lptr < rptr):
            mincutoff = min(height[lptr], height[rptr])
            area = mincutoff * (rptr - lptr)
            if area > maxArea:
                maxArea = area
            if height[lptr] >= height[rptr]:
                rptr -= 1
            else:
                lptr += 1
        return maxArea

# Time = O(n)
# Space = O(1)

      
