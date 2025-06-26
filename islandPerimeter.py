# 463. Island Perimeter
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

# Example 1:


# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
# Example 2:

# Input: grid = [[1]]
# Output: 4
# Example 3:

# Input: grid = [[1,0]]
# Output: 4
 

# Constraints:

# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 100
# grid[i][j] is 0 or 1.
# There is exactly one island in grid.


#My Solution:
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter=0
        rows=len(grid)
        cols=len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    perimeter+=4

                    if row+1 <rows and grid[row+1][col]==1:
                        perimeter-=2

                    if col+1 < cols and grid[row][col+1]==1:
                        perimeter-=2

        return perimeter
    
    #Time Complexity: O(n^2)
    #Space Complexity: O(1)