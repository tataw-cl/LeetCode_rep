# 523. Continuous Subarray Sum
# Solved
# Medium
# Topics
# Companies
# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

# A good subarray is a subarray where:

# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
# Note that:

# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 

# Example 1:

# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
# Example 2:

# Input: nums = [23,2,6,4,7], k = 6
# Output: true
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
# Example 3:

# Input: nums = [23,2,6,4,7], k = 13
# Output: false
 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109
# 0 <= sum(nums[i]) <= 231 - 1
# 1 <= k <= 231 - 1

# My Solution:
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        modDict=defaultdict(int)
        modDict[0]=-1
        preSum=0
        res=0
        if len(nums)<2:
            return False
        for i in range(len(nums)):
            preSum+=nums[i]
            mod=preSum%k
            if mod not in modDict:
                modDict[mod]=i
            elif i-modDict[mod] >1:
                    return True
    
        return False
    
    # Time complexity: O(n)
    # Space complexity: O(n)


    # Other Solutions:
    class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen_rem = set()
        sum = 0
        prev = 0
        for num in nums:
            sum += num
            curr_rem = sum % k
            if curr_rem in seen_rem:
                return True
            seen_rem.add(prev)
            prev = curr_rem

        return False
        
        # Time complexity: O(n)
        # Space complexity: O(n)