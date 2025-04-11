# 1658. Minimum Operations to Reduce X to Zero
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

# Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

 

# Example 1:

# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
# Example 2:

# Input: nums = [5,6,7,8,9], x = 4
# Output: -1
# Example 3:

# Input: nums = [3,2,20,1,1,3], x = 10
# Output: 5
# Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
# 1 <= x <= 109


#My Solution:
class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        ops=float('inf')
        currSum=0
        if nums[0]>x and nums[len(nums)-1]>x:
            return -1
        target=sum(nums)-x
        l,r=0,0
        while r< len(nums):
            currSum+=nums[r]
            while l<=r and currSum > target:
                currSum-=nums[l]
                l+=1

            if currSum==target:
                n=len(nums)-((r-l)+1)
                ops = min(ops,n)
            r+=1

            
        if ops==float('inf'):
            return -1
        else:
            return ops
        

    #Time complexity: O(n)
    #Space complexity: O(1)



#Other Solutions:
class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        n = len(nums)
        target = sum(nums) - x
        if target < 0:
            return -1

        left = 0
        max_len = -1
        curr_sum = 0

        for right in range(n):
            curr_sum += nums[right]

            while curr_sum > target:
                curr_sum -= nums[left]
                left += 1

            if curr_sum == target:
                max_len = max(max_len, right - left + 1)

        return n - max_len if max_len != -1 else -1

    #Time complexity: O(n)
    #Space complexity: O(1)
# The above solution uses a sliding window approach to find the longest subarray with a sum equal to target.