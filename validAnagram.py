# 242. Valid Anagram
# Solved
# Easy
# Topics
# Companies
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

# My solution:
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        s_Count=Counter(s)
        t_Count=Counter(t)
        if s_Count==t_Count:
            return True
        else:
            return False
        
    #Time complexity: O(n)
    #Space complexity: O(n)

    #Other solution:
    class Solution(object):
        def isAnagram(self, s, t):
            """
            :type s: str
            :type t: str
            :rtype: bool
            """
            if len(s)!=len(t):
                return False
            s_Count=[0]*26
            for i in range(len(s)):
                s_Count[ord(s[i])-ord('a')]+=1
                s_Count[ord(t[i])-ord('a')]-=1
            for i in range(26):
                if s_Count[i]!=0:
                    return False
            return True
        
        #Time complexity: O(n)
        #Space complexity: O(1)
        # The space complexity is O(1) because the size of the array is constant (26 for lowercase letters).