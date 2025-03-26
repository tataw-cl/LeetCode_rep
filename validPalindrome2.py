# 680. Valid Palindrome II
# Solved
# Easy
# Topics
# Companies
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false
 

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.


# My Solution:
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                lSkip=s[l+1:r+1]
                rSkip=s[l:r]
                return lSkip==lSkip[::-1] or rSkip==rSkip[::-1]
            l+=1
            r-=1
        return True
    
# Time complexity: O(n)
# Space complexity: O(n)


# Other Solutions:
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return self.isPalindrome(s[l+1:r+1]) or self.isPalindrome(s[l:r])
            l+=1
            r-=1
        return True
    
    def isPalindrome(self,s):
        return s==s[::-1]
    
# Time complexity: O(n)
# Space complexity: O(n)