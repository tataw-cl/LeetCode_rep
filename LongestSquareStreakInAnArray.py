# 2501. Longest Square Streak in an Array
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given an integer array nums. A subsequence of nums is called a square streak if:

# The length of the subsequence is at least 2, and
# after sorting the subsequence, each element (except the first element) is the square of the previous number.
# Return the length of the longest square streak in nums, or return -1 if there is no square streak.

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:

# Input: nums = [4,3,6,16,8,2]
# Output: 3
# Explanation: Choose the subsequence [4,16,2]. After sorting it, it becomes [2,4,16].
# - 4 = 2 * 2.
# - 16 = 4 * 4.
# Therefore, [4,16,2] is a square streak.
# It can be shown that every subsequence of length 4 is not a square streak.
# Example 2:

# Input: nums = [2,3,5,6,7]
# Output: -1
# Explanation: There is no square streak in nums so return -1.
 

# Constraints:

# 2 <= nums.length <= 105
# 2 <= nums[i] <= 105

# My Solution:
class Solution(object):
    def longestSquareStreak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        checker_set=set(nums)
        Longeststreak=0
        nums.sort()
        for i in range(len(nums)):
            n=nums[i]
            streak=0
            while n in checker_set:
                streak+=1
                n=n*n
            Longeststreak=max(Longeststreak, streak)
        if Longeststreak>1:
            return Longeststreak
        else:
            return -1
        
# Time complexity: O(n^2)
# Space complexity: O(n)

# Optimized Solution:
class Solution(object):
    def longestSquareStreak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return -1
        nums.sort()
        res=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[j]==nums[i]**2:
                    res=max(res,j-i+1)
        return res if res>2 else -1
    
# Time complexity: O(n^2)
# Space complexity: O(1)