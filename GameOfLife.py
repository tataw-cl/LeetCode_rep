# 289. Game of Life
# Solved
# Medium
# Topics
# Companies
# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

# Given the current state of the board, update the board to reflect its next state.

# Note that you do not need to return anything.

 

# Example 1:


# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
# Example 2:


# Input: board = [[1,1],[1,0]]
# Output: [[1,1],[1,1]]
 

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 25
# board[i][j] is 0 or 1.
 

# Follow up:

# Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?

# My solution:
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])
        tempMat=[row[:] for row in board]
        directions=[(-1,-1),(-1,0),(0,-1),(-1,1),(1,-1),(1,1),(1,0),(0,1)]
        for row in range(m):
            for col in range(n):
                liveNeighbors=0
                for d_row,d_col in directions:
                    r=row+d_row
                    c=col+d_col
                    if 0<=r<=(m-1) and 0<=c<=(n-1) and tempMat[r][c]==1:
                        liveNeighbors+=1
                if board[row][col]==1:
                    if liveNeighbors <2 or liveNeighbors>3:
                        board[row][col]=0
                else:
                    if liveNeighbors==3:
                        board[row][col]=1

                
# Time complexity: O(n*m)
# Space complexity: O(n*m)

#Other solution:
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])
        directions=[(-1,-1),(-1,0),(0,-1),(-1,1),(1,-1),(1,1),(1,0),(0,1)]
        for row in range(m):
            for col in range(n):
                liveNeighbors=0
                for d_row,d_col in directions:
                    r=row+d_row
                    c=col+d_col
                    if 0<=r<=(m-1) and 0<=c<=(n-1) and abs(board[r][c])==1:
                        liveNeighbors+=1
                if board[row][col]==1:
                    if liveNeighbors <2 or liveNeighbors>3:
                        board[row][col]=-1
                else:
                    if liveNeighbors==3:
                        board[row][col]=2
        for row in range(m):
            for col in range(n):
                if board[row][col]>0:
                    board[row][col]=1
                else:
                    board[row][col]=0

    
# Time complexity: O(n*m)
# Space complexity : O(1) because we are using the same board to store the result