# 20. Valid Parentheses
# Easy
# Topics
# Companies
# Hint
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

# My solution:
def isValid(s):
    # Stack to keep track of opening parentheses
    stack = []
    
    # Mapping of closing to opening parentheses
    mapping = {')': '(', ']': '[', '}': '{'}
    
    # Iterate through the string
    for char in s:
        # If the character is a closing parenthesis
        if char in mapping:
            # Pop the top element from the stack if it is not empty, otherwise assign a dummy value
            top_element = stack.pop() if stack else '#'
            
            # The mapping for the closing parenthesis must match the top element of the stack
            if mapping[char] != top_element:
                return False
        else:
            # It is an opening parenthesis, push onto the stack
            stack.append(char)
    
    # If the stack is empty, all parentheses are matched
    return not stack

# Example usage:
print(isValid("()"))     # Output: True
print(isValid("()[]{}")) # Output: True
print(isValid("(]"))     # Output: False
print(isValid("([)]"))   # Output: False
print(isValid("{[]}"))   # Output: True