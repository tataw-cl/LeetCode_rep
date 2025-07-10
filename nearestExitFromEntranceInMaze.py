# 1926. Nearest Exit from Entrance in Maze
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

# In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

# Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

 

# Example 1:


# Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
# Output: 1
# Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
# Initially, you are at the entrance cell [1,2].
# - You can reach [1,0] by moving 2 steps left.
# - You can reach [0,2] by moving 1 step up.
# It is impossible to reach [2,3] from the entrance.
# Thus, the nearest exit is [0,2], which is 1 step away.
# Example 2:


# Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
# Output: 2
# Explanation: There is 1 exit in this maze at [1,2].
# [1,0] does not count as an exit since it is the entrance cell.
# Initially, you are at the entrance cell [1,0].
# - You can reach [1,2] by moving 2 steps right.
# Thus, the nearest exit is [1,2], which is 2 steps away.
# Example 3:


# Input: maze = [[".","+"]], entrance = [0,0]
# Output: -1
# Explanation: There are no exits in this maze.
 

# Constraints:

# maze.length == m
# maze[i].length == n
# 1 <= m, n <= 100
# maze[i][j] is either '.' or '+'.
# entrance.length == 2
# 0 <= entrancerow < m
# 0 <= entrancecol < n
# entrance will always be an empty cell.


#My Solution:
class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        m, n = len(maze), len(maze[0])
        queue = deque()
        queue.append((entrance[0], entrance[1], 0))
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        while queue:
            row, col, steps = queue.popleft()

            # Checking if current pos is an exit (on border and not entrance)
            if (row != entrance[0] or col != entrance[1]) and (row == 0 or row == m-1 or col == 0 or col == n-1):
                return steps

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < m and 0 <= new_col < n and maze[new_row][new_col] == '.':
                    maze[new_row][new_col] = '+'  # marking position as visited
                    queue.append((new_row, new_col, steps + 1))

        return -1
    
    #Time Complexity: O(m * n), where m is the number of rows and n is the number of columns in the maze.
    #Space Complexity: O(m * n), for the queue and the maze marking.
    

    
from collections import deque
class Solution:
    def nearestExit(self, maze, entrance):
        rows, cols = len(maze), len(maze[0])
        queue = deque([entrance])
        visited = set()
        visited.add(tuple(entrance))
        steps = 0
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                # Check if we are at an exit
                if (r != entrance[0] or c != entrance[1]) and (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                    return steps
                
                # Explore neighbors
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '.' and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            
            steps += 1
        
        return -1
    

# Time Complexity: O(m * n), where m is the number of rows and n is the number of columns in the maze.
# Space Complexity: O(m * n), for the queue and visited set.
