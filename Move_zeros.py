# 283. Move Zeroes
# Easy
# Topics
# Companies
# Hint
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
 

# Follow up: Could you minimize the total number of operations done?

# My solution:
def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    i=0
    for j in range(len(nums)):
        if nums[j]!=0:
            nums[i], nums[j]=nums[j], nums[i]
            i+=1
    return nums
# Time complexity: O(n)
# Space complexity: O(1)

# Other solution:
def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    i=0
    for j in range(len(nums)):
        if nums[j]!=0:
            nums[i]=nums[j]
            i+=1
    for j in range(i, len(nums)):
        nums[j]=0
    return nums

# Time complexity: O(n)
# Space complexity: O(1)


# Other solution:
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        poppedZeros = []
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                poppedZeros.append(0)
            else:
                i += 1
        size = len(nums)
        nums[size:] = poppedZeros

# Time complexity: O(n)
# Space complexity: O(n)