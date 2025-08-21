# 136. Single Number
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]

# Output: 1

# Example 2:

# Input: nums = [4,1,2,1,2]

# Output: 4

# Example 3:

# Input: nums = [1]

# Output: 1

 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.


#My Solution:
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num
        return result
    

#Time Complexity: O(n)
#Space Complexity: O(1) - since we are using a constant amount of space for the result variable.


#Other Solutions:
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set()
        for num in nums:
            if num in num_set:
                num_set.remove(num)
            else:
                num_set.add(num)
        return num_set.pop() if num_set else None


#Time Complexity: O(n) - we traverse the list once.
#Space Complexity: O(n) - in the worst case, we might store all elements in the set.
# However, since the problem guarantees that there is exactly one unique number, the space complexity can be considered O(1) in practice, as the set will not grow beyond a certain size.
# This is because we only store numbers that appear once, and the set will only contain at most one element at the end.
