# 1975. Maximum Matrix Sum
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given an n x n integer matrix. You can do the following operation any number of times:

# Choose any two adjacent elements of matrix and multiply each of them by -1.
# Two elements are considered adjacent if and only if they share a border.

# Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

 

# Example 1:


# Input: matrix = [[1,-1],[-1,1]]
# Output: 4
# Explanation: We can follow the following steps to reach sum equals 4:
# - Multiply the 2 elements in the first row by -1.
# - Multiply the 2 elements in the first column by -1.
# Example 2:


# Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
# Output: 16
# Explanation: We can follow the following step to reach sum equals 16:
# - Multiply the 2 last elements in the second row by -1.
 

# Constraints:

# n == matrix.length == matrix[i].length
# 2 <= n <= 250
# -105 <= matrix[i][j] <= 105

# My solution:
class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        result=0
        n=len(matrix)
        negatives_count=0
        smallestVal=abs(matrix[0][0])
        for row in matrix:
            for value in row:
                result+=abs(value)
                if value<0:
                    negatives_count+=1
                smallestVal=min(smallestVal,abs(value))
        if negatives_count %2!=0:
            result=result-(2*smallestVal)
        return result
    
# Time complexity: O(n*m)
# Space complexity: O(1)


#Other solution:
class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n=len(matrix)
        minVal=10**5
        sumVal=0
        count=0
        for i in range(n):
            for j in range(n):
                if matrix[i][j]<0:
                    count+=1
                minVal=min(minVal,abs(matrix[i][j]))
                sumVal+=abs(matrix[i][j])
        if count%2==0:
            return sumVal
        return sumVal-2*minVal

# Time complexity: O(n*m)
# Space complexity: O(1)