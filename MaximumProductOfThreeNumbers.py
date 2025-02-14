# 628. Maximum Product of Three Numbers
# Solved
# Easy
# Topics
# Companies
# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: 6
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 24
# Example 3:

# Input: nums = [-1,-2,-3]
# Output: -6
 

# Constraints:

# 3 <= nums.length <= 104
# -1000 <= nums[i] <= 1000

#My solution:
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        max1 = nums[-1] * nums[-2] * nums[-3]
        max2 = nums[0] * nums[1] * nums[-1]
        return max(max1, max2)
    
    #Time complexity: O(nlogn)
    #Space complexity: O(1)

#Other solutions:
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')
        for num in nums:
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
        return max(max1 * max2 * max3, max1 * min1 * min2)
    
    #Time complexity: O(n)
    #Space complexity: O(1)