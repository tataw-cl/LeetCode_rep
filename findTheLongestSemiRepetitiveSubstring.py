# 2730. Find the Longest Semi-Repetitive Substring
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given a digit string s that consists of digits from 0 to 9.

# A string is called semi-repetitive if there is at most one adjacent pair of the same digit. For example, "0010", "002020", "0123", "2002", and "54944" are semi-repetitive while the following are not: "00101022" (adjacent same digit pairs are 00 and 22), and "1101234883" (adjacent same digit pairs are 11 and 88).

# Return the length of the longest semi-repetitive substring of s.

 

# Example 1:

# Input: s = "52233"

# Output: 4

# Explanation:

# The longest semi-repetitive substring is "5223". Picking the whole string "52233" has two adjacent same digit pairs 22 and 33, but at most one is allowed.

# Example 2:

# Input: s = "5494"

# Output: 4

# Explanation:

# s is a semi-repetitive string.

# Example 3:

# Input: s = "1111111"

# Output: 2

# Explanation:

# The longest semi-repetitive substring is "11". Picking the substring "111" has two adjacent same digit pairs, but at most one is allowed.

 

# Constraints:

# 1 <= s.length <= 50
# '0' <= s[i] <= '9'

# My Solution:
class Solution(object):
    def longestSemiRepetitiveSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        pairOccurence=0
        l=0
        res=0
        for r in range(n):
            if r>0 and s[r]==s[r-1]:
                pairOccurence+=1
            while pairOccurence>1:
                if l<n-1 and s[l]==s[l+1]:
                    pairOccurence-=1
                l+=1
            res=max(res,(r-l)+1)
        return res
    
    # Time complexity: O(n)
    # Space complexity: O(1)


    # Other Solutions:
    class Solution(object):
    def longestSemiRepetitiveSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        count = 0
        repeated_ind = 0
        max_len = 1

        for right in range(1, len(s)):

            if s[right] == s[right-1]:
                #print(count, left, right)
                if count == 0:
                    repeated_ind = right
                    count += 1
                else:
                    left = repeated_ind
                    repeated_ind = right
            
            max_len = max(max_len, right+1-left)

        return max_len 
    
    # Time complexity: O(n)
    # Space complexity: O(1)