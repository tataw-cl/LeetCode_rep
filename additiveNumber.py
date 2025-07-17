# 306. Additive Number
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# An additive number is a string whose digits can form an additive sequence.

# A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

# Given a string containing only digits, return true if it is an additive number or false otherwise.

# Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

 

# Example 1:

# Input: "112358"
# Output: true
# Explanation: 
# The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
# 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# Example 2:

# Input: "199100199"
# Output: true
# Explanation: 
# The additive sequence is: 1, 99, 100, 199. 
# 1 + 99 = 100, 99 + 100 = 199
 

# Constraints:

# 1 <= num.length <= 35
# num consists only of digits.
 

# # Follow up: How would you handle overflow for very large input integers?


#My Solution:
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        #Helper function to check if the next strings are valid sequences
        def validSequence(first,second,leftover):
            while leftover:
                nextNum=first+second
                nextNumStr=str(nextNum)

                if not leftover.startswith(nextNumStr):
                    return False

                first=second
                second=nextNum
                leftover=leftover[len(nextNumStr):]

            return True



        n=len(num)

        #Time Complexity: O(n^3) - The outer loop runs for the first number, the middle loop runs for the second number, and the inner loop checks the sequence validity.
        #Space Complexity: O(1) - The space used is constant, as we are only using a few variables to store the indices and the current numbers in the sequence.


class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        
        for i in range(1, n // 2 + 1):
            for j in range(i + 1, n - i + 1):
                a, b = num[:i], num[i:j]
                if (len(a) > 1 and a[0] == '0') or (len(b) > 1 and b[0] == '0'):
                    continue
                
                while j < n:
                    c = str(int(a) + int(b))
                    if not num.startswith(c, j):
                        break
                    j += len(c)
                    a, b = b, c
                
                if j == n:
                    return True
        
        return False

# Time Complexity: O(n^2) - where n is the length of the input string num. The nested loops iterate through possible lengths for the first two numbers in the sequence.
# Space Complexity: O(1) - The space used is constant, as we are only using a few variables to store the indices and the current numbers in the sequence.

