# 1347. Minimum Number of Steps to Make Two Strings Anagram
# Medium
# Topics
# Companies
# Hint
# You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

# Return the minimum number of steps to make t an anagram of s.

# An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

 

# Example 1:

# Input: s = "bab", t = "aba"
# Output: 1
# Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
# Example 2:

# Input: s = "leetcode", t = "practice"
# Output: 5
# Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
# Example 3:

# Input: s = "anagram", t = "mangaar"
# Output: 0
# Explanation: "anagram" and "mangaar" are anagrams. 
 

# Constraints:

# 1 <= s.length <= 5 * 104
# s.length == t.length
# s and t consist of lowercase English letters only.

# My solution:
class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        count_s=Counter(s)
        count_t=Counter(t)
        res=0
        for letter in count_s:
            if count_s[letter] > count_t[letter]:
                res+=count_s[letter]-count_t[letter]
        return res
    
# Time complexity: O(n)
# Space complexity: O(n)

#Other solutions:
def minSteps(self, s: str, t: str) -> int:
        return sum((Counter(s) - Counter(t)).values())

# Time complexity: O(n)
# Space complexity: O(n)


# Other approach 1: Counting alphabets
from collections import Counter
class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        res = 0
        for i in range(26):
            if s.count(chr(i+97)) - t.count(chr(i+97)) > 0:
                res += s.count(chr(i+97)) - t.count(chr(i+97))
        return res
    # Time complexity: O(n)
    # Space complexity: O(1)

# Other approach 2: Counting alphabets
class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        s_characters = collections.defaultdict(lambda: 0)
        t_characters = collections.defaultdict(lambda: 0)

        num_steps = 0

        for c in s:
            s_characters[c] += 1
        for c in t:
            t_characters[c] += 1

        for c in t_characters:
            if c not in s_characters:
                num_steps += t_characters[c]
            elif c in s_characters and t_characters[c] > s_characters[c]:
                num_steps += (t_characters[c] - s_characters[c])

        return num_steps
    # Time complexity: O(n)
    # Space complexity: O(n)