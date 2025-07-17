# 542. 01 Matrix
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two cells sharing a common edge is 1.

 

# Example 1:


# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
# Example 2:


# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.
 

# Note: This question is the same as 1765: https://leetcode.com/problems/map-of-highest-peak/

#My Solution:
from collections import deque
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(mat), len(mat[0])
        dist = [[float('inf')] * cols for _ in range(rows)]
        queue = deque()

        # Initialize the queue with all 0s and set their distance to 0
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if dist[nr][nc] > dist[r][c] + 1:
                        dist[nr][nc] = dist[r][c] + 1
                        queue.append((nr, nc))

        return dist
    
        #Time Complexity: O(m * n), where m is the number of rows and n is the number of columns in the matrix.
        #Space Complexity: O(m * n), for the distance matrix and the queue used in BFS.

