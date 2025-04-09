# 1358. Number of Substrings Containing All Three Characters
# Solved
# Medium
# Topics
# Companies
# Hint
# Given a string s consisting only of characters a, b and c.

# Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

# Example 1:

# Input: s = "abcabc"
# Output: 10
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
# Example 2:

# Input: s = "aaacb"
# Output: 3
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
# Example 3:

# Input: s = "abc"
# Output: 1
 

# Constraints:

# 3 <= s.length <= 5 x 10^4
# s only consists of a, b or c characters.


#My Solution:
class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        count = 0
        left = 0
        right = 0
        char_count = {}
        
        while right < n:
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            
            while len(char_count) == 3:
                count += n - right
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            
            right += 1
        
        return count
    
        #Time complexity: O(n) where n is the length of the input string.
        #Space complexity: O(1) because we are using a fixed-size dictionary to store the character counts.
        #The space complexity is O(1) because we are using a fixed-size dictionary to store the character counts.



# #Other Solutions:
class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        count = [-1] * 3
        for i, c in enumerate(s):
            count[ord(c) - 97] = i
            res += min(count) + 1
        return res
        lastSeen = [-1, -1, -1] 
        count = 0 
        for i in range(len(s)):
            lastSeen[ord(s[i]) - ord('a')] = i
            if lastSeen[0] != -1 and lastSeen[1] != -1 and lastSeen[2] != -1:
                count += (1 + min(lastSeen[0], lastSeen[1], lastSeen[2]))
        return count
    

        #Time complexity: O(n) where n is the length of the input string.
        #Space complexity: O(1) because we are using a fixed-size array to store the last seen indices of the characters.
