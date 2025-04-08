# 9. Palindrome Number
# Solved
# Easy
# Topics
# Companies
# Hint
# Given an integer x, return true if x is a palindrome, and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1
 

# Follow up: Could you solve it without converting the integer to a string?


#My Solution:
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s=str(x)
        s1=s[::-1]
        if s==s1:
            return True
        else:
            return False
        
        #Time complexity: O(n) where n is the number of digits in the input number.
        #Space complexity: O(n) because we are storing the string representation of the number.
        #The space complexity is O(n) because we are storing the string representation of the number.


#Other Solutions:
#The above solution uses string manipulation to check if the number is a palindrome.
#We can also solve this problem without converting the integer to a string.
#We can reverse the number and compare it with the original number.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        else:
            rev=0
            temp=x
            while temp!=0:
                rev=rev*10+temp%10
                temp//=10
            return rev==x
        
        #Time complexity: O(log10(n)) where n is the input number.
        #Space complexity: O(1) because we are using a constant amount of space.
        #The space complexity is O(1) because we are not using any additional data structures that grow with the input size.