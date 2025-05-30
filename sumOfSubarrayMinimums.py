
# Code
# Code
# Code Sample
# Testcase
# Testcase
# Test Result
# 907. Sum of Subarray Minimums
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

 

# Example 1:

# Input: arr = [3,1,2,4]
# Output: 17
# Explanation: 
# Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
# Sum is 17.
# Example 2:

# Input: arr = [11,81,94,43,3]
# Output: 444
 

# Constraints:

# 1 <= arr.length <= 3 * 104
# 1 <= arr[i] <= 3 * 104


#My Solution:
class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        mod = 10**9 + 7
        stack = []
        res = 0
        n = len(arr)
        
        for i in range(n + 1):
            while stack and (i == n or arr[stack[-1]] > arr[i]):
                j = stack.pop()
                k = stack[-1] if stack else -1
                res += arr[j] * (j - k) * (i - j)
                res %= mod
            stack.append(i)
        
        return res
    
    #Time Complexity: O(n)
    #Space Complexity: O(n)


    #Other Solutions:
class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        # permutation and min
        arr.insert(0, 0)
        result = [0] * len(arr)
        stack = [0]

        for i in range(len(arr)):
            while arr[stack[-1]] > arr[i]:
                stack.pop()
            j = stack[-1]
            result[i] = result[j] + (i-j) * arr[i]
            stack.append(i)
        return sum(result) % (10**9+7)


    #Time Complexity: O(n)
    #Space Complexity: O(n)

# Other Solutions:
#Using a monotonic stack to find the next smaller element on the left and right for each element in the array.
class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        mod = 10**9 + 7
        n = len(arr)
        left = [0] * n
        right = [0] * n
        stack = []

        # Find the next smaller element on the left
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()

        # Find the next smaller element on the right
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        result = 0
        for i in range(n):
            result += arr[i] * (i - left[i]) * (right[i] - i)
            result %= mod

        return result
    
    #Time Complexity: O(n)
    #Space Complexity: O(n)
