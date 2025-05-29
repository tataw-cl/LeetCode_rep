# 779. K-th Symbol in Grammar
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

# For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
# Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

 

# Example 1:

# Input: n = 1, k = 1
# Output: 0
# Explanation: row 1: 0
# Example 2:

# Input: n = 2, k = 1
# Output: 0
# Explanation: 
# row 1: 0
# row 2: 01
# Example 3:

# Input: n = 2, k = 2
# Output: 1
# Explanation: 
# row 1: 0
# row 2: 01
 

# Constraints:

# 1 <= n <= 30
# 1 <= k <= 2n - 1


#My Solution:
class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        val=0
        l,r=1,2**(n-1)
        for _ in range(n-1):
            mid=(l+r)//2
            if k <=mid:
                r=mid
            else:
                l=mid+1
                val = 0 if val==1 else 1

        return val


        #Time Complexity: O(n)
        #Space Complexity: O(1)


        #Other Solutions
        # 1. Recursive Solution
        def kthGrammarRecursive(n, k):
            if n == 1:
                return 0
            if k % 2 == 1:
                return kthGrammarRecursive(n - 1, (k + 1) // 2)
            else:
                return 1 - kthGrammarRecursive(n - 1, k // 2)

        #Time Complexity: O(n)
        #Space Complexity: O(n) due to recursion stack

        # 2. Bit Manipulation Solution
        def kthGrammarBitManipulation(n, k):
            k -= 1
            result = 0
            while k > 0:
                result ^= (k & 1)
                k >>= 1
            return result
        
        #Time Complexity: O(log k)
        #Space Complexity: O(1)

