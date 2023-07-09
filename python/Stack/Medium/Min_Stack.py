"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

"""

#Basic Approach
#Keep two stacks one to track elements and the other to track the minimum
#Remove and add to the minimum stack if old min is removed or a newer min is added

#Solution

class MinStack:

    def __init__(self):
        self.stack = []
        self.minumHist = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minumHist) == 0 or val <= self.minumHist[-1]:
            self.minumHist.append(val)
        
    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        if(self.stack[-1] == self.minumHist[-1]):
            self.minumHist.pop()
        self.stack.pop()

    def top(self) -> int:
        r = self.stack[-1]
        return r

    def getMin(self) -> int:
        if len(self.minumHist) == 0:
            return   # Stack is empty
        return self.minumHist[-1]



#Time O(1) 
#Space O(n) for stack
    
