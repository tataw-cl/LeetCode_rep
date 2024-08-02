# 344. Reverse String
# Easy
# Topics
# Companies
# Hint
# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is a printable ascii character.

# My Solution
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

# Time complexity: O(N)
# Space complexity: O(1)

# Leetcode Solution
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1

# Time complexity: O(N)
# Space complexity: O(1)

# Using Recursion
class Solution:
    def reverseString(self, s: List[str]) -> None:
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)
        helper(0, len(s) - 1)

# Time complexity: O(N)
# Space complexity: O(N) due to the recursion stack

# Other Solution
class Solution(object):
    def reverseString(self, s):
       s[:] = s[::-1]
       return s 
    
# Time complexity: O(N)
# Space complexity: O(1)

# Using Two Pointers
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# Time complexity: O(N)
# Space complexity: O(1)

# Using Pythonic way
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]


# Time complexity: O(N)
# Space complexity: O(1)

# Using Stack
class Solution:
    def reverseString(self, s: List[str]) -> None:
        stack = []
        for i in range(len(s)):
            stack.append(s.pop())
        for i in range(len(stack)):
            s.append(stack.pop())

# Time complexity: O(N)
# Space complexity: O(N)

# other solution

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l,r= 0,len(s)-1
        while l< r:
            s[l],s[r] = s[r],s[l]
            l+=1
            r-=1

# Time complexity: O(N)
# Space complexity: O(1)