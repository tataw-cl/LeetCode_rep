# 424. Longest Repeating Character Replacement
# Solved
# Medium
# Topics
# Companies
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length


# My Solution:
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        right = 0
        max_count = 0
        count = {}
        while right < len(s):
            count[s[right]] = count.get(s[right], 0) + 1
            max_count = max(max_count, count[s[right]])
            if right - left + 1 - max_count > k:
                count[s[left]] -= 1
                left += 1
            right += 1
        return right - left


        #Time Complexity: O(n)
        #Space Complexity: O(1)
        #The space complexity is O(1) because the size of the count dictionary is limited to 26 characters (A-Z).


        #Other Solutions:
        class Solution(object):
    def characterReplacement(self, s, k):
        freq = defaultdict(int)
        max_freq = 0
        l = 0  
        
        for r, c in enumerate(s):
            freq[c] += 1
            if freq[c] > max_freq: 
                max_freq = freq[c]
            if r - l + 1 - max_freq > k:
                freq[s[l]] -= 1
                l += 1
        return r - l + 1

        #Time Complexity: O(n)
        #Space Complexity: O(1)