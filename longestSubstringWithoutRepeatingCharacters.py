# 3. Longest Substring Without Repeating Characters
# Solved
# Medium
# Topics
# Companies
# Hint
# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

# My Solution:
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen=set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
                
            seen.add(s[r]) 
            res=max(res, (r - l)+1)
            
        return res 

        ## Time complexity: O(n)
        ## Space complexity: O(n)


# Other Solutions:
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l,r=0,0
        count=float('-inf')
        while r<len(s):
            if s[r] in s[l:r]:
                l+=1
            else:
                count=max(count,r-l+1)
                r+=1
        return count if count!=float('-inf') else 0
    
    # Time complexity: O(n)
    # Space complexity: O(n)