# 53. Maximum Subarray
# Solved
# Medium
# Topics
# Companies
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
 

# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# My Solution:
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        currMax=maxSum=nums[0]
        for i in range(1,len(nums)):
            currMax=max(nums[i],currMax+nums[i])
            maxSum=max(currMax,maxSum)
        return maxSum

# Time complexity: O(n)
# Space complexity: O(1)


# Other Solutions:
#Divide and Conquer
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def helper(nums,l,r):
            if l==r:
                return nums[l]
            mid=(l+r)//2
            leftMax=helper(nums,l,mid)
            rightMax=helper(nums,mid+1,r)
            crossMax=self.crossMax(nums,l,mid,r)
            return max(leftMax,rightMax,crossMax)
        
        def crossMax(nums,l,mid,r):
            leftSum=float('-inf')  
            currSum=0
            for i in range(mid,l-1,-1):
                currSum+=nums[i]
                leftSum=max(leftSum,currSum)
            rightSum=float('-inf')
            currSum=0
            for i in range(mid+1,r+1):
                currSum+=nums[i]
                rightSum=max(rightSum,currSum)
            return leftSum+rightSum
        return helper(nums,0,len(nums)-1)
# Time complexity: O(nlogn)
# Space complexity: O(logn)