# 118. Pascal's Triangle
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]
 

# Constraints:

# 1 <= numRows <= 30


#My solution:
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []
        
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)
        
        return triangle
    
    #Time complexity: O(numRows^2)
    #Space complexity: O(numRows)


    #Other solutions:
    #Using list comprehension
    def generate(self, numRows: int) -> list[list[int]]:
        return [[1] * (i + 1) for i in range(numRows)] if numRows > 0 else []   
    
#Time complexity: O(numRows^2)
#Space complexity: O(numRows)
