# 344. Reverse String
# Solved
# Easy
# Topics
# Companies
# Hint
# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 

# Constraints:

# 1 <= s.length <= 105

#My Solution:
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l,r=0,len(s)-1
        while l<r:
            temp=s[l]
            s[l]=s[r]
            s[r]=temp
            l+=1
            r-=1
        return s
    #Time Complexity: O(n/2)
    #Space Complexity: O(1) because we are using only a temp variable


    #Other Solutions:
    class Solution(object):
        def reverseString(self, s):
            """
            :type s: List[str]
            :rtype: None Do not return anything, modify s in-place instead.
            """
            s.reverse()
            return s
        #Time Complexity: O(n)
        #Space Complexity: O(1) because we are using only a temp variable