# 844. Backspace String Compare
# Easy
# Topics
# Companies
# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

 

# Example 1:

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
# Example 2:

# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
# Example 3:

# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".
 

# Constraints:

# 1 <= s.length, t.length <= 200
# s and t only contain lowercase letters and '#' characters.
 

# Follow up: Can you solve it in O(n) time and O(1) space?

# My solution:
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack_s=[]
        stack_t=[]
        for char in t:
            if char == "#" and stack_t:
                stack_t.pop()
            elif char!="#":
                stack_t.append(char)
        for char in s:
            if char == "#" and stack_s:
                stack_s.pop()
            elif char!="#":
                stack_s.append(char)
        if stack_s==stack_t:
            return True
        else:
            return False
# Time complexity: O(n)
# Space complexity: O(n)

#Comparing with other solutions:
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def build(s):
            ans = []
            for c in s:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return ans
        return build(s) == build(t)
# Time complexity: O(n)
# Space complexity: O(n)