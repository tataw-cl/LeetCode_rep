# 1849. Splitting a String Into Descending Consecutive Values
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given a string s that consists of only digits.

# Check if we can split s into two or more non-empty substrings such that the numerical values of the substrings are in descending order and the difference between numerical values of every two adjacent substrings is equal to 1.

# For example, the string s = "0090089" can be split into ["0090", "089"] with numerical values [90,89]. The values are in descending order and adjacent values differ by 1, so this way is valid.
# Another example, the string s = "001" can be split into ["0", "01"], ["00", "1"], or ["0", "0", "1"]. However all the ways are invalid because they have numerical values [0,1], [0,1], and [0,0,1] respectively, all of which are not in descending order.
# Return true if it is possible to split s​​​​​​ as described above, or false otherwise.

# A substring is a contiguous sequence of characters in a string.

 

# Example 1:

# Input: s = "1234"
# Output: false
# Explanation: There is no valid way to split s.
# Example 2:

# Input: s = "050043"
# Output: true
# Explanation: s can be split into ["05", "004", "3"] with numerical values [5,4,3].
# The values are in descending order with adjacent values differing by 1.
# Example 3:

# Input: s = "9080701"
# Output: false
# Explanation: There is no valid way to split s.
 

# Constraints:

# 1 <= s.length <= 20
# s only consists of digits.


#My Solution:
class Solution(object):
    def splitString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        
        # Try every possible first number length
        for i in range(1, n // 2 + 1):
            first_num = int(s[:i])
            current_num = first_num
            
            # Start checking from the end of the string
            j = i
            while j < n:
                current_num -= 1
                next_num_str = str(current_num)
                next_num_len = len(next_num_str)
                
                # If the next number doesn't match the substring, break
                if s[j:j + next_num_len] != next_num_str:
                    break
                
                j += next_num_len
            
            # If we reached the end of the string, return True
            if j == n:
                return True
        
        return False

# Time Complexity: O(n^2) in the worst case, where n is the length of the string. This is because we may try every possible first number and then check the rest of the string.
# Space Complexity: O(1) since we are using a constant amount of extra space for variables, regardless of the input size.

