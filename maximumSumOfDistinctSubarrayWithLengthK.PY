# 2461. Maximum Sum of Distinct Subarrays With Length K
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

# The length of the subarray is k, and
# All the elements of the subarray are distinct.
# Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,5,4,2,9,9,9], k = 3
# Output: 15
# Explanation: The subarrays of nums with length 3 are:
# - [1,5,4] which meets the requirements and has a sum of 10.
# - [5,4,2] which meets the requirements and has a sum of 11.
# - [4,2,9] which meets the requirements and has a sum of 15.
# - [2,9,9] which does not meet the requirements because the element 9 is repeated.
# - [9,9,9] which does not meet the requirements because the element 9 is repeated.
# We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions
# Example 2:

# Input: nums = [4,4,4], k = 3
# Output: 0
# Explanation: The subarrays of nums with length 3 are:
# - [4,4,4] which does not meet the requirements because the element 4 is repeated.
# We return 0 because no subarrays meet the conditions.
 

# Constraints:

# 1 <= k <= nums.length <= 105
# 1 <= nums[i] <= 105

#My Solution:
class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        if k>n:
            return 0
        count_dict=defaultdict(int)
        max_sum=0
        curr_sum=0
        l=0
        for i in range(n):
            curr_sum+=nums[i]
            count_dict[nums[i]]+=1
            if i-l+1>k:
                count_dict[nums[l]]-=1
                if count_dict[nums[l]]==0:
                    count_dict.pop(nums[l])
                curr_sum-=nums[l]
                l+=1

            if len(count_dict)== i-l+1==k:
                max_sum=max(max_sum,curr_sum)

        return max_sum
    
# Time complexity: O(n)
# Space complexity: O(n)


#Other Solutions:
class Solution:
    def maximumUniqueSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        r = 0
        s = set()
        cur_sum = 0
        ans = 0
        while r < n:
            while nums[r] in s:
                s.remove(nums[l])
                cur_sum -= nums[l]
                l += 1
            s.add(nums[r])
            cur_sum += nums[r]
            r += 1
            if r - l > k:
                s.remove(nums[l])
                cur_sum -= nums[l]
                l += 1
            ans = max(ans, cur_sum)
        return ans
    
# Time complexity: O(n)
# Space complexity: O(n)