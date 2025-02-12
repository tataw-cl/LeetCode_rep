# 1684. Count the Number of Consistent Strings
# Solved
# Easy
# Topics
# Companies
# Hint
# You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

# Return the number of consistent strings in the array words.

 

# Example 1:

# Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
# Output: 2
# Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
# Example 2:

# Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
# Output: 7
# Explanation: All strings are consistent.
# Example 3:

# Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
# Output: 4
# Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
 

# Constraints:

# 1 <= words.length <= 104
# 1 <= allowed.length <= 26
# 1 <= words[i].length <= 10
# The characters in allowed are distinct.
# words[i] and allowed contain only lowercase English letters.


#My Solution:
class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowed_Set=set(allowed)
        consistent_Count=0
        for word in words:
            consistent=True
            for char in word:
                if char not in allowed_Set:
                    consistent=False
                    break
            if consistent:
                consistent_Count+=1
        return consistent_Count

        #Time complexity: O(n*m)
        #Space complexity: O(n)

#Other Solutions:
class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        return sum(all(c in allowed for c in word) for word in words)

        #Time complexity: O(n*m)
        #Space complexity: O(n)