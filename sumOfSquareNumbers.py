# 633. Sum of Square Numbers
# Solved
# Medium
# Topics
# Companies
# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

# Example 1:

# Input: c = 5
# Output: true
# Explanation: 1 * 1 + 2 * 2 = 5
# Example 2:

# Input: c = 3
# Output: false
 

# Constraints:

# 0 <= c <= 231 - 1


#My Solution:
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        l,r=0,int(c**0.5)
        while l<=r:
            currSum=(l**2) + (r**2)
            if currSum > c:
                r-=1
            elif currSum < c:
                l+=1
            elif currSum==c:
                return True
            
        return False
    

#Time complexity: O(sqrt(c))
#Space complexity: O(1)


#Other solution:
class Solution(object):
    def judgeSquareSum(self, c):
        divisor=2
        while divisor*divisor<=c:
            if c%divisor==0:
                exponentCount=0
                while c%divisor==0:
                    exponentCount+=1
                    c//=divisor
                if divisor%4==3 and exponentCount%2!=0:
                    return False
            divisor+=1
        return c%4!=3
    
#Time complexity: O(sqrt(c))
#Space complexity: O(1)