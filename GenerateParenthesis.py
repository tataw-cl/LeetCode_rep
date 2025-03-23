# 22. Generate Parentheses
# Solved
# Medium
# Topics
# Companies
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8

# My Solution:
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        def callBack(close_P,open_P,pair):
            if close_P==open_P==n: #Base case for the backtracking function
                res.append(pair)
                return
    #only add a closing parenthesis when close_P is less than open_P
            if close_P<open_P:
                callBack(close_P+1,open_P,pair + ")")
            #Add as many opening parenthesis till we get to n
            if open_P<n:
                callBack(close_P,open_P+1, pair + "(")
            
        #Callback to itself to begin
        callBack(0,0,"")
        return res
    
# Time complexity: O(4^n/sqrt(n))
# Space complexity: O(4^n/sqrt(n))


# Other Solutions:
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def backtrack(s):

            if len(s)==n*2:
                if s.count('(') == s.count(')') and (s[-1] == ')' and s[0]=='('):
                    res.append(s)
                return

            if not s or s.count(')') > s.count('('):
                return
            
            if s.count('(') < n:
                backtrack(s + '(')
            if s.count(')') < n:
                backtrack(s + ')')

        backtrack('(')

        return res
    
# Time complexity: O(4^n/sqrt(n))
# Space complexity: O(4^n/sqrt(n))