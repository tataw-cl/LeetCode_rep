# 17. Letter Combinations of a Phone Number
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]
 

# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].


#My Solution:
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letterCombs={
            '2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'
        }
        res=[]
        if not digits:
            return res
        
        def backtrack(i,combs):
            if len(combs)==len(digits):
                res.append(''.join(combs))
                return

            currNum=digits[i]
            for letter in letterCombs[currNum]:
                combs.append(letter)
                backtrack(i+1, combs)
                combs.pop()

        backtrack(0,[])
        return res
    
    #Time Complexity: O(4^n * n) where n is the length of digits. The 4^n comes from the maximum number of combinations (each digit can map to 3 or 4 letters), and n is for the string concatenation in the result.
    #Space Complexity: O(n) for the recursion stack and the result list.


    #Other Solutions:
    # Iterative Solution
    def letterCombinationsIterative(self, digits):
        if not digits:
            return []
        
        letterCombs = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        res = ['']
        
        for digit in digits:
            new_res = []
            for combination in res:
                for letter in letterCombs[digit]:
                    new_res.append(combination + letter)
            res = new_res
        
        return res

        #Time Complexity: O(4^n * n) where n is the length of digits. The 4^n comes from the maximum number of combinations (each digit can map to 3 or 4 letters), and n is for the string concatenation in the result.
        #Space Complexity: O(n) for the result list.
