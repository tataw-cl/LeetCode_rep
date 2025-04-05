# 567. Permutation in String
# Solved
# Medium
# Topics
# Companies
# Hint
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
 

# Constraints:

# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.


#My Solution:
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1Count=Counter(s1)
        s2Count=defaultdict(int)
        n=len(s1)
        l,r=0,n
        while r<=len(s2):
            for i in range(l,r):
                s2Count[s2[i]]+=1
            if s2Count==s1Count:
                return True
            else:
                s2Count.clear()
            l+=1
            r+=1
        return False
    
    #Time complexity: O(n*m)
    #Space complexity: O(n)
    #where n is the length of s1 and m is the length of s2.
    #The time complexity is O(n*m) because we are iterating through s2 and checking if the count of characters in s2Count is equal to s1Count.
    #The space complexity is O(n) because we are using a dictionary to store the count of characters in s1 and s2.


#Other solution:
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1Count=Counter(s1)
        s2Count=defaultdict(int)
        n=len(s1)
        l,r=0,n
        for i in range(len(s2)):
            s2Count[s2[i]]+=1
            if i>=n:
                if s2Count[s2[i-n]]==1:
                    del s2Count[s2[i-n]]
                else:
                    s2Count[s2[i-n]]-=1
            if s2Count==s1Count:
                return True
        return False
    
    #Time complexity: O(n*m)
    #Space complexity: O(n)
    #where n is the length of s1 and m is the length of s2.
    #The time complexity is O(n*m) because we are iterating through s2 and checking if the count of characters in s2Count is equal to s1Count.
    #The space complexity is O(n) because we are using a dictionary to store the count of characters in s1 and s2.
    