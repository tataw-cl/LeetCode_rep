# 50. Pow(x, n)
# Medium
# Topics
# Companies
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Example 2:

# Input: x = 2.10000, n = 3
# Output: 9.26100
# Example 3:

# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25


#My Solution:
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        elif n<0:
            x=1/x
            n=-n

        half=self.myPow(x,n//2)
        if n%2==0:
            return half*half
        else:
            return half*half*x
        

        #Time Complexity: O(log n)
        #Space Complexity: O(log n)
# 1. The time complexity is O(log n) because the function reduces the problem size by half in each recursive call.
# 2. The space complexity is O(log n) because of the recursion stack, which can go up to a depth of log n in the worst case.


#Other Solutions:
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n < 0:
            x = 1 / x
            n = -n
        
        result = 1
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2
        
        return result
    

    #Time Complexity: O(log n)
    #Space Complexity: O(1)
# 1. The time complexity is O(log n) because we are halving n in each iteration of the while loop.
# 2. The space complexity is O(1) because we are using a constant amount of space for the variables result, x, and n, regardless of the size of n.
