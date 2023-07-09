"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 
Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""

#Basic Approach
#Keep pushing to stack if vals are numbers:
#If it is an operation remove the last two vals from the stack with the latest one being on the left of the exp
#Do the operation and append the result back into the stack
#Pop from stack at the end for final result when for loop is done

#Solution

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for val in tokens:
            if val == "+" :
                rightexp = stack.pop()
                leftexp = stack.pop()
                res = leftexp + rightexp
                stack.append(res)
            elif val == "-":
                rightexp = stack.pop()
                leftexp = stack.pop()
                res = leftexp - rightexp
                stack.append(res)
            elif val == "*" :
                rightexp = stack.pop()
                leftexp = stack.pop()
                res = leftexp * rightexp
                stack.append(res)
            elif val == "/" :
                rightexp = stack.pop()
                leftexp = stack.pop()
                res = int(leftexp / rightexp)
                stack.append(res)
            else:
                stack.append(int(val))

        return stack.pop()


#Time O(n) 
#Space O(n) for stack
    
