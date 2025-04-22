# 387. First Unique Character in a String
# Solved
# Easy
# Topics
# Companies
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"

# Output: 0

# Explanation:

# The character 'l' at index 0 is the first character that does not occur at any other index.

# Example 2:

# Input: s = "loveleetcode"

# Output: 2

# Example 3:

# Input: s = "aabb"

# Output: -1

 

# Constraints:

# 1 <= s.length <= 105
# s consists of only lowercase English letters.


#My Solution:
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_count=Counter(s)
        for i in range (len(s)):
            if s_count[s[i]]==1:
                return i
        return -1
    
    #Time Complexity: O(n)
    #Space Complexity: O(1)


#Other Solutions:
# Using a dictionary to count the occurrences of each character in the
# string and then checking for the first unique character.
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return -1

    #Time Complexity: O(n)
    #Space Complexity: O(1)

