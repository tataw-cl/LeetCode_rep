# 856. Score of Parentheses
# Solved
# Medium
# Topics
# Companies
# Given a balanced parentheses string s, return the score of the string.

# The score of a balanced parentheses string is based on the following rule:

# "()" has score 1.
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.
 

# Example 1:

# Input: s = "()"
# Output: 1
# Example 2:

# Input: s = "(())"
# Output: 2
# Example 3:

# Input: s = "()()"
# Output: 2
 

# Constraints:

# 2 <= s.length <= 50
# s consists of only '(' and ')'.
# s is a balanced parentheses string.

# My Solution:
class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[0]
        for char in s:
            if char=='(':
                stack.append(0)
            else:
                top_O_Stack=stack.pop()
                if top_O_Stack == 0:
                    score=1
                else:
                    score=2*top_O_Stack
                stack[-1]+=score
        return stack[0]

# Time complexity: O(n)
# Space complexity: O(n)


# Other Solutions:
class Solution(object):
    def scoreOfParentheses(self, s):
        stack = []
        ans = 0

        for i in s:
            if i == ')':
                ans += stack.pop() + max(ans , 1)
        
            else:
                stack.append(ans)
                ans = 0
        
        return ans
    
# Time complexity: O(n)
# Space complexity: O(n)