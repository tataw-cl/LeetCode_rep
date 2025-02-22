# 498. Diagonal Traverse
# Solved
# Medium
# Topics
# Companies
# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

# Example 1:


# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]
# Example 2:

# Input: mat = [[1,2],[3,4]]
# Output: [1,2,3,4]
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# -105 <= mat[i][j] <= 105


#My Solution:
class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        if not mat or not mat[0]:
            return []
        result=[]
        n,m=len(mat),len(mat[0])
        for d in range((m+n)-1):
            if d<m:
                row=0
                col=d
            else:
                row=d-m+1
                col=m-1
            diagonal=[]
            while row<n and col>=0:
                diagonal.append(mat[row][col])
                row+=1
                col-=1
            if d%2==0:
                result.extend(reversed(diagonal))
            else:
                result.extend(diagonal)
        return result
    
    #Time Complexity: O(mn)
    #Space Complexity: O(1)

#Other Solution:
class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        if not mat or not mat[0]:
            return []
        result=[]
        n,m=len(mat),len(mat[0])
        for d in range((m+n)-1):
            if d%2==0:
                row=max(0,d-m+1)
                col=min(d,m-1)
            else:
                row=min(d,n-1)
                col=max(0,d-n+1)
            while row>=0 and col<m:
                result.append(mat[row][col])
                row-=1
                col+=1
        return result
    
    #Time Complexity: O(mn)
    #Space Complexity: O(1)

    #Other Solution:
    import heapq as hq

class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        m = len(mat)
        n = len(mat[0])
        
        i = 0
        j = 0
        output = []

        for _ in range(m * n):
            output.append(mat[i][j])

            

            if (i+j) % 2 == 0:  # Even dist means moving upward diagonally
                if j == n - 1:  # If at the last column, move down
                    i += 1
                elif i == 0:  # If at the first row, move right
                    j += 1
                else:  # Otherwise, move diagonally up-right
                    i -= 1
                    j += 1
            else:  # Odd dist means moving downward diagonally
                if i == m - 1:  # If at the last row, move right
                    j += 1
                elif j == 0:  # If at the first column, move down
                    i += 1
                else:  # Otherwise, move diagonally down-left
                    i += 1
                    j -= 1

        return output



#Time Complexity: O(mn)
#Space Complexity: O(1)