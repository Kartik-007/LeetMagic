"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

"""

#Basic Approach
# Remove all alphanum characters and convert to lower case
# See if reversed and original string are the same

#Solution

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ''.join(ch for ch in s if ch.isalnum())
        newstr = newstr.lower()
        rev = newstr[::-1]
        if(newstr == rev):
            return True
        else:
            return False
    
# Time = O(n)
# Space = O(n)

#Solution 2
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while l < r and not self.alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    # Could write own alpha-numeric function
    def alphanum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )
# Time = O(n)
# Space = O(1)
      
