"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

"""

#Basic Approach
#If the length of the two strings are different then return false
#Initialize two dictionaries to create and count each letter in the string and then compare the two dictionaries to see if they are the same or not

#My Solution

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
    
#Time: O(N)
#Space: O(N)
      
#My Original Sol

#Ran slower potentially due to the use of the Counter data structure which uses dictionary underneath and hence might have some extra overhead.
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sett = Counter()
        settt = Counter()
        for char in s:
            sett[char] += 1
        
        for char in t:
            settt[char] += 1

        return sett == settt
      

   
