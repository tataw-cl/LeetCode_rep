# 1790. Check if One String Swap Can Make Strings Equal
# Attempted
# Easy
# Topics
# Companies
# Hint
# You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

# Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

 

# Example 1:

# Input: s1 = "bank", s2 = "kanb"
# Output: true
# Explanation: For example, swap the first character with the last character of s2 to make "bank".
# Example 2:

# Input: s1 = "attack", s2 = "defend"
# Output: false
# Explanation: It is impossible to make them equal with one string swap.
# Example 3:

# Input: s1 = "kelb", s2 = "kelb"
# Output: true
# Explanation: The two strings are already equal, so no string swap operation is required.
 

# Constraints:

# 1 <= s1.length, s2.length <= 100
# s1.length == s2.length
# s1 and s2 consist of only lowercase English letters.


#My Solution:
class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        diff=0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                diff+=1
        if (diff==2 and Counter(s1)==Counter(s2)) or diff==0:
            return True
        else:
            return False
        
#Other Solutions:
class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        error = []
        for i, j in zip(s1, s2):
            if i != j:
                error.append([i, j])
        
        if len(error) > 2: return False

        resolved = 0 
        for err in error:
            if err[::-1] in error:
                resolved += 1
        
        return resolved == len(error)
    
#Other Solution:

class Solution(object):
    def areAlmostEqual(self, s1, s2):
        dict1, dict2, count = Counter(s1), Counter(s2), 0

        if dict1 != dict2:
            return False 

        for i,j in zip(s1,s2):
            if i != j:
                count += 1 