# 438. Find All Anagrams in a String
# Solved
# Medium
# Topics
# Companies
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

 

# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
 

# Constraints:

# 1 <= s.length, p.length <= 3 * 104
# s and p consist of lowercase English letters.


#My Solution:
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res=[]
        pDict=defaultdict(int)
        sDict=defaultdict(int)
        n=len(p)
        l=0
        for char in p:
            pDict[char]+=1
        for r in range(len(s)):
            sDict[s[r]]+=1
            if sum(sDict.values())==n:
                if sDict==pDict:
                    res.append((r+1)-n)
                sDict[s[l]]-=1
                if sDict[s[l]]==0:
                    del sDict[s[l]]
                l+=1

        return res

    #Time complexity: O(n)
    #Space complexity: O(n)
    #The space complexity is O(n) because we are storing the result in a new list of size n.

