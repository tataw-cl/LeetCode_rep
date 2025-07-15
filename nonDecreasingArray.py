# 665. Non-decreasing Array
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

 

# Example 1:

# Input: nums = [4,2,3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
# Example 2:

# Input: nums = [4,2,1]
# Output: false
# Explanation: You cannot get a non-decreasing array by modifying at most one element.
 

# Constraints:

# n == nums.length
# 1 <= n <= 104
# -105 <= nums[i] <= 105


#My Solution:
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        increases = 0

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                increases += 1
                if increases > 1:
                    return False
                
                if i == 0 or nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i + 1] 
                else:
                    nums[i + 1] = nums[i]

        return True


        #Time Complexity: O(n)
        #Space Complexity: O(1)



