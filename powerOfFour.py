# 342. Power of Four
# Solved
# Easy
# Topics
# Companies
# Given an integer n, return true if it is a power of four. Otherwise, return false.

# An integer n is a power of four, if there exists an integer x such that n == 4x.

 

# Example 1:

# Input: n = 16
# Output: true
# Example 2:

# Input: n = 5
# Output: false
# Example 3:

# Input: n = 1
# Output: true
 

# Constraints:

# -231 <= n <= 231 - 1
 

# Follow up: Could you solve it without loops/recursion?


#My Solution:
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n % 4 == 0:
            n //= 4
        return n == 1

        #Time Complexity: O(log n)
        #Space Complexity: O(1)
# 1. The time complexity is O(log n) because we are dividing n by 4 in each iteration until it becomes less than or equal to 1.
# 2. The space complexity is O(1) because we are using a constant amount of space for the variables.


#Other Solutions:
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n & (n - 1)) == 0 and (n - 1) % 3 == 0

        #Time Complexity: O(1)
        #Space Complexity: O(1)
# 1. The time complexity is O(1) because we are performing a constant number of operations regardless of the size of n.
# 2. The space complexity is O(1) because we are using a constant amount of space for the variables.
