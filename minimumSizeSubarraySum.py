# 209. Minimum Size Subarray Sum
# Solved
# Medium
# Topics
# Companies
# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
 

# Constraints:

# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
 

# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).



# My Solution:
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        sum = 0
        min_len = float('inf')
        
        while right < len(nums):
            sum += nums[right]
            while sum >= target:
                min_len = min(min_len, right - left + 1)
                sum -= nums[left]
                left += 1
            right += 1
        
        return min_len if min_len != float('inf') else 0
    

        #Time Complexity: O(n)
        #Space Complexity: O(1)
        #The space complexity is O(1) because we are using a constant amount of space to store the variables left, right, sum, and min_len.



        #Other Solutions:
# Solution which takes O(n log(n)) time complexity:
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        min_len = float('inf')
        
        for i in range(n):
            left = bisect.bisect_left(prefix_sum, prefix_sum[i] + target)
            if left <= n:
                min_len = min(min_len, left - i)
        
        return min_len if min_len != float('inf') else 0
    

    #Time Complexity: O(n log(n))
    #Space Complexity: O(n)