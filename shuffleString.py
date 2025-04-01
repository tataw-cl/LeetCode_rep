# 1528. Shuffle String
# Solved
# Easy
# Topics
# Companies
# Hint
# You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

# Return the shuffled string.

 

# Example 1:


# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
# Example 2:

# Input: s = "abc", indices = [0,1,2]
# Output: "abc"
# Explanation: After shuffling, each character remains in its position.
 

# Constraints:

# s.length == indices.length == n
# 1 <= n <= 100
# s consists of only lowercase English letters.
# 0 <= indices[i] < n
# All values of indices are unique.



#My Solution:
class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        res=['']*len(s)
        for i in range(len(s)):
            res[indices[i]]=s[i]
        return ''.join(res)
    

#Time complexity: O(n)
#Space complexity: O(n)
# The space complexity is O(n) because we are using an additional list of size n to store the shuffled characters.


#Other solution:
class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        return ''.join(sorted(s, key=lambda x: indices[s.index(x)]))
    

#Time complexity: O(nlogn)
#Space complexity: O(n)