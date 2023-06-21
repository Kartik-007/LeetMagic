"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:

Input: s = "()"
Output: true

"""

#Basic Approach
#If open bracket then push into stack
#Once you encounter a closed bracket see if the stack is not empty and the top of the stack has the corresponding open bracket if so cont else false
# Go over entire string to and check if stack is empty at the end

#Solution

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if(len(s)%2 != 0):
            return False

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif char == ')':
                if len(stack) == 0:
                    return False
                topStack = stack.pop()
                if '(' != topStack:
                    return False 
            elif char == ']':
                if len(stack) == 0:
                    return False
                topStack = stack.pop()
                if '[' != topStack:
                    return False 
            elif char == '}':
                if len(stack) == 0:
                    return False
                topStack = stack.pop()
                if '{' != topStack:
                    return False 
        if (len(stack) != 0):
            return False
            
        return True

#Time O(n) 
#Space O(n) for stack
    
