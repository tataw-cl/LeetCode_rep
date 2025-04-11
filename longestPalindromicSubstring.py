# 5. Longest Palindromic Substring
# Solved
# Medium
# Topics
# Companies
# Hint
# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.


#My Solution:
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=""
        maxLen=0
        for i in range(len(s)):
            #Section of code to consider odd length palindromes
            l,r=i,i
            while (l>=0 and r<len(s)) and s[r]==s[l]:
                if (r-l)+1 > maxLen:
                    res=s[l:r+1]
                    maxLen=(r-l)+1
                l-=1
                r+=1
            
            #Section of code to consider even length palindromes
            l,r=i,i+1
            while ((l>=0 and r<len(s)) and s[r]==s[l]):
                if (r-l)+1 > maxLen:
                    res=s[l:r+1]
                    maxLen=(r-l)+1
                l-=1
                r+=1

        return res
    

    #Time complexity: O(n^2)
    #Space complexity: O(1)


    #Optimization:
    # The above solution can be optimized to O(n) time complexity using Manacher's algorithm.
    #Implementation:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Transform S into T.
        # For example, S = "aba", T = "^#a#b#a#$".
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range(1, n - 1):
            if i < R:
                P[i] = min(R - i, P[2 * C - i])
            # Attempt to expand palindrome centered at i
            while T[i + P[i] + 1] == T[i - P[i] - 1]:
                P[i] += 1
            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]
        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        # Extract the substring from original string.
        start = (centerIndex - maxLen) // 2
        return s[start: start + maxLen]
    

    #Time complexity: O(n)
    #Space complexity: O(n)