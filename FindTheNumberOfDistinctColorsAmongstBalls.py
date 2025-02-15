
# Code


# Testcase
# Testcase
# Test Result
# 3160. Find the Number of Distinct Colors Among the Balls
# Attempted
# Medium
# Topics
# Companies
# Hint
# You are given an integer limit and a 2D array queries of size n x 2.

# There are limit + 1 balls with distinct labels in the range [0, limit]. Initially, all balls are uncolored. For every query in queries that is of the form [x, y], you mark ball x with the color y. After each query, you need to find the number of colors among the balls.

# Return an array result of length n, where result[i] denotes the number of colors after ith query.

# Note that when answering a query, lack of a color will not be considered as a color.

 

# Example 1:

# Input: limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]

# Output: [1,2,2,3]

# Explanation:



# After query 0, ball 1 has color 4.
# After query 1, ball 1 has color 4, and ball 2 has color 5.
# After query 2, ball 1 has color 3, and ball 2 has color 5.
# After query 3, ball 1 has color 3, ball 2 has color 5, and ball 3 has color 4.
# Example 2:

# Input: limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]

# Output: [1,2,2,3,4]

# Explanation:



# After query 0, ball 0 has color 1.
# After query 1, ball 0 has color 1, and ball 1 has color 2.
# After query 2, ball 0 has color 1, and balls 1 and 2 have color 2.
# After query 3, ball 0 has color 1, balls 1 and 2 have color 2, and ball 3 has color 4.
# After query 4, ball 0 has color 1, balls 1 and 2 have color 2, ball 3 has color 4, and ball 4 has color 5.
 

# Constraints:

# 1 <= limit <= 109
# 1 <= n == queries.length <= 105
# queries[i].length == 2
# 0 <= queries[i][0] <= limit
# 1 <= queries[i][1] <= 109

#My solution:
class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        colors_Dict = {}
        color_Count = {}
        result = []

        for i, j in queries:
            if i in colors_Dict:
                old_color = colors_Dict[i]
                if old_color != j or old_color==j:
                    color_Count[old_color] -= 1
                    if color_Count[old_color] == 0:
                        del color_Count[old_color]
            
            
            colors_Dict[i] = j

            if j in color_Count:
                color_Count[j] += 1
            else:
                color_Count[j] = 1

            result.append(len(color_Count))

        return result
    #Time complexity: O(n)
    #Space complexity: O(n)

#Other solutions:
class Solution(object):
    def countColors(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        colors = [0] * (limit + 1)
        colorCount = 0
        result = []
        for query in queries:
            ball, color = query
            if colors[ball] == 0:
                colorCount += 1
            colors[ball] = color
            result.append(colorCount)
        return result
    #Time complexity: O(n)
    #Space complexity: O(n)