# 2413. Smallest Even Multiple
# Easy
# Topics
# Companies
# Hint
# Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.
 

# Example 1:

# Input: n = 5
# Output: 10
# Explanation: The smallest multiple of both 5 and 2 is 10.
# Example 2:

# Input: n = 6
# Output: 6
# Explanation: The smallest multiple of both 6 and 2 is 6. Note that a number is a multiple of itself.
 

# Constraints:

# 1 <= n <= 150

# My solution:
class Solution(object):
    def smallestEvenMultiple(self, n):
        x=2
        while n<=150:
            if x%n==0:
                return x
            else:
                x+=2

# Time complexity: O(n)
# Space complexity: O(1)
#Comparing with other solutions:
class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        return (n if n%2==0 else n*2)
# Time complexity: O(1)
# Space complexity: O(1)