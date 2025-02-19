# 202. Happy Number
# Easy
# Topics
# Companies
# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

 

# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# Example 2:

# Input: n = 2
# Output: false

#My Solution:
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen_Number=set()
        def SumOfSquares(x):
            Sum=0
            while x>0:
                digit=x%10
                x=x//10
                Sum+=digit**2
            return Sum
        while n not in seen_Number:
            seen_Number.add(n)
            n=SumOfSquares(n)
        return n==1
    #Time Complexity: O(logn)
    #Space Complexity: O(logn) because of seen_Number set

    #Other Solution:
    class Solution(object):
        def isHappy(self, n):
            """
            :type n: int
            :rtype: bool
            """
            def get_next(n):
                total_sum=0
                while n>0:
                    n,digit=divmod(n,10)
                    total_sum+=digit**2
                return total_sum
            slow_runner=n
            fast_runner=get_next(n)
            while fast_runner!=1 and slow_runner!=fast_runner:
                slow_runner=get_next(slow_runner)
                fast_runner=get_next(get_next(fast_runner))
            return fast_runner==1
        #Time Complexity: O(logn)
        #Space Complexity: O(1) because of slow_runner and fast_runner variables