# 151. Reverse Words in a String
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

# Constraints:

# 1 <= s.length <= 104
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.
 

# Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?


#My Solution:
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=s.split()
        res=" ".join(reversed(words))
        return res
    
#Time Complexity: O(n)
#Space Complexity: O(n) for the list of words


#Other Solutions:
class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into words, filter out empty strings, and reverse the list of words
        words = s.split()
        reversed_words = words[::-1]
        # Join the reversed words with a single space
        return ' '.join(reversed_words)
    
#Time Complexity: O(n)
#Space Complexity: O(n) for the list of words
