# 456. 132 Pattern
# Solved
# Medium
# Topics
# Companies
# Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

# Return true if there is a 132 pattern in nums, otherwise, return false.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: false
# Explanation: There is no 132 pattern in the sequence.
# Example 2:

# Input: nums = [3,1,4,2]
# Output: true
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
# Example 3:

# Input: nums = [-1,3,2,0]
# Output: true
# Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
 

# Constraints:

# n == nums.length
# 1 <= n <= 2 * 105
# -109 <= nums[i] <= 109

# My Solution:
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack=[]
        third=float("-inf")
        for num in reversed(nums):
            if num < third:
                return True
            while stack and num>stack[-1]:
                third=stack.pop()
            stack.append(num)
            
        return False
    
# Time complexity: O(n)
# Space complexity: O(n)


# Other Solutions:
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        min_i = nums[0]
        max_i = nums[0]
        for j in range(1, n):
            if min_i > nums[j]:
                min_i = nums[j]
                max_i = nums[j]
            elif max_i < nums[j]:
                max_i = nums[j]
            else:
                for k in range(j+1, n):
                    if nums[k] > min_i and nums[k] < max_i:
                        return True
        return False
    
# Time complexity: O(n^2)
# Space complexity: O(1)