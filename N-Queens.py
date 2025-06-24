# 51. N-Queens
# Solved
# Hard
# Topics
# premium lock icon
# Companies
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

# Example 1:


# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
# Example 2:

# Input: n = 1
# Output: [["Q"]]
 

# Constraints:

# 1 <= n <= 9


#My Solution:
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        #Sets to track columns and diagonals which are out of bound
        columns=set()
        leftDiag=set()
        rightDiag=set()

        # n x n board of dots(".")
        board=[["."]*n for _ in range(n)]
        # print(board)
        res=[]

        def backtrack(row):
#if we've passed the last row i.e we're at n, we've found a solution and add to the result and return
            if row==n:
                temp=[]
                for r in board:
                    rowN="".join(r)
                    temp.append(rowN)
                res.append(temp)
                
                return

#iterate through each column and check if this arrangement satisfies all conditions, else continue to next column
            for col in range(n):
                if (col in columns) or (row-col in rightDiag) or (row+col in leftDiag):
                    continue
#if valid place a queen, backtrack and continue to the next row and check if it's valid as well
                board[row][col]="Q"
                columns.add(col)
                rightDiag.add(row-col)
                leftDiag.add(row+col)
                backtrack(row+1)

#if a row isn't valid, remove the previous arrangement and go to the next column of current iteration of loop
                board[row][col]="."
                columns.remove(col)
                rightDiag.remove(row-col)
                leftDiag.remove(row+col)

        backtrack(0)    
        return res
    

    #Time Complexity: O(n!)
    #Space Complexity: O(n^2)


    #Other Solutions:
     def solveNQueens(self, n):
         def solve(row, cols, diags1, diags2):
                if row == n:
                    board = []
                    for i in range(n):
                        board.append("".join("Q" if j in cols else "." for j in range(n)))
                    res.append(board)
                    return
                for col in range(n):
                    if col in cols or (row - col) in diags1 or (row + col) in diags2:
                        continue
                    cols.add(col)
                    diags1.add(row - col)
                    diags2.add(row + col)
                    solve(row + 1, cols, diags1, diags2)
                    cols.remove(col)
                    diags1.remove(row - col)
                    diags2.remove(row + col)

            res = []
            solve(0, set(), set(), set())
            return res
    
# Time Complexity: O(n!)
# Space Complexity: O(n^2)
