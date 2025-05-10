# 74. Search a 2D Matrix
# Solved
# Medium
# Topics
# Companies
# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

 

# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104



# #My Solution:
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m,n=len(matrix), len(matrix[0])
        top,bot=0,m-1
        while top<=bot:
            row=(top+bot)//2
            if matrix[row][0] > target:
                bot=row-1
            elif matrix[row][-1] < target:
                top=row+1
            else:
                break

        if not (top<=bot):
            return False
        
        row=(top+bot)//2
        l,r=0,n-1
        while l<=r:
            mid=(l+r)//2
            if matrix[row][mid] < target:
                l=mid+1
            elif matrix[row][mid] > target:
                r=mid-1
            else:
                return True

        return False
    

# #Time Complexity: O(log(m + n))
# #Space Complexity: O(1)


# #Other Solution:
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        
        while l <= r:
            mid = (l + r) // 2
            mid_val = matrix[mid // n][mid % n]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
    

#     #Time Complexity: O(log(m * n))
#     #Space Complexity: O(1)
