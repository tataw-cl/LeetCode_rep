# 962. Maximum Width Ramp
# Solved
# Medium
# Topics
# Companies
# A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

# Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

 

# Example 1:

# Input: nums = [6,0,8,2,1,5]
# Output: 4
# Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
# Example 2:

# Input: nums = [9,8,1,0,1,9,4,0,4,1]
# Output: 7
# Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.
 

# Constraints:

# 2 <= nums.length <= 5 * 104
# 0 <= nums[i] <= 5 * 104



#My Solution:
class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        stack = []
        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        ans = 0
        for j in range(n-1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                ans = max(ans, j - stack.pop())
        return ans
    
    #Time Complexity: O(n)
    #Space Complexity: O(n)
# 1. The time complexity is O(n) because we are iterating through the list of nums twice: once to build the stack and once to calculate the maximum width ramp.
# 2. The space complexity is O(n) because we are using a stack to store the indices of the elements in nums. In the worst case, all elements could be stored in the stack.
