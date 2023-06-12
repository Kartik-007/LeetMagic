"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

#Basic Approach
#Create a dictionary for each row, col and 3x3 box
#Loop over grid once and if the entry is not "." then update the relavant row, col and 3x3 grid dictionaries.
# box_index = (i // 3 ) * 3 + j // 3 is a unique index to identify the 3x3 grids
#Check if in any of the dictionaries the number occurs more than one, if so then return false

#Solution

from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [defaultdict(int) for _ in range(9)]
        cols = [defaultdict(int) for _ in range(9)]
        boxes = [defaultdict(int) for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    num = int(num)
                    box_index = (i // 3 ) * 3 + j // 3
                    
                    rows[i][num] += 1
                    cols[j][num] += 1
                    boxes[box_index][num] += 1

                    if rows[i][num] > 1 or cols[j][num] > 1 or boxes[box_index][num] > 1:
                        return False
        return True
      
# Time = O(n^2)
# Space = O(n) 

#Solution 2(Using sets)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True

# Time = O(n^2)
# Space = O(n)
      
