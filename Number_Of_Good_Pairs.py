# 1512. Number of Good Pairs
# Easy
# Topics
# Companies
# Hint
# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# Example 2:

# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
# Example 3:

# Input: nums = [1,2,3]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
# My solution:
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pairs=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i]==nums[j] and i<j):
                    pairs+=1
        return pairs
        
# Time complexity: O(n^2)
# Space complexity: O(1)
#Comparing with other solutions:
class Solution(object):
    def numIdenticalPairs(self, nums):
        count = {}
        ans = 0
        
        # Count the occurrences of each number
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # Calculate the number of good pairs
        for key in count:
            n = count[key]
            ans += n * (n - 1) // 2
        
        return ans
# Time complexity: O(n)
# Space complexity: O(n)