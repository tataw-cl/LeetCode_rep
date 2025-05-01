# 509. Fibonacci Number
# Solved
# Easy
# Topics
# Companies
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

 

# Example 1:

# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example 2:

# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# Example 3:

# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

# Constraints:

# 0 <= n <= 30


#My Solution:
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)

            #Time Complexity: O(2^n)
            #Space Complexity: O(n)
# 1. The time complexity is O(2^n) because the function makes two recursive calls for each value of n,
# leading to an exponential growth in the number of calls.
# 2. The space complexity is O(n) because the maximum depth of the recursion stack is n, which occurs when n is 0 or 1.


#Other Solutions:
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            fib = [0] * (n + 1)
            fib[0] = 0
            fib[1] = 1
            for i in range(2, n + 1):
                fib[i] = fib[i - 1] + fib[i - 2]
            return fib[n]

            #Time Complexity: O(n)
            #Space Complexity: O(n)
# 1. The time complexity is O(n) because we are iterating through the list of Fibonacci numbers once.
# 2. The space complexity is O(n) because we are using a list to store the Fibonacci numbers. In the worst case,
# all Fibonacci numbers could be stored in the list.

