"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

"""

#Basic Approach
#Create a dictionary with default type list
#Loop over all the words in the list and sort the word and convert it to a tuple
#Add as the key the sorted word as a tuple and the value being the actual word act -> cat
#Return as a list the values of the dictionary

#Solution

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word))
            res[key].append(word)
        
        return list(res.values())
    
#Time: O(n * m * log(m)), where n is the length of the strs list, and m is the maximum length of the strings in strs 
#this is due to the sorting operation performed on each string using sorted(word), which has a time complexity of O(m * log(m)).
#Space:  O(n * m) where n is the length of the strs list, and m is the maximum length of the strings in strs. 
#The code uses a defaultdict called res to store the anagram groups. In the worst case scenario, where all strings are unique, 
#the defaultdict will store n key-value pairs, and each value may have a length of up to m. 
#Thus, the space complexity is proportional to the total size of the anagram groups, which is O(n * m).

#Solution 2
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()
# Time = O(n*m)
# Space = O(n*m) 
      
