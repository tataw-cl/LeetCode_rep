# 525. Contiguous Array
# Solved
# Medium
# Topics
# Companies
# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

# Example 1:

# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
# Example 2:

# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Example 3:

# Input: nums = [0,1,1,1,1,1,0,0,0]
# Output: 6
# Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

# My Solution:
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        count_map={0: -1}
        max_len=0
        balance=0
        for i in range(n):
            if nums[i]==1:
                balance+=1
            else:
                balance-=1
            if balance in count_map:
                curr_len = i-count_map[balance]
                max_len=max(curr_len, max_len)
            else:
                count_map[balance]=i
        return max_len
    
# Time complexity: O(n)
# Space complexity: O(n)

# Other Solutions:
    class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = {}
        sum = 0
        hashmap[0]=-1
        max = 0
        for i in range(len(nums)):
            if nums[i]==0:
                sum-=1
            elif nums[i]==1:
                sum+=1
            if sum in hashmap:
                index = hashmap[sum]
                length = i-index
                if length>max:
                    max = length
            else:
                hashmap[sum]=i
        return max
        
# Time complexity: O(n)
# Space complexity: O(n)