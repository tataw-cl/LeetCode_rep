# 713. Subarray Product Less Than K
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

# Example 1:

# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
# Example 2:

# Input: nums = [1,2,3], k = 0
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# 1 <= nums[i] <= 1000
# 0 <= k <= 106


#My Solution:
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l=0
        prod=1
        res=0
        for r in range(len(nums)):
            prod*=nums[r]
            while l<=r and prod >= k:
                prod=prod//nums[l]
                l+=1
            res+=((r-l)+1)
        return res


    #Time Complexity: O(n)
    #Space Complexity: O(1)
    # The time complexity is O(n) because we are iterating through the array once.
    # The space complexity is O(1) because we are using a constant amount of space to store the variables l, prod, and res.
# The algorithm uses a sliding window approach to find the number of contiguous subarrays with a product less than k.


